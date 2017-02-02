""" this program is to better the inventory of a rental place and
also better the customer interface"""

from datetime import datetime

def inventory():
    '''none -> list of inventory'''
    with open('inventory.txt', 'r') as file:
        inv = file.readlines()
        inv = [i.replace('\n', '') for i in inv]
        print(inv)

def total():
    '''none -> int '''
    name = input("give the name of the thing rented \t")
    types = input("give the type of rental \t")
    if types == "vhs":
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

    date = "{:%B %d, %Y}".format(datetime.now())
    totals = int(price) + (int(repval) * 0.1)
    reciept = str(date) + ' ' + name + " " + types + " " + str(totals)
    print(reciept)



def main():
    ''' the main function that houses all the other ones'''
    user = input("Am I talking to a customer or a employee?\t")
    if user == 'customer':
        inven = input("Would you like to see our inventory?\t")
        if inven == 'yes':
            inventory()
        elif inven == 'no':
            print('Please see an employee')
        else:
            main()
    elif user == 'employee':
            job = input("What is the customer wanting to do? rent or return\t")
            if job == 'rent':
                inventory()
                total()
            elif job == 'return':
                input("is the rental damaged?")


if __name__ == '__main__':
    main()
