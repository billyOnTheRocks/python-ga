grocery_item = []
item_price = []


while True:
    print("========== Welcome to cvs ==========")
    print("Please scan the item and place it in your bag")

    item = str(input("add your item"))
    price = float(input("item price"))
    item_price.append(price)
    grocery_item.append(item)


    choice = str(input("would you like to add another item?"))

    if choice == 'y':
            total = 0
            total += price
            print(total)
    elif choice == 'n':
            print(total)
            print(grocery_item, item_price)
            exit()




















