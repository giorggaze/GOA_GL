def full(num):
    x = 0
    for i in range(1 , num + 1):
        x += i
        continue
    return x
    
print(full(num = int(input("Enter any number ~ "))))

# დავალება:
# დაწერე ფუნქცია, რომელიც მიიღებს ერთ რიცხვს n და დააბრუნებს 1-დან n-მდე ყველა რიცხვის ჯამს.
