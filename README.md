# ACID dataset analysis

# Introduction
This reprository provides python codes to analyze the ACID dataset.

# Installation
## Setting up Environment and Dependencies

To create a Conda environment with Python 3.8, run the following command:

```bash
conda create --name acid_dataset python=3.8
```

## Activating the Conda Environment
After creating the environment, activate it using the following command:

```bash
conda activate acid_dataset
```
## Installing Required Packages

```bash
pip install matplotlib
pip install numpy
```
# Analyzing the classes in ACID dataset

[![Number of classes](results/Count%20of%20classes.png)]

- Run `getClasses.py` to generate the above graph and create the [`category_count_data.csv`](results/category_count_data.csv) inside the `results` folder.
- Make sure to change the `folder_path` variable inside the `getClasses.py` according to the location of the folder which contains the detetction annotations in VOC format.