import os

# Give the path of the folder which contains the .txt files of tasks/actions
folder_path = "D:/ACID dataset/tasks_data"

#  This will print tasks/actions which have a count greater than count_thresh
count_thresh = 250

def count_captions(file_path):
    with open(file_path, 'r') as file:
        captions_count = 0
        for line in file:
            if line.startswith("---"):
                captions_count += 1
    return captions_count

category_counts = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path) and file_path.endswith('.txt'):
        category = os.path.splitext(filename)[0]
        captions_count = count_captions(file_path)
        category_counts.append([category, captions_count])

category_counts.sort(key=lambda x: x[1], reverse=True)

for item in category_counts:
    if (item[1]>count_thresh):
        print(item)
