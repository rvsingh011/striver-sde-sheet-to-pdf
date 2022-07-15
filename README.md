# SDEtoPDF

This repo contains code for converting the SDE sheet given here (https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/) to PDF. 

#### How to run?

There are two choices of the code language. Based on the need pass "cpp" or "java" to get the code samples in the same format. 

```
pip install requirements.txt  # installs dependecies. 
python run main.py cpp     # For CPP code samples in the PDF
python run main.py java    # For Java code samples in the PDF
```

TODO - 
1. Generate one PDF instead of PDF per problem, may be thorugh an argument.
2. Beautify the HTML template with some script if possible. 
3. Add proper argument parser so user can point to the output directory.
4. Support both language code generation, Currently user can get code for CPP or JAVA.  

