import json
from tqdm import tqdm
import time

#Enter the file path to the captioning annotation file in COCO format (.json files)
file_path = "D:\ACID dataset\Dataset\Captioning Annotation (COCO format).json"
#Captions of each identified task or action is saved inside this folder as a .txt file
output_file_path = "tasks_data/"

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

#Importing actions
file_path = "D:/ACID dataset/actions-tasks-reduced.txt"
words = []
with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            # Remove leading/trailing whitespaces and newline characters
            word = line.strip()
            words.append([word,line_number])

total_iterations = len(words)
progress_bar = tqdm(total=total_iterations, desc="Processing")

results = []
for word in words:
    result = {}
    temp = []
    for key, value in caption_mapping.items():
        for item in value:
            if word[0] in item:
                if key not in temp:
                    temp.append(key)
                temp.append(item)
    if temp:
        result[word[0]] = temp
        results.append([result,word[0]])
    time.sleep(0.1)
    progress_bar.update(1)
progress_bar.close()

# Function to write dictionary to text file
def write_dict_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for key, values in dictionary.items():
            file.write(f"-{key}\n")
            for value in values:
                if value.endswith('.jpg'):
                    file.write(f"--{value}\n")
                else:
                    file.write(f"---{value}\n")
            file.write("\n")

# Write the dictionary to the text file
for item in results:
    write_dict_to_file(item[0], output_file_path + item[1] + '.txt')
