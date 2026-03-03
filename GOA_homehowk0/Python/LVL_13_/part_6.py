# დავალება:
# დაწერე ფუნქცია, რომელიც მიიღებს:

# რიცხვების სიას,
   
# ერთ კონკრეტულ რიცხვს,

# და დააბრუნებს რამდენჯერ გვხვდება ეს რიცხვი სიაში.

def list_count(num):
    num_count = []
    while num != 0:
        num_count.append(num)    
        num =int(input("enter any number ~ "))
    num_count.copy()
    look = int(input("\033[093m which number are you looking for? ~ "))
    if look in num_count:
        time = num_count.count(look)
        print(f"number {look} is finded and it repited {time} times.")
        print("")
        print("\033[097m list ~",num_count)
    else:
        print("there is no {look} in the list")


list_count(int(input("enter any number ~ ")))