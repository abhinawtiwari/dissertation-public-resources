import json
import requests 
import spacy

def print_values(json_object):
  """Prints the values of all the properties in a JSON object.

  Args:
    json_object: The JSON object to be printed.
  """
  source_url = json_object.get('source_url', None)
  source_text = requests.get(source_url).text

  for property_name, property_value in json_object.items():
    if property_name == "source_url":
        continue
    print(f"Property name: {property_name}")
    if isinstance(property_value, list):
      print("  List of values:")
      for item in property_value:
        if isinstance(item, dict):
          print("    - Dictionary:")
          for key, value in item.items():
            if isinstance(value, str):
                doc1 = nlp(value)
                doc2 = nlp(source_text)
                similarity = doc1.similarity(doc2)
                print(f"      - {key}: {value} - {similarity}")
            
        else:
          if isinstance(item, str):
            doc1 = nlp(item)
            doc2 = nlp(source_text)
            similarity = doc1.similarity(doc2)
            print(f"    - {item} - {similarity}")

    else:
      if isinstance(property_value, str):
        doc1 = nlp(property_value)
        doc2 = nlp(source_text)
        similarity = doc1.similarity(doc2)
        print(f"  Value: {property_value} - {similarity}")
            
def main():
  nlp = spacy.load("en_core_web_lg")
  with open("result.json", "r") as f:
    json_objects = json.load(f)
    
  for json_object in json_objects:
    print_values(json_object)

if __name__ == "__main__":
  main()