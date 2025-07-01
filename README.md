## Student Progression Outcome System 

This Python program predicts student progression outcomes at the end of each academic year based on University credit regulations. 

The program takes inputs for:
- Credits at **Pass**
- Credits at **Defer**
- Credits at **Fail**

It then determines the outcome:
- **Progress**
- **Progress (module trailer)**
- **Do not progress – module retriever**
- **Exclude**

The outcomes are displayed and summarised in both horizontal and vertical histograms.


## Features

- **Input validation**:
  - Ensures only integers are entered.
  - Accepts only values in `{0, 20, 40, 60, 80, 100, 120}`.
  - Ensures total credits entered equal 120.

- **Progression logic**:
  - Based on official university progression rules (see table from coursework spec).
  
- **Histograms**:
  - Shows the distribution of outcomes across all entered students.

## How to Run
1. Open a terminal and navigate to the project directory.
2. Run the script using:
```bash
python Python_Coursework_w1823431.py
