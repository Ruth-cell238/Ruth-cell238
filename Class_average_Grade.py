import os

student_names = []
student_grades = []


total_points = 0
numstudents = 0       

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def convert_to_4(grade):
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.0
    elif grade == 'D':
        return 1.0
    elif grade == 'F':
        return 0.0
    else:
        return None    

def get_grade():    
    while True:
        grade = input("Enter a grade(A, B, C, D, F) please: ").upper() 
        if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
            return grade  
        else:
            print("Invalid input. Please chose the correct input.")


def get_class_name():
    class_name = input("Enter the class name please: ")
    return class_name
                
class_name = get_class_name()

while True:
    student_name = input("Enter student names: ")

    student_grade = get_grade() 

    student_names.append(student_name)
    student_grades.append(student_grade) 

    grade_4_scale = convert_to_4(student_grade)
    if grade_4_scale is not None:
        total_points += grade_4_scale
        numstudents += 1

    if numstudents >0:
       class_average = total_points / numstudents 
    else:
        class_average = 0.0   

        
    print(f"\nClass: {class_name}")
    print("Student Grades:")
    
    for i in range(len(student_names)):
        print(f"{student_names[i]}: {student_grades[i]}")
    print(f"\nClass Average: {class_average:f}")


    