sia = []
print("\033[092m if you done,type '0' ")
while True:
    num = int(input("Enter any number for list: "))
    if num == 0:
        break
    sia.append(num)

u = int(input("What are you loking for: "))
x = sia.count(u)

print(f"{u} has mainteind in list {x} times")        
    
