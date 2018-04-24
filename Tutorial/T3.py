#Tutorial 3

'''#q2
myString = "abc"
reversedString = ""

for char in myString:
    reversedString = char + reversedString

print(reversedString)
'''

'''#q2
myString = input("Enter string: ")
reversedString = ''

for char in range(len(myString) - 1, -1, -1):
    reversedString = reversedString + myString[char]

print(reversedString)
'''

'''#q3
first = input("Enter first file: ")
second = input("Enter second file: ")

file1 = open(first, "r")
file2 = open(second, "w")

for line in file1:
    file2.write(line)

file1.close()
file2.close()
'''

'''#q4
same = True

first = input("Enter first file: ")
second = input("Enter second file: ")

file1 = open("firstFile.txt", "r")
file2 = open("secondFile.txt", "r")

first = file1.readlines()
second = file2.readlines()

if(len(first) != len(second)):
    same = False
else:
    for num in range(0, len(first)):
    if first[num].strip() != second[num].strip():
        print("No")
        same = False
        break

if same == True:
    print("Yes")
    
file1.close()
file2.close()'''

#q5
file = input("Enter a file: ")

inputFile = open(file, "r")
print("%-10s%-10s%-10s" % ("Name", "Hours", "Wage"))

for line in inputFile:
    line = line.rstrip()
    name, wage, hours = line.split("|")

    totalWage = float(wage) * float(hours)
    print("%-10s%-10s%-10d" % (name, hours, totalWage))

inputFile.close()
