""" this program is to better the inventory of a rental place and
also better the customer interface"""


def inventory(filename):
    '''(string) -> (list of inventory)
    takes a file name and prints it out for the user to see'''
    with open(filename, 'r') as file:
        inv = file.readlines()
        for item in inv[1:]:
            return item


def total(filename, name, date, types, price, repval):
    ''' (string,string,string,int,int) -> (string)
    finds the total of the final bill and prints a reciept'''
    totals = int(price) + (int(repval) * 0.1)
    reciept = (str(date) + ' ' + name + " " + types + " " + str(totals)+ '\n')
    with open(filename, 'a') as file:
        file.write(reciept)
    return reciept

def add_inv(filename, item_name):
    """(string, string) -> (string)
    adds new inventory to the inventory file"""
    types = input('what type of rental is it?\t')
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
    item = (item_name + ', ' + types + ', ' + str(price) + ', ' + str(repval) + '\n')
    with open(filename, 'a') as file:
        file.write(item)
