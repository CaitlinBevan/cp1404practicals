"""
CP1404/CP5632 Practical
Word Occurrences
"""

words_dict = {}

string = input("Text: ")
word_occurrences = string.split()
word_occurrences.sort()
for words in word_occurrences:
    if words in words_dict:
        words_dict[words] += 1
    else:
        words_dict[words] = 1

for words, counts in words_dict.items():
    print(f"{words:10s} : {counts}")

