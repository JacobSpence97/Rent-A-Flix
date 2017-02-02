def inventory():
    '''none -> list of inventory'''
    with open('inventory.txt', 'r') as file:
        inv = file.readlines()
        inv = [i.replace('\n', '') for i in inv]
        print(inv)
