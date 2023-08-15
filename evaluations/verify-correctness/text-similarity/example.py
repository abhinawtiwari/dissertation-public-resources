import spacy

# Load the 'en_core_web_lg' model
nlp = spacy.load('en_core_web_lg')

# Define two example texts
text1 = "I love coding in Python"
text2 = "Python programming is awesome"

# Process the texts using the spaCy model
doc1 = nlp(text1)
doc2 = nlp(text2)

# Calculate the similarity between the texts
similarity = doc1.similarity(doc2)

# Print the similarity score
print("Similarity:", similarity)
