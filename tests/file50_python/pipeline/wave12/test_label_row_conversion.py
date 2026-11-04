from .loader import load

def converter():return load('cartesius/utils.py',['kaggle_convert_labels'])['kaggle_convert_labels']

def test_scalar_task_labels_become_named_rows_without_model_or_tensor_loading():
 assert converter()(['area','perimeter'],[12.5,16])==[{'id':'area','value':12.5},{'id':'perimeter','value':16}]

def test_vector_and_scalar_labels_expand_in_task_and_component_order():
 assert converter()(['centroid','area','bounds'],[(2,3),12,[0,1,4,5]])==[{'id':'centroid_0','value':2},{'id':'centroid_1','value':3},{'id':'area','value':12},{'id':'bounds_0','value':0},{'id':'bounds_1','value':1},{'id':'bounds_2','value':4},{'id':'bounds_3','value':5}]

def test_empty_labels_and_repeated_calls_keep_row_generation_stateless():
 fn=converter();assert fn([],[])==[]
 assert fn(['empty','one'],[[],[7]])==[{'id':'one_0','value':7}]
 assert fn(['one'],[[8]])==[{'id':'one_0','value':8}]
