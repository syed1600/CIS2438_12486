# Syed Ali
# 1799248

# Input
Words = input("")
# Create list of words
ListOfWords = Words.split()

Words_freq = {}  # Create an empty dictionary Words_freq

# loop run
for i in range(0, len(ListOfWords)):
    word = ListOfWords[i]
    if word not in Words_freq:
        Words_freq[word] = 1
    else:
        Words_freq[word] = Words_freq[word] + 1  # Increment by 1

for i in range(0, len(ListOfWords)):
    print(ListOfWords[i], Words_freq[ListOfWords[i]])
