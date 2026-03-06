# მომხმარებელს შეაყვანინე წინადადება.
# შეამოწმე, არის თუ არა სიტყვა "python" ამ ტექსტში (მცირე ასოებში).
# გამოიყენე lower() და find().



name = input("Enter your name ~ ")

name1 = name.lower()

if name1.find("python") != -1:
    print("სწორია")
else:
    print("არასწორია")