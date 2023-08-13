import json

def split_list_into_chunks(data_list, chunk_size):
    return [data_list[i:i + chunk_size] for i in range(0, len(data_list), chunk_size)]

# Specify the filename of the JSON file
filename = "result.json"

# Read the JSON file and load the data
with open(filename, "r") as file:
    list_of_dicts = json.load(file)

# Split the list into 10 chunks
chunk_size = len(list_of_dicts) // 10
chunks = split_list_into_chunks(list_of_dicts, chunk_size)

# Save the resulting chunks to a file
output_filename = "chunks.json"
with open(output_filename, "w") as file:
    json.dump(chunks, file, indent=2)

# print(f"Chunks saved to {output_filename}")
