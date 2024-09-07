# Aryabhatta Knowledge University batch result download script

This scipt is written to download end sem results of Aryabhatta Knowledge University.

Requires Python.

## Instructions
1. Install the packages required for the script, namely (use pip or conda), its preferred to create a virtual environment:
	1. pdfkit
	2. PyPDF2
	3. wkhtmltopdf
2. Install wkhtmltopdf binaries from your package manager (windows users may use **[scoop](https://scoop.sh)**)
3. If your package manager doesn't work, install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) manually and add it to PATH.
4. Edit regno, res_link, regno_le and pdf name variables.
  1. regno: Starting registration no.
  2. res_link: Get this link by accessing the result of any student in that specific exam and then removing the registration no. from the end of the link.
  3. regno_le: starting registration no. of lateral entry students.
  4. pdf: Enter the name for the output pdf file.
5. Edit the limits of the loop to fit the no. of students(for both regular and lateral entry students).
6. Run the script.

**The same script can be run for results of BEU, Patna as well, by just modifying
the res_link variable.**
