# RO-Crate Metadata Generator

### by Data Ingestion Team

---

## 1 - Overview
This script converts metadata from `output.json` to a standardized RO-Crate format (`ro-crate-metadata.json`). The tool is designed to support metadata management and ensure compatibility with RO-Crate standards.

---

## 2 - How to Use

### Step 1: Place Input File
- Ensure `output.json` is in the same directory as the script or specify its path.

### Step 2: Run the Script
- Use the following command:
  ```bash
  python output_to_rocrate.py /path/to/output.json

### Step 3: Verify the Output
- If successful, you will see the following confirmation message:
  ```bash
  Successfully converted /path/to/output.json to /path/to/ro-crate-metadata.json following the RO-Crate standard.

---

### Files
`output_to_rocrate.py`: The main script to convert metadata.

`output.json`: Input metadata file to be converted.

`ro-crate-metadata.json`: Generated metadata file in RO-Crate format.


---

### Current Features
Converts metadata to RO-Crate format with key attributes like:
File names and sizes.
Patient and Sample IDs.
File directories.
Adds machine-readable JSON and human-readable context for research datasets.

---

### Future Improvements
Validate output.json for missing or invalid fields.
Add more metadata fields specific to research needs.
Enhance error handling and logging.
