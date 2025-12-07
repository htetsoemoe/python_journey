import json

json_data = '{"name": "alice", "age": 27}'

# Change from JSON to Python Dictionary
sample_dict = json.loads(json_data)
print(f"from JSON to Python Dict: {sample_dict}")
print(sample_dict['name'])


# Change from Python Dictionary to JSON
sample_json = json.dumps(sample_dict)
print(f"From Dictionary to JSON: {sample_json}")