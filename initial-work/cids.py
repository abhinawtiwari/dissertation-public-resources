# import pandas as pd

# Define the CIDS resource
cids_resource = {
    "Organization": "The organization that developed or deployed the AI system.",
    "Program or Service": "The AI system or its components.",
    "Activity": "The specific action or interaction that took place.",
    "Outcome": "The result of the action or interaction.",
    "Stakeholders": "The people or groups affected by the action or interaction.",
    "Stakeholder Outcomes": "The impact of the action or interaction on the stakeholders.",
    "Impact Report": "A report that documents the impact of the AI system.",
    "Impact Risk": "The potential negative impact of the AI system.",
    "Indicator": "A measure of the impact of the AI system.",
    "Indicator Report": "A report that documents the indicators of the impact of the AI system.",
    "Impact Scale": "The scope of the impact of the AI system.",
    "Impact Depth": "The severity of the impact of the AI system.",
    "Impact Duration": "The length of time the impact of the AI system will last.",
}

# Define the `get_cids_to_annotation()` function
def get_cids_to_annotation():
    """
    Returns a dictionary that maps CIDS terms to annotations.
    """
    return cids_resource

# Define the `get_cids_terms()` function
def get_cids_terms(sentence):
    """
    Returns a list of CIDS terms that are used in a given sentence.
    """
    # Split the sentence into words.
    words = sentence.split()

    # Create a dictionary that maps each word to a CIDS term.
    cids_terms = {}
    for word in words:
        if word in cids_resource:
            cids_terms[word] = cids_resource[word]

    # Return a list of the CIDS terms that were found in the sentence.
    return list(cids_terms.values())

print(get_cids_terms('TikTok was sued for its role in the suicide of a young user'))

# ---

based on the Common Impact Data Standard ontology for representing impact, find the following: Title of the story, Organization, Impact Model, Program, Service, Activity, Input, Output, Outcome, Stakeholder, Stakeholder Outcome, Impact Report, Impact Risk, Indicator, Indicator Report, Impact Scale, Impact Depth, Impact Duration, Source URL, from this link and news links in the content at that link

https://www.aiaaic.org//aiaaic-repository/ai-and-algorithmic-incidents-and-controversies/facebook-australia-news-civil-society-blocks

present the result in json format