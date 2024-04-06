import json
from collections import Counter

#Enter the file path to the captioning annotation file in COCO format (.json files)
file_path = "D:\ACID dataset\Dataset\Captioning Annotation (COCO format).json"

# Path to save the caption per image count
file_save_name = "caption_duplicate_details.csv"

output_file_path = "results/" + file_save_name

caption_mapping = {}
captioning_count = {}
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

duplicate_data = []
for key, value in caption_mapping.items():
    caption_counts = Counter(value)
    print(caption_counts)
    duplicates = [[count, caption] for caption, count in caption_counts.items() if count > 1]
    if duplicates:
        duplicate_data.append([key, len(value), duplicates])


with open(output_file_path, 'w') as file:
    file.write(f"File name,Total number of captions, Duplicate caption, Number of duplicates\n")
    for item in duplicate_data:
        file.write(f"{item[0]},{item[1]},{item[2][0][1].replace(',', '')},{item[2][0][0]}\n")
        if len(item[2]) > 1:
            for i in range(1,len(item[2])):
                file.write(f",,{item[2][i][1].replace(',', '')},{item[2][i][0]}\n")


