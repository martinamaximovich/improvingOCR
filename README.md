# improvingOCR
a command-line utility and Python package for detecting garbage strings in text files

# Installation
pip install pdf 

# Usage
```
# from the command line
usage: pdf.py text_file 
Generates an excel file containing garbage strings in text file

positional arguments:
  text_file          text file provided as input
  
# from within python
from pdf import improvingOCR
improvingOCR.garbageDetector(filepath)

method arguments:
filepath            path to text file 
```
