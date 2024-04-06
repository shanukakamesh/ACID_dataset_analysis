import os

# Give the file path to the text file which contains the selected captions in the format of `task1,task2,task3-taskName`
file_path = "D:/ACID dataset/selected_actions.txt"

# Give the path of the folder which contains the .txt files of tasks/actions
folder_path = "D:/ACID dataset/tasks_data"

#Name of the .csv file to store the caption count
output_file_name = "caption_count_data.csv"



output_file_path = "results/" + output_file_name

words = []
with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, 1):
        word = line.strip()
        row = word.split('-')
        words.append([row[0].split(','), row[1]])

# Function to count captions in a text file
def count_captions(file_path):
    with open(file_path, 'r') as file:
        captions_count = 0
        for line in file:
            if line.startswith("---"):
                captions_count += 1
    return captions_count

category_counts = []

# Iterate through each file in the folder
for item in words:
    captions_count =  0
    for file_name in item[0]:
        file_path = folder_path + '/' + file_name  + '.txt'  
        if os.path.isfile(file_path):
            category = item[1]
            captions_count = captions_count + count_captions(file_path)
    category_counts.append([category, captions_count])

print(category_counts)

with open(output_file_path, 'w') as file:
    file.write("activity,count\n")
    for row in category_counts:
        file.write(f"{row[0]},{row[1]}\n")