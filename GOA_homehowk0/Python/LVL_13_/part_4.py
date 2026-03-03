# დავალება:
# დაწერე ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ყველა ელემენტის ჯამს.

def full():
    num_list = int(input("Enter any number ~ "))
    list_1 = []
    x = 0
    
    while num_list != 0:    
        list_1.append(num_list)
        list_1.copy()
        num_list = int(input("Enter any number ~ "))
    else:
        for list_1 in list_1:
            x += list_1
            continue
        print(x)

full()


    