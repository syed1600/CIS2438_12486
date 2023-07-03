# Syed Ali
# 1799248
# my tutor helped me with this but we are unable to get rid of this error on line 36
# code still gives output


import datetime

# Create a dictionary to store the month name as key & month number as value
monthNum = {'january': 1, 'February': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
            'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

# current date
current_date = datetime.datetime.now()

# writing the parsed date
filed = open('parsedDates.txt', 'w')

# Open file for the dates (part b)
with open('inputDates.txt', 'r') as file:

    for date in file:

        # part a
        if date == '-1':
            # Exit from loop
            break

            # Removes newline from date
        date = date.strip()

        if date.find(',') != -1:

            date = date.split()

            month = monthNum[date[0].lower()]

            day = date[1][:-1]

            year = date[2]
            # part c
            if datetime.datetime(int(year), month, int(day)) < current_date:
                validDate = str(month) + '/' + day + '/' + year

                filed.write(validDate + '\n')
file.close()
filed.close()
