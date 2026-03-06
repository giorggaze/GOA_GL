# დაწერე ფუნქცია, რომელიც მიიღებს ტექსტს და დაითვლის რამდენი დიდი ასოა.


def count_uppercase(text):
    count = 0
    for asa in text:
        if asa.isupper():
            count += 1
    return count


# გამოყენების მაგალითი
sentence = input("შეიყვანეთ ტექსტი: ")
result = count_uppercase(sentence)
print("დიდი ასოების რაოდენობა:", result)