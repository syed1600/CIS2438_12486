# Syed Ali
# 1799248

# user input
word = str(input())

# Removing white spaces
spaceless_word = word.replace(" ", "")

# reverse string
new = spaceless_word[::-1]

# comparing and using .format to print user's input with whitespaces
if spaceless_word == new:
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))
