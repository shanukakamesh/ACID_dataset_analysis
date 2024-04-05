import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

#Enter the folder path to the folder that contains the detetction annotation in VOC format (.xml files)
folder_path = "D:\ACID dataset\Dataset\Detection Annotation (VOC format)"

#Enter the name of  the csv file to save the category counts ending .csv 
output_file_name = "category_count_data.csv"

output_file_path = "results/" + output_file_name

bbox_data = {}
if folder_path:
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            xml_file = os.path.join(folder_path, filename)
            tree = ET.parse(xml_file)
            root = tree.getroot()
            image_filename = root.find('filename').text
            image_filename = image_filename.split('.')[0]
            bbox_data[image_filename] = []

            # Iterate over each object in the XML
            for obj in root.findall('object'):
                obj_name = obj.find('name').text
                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)

                # Store bounding box data in the dictionary
                bbox_data[image_filename].append({'class': obj_name, 'bbox': (xmin, ymin, xmax, ymax)})

classes = {}
for file_data in bbox_data.values():
    file_considered = False
    for item in file_data:
        class_name = item['class']
        if class_name not in classes:
            classes[class_name] = {'objects': 1, 'images': 1}
            file_considered = True
        else:
            if not file_considered:
                classes[class_name]['images'] += 1
                file_considered = True
            classes[class_name]['objects'] += 1

categories, objects, images = [], [], [] 
for class_name, counts in classes.items():
    print(f"Class: {class_name}, \t\tObjects: {counts['objects']}, \t\tImages: {counts['images']}")
    categories.append(class_name.replace('_', ' ').capitalize())
    objects.append(counts['objects'])
    images.append(counts['images'])

# Write the data to the text file in CSV format
with open(output_file_path, 'w') as file:
    file.write("category,number of objects,number of images\n")
    for i in range(len(categories)):
        file.write(f"{categories[i]},{objects[i]},{images[i]}\n")


# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.4

# Positions of bars on X-axis
bar_positions = range(len(categories))[::-1]


# Plotting the bars
bars1 = ax.barh([p - bar_width/2 for p in bar_positions], objects, bar_width, label='Number of objects', color=(1,0.3,0.3), zorder=2)
bars2 = ax.barh([p + bar_width/2 for p in bar_positions], images, bar_width, label='Number of images that contain the object', color=(0.4,0.9,1), zorder=2)

# Y-axis ticks and labels
ax.set_yticks(bar_positions)
ax.set_yticklabels(categories)

# Labels and title
ax.set_ylabel('Term', fontweight='bold')
#ax.set_title('Count of Objects and Images for Different Classes')

x_ticks = np.arange(0, max(max(objects), max(images)) + 250, 250)  # Define x-axis tick range with spacing
ax.set_xticks(x_ticks)
ax.set_xlabel('Count', fontweight='bold')

ax.set_facecolor((0.9,0.9,0.9))

# Legend
ax.legend()


# Set major and minor grid distances
major_locator = MultipleLocator(1000)  # Major grid distance
minor_locator = MultipleLocator(250)   # Minor grid distance

ax.xaxis.set_major_locator(major_locator)
ax.xaxis.set_minor_locator(minor_locator)

# Show gridlines behind the bars
ax.grid(which='major', linestyle='-', linewidth='1', color='white', zorder=0)  # Gridlines behind bars
ax.grid(which='minor', linestyle='-', linewidth='0.4', color='white', zorder=0)  # Gridlines behind bars

# Show plot
plt.tight_layout()
plt.show()


