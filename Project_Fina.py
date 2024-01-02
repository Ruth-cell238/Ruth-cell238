# Initialize numbers and varibles for grand total and store num
grand_total = 0
store_num = int(input("Enter number of stores you have? "))

#Main program loop input and calculate store total
for i in range(store_num):
    print(f"\nStore {i + 1}")
    
    # create variables for store total
    store_total_data = 0
    
    # Initialize variables to store currencry values
    currency = { '100s': 100, '50s': 50, '20s': 20, '10s': 10, '5s': 5, '1s': 1,
        'quarters': 0.25, 'dimes': 0.1, 'nickels': 0.05, 'pennies': 0.01}
    
    #setting input validity 
    for currency, value in currency.items():
        while True:
            try:
                store_bill = int(input(f"Number of {currency}: "))
                if store_bill < 0:
                    raise ValueError("Number cannot be negative")
                break
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        
        # Calculate and display store total
        store_total_data += store_bill * value
    
    # Add store total to grand total
    grand_total += store_total_data
    
    # Display the store total
    print(f"\nStore {i + 1} Total: ${store_total_data:.2f}")

# Display the grand total
print(f"\nGrand Total for All Stores: ${grand_total:.2f}")

# Ask user if they want to save the data to a texy file
save_choice = input("Do you want to save the information? (yes/no): ").lower()

if save_choice.lower() == "yes":
    # Save data to a .txt file
    with open('store_totals.txt', 'w') as file:
        file.write(f"Grand Total: ${grand_total:.2f}\n")
        for i in range(store_num):
            file.write(f"Store {i + 1} Total: ${store_total_data:.2f}\n")

    print("Data has been saved to store_totals.txt")
else:
    print("Data not saved.")    