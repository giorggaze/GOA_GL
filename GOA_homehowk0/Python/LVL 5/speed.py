import math
print("კალკულატორი")
calculus = input("აირჩიე მოქმედება(+ ან - ): ")
if calculus == "+":
    x = float(input("ჩაწერე პირველი ციპრი: "))
    y = float(input("ჩაწერე მეორე ციპრი: "))
    print(float(x + y))
elif calculus == "-":
    x = float(input("ჩაწერე პირველი ციპრი: "))
    y = float(input("ჩაწერე მეორე ციპრი: "))
    print(float(x - y))
else:
    print("ძმაო ასეტი მოქმედება არ არსებობს ჯერ!!")