# დავალება:
# დაწერე ფუნქცია, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ახალ სიას, სადაც იქნება მხოლოდ ლუწი რიცხვები.


def full():
    num_list = int(input("Enter any number ~ "))
    list_1 = []
    list_2  =[]
    x = 0
    
    while num_list != 0:    
        list_1.append(num_list)
        list_1.copy()
        num_list = int(input("Enter any number ~ "))
    else:
        for list_1 in list_1:
            if list_1 % 2 == 0:
                list_2.append(list_1)
                continue
        print(" ლუწი რიცხვთა სია ")
        print(list_2)

full()



    