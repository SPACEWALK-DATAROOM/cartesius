"""Source: cartesius/utils.py"""
from pathlib import Path

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shapely.geometry import LineString
from shapely.geometry import MultiPolygon
from shapely.geometry import Point
from shapely.geometry import Polygon

from cartesius.utils import print_polygon
from cartesius.utils import save_polygon


def test_multipart_geometry_adds_actual_line_artists():
    plt.figure()
    source = MultiPolygon([Polygon([(0, 0), (2, 0), (0, 2)]), Polygon([(4, 0), (6, 0), (4, 2)])])
    print_polygon(source, color='red')
    lines = plt.gca().lines
    assert len(lines) == 2
    assert list(lines[1].get_xdata()) == [4, 6, 4, 4]
    print_polygon(Point(0, 0))
    assert len(plt.gca().lines) == 2
    plt.close('all')


def test_save_raster_creates_real_png_and_fill_collection(tmp_path):
    polygon = Polygon([(0, 0), (3, 0), (0, 2)])
    plt.figure()
    print_polygon(polygon, fill='blue')
    assert len(plt.gca().collections) == 1
    path = tmp_path / 'geometry.png'
    save_polygon(polygon, LineString([(0, 0), (3, 2)]), path=str(path))
    assert path.read_bytes()[:8] == b'\x89PNG\r\n\x1a\n'
    plt.close('all')
