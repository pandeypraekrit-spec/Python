import string

user_input = input("Enter a sentence: ")

cleaned_sentence = " ".join(user_input.split()).lower()


raw_words = cleaned_sentence.split()
words = [word.strip(string.punctuation) for word in raw_words]
words = [word for word in words if word]  

total_words = len(words)

python_count = words.count("python")

longest_word = max(words, key=len) if words else ""


print("\n--- Sentence Analysis Results ---")
print(f"Cleaned Lowercase Sentence : {cleaned_sentence}")
print(f"Total Word Count          : {total_words}")
print(f"Occurrences of 'python'   : {python_count}")
print(f"Longest Word              : {longest_word}")