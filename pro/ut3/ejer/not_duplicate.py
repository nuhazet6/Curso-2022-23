input_list = ["this", "is", "a", "real", "real", "real", "story"]
unique_words = []
for word in input_list:
    if word not in unique_words:
        unique_words.append(word)
print(unique_words)
