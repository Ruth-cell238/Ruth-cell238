def get_num():
    while True:
        try:
            x = int(input("give num "))
            return x
        except ValueError:
            print("Why no give num?")
def main():      
    num1 = get_num()
    num2 = get_num()
    num3 = get_num()
    print(num1, num2, num3)   
main()



