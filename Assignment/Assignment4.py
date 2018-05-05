#Question 1
FILE_PATH = "C:\\Users\\tong\\Desktop\\Hwa Chong Institution\\Programming\\H2 computing\\Text\\"
print(FILE_PATH)
FILE_NAME = FILE_PATH + "numbers.txt"

numbers = []
modeD = {}

file = open(FILE_NAME, "r")

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
    if value in modeD: #alrdy got value in the dictionary
        modeD[value] = modeD.get(value, "none") + 1
    else:
        modeD[value] = 1

list_values = list(modeD.values())
list_values.sort(reverse = True)

print("Mode: " + str(list_values[0]))

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
