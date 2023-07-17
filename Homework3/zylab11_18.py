# Syed Ali
# 1799248

# reading list of integers entered by the user
nums = input()
user_list = nums.split()

nList = []

for i in user_list:
    if int(i) > -1:
        nList.append(int(i))

nList.sort()  # lowest to highest list

for x in nList:
    print(x, end=' ')
