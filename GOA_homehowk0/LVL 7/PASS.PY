pas = 12345

passcode = int(input("Enter password: "))

while passcode != pas:
    print("password is incorect,try again!")
    passcode = int(input("Enter password: "))
print(f"password {passcode} is corect")