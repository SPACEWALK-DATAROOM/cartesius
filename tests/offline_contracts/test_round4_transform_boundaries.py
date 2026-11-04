from shapely.geometry import LineString
from shapely.geometry import MultiPolygon
from shapely.geometry import Polygon

from cartesius.transforms import NormalizePositionTransform
from cartesius.transforms import NormalizeScaleStaticTransform
from cartesius.transforms import NormalizeScaleTransform
from cartesius.transforms import TRANSFORMS


def test_position_normalization_translates_multipolygon_parts_and_preserves_holes_z_and_source():
    source = MultiPolygon([
        Polygon(
            shell=[(10, 20, 5), (14, 20, 6), (14, 24, 7), (10, 24, 8), (10, 20, 5)],
            holes=[
                [(11, 21, 5), (12, 21, 5), (12, 22, 5), (11, 22, 5), (11, 21, 5)],
            ],
        ),
        Polygon([(20, 30, 1), (22, 30, 2), (22, 32, 3), (20, 32, 4), (20, 30, 1)]),
    ])
    original = source.wkt

    result = NormalizePositionTransform()(source)

    assert result.geom_type == "MultiPolygon"
    assert len(result.geoms) == 2
    assert len(result.geoms[0].interiors) == 1
    assert result.bounds == (0.0, 0.0, 12.0, 12.0)
    assert tuple(result.geoms[0].exterior.coords[0]) == (0.0, 0.0, 5.0)
    assert tuple(result.geoms[0].interiors[0].coords[0]) == (1.0, 1.0, 5.0)
    assert tuple(result.geoms[1].exterior.coords[0]) == (10.0, 10.0, 1.0)
    assert result.area == source.area
    assert source.wkt == original


def test_scale_normalization_uses_one_xy_factor_and_leaves_line_z_values_unchanged():
    source = LineString([(10, 20, 4), (30, 25, 8)])
    original = list(source.coords)

    result = NormalizeScaleTransform()(source)

    assert list(result.coords) == [(10.0, 20.0, 4.0), (11.0, 20.25, 8.0)]
    assert result.bounds == (10.0, 20.0, 11.0, 20.25)
    assert list(source.coords) == original


def test_public_transform_registry_resolves_each_supported_name_to_its_implementation():
    assert set(TRANSFORMS) == {"norm_pos", "norm_scale", "norm_static_scale"}
    assert TRANSFORMS["norm_pos"] is NormalizePositionTransform
    assert TRANSFORMS["norm_scale"] is NormalizeScaleTransform
    assert TRANSFORMS["norm_static_scale"] is NormalizeScaleStaticTransform
