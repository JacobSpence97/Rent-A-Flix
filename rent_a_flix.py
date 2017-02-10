""" this program is to better the inventory of a rental place and
also better the customer interface"""
import datetime
import core

def main():
    ''' the main function that houses all the other ones'''
    user = input("Am I talking to a customer or a employee?\t")
    if user == 'customer':
        inven = input("Would you like to see our inventory?\t")
        if inven == 'yes':
            print(core.inventory('inventory.txt'))
        elif inven == 'no':
            print('Please see an employee')
        else:
            main()
    elif user == 'employee':
        job = input("What is the customer wanting to do? rent or return or inv?\t").strip().lower()
        if job == 'rent':
            print(core.inventory('inventory.txt'))
            name = input("give the name of the item being rented \t")
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
            date = "{:%B %d, %Y}".format(datetime.datetime.now())
            print(core.total('transaction.txt', name, date, types, price, repval))
        elif job == 'return':
            damage = input('is the rental damaged?\t')
            if damage == 'yes':
                types = input("give the type of rental \t")
                if types == "vhs":
                    repval = 5.00
                elif types == 'dvd':
                    repval = 20.00
                elif types == 'blu-ray':
                    repval = 25.00
                elif types == 'special':
                    repval = 30.00
                elif types == 'comic':
                    repval = 30.00
                return repval
            elif damage == 'no':
                print('please return the customers repval deposit.')
        elif job == 'inv':
            print(core.inventory('inventory.txt'))
            print('Make sure the item isnt already in the inventory')
            item_name = input('what is the name of the item being added?\t')
            core.add_inv('inventory.txt', item_name)
        else:
            main()


if __name__ == '__main__':
    main()
