my_friends = []
question = "y"
while question != "n":
    my_friends.append(input("Enter the name of a friend: "))
    while True:
        question = input("Would you like to add another?\n[Y|n]").lower()
        if question in ["y", "n", ""]:
            break
        else:
            print("Invalid entry.\nUse 'y' for yes, or use 'n' for no.")
print(my_friends)
            