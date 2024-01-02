names = []
cost = []
ques = "yes"
while ques in ["Y", "y", "yes", "Yes"]:
        names.append(input("What is your name?\n "))
        try:
            num = float(input("how much did you food cost?|n ")) 
        except ValueError:
               print("that is not the number.")
        cost.append(num)
        while True: 
            ques = input("Do you want add more people? n\[y|n]")
            if ques in ["y", "Y", "yes", "Yes"]:
              break
            elif ques in ["n", "N", "no", "No"]:
                 break
            else:
                 print("please use y or n")


avarage = sum(cost)/len(cost)
for i,j in zip(names,cost):
     print(f"{i} you spent cost{j} while the avarge was{avarage}")                 
