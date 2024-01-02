my_list = [1, 2, "up", "down", "left"]
print(my_list)
print(my_list[2])
print(my_list.index("down"))
my_list.append(input("What comes next in the list: "))
print(my_list)
del my_list[0]
print(my_list)
my_list.remove(int(input("What does not fit in the list: ")))
print(my_list)
