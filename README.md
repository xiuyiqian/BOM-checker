# Project Name
BOM-Chekcer
## Overview
This repository includes 3D CAD part files, primarily in `.sldprt` format, which are integral to our design process.

## File Integrity Verification
To ensure the integrity of our design files and to prevent accidental modifications that could potentially break the design, we implement a SHA256 hashing system. This system helps in distinguishing innocuous changes, like view angle adjustments, from critical alterations, such as unintended dimension modifications.

### How it Works
Each `.sldprt` file in the Bill of Materials (BOM) includes a SHA256 hash. This hash serves as a checksum to verify the file's integrity. By recalculating the SHA256 hash of each file and comparing it to the hash listed in the BOM, we can detect any unintended file changes.

### Steps to Verify File Integrity
1. **Calculate the SHA256 Hash of Your File:** Use a hashing tool to generate the SHA256 hash of the `.sldprt` file you've worked on.
2. **Compare the Hash:** Check the newly calculated hash against the hash listed in the BOM. If they match, the file has not been altered in an unintended manner.
3. **Update the BOM:** If intentional changes are made to a `.sldprt` file, update the corresponding hash in the BOM to reflect these changes.

### Tool Description 
compare the actual part files ( *.sldprt files) in the folder to the BOM and detect following types of errors.
• Modification of part files (SHA256 hash inconsistent with what is recorded in the BOM)
• Missing part files ( *.sldprt file specified in the BOM but missing from the 
folder)
• Unidentified part files ( *.sldprt file present in the folder but missing from the BOM)
• Duplication of part files (multiple *.sldprt files with the same name in different 
folders)

## Conclusion
This method ensures that all changes to our design files are intentional and verified, maintaining the integrity and reliability of our design process.
