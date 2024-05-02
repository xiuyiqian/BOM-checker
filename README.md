# BOM-Checker

## Overview
In our mechanical design process, we use SolidWorks to create devices, organizing the part files (*.sldprt) across subdirectories, usually involving thousands of files. To manage these files effectively, each is documented in a bill of materials (BOM). 3D CAD part files are susceptible to inadvertent changes, such as adjusting the view angle or accidentally modifying dimensions by hitting Ctrl-S unintentionally. To prevent these from impacting the design, each file's integrity is verified using a SHA256 hash stored in the BOM.

## File Integrity Verification

We use a SHA256 hashing system to distinguish between innocuous changes and critical alterations in the design files.

### How it Works
Each `.sldprt` file in the BOM includes a SHA256 hash serving as a checksum to verify the file's integrity. By recalculating the SHA256 hash of each file and comparing it to the hash listed in the BOM, we can detect unintended file changes.

### Steps to Verify File Integrity
1. **Calculate the SHA256 Hash of Your File:** Use a hashing tool to generate the SHA256 hash of the `.sldprt` file.
2. **Compare the Hash:** Match the newly calculated hash against the hash listed in the BOM. If they align, the file has not been altered unintentionally.
3. **Update the BOM:** Reflect any intentional changes made to a `.sldprt` file in the BOM by updating the corresponding hash.

### Tool Description
This tool compares the actual part files (*.sldprt files) in the folder to the BOM and detects the following types of errors:
- **Modification:** SHA256 hash is inconsistent with what is recorded in the BOM.
- **Missing Files:** `.sldprt` file specified in the BOM but missing from the folder.
- **Unidentified Files:** `.sldprt` file present in the folder but not listed in the BOM.
- **Duplication:** Multiple `.sldprt` files with the same name in different folders.

### Output Format
Errors are categorized and displayed as follows:
- **MODIFIED:** `MODIFIED: <file_path>`
- **MISSING:** `MISSING: <file_name>`
- **UNIDENTIFIED:** `UNIDENTIFIED: <file_path>`
- **DUPLICATE:** `DUPLICATE: <file_path>`
- **CORRECT:** If none of those errors are detected, output "OK".

## Conclusion
Implementing this method ensures all changes to our design files are intentional and verified, maintaining the integrity and reliability of our design process.
