
mun1 = int(input("Enter number: "))
mun2 = int(input("Enter number: "))
mun3 = int(input("Enter number: "))
mun4 = int(input("Enter number: "))
mun5 = int(input("Enter number: "))

list_num = [mun1] + [mun2]+ [mun3]+ [mun4]+ [mun5]
num  = 0

for i in list_num:
    num += i
    continue
print(num)