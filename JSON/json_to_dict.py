# Json to be encoded to Python dictionary
import json

my_Json = '{"name": "John", "age": 30, "city": "New York"}'
my_dict = json.loads(my_Json)
print("Python Dictionary= ", my_dict)
