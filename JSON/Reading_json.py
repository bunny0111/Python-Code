import json

# Read Json from a file
with open("shubham.json", "r") as file:
    data = json.load(file)

print("JSON Data from a file:", data)
