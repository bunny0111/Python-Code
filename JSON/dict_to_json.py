import json

# Python dictionary to be encoded to json
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Encoding the Python dictionary to JSON
my_json = json.dumps(my_dict)
print("Json Data=", my_json)
