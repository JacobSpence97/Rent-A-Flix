""" this program is to better the inventory of a rental place and
also better the customer interface"""


def inventory(filename):
    '''(string) -> (list of inventory)
    takes a file name and prints it out for the user to see'''
    string = ''
    with open(filename, 'r') as file:
        inv = file.readlines()
        for item in inv:
            string += item
        return string


def total(filename, name, date, types, price, repval):
    ''' (string,string,string,int,int) -> (string)
    finds the total of the final bill and prints a reciept'''
    tax = (int(price) * .07)
    totals = int(price) + (int(repval) * 0.1) + tax 
    reciept = (str(date) + ' ' + name + " " + types + " " + str(totals) + '\n')
    with open(filename, 'a') as file:
        file.write(reciept)
    return reciept


def add_inv(filename, item_name, types):
    """(string, string) -> (string)
    adds new inventory to the inventory file"""
    if types == 'vhs':
        price = 2.00
        repval = 5.00
    elif types == 'dvd':
        price = 5.00
        repval = 20.00
    elif types == 'blu-ray':
        price = 8.00
        repval = 25.00
    elif types == 'special':
        price = 10.00
        repval = 30.00
    elif types == 'comic':
        price = 10.00
        repval = 30.00
    else:
        print("invalad type")
        add_inv(filename, item_name, types)

    item = (item_name + ', ' + types + ', ' + str(price) + ', ' + str(repval) + '\n')
    with open(filename, 'a') as file:
        file.write(item)
    return item


def removeinv(filename, name, types, price, repval):
    ''' (str, str, str, str,str) -> None
    removes item from inventory when rented'''
    inv = inventory(filename)
    inven = inv.split('\n')
    items = (name + ',' + types + ',' + '{:.2f}'.format(price) + ',' + '{:.2f}'.format(repval))
    string = ''
    if items in inven:
        inven.pop(inven.index(items))
        for item in inven:
            string += item + '\n'
        with open(filename, 'w') as file:
            file.write(string)
        return string
    else:
        with open(filename, 'w') as file:
            file.write(inv)
        return inv


def returninv(filename, name, types, price, repval):
    ''' (str, str, str, str,str) -> None
    returns an item from inventory when rented'''
    inv = inventory(filename)
    inven = inv.split('\n')
    items = (name + ',' + types + ',' + '{:.2f}'.format(price) + ',' + '{:.2f}'.format(repval))
    string = ''
    if items not in inven:
        inven.append(items)
        for item in inven:
            string += item + '\n'
        with open(filename, 'w') as file:
            file.write(string)
        return string
    else:
        with open(filename, 'w') as file:
            file.write(inv)
        return inv

def revenue(filename, types, damage):
    '''(str,str,str) -> None
     gets the total revenue of the transaction and writes it to a txt file'''
    if types == 'vhs':
        price = 2.00
        repval = 5.00
    elif types == 'dvd':
        price = 5.00
        repval = 20.00
    elif types == 'blu-ray':
        price = 8.00
        repval = 25.00
    elif types == 'special':
        price = 10.00
        repval = 30.00
    elif types == 'comic':
        price = 10.00
        repval = 30.00
    else:
        print("invalad type")
    deposit = int(repval) * 0.1
    revenue = int(price) + deposit
    if damage == 'yes':
        revenue += (repval - deposit)
    elif damage == 'no':
        revenue -= deposit
    
    with open(filename, 'a') as file:
        file.write(str(revenue) + '\n')
        return revenue