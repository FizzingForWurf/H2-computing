#Question 1


numbers = []
modeD = {}

file = open("numbers.txt", "r")

for line in file:
    line = line.rstrip()
    for element in line.split():
        numbers.append(int(element))

file.close()

numbers.sort()

midpoint = int(len(numbers) / 2)

if len(numbers) % 2 == 1:
    median = numbers[midpoint]
else:
    median = (numbers[midpoint] + numbers[midpoint - 1]) / 2

print("Median: " + str(median))

for value in numbers:
    if modeD.get(value, "none") != "none": #alrdy got value in the dictionary
        modeD[value] = modeD.get(value, "none") + 1
    else:
        modeD[value] = 1

#Question 2

'''
name = input("Enter the filename: ")

file = open(name, "r")

lines = []

for line in file:
    line = line.rstrip()
    lines.append(line)

print("There are " + str(len(lines)) + " lines in the file.") #["First line", "Second line", "Third line", "Fourth line"]

userInput = 1

while userInput != 0:
    userInput = int(input("Enter line number or '0' to end program: "))

    if userInput > len(lines):
        print("Invalid line entered!")
    else:
        count = 1
        for line in lines:
            if userInput == count:
                print(line)
            count += 1

file.close()    
'''
