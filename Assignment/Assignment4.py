#! Assignment 4

#? Question 1
'''
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
    if value in modeD: #alrdy got key in the dictionary
        modeD[value] = modeD.get(value, "none") + 1
    else:
        modeD[value] = 1

list_values = list(modeD.values())
list_values.sort(reverse = True)

for key in modeD:
    if modeD[key] == list_values[0]:
        print("Mode:", key)

print("Mode frequency: " + str(list_values[0]))
'''

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

#? Question 3

FILE_PATH = "C:\\Users\\tong\\Desktop\\Hwa Chong Institution\\Programming\\H2 computing\\Text\\"

unique_words = {}
most_freq = []

def main():
    file = open(FILE_PATH + "unique_words.txt", "r")

    for line in file:
        line = line.strip()

        if line in unique_words:
            unique_words[line] += 1
        else:
            unique_words[line] = 1
    
    file.close()

def partA():
    print("Unique words: ")
    
    key_list = sorted(list(unique_words.keys()))

    for key in key_list:
        print(key)

def partB():
    print("%-10s%-10s" % ("Words", "Frequency"))

    key_list = sorted(list(unique_words.keys()))

    for key in key_list:
        print("%-10s%-10d" % (key, unique_words[key]))

def partC():
    max_freq = 0

    for key in unique_words:
        value = unique_words[key]

        if value > max_freq:           
            max_freq = value
            most_freq = [key]
        elif value == max_freq:
            most_freq.append(key)

    most_freq.sort()

    print("Most frequent words: ", end = "")

    loop_counter = 0
    for element in most_freq:
        if loop_counter == 0:
            print(element, end = "")
        else:
            print(",", element, end = "")

        loop_counter += 1

main()