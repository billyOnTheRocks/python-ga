grocery_item = []
item_price = []
total = 0

while True:
    print("========== Welcome to cvs ==========")
    print("Please scan the item and place it in your bag")

    item = str(input("Please enter the item"))
    price = float(input("Please enter the price"))
    grocery_item.append(item)
    item_price.append(price)



    print(grocery_item)
    print(item_price)