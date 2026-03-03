# დავალება:
# დაწერე ფუნქცია, რომელიც მიიღებს ერთ რიცხვს n და დააბრუნებს რამდენი კენტი რიცხვია 1-დან n-მდე.


def full(num):
    for i in range(1 , num + 1):
        if i % 2 ==0:
            print(f"{i}. is ლუწი")
        else:
            print(f"{i}. is კენტი")
    
print(full(num = int(input("Enter any number ~ "))))