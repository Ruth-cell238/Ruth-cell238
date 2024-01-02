menu_items = {"Burger":14.99, "cheese Burger":16.99, "Fries":7.99, "Drink":6.99}
#print(menu_items)
menu_items["Hotdog"] = 8.99
#print(menu_items)
menu_items.update({"Burger":19.99, "cheese Burger":23.99, "Hotdog":14.99})

#print(menu_items)
#print(menu_items.keys())
#for key in menu_items.keys():
    #print(key)  

#print(menu_items.values())
#for value in menu_items.value():
 #   print(value)

#print(menu_items.items())
#for key, value in menu_items.items():
#    print(key, value)    

#print(menu_items["cheese Burger"])

#price = menu_items["cheese Burger"]
#print(price)

#def get_key(arg, dictionary):
#    for key, value in dictionary.items():
#        if value == arg:
#            return key
        
#x = get_key(23.99, menu_items)
#print(x)        



order = ["cheese Burger", "Hotdog", "Fries", "Drink", "Burger", "Fries", "Drink", "Fries", "Fries", "Drink", "cheese Burger", "Fries", "cheese Burger", "Fries", "Drink", "Drink", "Drink", "Fries", "Burger"]

count = {}
total = 0
for i in order:
    count[i] = count.get(i, 0) + 1
for item, quantity in count.items():
    print(item, quantity)   
    total += menu_items[item] * quantity
print(total)     