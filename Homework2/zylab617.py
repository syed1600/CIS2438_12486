# Syed Ali
# 1799248


# read password
password = input()

# replacement
password = password.replace('i', '!')
password = password.replace('a', '@')
password = password.replace('m', 'M')
password = password.replace('B', '8')
password = password.replace('o', '.')

# adding 'g*s' in the end
password += 'q*s'

# print new password
print(password)
