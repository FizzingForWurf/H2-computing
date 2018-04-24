max_size = 30
week = 5

salesmanNo = 0

sales = [[0 for y in range(5)] for x in range(max_size)]
names = [''] * max_size

names[salesmanNo] = input("Enter the salesman's name: ")

while (salesmanNo < max_size) and (names[salesmanNo] != "xxx"):
    for day in range(5):
        sales[salesmanNo][day] = int(input("Enter the sales for the day: "))
    salesmanNo += 1

    names[salesmanNo] = input("Enter the salesman's name: ")

print()
print("%-6s%-4s%-4s%-4s%-4s%-4s" % ("Name", "Mon", "Tue", "Wed", "Thu", "Fri"))
for count in range(salesmanNo):
    print("%-6s" % names[count], end = "")
    print("%-4d%-4d%-4d%-4d%-4d" % (sales[count][0], sales[count][1], sales[count][2], sales[count][3], sales[count][4]))