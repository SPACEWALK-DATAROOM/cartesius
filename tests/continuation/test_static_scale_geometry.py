"""Source: cartesius/transforms.py"""
import pytest
from shapely.geometry import box

from cartesius.transforms import NormalizeScaleStaticTransform


def test_common_reference_scale_preserves_relative_size_between_samples():
    transform = NormalizeScaleStaticTransform(max_radius_range=5)
    small = transform(box(3, 4, 7, 8))
    large = transform(box(3, 4, 11, 12))
    assert small.area == pytest.approx(.04)
    assert large.area == pytest.approx(4 * small.area)
    assert small.bounds[:2] == large.bounds[:2] == (3, 4)


def test_zero_static_range_is_an_explicit_error():
    with pytest.raises(ZeroDivisionError):
        NormalizeScaleStaticTransform(0)(box(0, 0, 1, 1))
