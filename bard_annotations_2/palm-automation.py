"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm

palm.configure(api_key="")

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
prompt = f"""<Literal xml:lang="en">The StakeholderOutcome specifies for a specific Stakeholder, a more specific outcome, whether the Outcome will have a positive, negative, or neutral affect on the Stakeholder, and the nature of the impact:
•	hasCode: Associates codes from standard codelists with the StakeholderOutcome.
•	forStakeholder: Identifies the Stakeholder affected.
•	forOutcome: Identifies the more general outcome this is part of.
•	fromPerspectiveOf: Identifies the Stakeholder who is determining the importance of the Impact.
•	hasImportance: Specifies the nature of the importance. One of {“high importance”, “moderate important”, “neutral”, “unimportant”}.
•	isUnderserved: A Boolean that denotes if the stakeholder is underserved in relation to their specific outcome.
•	intendedImpact: Identifies the intended direction of the change – note that ImpactReport captures the actual direction.
•	hasIndicator: Identifies the set of Indicators the Organization assigns to the Outcome but are specific to this Stakeholder.
•	hasImpactReport: identifies the set of ImpactReport that report on the results pertaining to each Outcome.
•	org:hasName: string that is name of the StakeholderOutcome.
•	org:hasDescription: string that is description of the StakeholderOutcome.</Literal>

<Literal xml:lang="en">The Stakeholder class is a subclass of an Organization or Person. It identifies what activities they perform using the performs property, where they are located geographically using the i72:located_In property. Some methods for measuring impact, such as a Social Return on Investment, require that Social Purpose Organizations distinguish between the beneficiary and contributing stakeholders. A BeneficiaryStakeholder is a stakeholder that benefits from a logic model’s outcome. A ContributorStakeholder is a stakeholder that contributes input to ensure a service can produce outcomes. These are explicitly defined as separate classes to highlight the fact that a contributor stakeholder is not always the same instance as the beneficiary stakeholder. The distinction is available in the ontology but is not required. 

Stakeholder contains the following properties:
•	hasName (title): A title for the stakeholder as a string.
•	hasDescription: A general description of the stakeholder as a string.
•	hasCatchmentArea: Specifies the regional span of the stakeholders.
•	hasStakeholderCharacteristic: Specifies characteristics of the stakeholder 
•	performs: Links to the activities performed by the stakeholder.
•	i72:located_in: Links to the specific geographic area in which the stakeholder is located.
•	oep:part of: Links the Impact Model that the stakeholder is being specified for.</Literal>

<Literal xml:lang="en">ImpactRisk “assesses the likelihood that impact will be different than expected, and that the difference will be material from the perspective of people or the planet who experience impact.” Stating the riskiness of the impact is important for interpreting the subsequent results. The Impact Management Project recommends that as part of any impact assessment, the risk of the impact be considered as one of the five dimensions of performance. 
The following defines the taxonomy of risk and key properties:
•	forOutcome: Identifies the Outcome the risk is associated with.
•	hasLikelihood: Identifies the likelihood that the risk will occur.
•	hasConsequence: Identifies the degree of impact the risk could have.
•	hasMitigation: A string that specifies a mitigation plan or references a document.
•	hasIdentifier: A unique identifier for this risk.
•	hasDescription: A description of this risk.</Literal>

consider the above 3 definitions for StakeholderOutcome, stakeholder and ImpactRisk and find these three for https://www.aiaaic.org/aiaaic-repository/ai-and-algorithmic-incidents-and-controversies/virginia-non-violent-risk-assessment"""

response = palm.generate_text(
  **defaults,
  prompt=prompt
)
print(response.result)