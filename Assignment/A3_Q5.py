file = input("Enter a file: ")

inputFile = open(file, "r")
print("%-10s%-10s%-10s" % ("Name", "Hours", "Wage"))

for line in inputFile:
    line = line.rstrip()
    name, wage, hours = line.split("|")

    totalWage = float(wage) * float(hours)
    print("%-10s%-10s%-10d" % (name, hours, totalWage))

inputFile.close()
