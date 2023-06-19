height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))

area = height * width
paint_needed = area / 350
cans = round(paint_needed)

print('Wall area: ' + str(area) + ' square feet')
print('Paint needed: %.2f gallons' % paint_needed)
print('Cans needed: ' + str(cans) + ' can(s)')

color = input('\nChoose a color to paint the wall:\n')
if color == 'red':
    cost = 35 * cans
elif color == 'blue':
    cost = 25 * cans
elif color == 'green':
    cost = 23 * cans
else:
    cost = 0
print('Cost of purchasing', color, 'paint: $' + str(cost))