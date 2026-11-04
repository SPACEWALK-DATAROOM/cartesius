import pytest
from shapely.geometry import Polygon,Point,LineString,box
from cartesius.transforms import Transform,NormalizePositionTransform,NormalizeScaleTransform,NormalizeScaleStaticTransform


def test_base_transform_requires_implementation():
    with pytest.raises(NotImplementedError):Transform()(Point(0,0))


def test_translation_preserves_hole_area_vertices_and_original():
    p=Polygon([(-4,-8),(4,-8),(4,-2),(-4,-2)],holes=[[(-2,-7),(0,-7),(0,-5),(-2,-5)]])
    got=NormalizePositionTransform()(p)
    assert got.bounds==(0.,0.,8.,6.)
    assert got.area==44
    assert len(got.interiors)==1
    assert got.interiors[0].bounds==(2.,1.,4.,3.)
    assert p.bounds==(-4.,-8.,4.,-2.)


def test_scale_preserves_anchor_aspect_ratio_and_area_scaling():
    p=box(-3,5,5,9);got=NormalizeScaleTransform()(p)
    assert got.bounds==(-3.,5.,-2.,5.5)
    assert got.area==.5
    assert p.bounds==(-3.,5.,5.,9.)


def test_degenerate_point_is_preserved_without_division_by_zero():
    p=Point(-2,7);assert NormalizeScaleTransform()(p).equals_exact(p,0)


def test_vertical_line_length_normalized_without_horizontal_displacement():
    got=NormalizeScaleTransform()(LineString([(3,-5),(3,5)]))
    assert got.bounds==(3.,-5.,3.,-4.)
    assert got.length==1


def test_static_scaling_uses_one_common_factor_for_different_shapes():
    t=NormalizeScaleStaticTransform(2)
    assert t(box(0,0,8,4)).bounds==(0.,0.,1.,.5)
    assert t(box(0,0,4,2)).bounds==(0.,0.,.5,.25)
