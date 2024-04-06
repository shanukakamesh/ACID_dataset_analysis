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
- After installing `nltk`, you will need to download additional data for WordNet and punkt tokenizer resource. Run Python in your terminal or command prompt and execute the following commands:
 ```python
import nltk
nltk.download('wordnet')
nltk.download('punkt')
```
- After installing spacy, you need to download the English language model. Run the following command in your terminal or command prompt:
```bash
python -m spacy download en_core_web_sm
```
# Analyzing the classes in ACID dataset

![Number of classes](results/Count%20of%20classes.png)

- Run [`getClasses.py`](getClasses.py) to generate the above graph and create the [`category_count_data.csv`](results/category_count_data.csv) inside the [`results`](results) folder.
- Make sure to change the `folder_path` variable inside the [`getClasses.py`](getClasses.py) according to the location of the folder which contains the detetction annotations in VOC format.

# Analyzing the captions in ACID dataset

1. First run [`getCaptions.py`](getCaptions.py) file. Make sure to change the `file path` variable inside the [`getCaptions.py`](getCaptions.py) according to the location of the captioning annotation file which is in COCO format. Then possible tasks/actions will be saved to the [`actions-tasks-original.txt`](actions-tasks-original.txt) file.
2. Take a copy of [`actions-tasks-original.txt`](actions-tasks-original.txt) file and rename it to [`actions-tasks-reduced.txt`](actions-tasks-reduced.txt). Then remove the keywords that cannot be a task or an action.
3. [`find_duplicates.py`](find_duplicates.py) file can be used to check if any duplicate presents inside the [`actions-tasks-reduced.txt`](actions-tasks-reduced.txt) file.
4. Then run [`find_captions_for_tasks.py`](find_captions_for_tasks.py) file. Make sure to change the `file path` variable inside the [`find_captions_for_tasks.py`](find_captions_for_tasks.py) according to the location of the captioning annotation file which is in COCO format. This code will write the captions of each identified task or action inside the folder [`tasks_data`](tasks_data) as a .txt file.
5. Next, the caption count of tasks/actions stored inside the the folder [`tasks_data`](tasks_data) can be calculated by using the python script [`count_captions.py`](count_captions.py). Make sure to give the path of the folder which contains the .txt files of tasks/actions as the `folder_path` and change the `count_thresh` variable to print the names of the tasks/actions which have a count greater than that value.
6. Then the [`selected_actions.txt`](selected_actions.txt) file is manually created based on the outputs of the previous step. The reason to create this file manually is to avoid the consideration of unnecessary terms as tasks. (For example: the task `dump` can be misinterprited and it includes the captions which have the words `dump truck`; And also the task `lift` includes all the captions that has the task `lifting`.) When creating this .txt file, it follows the format of `task1,task2,task3-taskName`. (For example: one line of this .txt file can be `dumps,dumping-dump`. In step 7, the python will count all the captions that contain the tasks `dumps`, `dumping` and store their count under the task name `dump`.)
7. After that run [`count_selected_captions.py`](count_selected_captions.py) file to get the caption count of the selected captions which are included in the [`selected_actions.txt`](selected_actions.txt) file. Make sure to give the file path of the text file that contains the details of selected captions as the `file_path`, the path of the folder which contains the .txt files of tasks/actions as the `folder_path`, and the name to save the caption count in .csv format as `output_file_name`. Caption counts are included in the [`caption_count_data.csv`](results/caption_count_data.csv) file.
8. [`visualize_caption_count.py`](visualize_caption_count.py) can be used to plot the caption count. Make sure to give the file path to the [`caption_count_data.csv`](results/caption_count_data.csv) file. The following shows the graph of caption count,
![Number of captions](results/Count%20of%20captions.png)
9. [`visualize_category_and_caption_count.py`](visualize_category_and_caption_count.py) can be used to plot both category and caption count. Make sure to give the file path to the [`category_count_data.csv`](results/category_count_data.csv) file and [`caption_count_data.csv`](results/caption_count_data.csv) file. The following shows the graph of caption count,
![Element distribution of captioning dataset](results/Element%20distribution%20of%20captioning%20dataset.png)

# Analyzing the n-grams in ACID dataset

- Run [`get_caption_ngram_count.py`](get_caption_ngram_count.py) file to generate the n-gram caption count as shown in [`caption_ngram_count.csv`](results/caption_ngram_count.csv) file.
- Make sure to enter the file path to the captioning annotation file in COCO format (.json files) as the `file_path`, set `file_save_name` variable to the name of the .csv file to save the results, and set the `ngram_thresh` variable to save ngram counts greater than `ngram_thresh`.

# Analysing the number of captions per image

- Run [`count_captions_per_image.py`](count_captions_per_image.py) file to generate [`captions_per_image_count.csv`](results/caption_per_image_count.csv) file that contains the captions per image statistic and the following graph.
![Captions per image statistics](results/Captions%20per%20image%20count.png)