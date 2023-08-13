import json
import requests
import spacy
from bs4 import BeautifulSoup


def get_source_text(url):
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for non-successful status codes
  soup = BeautifulSoup(response.content, 'html.parser')
  description_elements = soup.find_all('p', dir='ltr')
  descriptions = [element.text.strip() for element in description_elements] if description_elements else ['Description not found']

  for description in descriptions:
    try:
        if description.startswith('http'):
            description_response = requests.get(description)
            description_soup = BeautifulSoup(description_response.content, 'html.parser')
            # Extract all paragraph elements from the description page
            paragraph_elements = description_soup.find_all('p')
            paragraphs = [element.text.strip() for element in paragraph_elements] if paragraph_elements else []
            # Write the scraped data to the file
            text += 'URL: ' + description + '\n'
            for paragraph in paragraphs:
                text += '- ' + paragraph + '\n'
            text += '\n'
        else:
            text += '- ' + description + '\n'
    except Exception as e:
        print("An error occurred:", str(e))
        continue

  return text

def verify_correctness_similarity(json_object):
  """Prints the values of all the properties in a JSON object, and writes the similarity with source text to a file.

  Args:
    json_object: The JSON object to be printed.
  """
  source_url = json_object.get('source_url', None)
  source_text = get_source_text(source_url)

  with open("result.txt", "a") as f:
    for property_name, property_value in json_object.items():
      if property_name == "source_url":
        print(property_value)
        f.write(f"Property name: {property_name}\n")
        continue
      f.write(f"Property name: {property_name}\n")
      if isinstance(property_value, list):
        f.write("  List of values:\n")
        for item in property_value:
          if isinstance(item, dict):
            f.write("    - Dictionary:\n")
            for key, value in item.items():
              if isinstance(value, str):
                  doc1 = nlp(value)
                  doc2 = nlp(source_text)
                  similarity = doc1.similarity(doc2)
                  f.write(f"      - {key}: {value} - {similarity}\n")

          else:
            if isinstance(item, str):
              doc1 = nlp(item)
              doc2 = nlp(source_text)
              similarity = doc1.similarity(doc2)
              f.write(f"    - {item} - {similarity}\n")

      else:
        if isinstance(property_value, str):
          doc1 = nlp(property_value)
          doc2 = nlp(source_text)
          similarity = doc1.similarity(doc2)
          f.write(f"  Value: {property_value} - {similarity}\n")


def main():
  nlp = spacy.load("en_core_web_lg")
  with open("result.json", "r") as f:
    json_objects = json.load(f)

  for json_object in json_objects:
    verify_correctness_similarity(json_object)


if __name__ == "__main__":
  main()
