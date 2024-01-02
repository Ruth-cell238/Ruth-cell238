def is_num(question): #check the input user can convert to an integer.
    while True:
        try:
            x = int(input(question)) #start using input user to an integer.
            break
        except ValueError:
            print("That is not a number") # error handeling to inform the use the input is fails
            continue
        return x
 # present and represent pet class   
class Cat():
    def __init__(self):
        self.name = input("\nWhat is your pet's name?\n") # question about pet's name
        self.type = input(f"What type of pet is {self.name}?\n").lower()# question about pet type
        self.color = input(f"What color is {self.name}?\n").lower() #question for pet color
        self.age = is_num(f"How old is {self.name}?\n") #question about pet age

# main function program
def main():
    pet = [] #start andstore an empty list of pet describtion
    response = "y" # start "y" respone loop
    name = input("Hello! What is your name?\n") #question about user name
    while response != "n": #continue looping by asking pet information untile user says 'n'
        pet.append(Cat()) #by creating new pet object and adding to list

        while True:
            response =input("\nDo you have another pet? Y|n: ").lower() # ask the user if have another pet

            if response == "y" or response =="":
                break
            elif response == "n":
                break
            else:
                print("\nYou did not make a correct response, please use 'Y' for yes and 'n' for no.")
                continue

    num_pets = len(pet) # get the number of pets in the list

    with open('My_Pet_List.txt', 'w') as file: # opening a file for writing
        if num_pets == 1:
            file.write(f"{name} has one pet, it's name is {pet[0].name}.\n\n")
        else:
            file.write(f"{name} has {num_pets} pets. Those pet's names are:")
            count = 0
            for i in pet:
                count += 1
                if count == 1:
                    file.write(f" {i.name}")
                elif count != 1:
                    file.write(f", {i.name}")
            file.write(".\n\n")

        for i in pet:
            file.write(f"{i.name} is a {i.color} {i.type} and is {i.age} years old.\n")

# to check if this script is being run as the main program
if __name__ == "__main__":
    main()
else:
    exit    


                    
