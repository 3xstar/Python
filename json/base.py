import json

data = {
    "name": "Виталик",
    "age": 15
}

json_str = json.dumps(data)

data_json_str = '{"name": "Виталик", "age": 15}'
data = json.loads(data_json_str)
print(type(data))
print(type(json_str))

