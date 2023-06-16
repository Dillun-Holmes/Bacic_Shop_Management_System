#SJ Pretorius
#Dillun Holmes

class ctuStock:
    def __init__(self, shopName, shopLocation, customers, sales, returns):
        self.shopName = shopName
        self.shopLocation = shopLocation
        self.customers = int(customers)
        self.sales = int(sales)
        self.returns = int(returns)

    @staticmethod
    def nameCheck(name):
        if name != '':
            passed = 1
        else:
            passed = 0
        return passed

# Initializing the objects
shop1 = ctuStock('Default', 'Default', 0, 0, 0)
shop2 = ctuStock('Default', 'Default', 0, 0, 0)
shop3 = ctuStock('Default', 'Default', 0, 0, 0)
shop4 = ctuStock('Default', 'Default', 0, 0, 0)

# Initializing the lists
itemName = []
itemPrice = []
itemStock = []

# Stocks menu
def stocks():
    while True:
        print('''
Stocks
1. Add Product
2. Update Product
3. Remove Product
4. Display Product
5. Exit
''')
        act = input('Enter your choice: ')
        if act == '1':
            addStock()
        elif act == '2':
            updateStock()
        elif act == '3':
            removeStock()
        elif act == '4':
            displayStock()
        elif act == '5':
            exit()
        else:
            print('Invalid selection!')

# Display stocks
def displayStock():
    print('\nDisplay Stock')
    if len(itemName) == 0:
        print('No Stock!')
    else:
        for i in range(len(itemName)):
            print(f'{i+1}. {itemName[i]}///R{round(itemPrice[i], 2)}{itemStock[i]} available in stock')
    input()

# Add stock
def addStock():
    print('\nAdd Stock')
    # Input name for new item and check if it is not blank
    while True:
        name = input('Enter new item name: ')
        valid = ctuStock.nameCheck(name)
        if valid == 1:
            break
        else:
            print('Name cannot be blank!')

    # Input price for new item
    while True:
        price = input('Enter price for new item: R')
        try:
            price = float(price)
            break
        except ValueError:
            print('Only numbers!')

    # Input quantity of item
    while True:
        qt = input('Enter quantity: ')
        if qt.isdigit():
            qt = int(qt)
            break
        else:
            print('Only numbers!')

    # Add to lists
    itemName.append(name)
    itemPrice.append(price)
    itemStock.append(qt)
    print('Stock successfully added!')
    stocks()

def displayStock():
    print('Stock:')
    for i in range(len(itemName)):
        print(f'{i+1}. {itemName[i]}    ///   R{round(itemPrice[i], 2)}    ///   {itemStock[i]}    ///   available in stock')

def updateStock():
    print('\nUpdate Stock')
    if len(itemName) == 0:
        print('No Stock!')
    else:
        displayStock()
        print('\n')
        updatenext = input('Enter the item ID (0 to cancel): ')
        while True:
            choice = updatenext
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    return
                elif 1 <= choice <= len(itemName):
                    break
            print('Invalid choice!')

        # Input new details
        while True:
            name = input('Enter new item name: ')
            valid = ctuStock.nameCheck(name)
            if valid == 1:
                break
            else:
                print('Name cannot be blank!')

        while True:
            price = input('Enter price for new item: R')
            try:
                price = float(price)
                break
            except ValueError:
                print('Only numbers!')

        while True:
            qt = input('Enter quantity: ')
            if qt.isdigit():
                qt = int(qt)
                break
            else:
                print('Only numbers!')

        # Print the input values
        print('Input values:')
        print(f'Item Name: {name}')
        print(f'Price: R{price}')
        print(f'Quantity: {qt}')

        # Update the item details in the lists
        itemName[choice - 1] = name
        itemPrice[choice - 1] = price
        itemStock[choice - 1] = qt
        print('Stock successfully updated!')

        # Print the updated stock
        displayStock()

# Remove stock
def removeStock():
    print('\nRemove Stock')
    if len(itemName) == 0:
        print('No Stock!')
    else:
        displayStock()
        while True:
            choice = input('Enter the item ID (0 to cancel): ')
            if choice.isdigit():
                choice = int(choice)
                if choice == 0:
                    return
                elif 1 <= choice <= len(itemName):
                    break
            print('Invalid choice!')

        # Remove the item from the lists
        itemName.pop(choice - 1)
        itemPrice.pop(choice - 1)
        itemStock.pop(choice - 1)
        print('Stock successfully removed!')
        stocks()

stocks()


