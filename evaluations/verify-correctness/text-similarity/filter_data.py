import json

def filter_dictionaries(json_data):
    """
    Filters a list of dictionaries to only those that have the impact_risk property.

    Args:
        json_data: A list of dictionaries.

    Returns:
        A list of dictionaries that have the impact_risk property.
    """
    filtered_dictionaries = []

    for dictionary in json_data:
        # print(dictionary) # Moved print statement here for clarity and debugging purposes
        if "impact_risk" in dictionary:
            filtered_dictionaries.append({
                "source": dictionary["source"],
                "impact_risk": dictionary["impact_risk"]
            })
        else:
            for property in dictionary:
                if isinstance(dictionary[property], dict):
                    if "impact_risk" in dictionary[property]:
                        filtered_dictionaries.append({
                            "source": dictionary["source"],
                            "impact_risk": dictionary[property]["impact_risk"]
                        })

    return filtered_dictionaries

# 
with open("data.json", "r") as f:
    json_data = json.load(f)

filtered_dictionaries = filter_dictionaries(json_data)

with open("filtered_json_file.json", "w") as f:
    json.dump(filtered_dictionaries, f)
