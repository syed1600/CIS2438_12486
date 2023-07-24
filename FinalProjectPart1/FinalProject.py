# Syed Ali
# 1799248

import csv  # working with csv files
from datetime import datetime  # this will allow accessing time


class InventoryReports:
    def __init__(self, item_list):
        self.item_list = item_list

    def fullInventory(self):
        with open('FullInventory.csv', 'w') as file:
            itemsList = self.item_list
            keys = sorted(itemsList.keys(), key=lambda x: itemsList[x]['manufacturer'])
            for item in keys:
                id = item
                manufacture = itemsList[item]['manufacturer']
                itemType = itemsList[item]['item_type']
                price = itemsList[item]['price']
                serviceDate = itemsList[item]['service_date']
                damaged = itemsList[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, manufacture, itemType, price, serviceDate, damaged))

    def inventoryList(self):
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            itemType = items[item]['item_type']
            if itemType not in types:
                types.append(itemType)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open(file_name, 'w') as file:
                for item in keys:
                    id = item
                    manufacture = items[item]['manufacturer']
                    price = items[item]['price']
                    serviceDate = items[item]['service_date']
                    damaged = items[item]['damaged']
                    itemType = items[item]['item_type']
                    if type == itemType:
                        file.write('{},{},{},{},{}\n'.format(id, manufacture, price, serviceDate, damaged))

    def pastService(self):
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime("%m/%d/%Y",
                                                                    items[x]['service_date']).date())
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacture = items[item]['manufacturer']
                itemType = items[item]['item_type']
                price = items[item]['price']
                serviceDate = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(serviceDate, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:  # list if it damaged
                    file.write('{},{},{},{},{},{}\n'.format(id, manufacture, itemType, price, serviceDate, damaged))

    def damagedInventory(self):
        items = self.item_list
        # order to file based on price
        keys = sorted(items.keys(), reverse=True,
                      key=lambda x: items[x]['price'])
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufactureName = items[item]['manufacturer']
                itemTyp = items[item]['item_type']
                price = items[item]['price']
                serviceDate = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, manufactureName, itemTyp, price, serviceDate))


if __name__ == '__main__':  # main program
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv',
             'ServiceDatesList.csv']  # create list of input files and read every files
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manufacture = line[1]
                    itemType = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manufacture.strip()
                    items[item_id]['item_type'] = itemType.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    serviceDate = line[1]
                    items[item_id]['service_date'] = serviceDate

    inventory = InventoryReports(items)
    # Creating all the output files
    inventory.fullInventory()
    inventory.pastService()
    inventory.damagedInventory()
    inventory.inventoryList()
    print("csv files generated")
