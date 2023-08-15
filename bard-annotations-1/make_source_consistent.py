import json

def make_source_property_consistent(json_data):
  for dictionary in json_data:
    if "Source" in dictionary:
      dictionary["source"] = dictionary.pop("Source")
    elif "SourceURL" in dictionary:
      dictionary["source"] = dictionary.pop("SourceURL")
    elif "source_url" in dictionary:
      dictionary["source"] = dictionary.pop("source_url")

  return json_data


with open("result.json", "r") as f:
  json_data = json.load(f)

json_data = make_source_property_consistent(json_data)

with open("json_file.json", "w") as f:
  json.dump(json_data, f)
