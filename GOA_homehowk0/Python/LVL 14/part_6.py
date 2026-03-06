# დაწერე ფუნქცია, რომელიც მიიღებს ტექსტს და ერთ სიმბოლოს.
# დათვალოს რამდენჯერ გვხვდება ეს სიმბოლო ტექსტში.



def count():
    names = str(input("Enretr any name ~ "))

    look = input("What are you looking for ~ ")

    print(names)
    print(names.count(look))

count()