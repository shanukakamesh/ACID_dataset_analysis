import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Give the .csv file path to the caption_count_data file
input_file_path = "results\caption_count_data.csv"

data = []

with open(input_file_path, 'r') as file:
    next(file)
    for line in file:
        activity, count = line.strip().split(',')
        count = int(count)
        data.append([activity.capitalize(), count])

captions, count = [], []
for i in data:
    captions.append(i[0])
    count.append(i[1])

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width
bar_width = 0.8

# Positions of bars on X-axis
bar_positions = range(len(captions))[::-1]


# Plotting the bars
bars1 = ax.barh([p for p in bar_positions], count, bar_width, label='Number of captions', color=(1,0.3,0.3), zorder=2)


# Y-axis ticks and labels
ax.set_yticks(bar_positions)
ax.set_yticklabels(captions)

# Labels and title
ax.set_ylabel('Term', fontweight='bold')
#ax.set_title('Count of Objects and Images for Different Classes')

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