import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

#Enter the file path to the captioning annotation file in COCO format (.json files)
file_path = "D:\ACID dataset\Dataset\Captioning Annotation (COCO format).json"

# Path to save the caption per image count
file_save_name = "caption_per_image_count.csv"

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
total_captions = 0
for key, value in caption_mapping.items():
    count = len(value)
    total_captions += count
    count = str(count)
    if count in captioning_count:
        captioning_count[count] += 1
    else:
        captioning_count[count] = 1


print(captioning_count)
print(total_captions)
sorted_count = sorted(captioning_count.items(), key=lambda x: int(x[0]))
keys = [item[0] for item in sorted_count]
values = [item[1] for item in sorted_count]
print(sorted_count)

# Saving data
with open(output_file_path, 'w') as file:
    file.write(f"Total number of captions,{total_captions}\n\n")
    file.write("Number of captions, Number of images\n")
    for i in range(len(keys)):
        file.write(f"{keys[i]},{values[i]}\n")

keys = keys[::-1]
values = values[::-1]
# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.8

# Positions of bars on X-axis
bar_positions = range(len(keys))[::-1]

# Plotting the bars
bars1 = ax.barh(keys, values, bar_width, label='Number of captions', color=(1,0.3,0.3), zorder=2, log=True)

ax.set_facecolor((0.9,0.9,0.9))
ax.set_xlabel('Number of images', fontweight='bold')
ax.set_ylabel('Number of captions per image', fontweight='bold')
# Legend
#ax.legend()

# Show gridlines behind the bars
ax.grid(which='major', linestyle='-', linewidth='1', color='white', zorder=0)  # Gridlines behind bars
ax.grid(which='minor', linestyle='-', linewidth='0.4', color='white', zorder=0)  # Gridlines behind bars

# Show plot
plt.tight_layout()
plt.show()