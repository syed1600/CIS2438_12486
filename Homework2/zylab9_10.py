# Syed Ali
# 1799248


import csv

filename = input()
f = open(filename)
data = csv.reader(f, delimiter=',')
words = []
for row in data:
    for word in row:
        words.append(word.strip())

for i in range(len(words)):
    if words[i] not in words[:i]:
        count = 0
        for w in words:
            if words[i] == w:
                count += 1
        print(words[i], count)
f.close()
