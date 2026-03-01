def number():
    print(f"ნამრავლი ~ {point[-1]}")

point = []
num = 1

while num != 0 :
    C = int(input("Enter any number ~ "))
    if num == 0:
        break
    point.append(num)
    num *= C
number()