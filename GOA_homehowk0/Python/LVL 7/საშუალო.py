num = int(input("Enter number: "))

tot1 = 0
tot2 = num

while num != 0:
    num = int(input("Enter number: "))
    tot1 = tot1 + 1 
    tot2 = (tot2 + num)
print(tot2 / tot1)