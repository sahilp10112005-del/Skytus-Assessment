sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

if word in sentence:
    print(f"Yes, '{word}' is present.")
else:
    print(f"No, '{word}' is not present.")