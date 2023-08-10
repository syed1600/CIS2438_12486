# Syed Ali
# 1799248

# storing data in a dictionary because i am having problems creating a dictionary with given data
data = {"id": [1167234, 2347800, 2390112, 9034210, 7346234, 1009453, 3001265],

        "manufacturer": ["Apple", "Apple", "Dell", "Dell", "Lenovo", "Lenovo", "Samsung"],

        "type": ["phone", "laptop", "laptop", "tower", "laptop", "tower", "phone"],

        "price": [534, 999, 799, 345, 239, 599, 1200]}

while True:
    q = input("Type a query or q to quit: ")
    if q == "q":
        break
    # initialize the manufacturer and type
    item = ""
    types = ""
    # iterate over the dictionary
    for i in data["manufacturer"]:
        if i in q:
            item = i

    for i in data["type"]:
        if i in q:
            types = i

        if item == "" or types == "":
            print("No such item in inventory")
        else:
            details = ["", "", "", 0]
        for i in range(len(data["id"])):

            if data["manufacturer"][i] == item and data["type"][i] == types:

                if details[3] < data["price"][i]:
                    details[0] = data["id"][i]
                    details[1] = data["manufacturer"][i]
                    details[2] = data["type"][i]
                    details[3] = data["price"][i]

        print("Your item is " + str(details[0]) + " " + str(details[1]) + " " + str(details[2]) + " " + str(details[3]))
        extra = []

    for i in range(len(data["id"])):
        if data["type"][i] == types and data["manufacturer"][i] != item:
            extra.append([data["id"][i], data["manufacturer"][i], data["type"][i], data["price"][i]])
        if len(extra) != 0:
            print("You may also like ")
    for i in range(len(extra)):
        print(str(extra[i][0]) + " " + extra[i][1] + " " + extra[i][2] + " " + str(extra[i][3]))
