# BranchPlotter
Visualizes a parent-branch style directory/version history via the ETE Toolkit.

## Dependencies
- ETE Toolkit (ete3 3.1.2 and higher). Run `pip install ete3` to install.

## Usage
This program is specifically designed to plot a 2 column .csv file containing the directory/version history data as a hierarchical tree. The first column should contain each branch, and the second should contain each branch's parent. In `main.py`, the file `branches_parents.csv` should be changed to point to the desired data file. Formatting options such as `ts.scale` can be used to make the tree visualization easier to read.
