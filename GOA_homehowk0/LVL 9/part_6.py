print("\033[093m")

for i in range(1 , 50):
    if i % 2 != 0:
        print("\033[091m")
        print(  i , " ~number is odd!~")
    else:
        print("\033[096m")
        print( i ,"~number is even~")