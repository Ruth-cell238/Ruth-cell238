count = 0
while count < 10: 
    print(count)
    count = count + 1
question = "y"
while question == "y":
   question = input("Do you want me to ask you again?\n[y|n]: ")
question = "n"
while question != "y":
    question = input("Do you want to stop?\n[y|n]: ")