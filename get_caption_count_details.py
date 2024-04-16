import json
import matplotlib.pyplot as plt
import numpy as np

#Enter the file path to the captioning annotation file in COCO format (.json files)
file_path = "D:\ACID dataset\Dataset\captioning_annotation_no_duplicates.json"

# Path to save the caption per image count
file_save_name = "caption_count_details.csv"

output_file_path = "results/" + file_save_name

caption_mapping = {}
if file_path:
    with open(file_path, 'r') as file:
        data = json.load(file)

    for annotation in data["annotations"]:
        image_id = annotation["image_id"]
        file_name = next(image["file_name"] for image in data["images"] if image["id"] == image_id)
        caption = annotation["caption"]
        if file_name not in caption_mapping:
            caption_mapping[file_name] = [caption]
        else:
            caption_mapping[file_name].append(caption)
total_captions = 0

caption_count_data = {}
for key, value in caption_mapping.items():
    caption_count = len(value)
    if caption_count not in caption_count_data:
        caption_count_data[caption_count] = [[key,value]]
    else:
        caption_count_data[caption_count].append([key,value])    

caption_count_data = dict(sorted(caption_count_data.items()))

# Saving data
with open(output_file_path, 'w') as file:
    file.write("Number of captions, Number of images\n")
    for key, value in caption_count_data.items():
        file.write(f"{key},{len(value)}\n")
    file.write("\nNumber of captions, Image name,captions\n")
    for key, value in caption_count_data.items():
        for val in value:
            for cap in val[1]:
                file.write(f"{key},{val[0]},{cap.replace(',', '')}\n")