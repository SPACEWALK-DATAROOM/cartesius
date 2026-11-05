"""Source: cartesius/tokenizers.py"""
from shapely.geometry import Polygon
import torch

from cartesius.tokenizers import Tokenizer
from cartesius.transforms import NormalizePositionTransform
from cartesius.transforms import NormalizeScaleTransform


def test_translation_and_uniform_scaling_produce_identical_normalized_tokens():
    original = Polygon([(10, 20), (18, 20), (18, 24), (10, 24)])
    equivalent = Polygon([(-4, -8), (12, -8), (12, 0), (-4, 0)])

    def normalized(polygon):
        return NormalizeScaleTransform()(NormalizePositionTransform()(polygon))

    tokens = Tokenizer()([normalized(original), normalized(equivalent)])
    assert torch.equal(tokens['polygon'][0], tokens['polygon'][1])
    assert tokens['polygon'][0].tolist() == [[0, 0], [1, 0], [1, .5], [0, .5], [0, 0]]
    assert tokens['mask'].all().item() is True
    assert original.bounds == (10, 20, 18, 24)


def test_tokenized_normalized_polygon_keeps_concavity_and_vertex_order():
    source = Polygon([(2, 3), (6, 3), (6, 4), (3, 4), (3, 7), (2, 7)])
    normalized = NormalizeScaleTransform()(NormalizePositionTransform()(source))
    encoded = Tokenizer()(normalized)['polygon'][0].tolist()
    decoded = Polygon(encoded)
    assert decoded.equals_exact(normalized, 0)
    assert decoded.area == source.area / 16
    assert decoded.area < decoded.convex_hull.area
