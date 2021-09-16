# import pickle
#
# with open('persistants/marks.pickle', 'rb') as f:
#     marks = pickle.load(f)
#
# with open('persistants/modelss.pickle', 'rb') as f:
#     models = pickle.load(f)
#
#
# with open('persistants/citys.pickle', 'rb') as f:
#     citys = pickle.load(f)
#
# with open('persistants/citys_map.pickle', 'rb') as f:
#     citys_map = pickle.load(f)

import json

with open('function/persistants/marks.json') as f:
    marks = json.load(f)

with open('function/persistants/modelss.json', 'rb') as f:
    models = json.load(f)

with open('function/persistants/citys.json', 'rb') as f:
    citys = json.load(f)

with open('function/persistants/citys_map.json', 'rb') as f:
    citys_map = json.load(f)


citys_map = {int(k): v for k, v in citys_map.items()}

marks_revers: dict = {v: k for k, v in marks.items()}

models_revers: dict = {v: k for k, v in models.items()}