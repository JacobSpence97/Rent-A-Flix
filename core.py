""" this program is to better the inventory of a rental place and
also better the customer interface"""

from datetime import datetime


def inventory(filename):
    '''string -> list of inventory
    takes a file name and prints it out for the user to see'''
    with open(filename, 'r') as file:
        inv = file.readlines()
        inv = [i.replace('\n', '') for i in inv]
        return inv


def total(filename, name, types, price, repval):
    ''' string,string,int,int -> string 
    finds the total of the final bill and prints a reciept'''
    date = "{:%B %d, %Y}".format(datetime.now())
    totals = int(price) + (int(repval) * 0.1)
    reciept = str(date) + ' ' + name + " " + types + " " + str(totals)
    with open(filename, 'w') as file:
        file.write(reciept)
    return reciept
