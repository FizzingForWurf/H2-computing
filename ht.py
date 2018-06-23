'''
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))

area = (base*height)/2

print("The area is:", area)

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



sum = 0
number = int(input("Enter a number: "))

while number != -1:
    number = int(input("Enter your number: "))
    sum = number + sum
    print(number)

print(sum)





max = 0
sum = 0

for x in range(3):
    number = int(input("Enter a number: "))

    sum = number + sum

    if (number > max):
        max = number

print(sum)
print(max)
'''

numb = int(input("Enter a number: "))

for number in range (1, numb+1):
    if number == 1 or number == numb:
        print (2*numb*"*")
    else:
        print ("*",(2*numb-4)*" ","*")