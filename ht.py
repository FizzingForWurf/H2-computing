#while loop

number = input("Enter a number: ")

while not number.isdigit():
    print("Please enter an integer INSTEAD!")
    number = input("Enter a number: ")

number = int(number)

while number < 0 or number > 100:
    print("Please enter your REAL score: ")
    number = input("Enter a number: ")

    while not number.isdigit():
        print("Please enter an integer INSTEAD!")
        number = input("Enter a number: ")

    number = int(number)

while number != 0:
    print(number)
    number -= 1