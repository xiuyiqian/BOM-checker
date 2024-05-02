# Project Name
BOM-Checker

## OverView
while performing the mechanical design of our devices using a 3D CAD (SolidWorks). Such a mechanical design is a collection of part files ( *.sldprt ) organized in subdirectories and typically contains a few thousand files.
In addition to the CAD part files, we write down all part files in a "part list" file called a bill 
of materials (BOM).
The 3D CAD part files are easy to change (e.g., simply by moving the view angle and accidentally hitting Ctrl-S) and this poses a problem because it is difficult to tell those innocuous changes (e.g., view angle changes) from potentially critical errors (e.g., accidentally dragging and changing an important dimension). To mitigate the chance of breaking the design, this BOM contains a SHA256 hash of each part file ( *.sldprt file) so that we can detect unintentional file changes by calculating the SHA256 hash of actual files and comparing them to the BOM.
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

### Output Format
Errors are categorized and displayed as follows:
- **MODIFIED:** Indicates that a file's current hash does not match its recorded hash in the BOM.
  - Format: `MODIFIED: <file_path>`
- **MISSING:** Indicates a file listed in the BOM cannot be found in the expected location.
  - Format: `MISSING: <file_name>`
- **UNIDENTIFIED:** Refers to a file present in the directory but not listed in the BOM.
  - Format: `UNIDENTIFIED: <file_path>`
- **DUPLICATE:** Indicates that multiple instances of a file are found when only one is expected.
  - Format: `DUPLICATE: <file_path>`
- **CORRECT:** If none of those errors are detected, print OK to stdout.

## Conclusion
This method ensures that all changes to our design files are intentional and verified, maintaining the integrity and reliability of our design process.
