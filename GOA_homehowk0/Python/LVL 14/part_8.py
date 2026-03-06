# დაწერე ფუნქცია, რომელიც მიიღებს ტექსტს და სიტყვას.
# დააბრუნოს True თუ ეს სიტყვა ტექსტში არსებობს


def count():
    names = str(input("Enretr any name ~ "))

    look = input("What are you looking for ~ ")

    if look in names:
        print(True)
    else:
        print(False)

count()