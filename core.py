def inventory():
    '''none -> list of inventory'''
    with open('inventory.txt', 'r') as file:
        inv = file.readlines()
        inv = [i.replace('\n', '') for i in inv]
        print(inv)

def total():
    input()
# def damage():

def main():
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
            # else job == 'return':
            #     # damage()


if __name__ == '__main__':
    main()
