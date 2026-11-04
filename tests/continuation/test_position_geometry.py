"""Source: cartesius/transforms.py"""
import pytest
from shapely.geometry import Polygon,LineString
from cartesius.transforms import NormalizePositionTransform

def test_translation_normalizes_negative_l_shaped_polygon_without_changing_topology():
    source=Polygon([(-6,-4),(-2,-4),(-2,-3),(-5,-3),(-5,0),(-6,0)])
    result=NormalizePositionTransform()(source)
    assert result.bounds==(0,0,4,4) and result.area==source.area
    assert result.is_valid and source.bounds==(-6,-4,-2,0)
    assert NormalizePositionTransform()(result).equals_exact(result,0)

def test_lines_keep_distance_and_relative_coordinate_order():
    source=LineString([(8,-2),(10,2),(12,-1)]);result=NormalizePositionTransform()(source)
    assert list(result.coords)==[(0,0),(2,4),(4,1)]
    assert result.length==pytest.approx(source.length)
