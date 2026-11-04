"""Isolate pure submodules from optional eager LLM/optimizer package bootstrap.
No target function or supporting geometry implementation is stubbed.
"""
from importlib.machinery import ModuleSpec
from pathlib import Path
import sys
import types


def pytest_configure(config):
    root = Path.cwd() / 'cartesius'
    package = types.ModuleType('cartesius')
    package.__path__ = [str(root)]
    package.__file__ = str(root / '__init__.py')
    package.__package__ = 'cartesius'
    package.__spec__ = ModuleSpec('cartesius', loader=None, is_package=True)
    package.__spec__.submodule_search_locations = package.__path__
    sys.modules['cartesius'] = package
