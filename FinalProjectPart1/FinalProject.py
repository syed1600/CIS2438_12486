# Syed Ali
# 1799248

import csv
import datetime


class Item:
    def __init__(self, ID=000000, man_name='none', item_type='none', item_price='none', service_date='never',
                 damage='no'):
        self.ID = ID
        self.man_name = man_name
        self.item_type = item_type
        self.item_price = item_price
        self.service_date = service_date
        self.damage = damage


# Sort methods
def sort_by_id(item):
    return item.ID


def sort_by_price(item):
    return item.item_price


def sort_by_service_date(item):
    return item.service_date


def sort_by_man_name(item):
    return item.man_name


# Read data from files

# dictionary using ID as key
item_dict = {}

# This will store item types
item_type_list = []

# Get manufacturer list
with open('ManufacturerList.csv') as file:
    reader = csv.reader(file, delimiter=',')

    for line in reader:
        # Check for damage
        damage = 'no'

        if line[3] != '':
            damage = 'yes'

        id = line[0]
        man_name = line[1]
        item_type = line[2]

        item_type_list.append(item_type)

        # Update dict using id as key
        item_dict[id] = {}
        item_dict[id]['id'] = id
        item_dict[id]['man_name'] = man_name
        item_dict[id]['item_type'] = item_type
        item_dict[id]['damage'] = damage

# Get service dates
with open('ServiceDatesList.csv') as file:
    reader = csv.reader(file, delimiter=',')

    for line in reader:
        id = line[0]
        date = line[1]

        # Update the s dictionary value
        item_dict[id]['service_date'] = date

# Get prices
with open('PriceList.csv') as file:
    reader = csv.reader(file, delimiter=',')

    for line in reader:
        id = line[0]
        price = line[1]

        # Update the dictionary value
        item_dict[id]['item_price'] = float(price)

# Convert the dictionary values
item_models = []

for item in item_dict.values():
    item_models.append(Item(
        ID=item['id'],
        man_name=item['man_name'],
        item_type=item['item_type'],
        item_price=item['item_price'],
        service_date=item['service_date'],
        damage=item['damage'],
    ))

# Full inv
item_models.sort(key=sort_by_man_name)

with open('FullInventory.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')

    for item in item_models:
        writer.writerow(
            [item.ID, item.man_name, item.item_type, item.item_price, item.service_date,
             item.damage])

# item type lists
for item_type in item_type_list:

    items_in_type = []

    for item in item_models:
        if item.item_type == item_type:
            items_in_type.append(item)

    # Sort by ID
    items_in_type.sort(key=sort_by_id)

    # creating the file name
    type_file = item_type.replace(" ", "") + "Inventory.csv"
    with open(type_file, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        for item in items_in_type:
            writer.writerow(
                [item.ID, item.man_name, item.item_price, item.service_date, item.damage])

past_date = []
for item in item_models:
    # Check Date
    date = item.service_date.split("/")
    service_date = datetime.date(int(date[2]), int(date[0]), int(date[1]))
    if service_date < datetime.date.today():
        past_date.append(item)

# Sort by date
past_date.sort(key=sort_by_service_date, reverse=True)

with open('PastServiceDateInventory.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')

    for item in past_date:
        writer.writerow([item.ID, item.man_name, item.item_price, item.service_date, item.damage])

# Damaged items
damaged_items = []
for item in item_models:
    if item.damage == 'yes':
        damaged_items.append(item)

damaged_items.sort(key=sort_by_price, reverse=True)

with open('DamagedInventory.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')

    for item in damaged_items:
        writer.writerow([item.ID, item.man_name, item.item_type, item.item_price, item.service_date])

