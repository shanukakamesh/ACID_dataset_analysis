import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

categories, objects = [], []

# Give the .csv file path to the category_count_data file
input_file_path_categories = "results\category_count_data.csv"

# Give the .csv file path to the caption_count_data file
input_file_path_captions = "results\caption_count_data.csv"


data = []
with open(input_file_path_categories, 'r') as file:
    next(file)
    for line in file:
        category, obj, images = line.strip().split(',')
        obj = int(obj)
        images = int(images)
        data.append([category, obj, images])
for i in data:
    categories.append(i[0])
    objects.append(i[1])
objects = objects[::-1]

captions, count = [], []


data = []
with open(input_file_path_captions, 'r') as file:
    next(file)
    for line in file:
        activity, counts = line.strip().split(',')
        counts = int(counts)
        data.append([activity.capitalize(), counts])

for i in data:
    categories.append(i[0])
    count.append(i[1])
count  = count[::-1]
categories = categories[::-1]

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))

# Bar width
bar_width = 0.8

# Positions of bars on X-axis
bar_positions1 = np.arange(len(count))
bar_positions2 = np.arange(len(count),len(objects) + len(count))
bar_positions = np.arange(len(objects) + len(count))

# Plotting the bars
bars1 = ax.barh(bar_positions2, objects, bar_width, label='Equipment', color=(1, 0.3, 0.3), zorder=2)
bars2 = ax.barh(bar_positions1, count, bar_width, label='Activity/Interaction', color=(0.4, 0.9, 1), zorder=2)

# Y-axis ticks and labels
ax.set_yticks(bar_positions)
ax.set_yticklabels(categories)

# Labels and title
ax.set_ylabel('Term', fontweight='bold')

x_ticks = np.arange(0, max(count) + 250, 250)  # Define x-axis tick range with spacing
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