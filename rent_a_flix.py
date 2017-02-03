from core import *

def main():
    ''' the main function that houses all the other ones'''
    user = input("Am I talking to a customer or a employee?\t")
    if user == 'customer':
        inven = input("Would you like to see our inventory?\t")
        if inven == 'yes':
            print(inventory('inventory.txt'))
        elif inven == 'no':
            print('Please see an employee')
        else:
            main()
    elif user == 'employee':
        job = input("What is the customer wanting to do? rent or return\t")
        if job == 'rent':
            print(inventory('inventory.txt'))
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
            print(total(name, types, price, repval))


if __name__ == '__main__':
    main()
