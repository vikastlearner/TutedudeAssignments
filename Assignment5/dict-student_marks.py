"""
This file contains dictionary and fetching the value of dictionary.
It also handles the lower case name, example if name = Pradeep is entered as "pradeep", it handles it too
"""

# Student details with their marks in Phy, Chem, Math, Bio, English and IT
student_marks = {"Ravi": {"Physics": 80,"Chemistry": 83,"Maths": 87,"Biology": 70,"English": 75,"Information Tech": 83},
                "Aniket": {"Physics": 86,"Chemistry":66,"Maths": 77,"Biology": 81,"English": 71,"Information Tech": 81},
                "Sumeet": {"Physics": 92,"Chemistry": 91,"Maths": 95,"Biology": 85,"English": 92,"Information Tech": 99},
                "Pradeep": {"Physics": 89,"Chemistry": 92, "Maths": 90,"Biology": 88,"English": 99,"Information Tech": 88},
                "Shivam": {"Physics": 95,"Chemistry": 90,"Maths": 98,"Biology": 82,"English": 88,"Information Tech": 85}}

name = input("Please enter your name: ")
case_sens = name
for student_name in student_marks:
    if case_sens.lower() == student_name.lower():
        print(f"Hi {name.capitalize()} following are your marks")
        marks = student_marks[name.capitalize()]
        sum = sum(marks.values())
        percentage = round(((sum/600)*100), 2)
        for i in marks:
            print(f"{i}: {marks[i]}/100")
        print("=====================================================")
        print(f"Total marks: {sum}/600 and Percentage: {percentage}%")
        print("=====================================================")
        break

else:
        print("Sorry, your name does not exist in list")

