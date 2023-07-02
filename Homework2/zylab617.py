#Syed Ali
#1799248


#read password
passs = input()

#replacement
passs = passs.replace('i', '!')
passs = passs.replace('a', '@')
passs = passs.replace('m', 'M')
passs = passs.replace('B', '8')
passs = passs.replace('o', '.')

#adding 'g*s' in the end
passs += 'q*s'

#print new password
print(passs)