'''file = open("testing.txt", "w")

file.write("one.\ntwo.\nthree.\nfour.\nfiveee.\n")

file.close()

file = open("testing.txt", "r+")

lines = file.readlines()
sum = 0

for words in lines:
    if len(words.strip()) == 4: #rmb to strip to get rid of the \n
        sum += 1
            
file.write("sum is ")
file.write(str(sum))

file.close()'''

'''
while(line != ""):
    line = file.readline()
    if(len(line) == 4):
        sum += 1

file.write("sum is ")
file.write(str(sum))

file.close()'''

'''
for line in file:
    line = line.strip()
    if(len(line) == 4):
        sum += 1

file.write("sum is ")
file.write(str(sum))

file.close()'''

file = input("Enter a file: ")

inputFile = open(file, "r")
print("%-10s%-10s%-10s" % ("Name", "Hours", "Wage"))

for line in inputFile:
    line = line.rstrip()
    name, wage, hours = line.split("|")

    totalWage = float(wage) * float(hours)
    print("%-10s%-10s%-10d" % (name, hours, totalWage))

inputFile.close()
