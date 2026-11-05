"""Execute selected original definitions, with explicit dependency bindings.

This is isolated source behavior, not application startup or framework integration.
Only Prefect's task decorator is removed. Original annotation policy is retained.
"""
import __future__

import ast
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def load(path, names, owner=None, **bindings):
    source = (ROOT / path).resolve()
    if ROOT not in source.parents or source.suffix != ".py":
        raise ValueError("Selected source must be a Python file inside this repository")
    text = source.read_text()
    tree = ast.parse(text, filename=str(source))
    body = tree.body
    for part in (owner.split(".") if owner else []):
        matches = [
            n for n in body if isinstance(n, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and n.name == part
        ]
        if len(matches) != 1:
            raise ValueError("Source owner must resolve exactly once: " + part)
        body = matches[0].body
    if len(names) != len(set(names)):
        raise ValueError("Duplicate requested definitions")
    nodes = []
    provenance = []
    for name in names:
        matches = [
            n for n in body
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.name == name or
            isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in n.targets)
        ]
        if len(matches) != 1:
            raise ValueError("Definition must resolve exactly once: " + name)
        node = matches[0]
        original_ast = ast.dump(node, include_attributes=False)
        removed = []
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            removed = [
                d for d in node.decorator_list
                if isinstance(d, ast.Call) and isinstance(d.func, ast.Name) and d.func.id == "task"
            ]
            node.decorator_list = [d for d in node.decorator_list if d not in removed]
        nodes.append(node)
        provenance.append({
            "name": name,
            "line": node.lineno,
            "original_ast_sha256": hashlib.sha256(original_ast.encode()).hexdigest(),
            "removed_prefect_task_decorators": len(removed)
        })
    # Preserve original declaration order, including dependencies between classes.
    nodes.sort(key=lambda n: n.lineno)
    flags = 0
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module == "__future__":
            for feature in node.names:
                flags |= getattr(__future__, feature.name).compiler_flag
    ns = {"__file__": str(source), "__name__": "isolated_source_contract", **bindings}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), "exec", flags=flags, dont_inherit=True), ns)
    ns["__source_provenance__"] = {
        "path": path,
        "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "owner": owner,
        "definitions": provenance,
        "future_flags": flags
    }
    return ns
