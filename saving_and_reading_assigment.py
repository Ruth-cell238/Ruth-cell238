 

quary = input("How is your day?").lower() #creat our input question for the user
try:
    with open('data.txt','w') as file: # save data to a "data.txt file"
        file.write(quary) # our text file will write over here
    if quary == "good":
            print("Yay, Glad you have a wonderful day.")# seting the good with comment include when user select.
    elif quary == "bad":
            print("Ohh!, Sorry your day was not as you planned.") # same setting bad with comment
    else:
          print("Invalid input use the correct input")    # we put error input to print instead of crashing    
except ValueError:
     print("Please try the correct input again.")    























 
