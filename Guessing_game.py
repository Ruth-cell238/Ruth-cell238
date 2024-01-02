# generates random number between 1 and 100 for the function
import random
random_number = random.randint(1, 100)
Guess = 0 # we set initial attempt 
attempt = 5 # we set maximam attempt
while Guess != random_number:
        try:
            Guess = int(input("Guess number: ")) #set the user to guess number
            if Guess < 1:
                 print("Not accept number less than 1.")
            elif Guess > 100:
                 print("Not accept number greater than 100.")  #if user enter greater 100 or less 1number,it comments not acceptable      
            if Guess < random_number:
                print("Guess a higher number") # set the user guessing number is higer or lower
            elif Guess > random_number:
                print("Guess lower number")
            elif Guess == random_number: # if the user guess the correct number , user win!
                print("You won! The secret number was", random_number)       
        except ValueError: 
            print("Please enter valid number") # set the user to try again and return if use invalid input
            #if attempt >= 5:
                 #print("attempt is over the limit", + "You lose!") # max attempt is not responding
play_again = input("Do you want to play again?n\[y|n]: ").lower() # asking the user if to contiune play or exit.
if play_again == "y":
     print("random_number: ")
else:
     print("Thank you for playing!, see you next time")

        
   
                                  

