import time
user = input("\033[92m Enter your name: ")
use = "Giorgi"

while user != use:
    print(" Your username is incorec!~")
    user = input("Try agein~:")
else:
    print("")
password = input(" Enter yor password: ")
P = "gio123"
while password != P:
    print("Your password is incorec!~: ")
    password = input("Try agein~: ")
else:
    time.sleep(2)
    print("")
print(use , "\033[95mdetected")
help = input("How can i help you, do you want list? ~")
if help == "yes":
    print("calculator ~~ 1")
    print("calculator ~~ 2")
    print("calculator ~~ 3")
    print("calculator ~~ 4")
else:
    print("ok sir,")
    time.sleep(1)
input("How can i help you sir")
