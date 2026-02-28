admin = str("giorgi")
password1 = int(19841984)

user = input("Enter user: ")
password = input("Enter password: ")

if user != admin or password1 != password:
    print("password or user is incorect.")
elif user == admin and password1 == password:
    print(f"Wellcom Mr.{admin}")
else:
    print(f"Try again {user}")
