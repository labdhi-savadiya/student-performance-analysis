# Student Performance Data Analysis

## Project objective
Analyze student study hours and marks using Python, Pandas, NumPy, and Matplotlib.

## Files
- `student_performance.csv`: practice dataset with a few missing values and one duplicate row.
- `analysis.py`: complete analysis script.
- `README.md`: project overview and instructions.

## Requirements
Python 3.12 or compatible, pandas, numpy, matplotlib.

Install libraries:
```bash
python -m pip install pandas numpy matplotlib
```

## Run
Keep `analysis.py` and `student_performance.csv` in the same folder, then run:
```bash
python analysis.py
```

## What the script does
1. Loads the CSV and checks shape, columns, data types, and summary.
2. Counts missing values and duplicate rows.
3. Removes duplicate rows.
4. Fills missing numeric values with their column mean.
5. Prints descriptive statistics.
6. Saves three graphs in the `graphs` folder: marks by student, study hours vs marks, and marks histogram.

## Important note
This is a learning dataset, not real student records. Mean imputation is used here for practice; in a real analysis, the cleaning method should be selected based on context and documented.
