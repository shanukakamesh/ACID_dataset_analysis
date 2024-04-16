import json
from collections import defaultdict
from textblob import TextBlob
from nltk.corpus import wordnet
import spacy

from tqdm import tqdm

#Enter the file path to the captioning annotation file in COCO format (.json files)
file_path = "D:\ACID dataset\Dataset\Captioning Annotation (COCO format).json"
#Path to save the actions/tasks
file_save_path = "actions-tasks-original.txt"

caption_mapping = {}
captioning_data = []
if file_path:
    with open(file_path, 'r') as file:
        data = json.load(file)

    for annotation in data["annotations"]:
        image_id = annotation["image_id"]
        file_name = next(image["file_name"] for image in data["images"] if image["id"] == image_id)
        caption = annotation["caption"]
        captioning_data.append(caption)
        if file_name not in caption_mapping:
            caption_mapping[file_name] = [caption]
        else:
            caption_mapping[file_name].append(caption)

nlp = spacy.load("en_core_web_sm")

# Function to merge tasks and actions with synonyms
def merge_tasks_actions(tasks_actions, synonyms):
    merged_tasks_actions = defaultdict(list)
    for task_action in tasks_actions:
        found = False
        for key, values in synonyms.items():
            if task_action in values:
                merged_tasks_actions[key].append(task_action)
                found = True
                break
        if not found:
            merged_tasks_actions[task_action].append(task_action)
    return merged_tasks_actions

# Function to extract tasks and actions
def extract_tasks(text):
    tasks = []
    doc = nlp(text)
    for token in doc:
        if token.pos_ == "VERB":
            tasks.append(token.text)
        elif token.dep_ == "compound":
            tasks.append(token.text)
    return tasks

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def correct_spelling(tasks_actions):
    corrected_tasks_actions = []
    for task_action in tasks_actions:
        corrected_task_action = TextBlob(task_action).correct().raw
        corrected_tasks_actions.append(corrected_task_action)
    return corrected_tasks_actions

# Extract tasks/actions/interactions from captioning data
total_iterations = len(captioning_data)
progress_bar = tqdm(total=total_iterations, desc="Processing")

actions = []
for caption in captioning_data: 
    tasks_actions = extract_tasks(caption)
    corrected_tasks_actions = correct_spelling(tasks_actions)
    synonyms = {}
    for task_action in corrected_tasks_actions:
        synonyms[task_action] = get_synonyms(task_action)
    
    merged_tasks_actions = merge_tasks_actions(corrected_tasks_actions, synonyms)
    for task in merged_tasks_actions:
        if task not in actions:
            actions.append(task)
    progress_bar.update(1)
progress_bar.close()

for a in actions:
    print(a)

# Open the file in write mode
with open(file_save_path, "w") as file:
    # Write each string to the file, one per line
    for string in actions:
        file.write(string + "\n")
