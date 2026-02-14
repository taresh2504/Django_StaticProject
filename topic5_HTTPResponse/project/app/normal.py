import json

p_data = {'x':True,"y":False,'''z''':None}

j_data = json.dumps(p_data)
print(j_data)
print(type(j_data))