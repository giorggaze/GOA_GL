# # დაწერე ფუნქცია, რომელიც მომხმარებელს სთხოვს რიცხვებს და აჯამებს მათ.
# # ციკლი გაგრძელდეს მანამ, სანამ მომხმარებელი 0-ს არ შეიყვანს.


def HEHE(num):
    x = 0
    while num != 0:
        for i in range(1 , num + 1):
            x += i
            continue
        print(x)
        num = int(input("Enter any number ~ "))
        x = 0


HEHE(num = int(input("Enter any number ~ ")))