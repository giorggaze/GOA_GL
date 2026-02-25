
wish_list = []

for i in range(5):
    x1 = input(".Enter anything you whan: ")
    wish_list.append(x1)
print(wish_list)

print("")
c = input("Do you whant to clear?(yes/no): ")

if c == "yes":
    wish_list.clear()
    print(wish_list)
elif c== "no":
    print("ok")
