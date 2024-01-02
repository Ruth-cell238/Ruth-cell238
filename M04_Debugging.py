def is_num():
    while True:
        try:
            x = int(input("Show me what you got.\n"))
            return x  #return if it is true
        except ValueError:
            print("Disqualified! Please enter valid number.")


# From here down should not be changed
num = is_num()
print(f"You got {int(num)}.")            