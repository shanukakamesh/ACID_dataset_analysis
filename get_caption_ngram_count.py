import json
import nltk
from collections import Counter
import string

# Enter the file path to the captioning annotation file in COCO format (.json files)
file_path = "D:\ACID dataset\Dataset\Captioning Annotation (COCO format).json"

# Path to save the caption ngram count
file_save_name = "caption_ngram_count.csv"

# ngram count greater than ngram_thresh will be saved
ngram_thresh = 50

output_file_path = 'results/' + file_save_name

caption_mapping = {}
captioning_data = []
if file_path:
    with open(file_path, 'r') as file:
        data = json.load(file)

    for annotation in data["annotations"]:
        image_id = annotation["image_id"]
        file_name = next(image["file_name"] for image in data["images"] if image["id"] == image_id)
        caption = annotation["caption"]
        captioning_data.append(caption)
        if file_name not in caption_mapping:
            caption_mapping[file_name] = [caption]
        else:
            caption_mapping[file_name].append(caption)

def generate_ngrams(tokens, n):
    return list(zip(*[tokens[i:] for i in range(n)]))

def  custom_tokenizer(text):
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    return tokens

def count_ngrams(captions, n):
    #tokenized_captions = [nltk.word_tokenize(caption.lower()) for caption in captions]
    tokenized_captions = [custom_tokenizer(caption) for caption in captions]
    ngrams = [generate_ngrams(tokens, n) for tokens in tokenized_captions]
    flattened_ngrams = [gram for sublist in ngrams for gram in sublist]
    ngram_counts = Counter(flattened_ngrams)
    return ngram_counts

ngram_data = []
# Count trigrams in the captioning dataset
for n in range(2,5):
    trigram_counts = count_ngrams(captioning_data, n)
    sorted_trigrams = sorted(trigram_counts.items(), key=lambda x: x[1], reverse=True)
    ngram = []
    for trigram, count in sorted_trigrams[:ngram_thresh]:
        ngram.append([trigram, count])
    ngram_data.append(ngram)
                        
with open(output_file_path, 'w') as file:
    file.write("Index,")
    for i in range(len(ngram_data)):
        file.write(f"{len(ngram_data[i][0][0])}-gram,Count")
        if i < len(ngram_data) - 1:
            file.write(",")
    file.write("\n")
    for i in range(len(ngram_data[0])):
        file.write(f"{i+1},")
        for j in range(len(ngram_data)):
            file.write(f"{' '.join(ngram_data[j][i][0])},{ngram_data[j][i][1]}")
            if j < len(ngram_data)- 1:
                file.write(",")
        file.write("\n")