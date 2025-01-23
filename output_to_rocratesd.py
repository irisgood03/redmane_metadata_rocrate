import json

def convert_output_to_ro_crate(input_file, output_file):
    """
    Converts the provided output.json to ro-crate-metadata.json following RO-Crate standards.

    :param input_file: Path to the input JSON file (output.json)
    :param output_file: Path to the output JSON file (ro-crate-metadata.json)
    """
    try:
        # Load the input JSON
        with open(input_file, 'r') as file:
            data = json.load(file)

        # Start building the RO-Crate metadata
        ro_crate_metadata = {
            "@context": "https://w3id.org/ro/crate/1.1/context",
            "@graph": [
                {
                    "@id": "./",
                    "@type": "Dataset",
                    "hasPart": [],
                    "description": "RO-Crate for the given dataset"
                }
            ]
        }

        # Add raw files to the RO-Crate
        raw_files = data.get("data", {}).get("files", {}).get("raw", [])
        for file_entry in raw_files:
            # Add file to hasPart
            ro_crate_metadata["@graph"][0]["hasPart"].append(file_entry["file_name"])

            # Add file metadata
            ro_crate_metadata["@graph"].append({
                "@id": file_entry["file_name"],
                "@type": "File",
                "contentSize": file_entry["file_size"],
                "encodingFormat": "application/octet-stream",
                "identifier": {
                    "patient_id": file_entry["patient_id"],
                    "sample_id": file_entry["sample_id"]
                },
                "path": file_entry["directory"]
            })

        # Write the RO-Crate metadata to the output file
        with open(output_file, 'w') as output:
            json.dump(ro_crate_metadata, output, indent=4)

        print(f"Successfully converted {input_file} to {output_file} following the RO-Crate standard.")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Input and output file paths
input_file = "/Users/irisshin/Desktop/untitled folder/output.json"
output_file = "/Users/irisshin/Desktop/untitled folder/ro-crate-metadata.json"

# Run the conversion
convert_output_to_ro_crate(input_file, output_file)

# Convert to RO-Crate format
convert_output_to_ro_crate(input_file, output_file)



