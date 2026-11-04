"""Source: cartesius/utils.py"""
import csv
import io

from cartesius.utils import kaggle_convert_labels


def test_vector_labels_flatten_with_conserved_weight_and_csv_roundtrip():
    rows = kaggle_convert_labels(['centroid', 'area'], [(2.5, -1.5), 8], [6, 4])
    assert rows == [{
        'id': 'centroid_0',
        'value': 2.5,
        'weight': 3
    }, {
        'id': 'centroid_1',
        'value': -1.5,
        'weight': 3
    }, {
        'id': 'area',
        'value': 8,
        'weight': 4
    }]
    stream = io.StringIO()
    writer = csv.DictWriter(stream, fieldnames=['id', 'value', 'weight'])
    writer.writeheader()
    writer.writerows(rows)
    stream.seek(0)
    result = list(csv.DictReader(stream))
    assert [r['id'] for r in result] == ['centroid_0', 'centroid_1', 'area']
    assert sum(float(r['weight']) for r in result) == 10


def test_without_weights_keeps_boolean_and_scalar_values():
    assert kaggle_convert_labels(['valid', 'bounds'], [True, [1, 2]]) == [{
        'id': 'valid',
        'value': True
    }, {
        'id': 'bounds_0',
        'value': 1
    }, {
        'id': 'bounds_1',
        'value': 2
    }]
