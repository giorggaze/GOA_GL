O = 0
def numm():
    print(f"{name}_ს საშუალო ქულა ~~ " , last_point)  
print("\033[095m")

name = input("Enter name ~ ")
point = []
active = True
numbers = 0
while active != 0:
    active = int(input(f"Enter points {name} got ~ " , end="\r"))
    if active == 0:
        break
    point.append(active)

number = sum(point)
last_point = (number / len(point))
numm()



