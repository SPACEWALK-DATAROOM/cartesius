"""Source: cartesius/tokenizers.py"""
import pytest
import torch
from shapely.geometry import Polygon,LineString,Point
from cartesius.tokenizers import Tokenizer

def test_mixed_geometry_batch_preserves_coordinates_and_padding_mask():
    polygon=Polygon([(1,1),(3,1),(1,4)])
    batch=Tokenizer()([polygon,LineString([(8,9),(10,11)]),Point(7,6)])
    assert tuple(batch['polygon'].shape)==(3,4,2)
    assert batch['mask'].dtype==torch.bool
    assert batch['mask'].tolist()==[[True]*4,[True,True,False,False],[True,False,False,False]]
    assert batch['polygon'][0].tolist()==[[1,1],[3,1],[1,4],[1,1]]
    assert batch['polygon'][1].tolist()==[[8,9],[10,11],[0,0],[0,0]]
    assert batch['polygon'].device.type=='cpu'

def test_single_input_matches_batch_and_limit_counts_closing_vertex():
    polygon=Polygon([(0,0),(2,0),(0,2)])
    single=Tokenizer(max_seq_len=4)(polygon);batched=Tokenizer(max_seq_len=4)([polygon])
    assert torch.equal(single['polygon'],batched['polygon'])
    with pytest.raises(RuntimeError,match='4 > 3'):Tokenizer(max_seq_len=3)(polygon)
