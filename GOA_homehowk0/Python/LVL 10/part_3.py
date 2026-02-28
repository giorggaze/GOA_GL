
wish_list = []

while True:
    x1 = input(".Enter anything you whan: ")\
    
    if x1 == "end" or x1 == "ვსო":
         break
    wish_list.append(x1)
c = 0
for i in wish_list:
    c += 1
    print(c ,"~" , i)