import spacy

def compare_nouns_and_verbs(text1, text2):
  """Compares the nouns in text1 with the verbs in text2 using spaCy.

  Args:
    text1: The first text.
    text2: The second text.

  Returns:
    A list of the nouns in text1 that are also verbs in text2.
  """

  doc1 = spacy.load("en_core_web_lg")(text1)
  doc2 = spacy.load("en_core_web_lg")(text2)
  nouns_doc1 = [token.text for token in doc1 if token.pos == "NOUN"]
  nouns_doc2 = [token.text for token in doc2 if token.pos == "NOUN"]
  matching_nouns = []
  for noun in nouns_doc1:
    if noun in nouns_doc2:
      matching_nouns.append(noun)
  return matching_nouns

if __name__ == "__main__":
  text1 = "This is the first text."
  text2 = "This is the second text."
  matching_nouns = compare_nouns_and_verbs(text1, text2)
  print(f"The matching nouns are {matching_nouns}")
