inventory = {

    'KeyBoard': 12,
    'Mouse': 20,
    'Monitors': 8,
    'Headphones': 15

}

def display_inventory():

    print()
    print('==== Current Inventory ====')

    for item, qauntity in inventory.items():
        print(item + ':', qauntity)

    print()

def add_item():

    item_added = input('What item are we adding? ')

    while True:
        try:

            amount_added = int(input('How many are we adding? '))
            print('Number is Valid!')

            break

        except ValueError:

            print('Invalid number!')

    if item_added not in inventory:
        inventory[item_added] = amount_added

    display_inventory()

def update_qauntity():

    item = input('Item name: ')

    if item in inventory:

        while True:
            try:

                qauntity = int(input('New qauntity? '))
                print('Number is valid!')

                break

            except ValueError:

                print('Invalid number!')

        inventory[item] = qauntity
        print('Inventory updated!')

        display_inventory()

    else:

        print('Item not found.')

def remove_item():

    item_removed = input('What item are we removing? ')

    if item_removed in inventory:

        del inventory[item_removed]
        print('Item removed')

        display_inventory()

    else:

        print('Item not found!')

def save_inventory():

    with open('inventory.txt', 'w') as file:

        for item, qauntity in inventory.items():

            file.write(item + ':' + str(qauntity) + '\n')

    print('Inventory Saved!')

while True:

    print('==== Inventory Menu ====')

    print('1. View inventory')
    print('2. Add item')
    print('3. Update inventory')
    print('4. Remove item')
    print('5. Save inventory')
    print('6. Exit')

    choice = input('Choose an option: ')

    if choice == '1':
        display_inventory()

    if choice == '2':
        add_item()

    if choice == '3':
        update_qauntity()

    if choice == '4':
        remove_item()

    if choice == '5':
        save_inventory()

    if choice == '6':
        print('Goodbye!')

        break