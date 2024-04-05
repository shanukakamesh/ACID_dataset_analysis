def find_duplicates(file_path):
    word_lines = {}
    duplicates = []

    # Open the file and read line by line
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            word = line.strip()
            
            if word in word_lines:
                duplicates.append((word, word_lines[word], line_number))
            else:
                word_lines[word] = line_number

    return duplicates

# Path to the text file
file_path = "D:/ACID dataset/actions-tasks-reduced.txt"

duplicates = find_duplicates(file_path)

# Print duplicates with their line numbers
if duplicates:
    print("Duplicates found:")
    for duplicate in duplicates:
        print(f"Word: {duplicate[0]}, Line {duplicate[1]} and Line {duplicate[2]}")
else:
    print("No duplicates found.")
