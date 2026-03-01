O = 0
def numm():
    print("ამ რიცხვების საშუალო არის ~~ " , lana / O)  
print("\033[095m")
num = True
number = []
lana = 0
while num != 0:
    num = int(input("Enter any number ~ "))
    if num == 0:
        break
    number.append(num)
    O += 1
    lana += num
print("\033[091m")
print(f"ციფრთა რაოდენობა ~~ {O} ")
print(f"ჯამი == {lana}")
if O > 0:
    numm()
else:
    print("ციფრთა რაოდენობა ნულია")

