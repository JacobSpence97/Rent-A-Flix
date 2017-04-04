""" this program is to better the inventory of a rental place and
also better the customer interface"""
import datetime
import core
from os import system

def main():
    ''' the main function that houses all the other ones'''
    user = input("Am I talking to a customer or a employee? press 'Q or q' to quit \t")
    if user == 'Q' or user == 'q':
        SystemExit()
    elif user == 'customer':
        inven = input("Would you like to see our inventory?\t").lower()
        if inven == 'yes' or inven == 'sure':
            print(core.inventory('inventory.txt'))
            main()
        elif inven == 'no' or inven == 'nah':
            print('Please see an employee')
            main()
        else:
            print('please enter yes/sure or no/nah')
            main()
    elif user == 'employee':
        job = input("What is the customer wanting to do? rent or return or add_inv?\t").strip().lower()
        if job == 'rent':
            print(core.inventory('inventory.txt'))
            name = input("give the name of the item being rented \t")
            types = input("give the type of rental?  vhs,dvd,blu-ray,special,comic \t")
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
            else:
                print('Incorect type')
                main()
            core.removeinv('inventory.txt', name, types, price, repval)
            date = "{:%B %d, %Y}".format(datetime.datetime.now())
            print(core.total('transaction.txt', name, date, types, price, repval))
            main()
        elif job == 'return':
            name = input('what is the name of the renturning rental?\t')
            types = input('what is the type of the rental?\t')
            damage = input('was there any damage to the rental?\t')
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
            core.revenue('revenue.txt', types, damage)
            core.returninv('inventory.txt', name, types, price, repval)
            main()
        elif job == 'add_inv':
            print(core.inventory('inventory.txt'))
            print('Make sure the item isnt already in the inventory')
            item_name = input('what is the name of the item being added?\t')
            types = input('what is the type of rental?  vhs,dvd,blu-ray,special,comic\t')
            core.add_inv('inventory.txt', item_name, types)
            main()
        else:
            print("please enter a correct item")
            main()
    else:
        print("please enter a correct item")
        main()

if __name__ == '__main__':
    main()
