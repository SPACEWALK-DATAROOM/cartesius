"""Source: cartesius/transforms.py"""
import pytest
from shapely.geometry import LineString
from shapely.geometry import Point
from shapely.geometry import Polygon

from cartesius.transforms import NormalizeScaleTransform


def test_scale_uses_longer_axis_preserves_origin_and_area_ratio():
    source = Polygon([(10, 20), (18, 20), (18, 24), (10, 24)])
    result = NormalizeScaleTransform()(source)
    assert result.bounds == pytest.approx((10, 20, 11, 20.5))
    assert result.area == pytest.approx(source.area / 64)
    assert source.area == 32


def test_zero_extent_point_and_vertical_line_are_supported():
    source = Point(5, 7)
    assert NormalizeScaleTransform()(source) is source
    line = NormalizeScaleTransform()(LineString([(2, 5), (2, 15)]))
    assert list(line.coords) == [(2, 5), (2, 6)]
