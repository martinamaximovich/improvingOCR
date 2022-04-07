# improvingOCR
a command-line utility and Python package for detecting garbage strings in PDFs

# Installation
pip install pdf 

# Usage
```
# from the command line
usage: pdf.py pdf_file 
Generates an excel file containing garbage strings in PDF

positional arguments:
  pdf_file          PDF file provided as input
  
# from within python
from pdf import improvingOCR
improvingOCR.garbageDetector(filepath)

method arguments:
filepath            path to PDF file 
```
