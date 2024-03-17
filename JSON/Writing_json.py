import json

# Python dictionary to be written to a json file

data = {"name": "John", "age": 30, "city": "New York"}

with open("output.json", "w") as file:
    json.dump(data, file)
