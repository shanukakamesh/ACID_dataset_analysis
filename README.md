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
pip install spacy 
pip install textblob 
pip install nltk 
pip install tqdm
```
- After installing `nltk`, you will need to download additional data for WordNet. Run Python in your terminal or command prompt and execute the following commands:
 ```python
import nltk
nltk.download('wordnet')
```
- After installing spacy, you need to download the English language model. Run the following command in your terminal or command prompt:
```bash
python -m spacy download en_core_web_sm
```
# Analyzing the classes in ACID dataset

![Number of classes](results/Count%20of%20classes.png)

- Run `getClasses.py` to generate the above graph and create the [`category_count_data.csv`](results/category_count_data.csv) inside the `results` folder.
- Make sure to change the `folder_path` variable inside the `getClasses.py` according to the location of the folder which contains the detetction annotations in VOC format.

# Analyzing the captions in ACID dataset

1. First run `getCaptions.py` file. Make sure to change the `file path` variable inside the `getCaptions.py` according to the location of the captioning annotation file which is in COCO format. Then possible tasks/actions will be saved to the [`actions-tasks-original.txt`](actions-tasks-original.txt) file.
2. Take a copy of `actions-tasks-original.txt` file and rename it to [`actions-tasks-reduced.txt`](actions-tasks-reduced.txt). Then remove the keywords that cannot be a task or an action.
3. [`find_duplicates.py`](find_duplicates.py) file can be used to check if any duplicate presents inside the [`actions-tasks-reduced.txt`](actions-tasks-reduced.txt) file.
4. Then run `find_captions_for_tasks.py` file. Make sure to change the `file path` variable inside the `find_captions_for_tasks.py` according to the location of the captioning annotation file which is in COCO format. This code will write the captions of each identified task or action inside the folder [`tasks_data`](tasks_data) as a .txt file.