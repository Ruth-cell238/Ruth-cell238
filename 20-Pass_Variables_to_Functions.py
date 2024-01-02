def get_pets(pets):
    while True:
        try:
            num = int(input(f"How many {pets} do you have: "))
            if num < 0:
                print(f"You can't have negative {pets}")
            else:
                return num
        except ValueError:
            print("That is not a number.")

cats = get_pets("cats")
dogs = get_pets("dogs")
fish = get_pets("fish")

print(f"You have {cats} cats, {dogs} dogs, {fish} fish.")
