stud_1 = "giorgi"
stud_2 = "maria"
stud_3 = "adolf"

stud = str(input("Enert Student name: "))
if stud == stud_1 or stud_2 or stud_3:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are student.")
    elif 99 > age:
        print("Dud,how are you still alive??")
    elif age <= 0:
        print("You are not born yet")
    else:
        print(f"Mr.{stud} you are child.")
else:
    print(f"we dont have student name as {stud}")
