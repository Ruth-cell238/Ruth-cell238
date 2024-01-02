def is_num(question):
   while True:
        try:
            x = float(input(question))
            return x
        except ValueError:
            print("\nThat is not a number.\n")

shopping_cart = []
response = "y" 

while response != "n":
    item_price = is_num("Enter the price of your item: $")
    shopping_cart.append(item_price)
    response = input("Add more items to your cart? Y|n: ").lower()
    if response == "y" or response == "":
        continue
    elif response == "n":
        continue
    else:
     response = input("\nPlease enter a 'Y' for yes or a 'N' for no:").lower
if len(shopping_cart) >= 25:
    total = sum(shopping_cart)* 0.75 #25% discount for 25 items or more
elif len(shopping_cart) >= 12:
    total = sum(shopping_cart) * 0.85 #15% discount for 12 items or more
else:
    total = sum(shopping_cart) 

tax = total * 1.08
print(f"The total is: ${tax:.{2}f}.")


