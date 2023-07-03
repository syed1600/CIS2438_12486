# Syed Ali
# 1799248


# takes input from user
word = input()
# removing spaces
word = word.replace(" ", "")

# rev string for storing reversed string of word
rev = ""

for i in word:
    rev = i + rev

    if word == rev:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
