#def add(x,y): 
 #   return x + y 
#print(add(1, 3))

#def subtract(x, y=0):
 #   return x - y
#print(subtract(5,1))
#print(subtract(4))

#def product(x, y=2):
 #   return x * y
#print(product (6,8))
#print(product (7))
#print(product ())

def get_pos(prompt="Enter a postive whole number: "):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("You must enter a postive number.")
            else:
                return num
        except ValueError:
            print("You did not enter a number.")


x = get_pos()
print(x)
cats = get_pos("Enter how many cat's you have: ")   
print(f"You have {cats} cats.")
         

