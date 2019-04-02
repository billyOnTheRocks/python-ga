grocery_item = []
item_price = []
total = 0

while True:
    print("========== Welcome to cvs ==========")
    print("Please scan the item and place it in your bag")

    choice = str(input("would you like to add another item?"))

    if choice == 'y':
            item = str(input("add your item"))
            price = float(input("item price"))
            item_price.append(price)
            grocery_item.append(item)
            total += price
            print(total)
    elif choice == 'n':
            print(total)
            print(grocery_item, item_price)
            exit()




















