import json
from collections import defaultdict

# Enter the file path to the captioning annotation file in COCO format (.json files)
file_path = "D:\ACID dataset\Dataset\Captioning Annotation (COCO format).json"

# Path to save the new captioning annotation JSON file without duplicates
new_file_path = "D:\ACID dataset\Dataset\captioning_annotation_no_duplicates.json"

# Dictionary to store unique captions for each image
unique_captions = defaultdict(list)

if file_path:
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Populate the dictionary with unique captions for each image
    for annotation in data["annotations"]:
        image_id = annotation["image_id"]
        caption = annotation["caption"]
        unique_captions[image_id].append(caption)

    # Create a new JSON structure with annotations containing only unique captions
    new_data = {"images": data["images"], "annotations": []}
    i = 0
    for image_id, captions in unique_captions.items():
        for caption in set(captions):  # Remove duplicates
            i = i + 1
            new_data["annotations"].append({"id": i, "image_id": image_id, "caption": caption})

    # Write the new JSON structure to a new file
    with open(new_file_path, 'w') as new_file:
        json.dump(new_data, new_file, indent=4)
