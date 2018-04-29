#! Tutorial 4A

#? Question 1

'''
no_of_games = 3
no_of_players = 3

ave = 0

players = [""] * no_of_players
totalPoints = [0] * no_of_games
scores = [[0 for x in range(no_of_games + 1)] for y in range(no_of_players)]

for name in range(no_of_players):
    players[name] = input("Enter the player's name: ")

    for score in range(no_of_games + 1):
        if score != (no_of_games):
            points = int(input("Enter points scored: "))
            scores[name][score] = points
            ave += points
        else:
            ave /= no_of_games
            scores[name][no_of_games] = ave
            ave = 0

print()

print("%6s" % "Name", end = "")
for gameNo in range(1, no_of_games + 1):
    print("%8s" % ("Game " + str(gameNo)), end = "")
print("%9s" % "Average")

for name in range(no_of_players):
    print("%6s" % players[name], end = "")
    for gameNo in range(no_of_games):
        print("%8d" % scores[name][gameNo], end = "")
    print("%9.2f" % scores[name][no_of_players])

for gameNo in range(no_of_games):
    for name in range(no_of_players):
        totalPoints[gameNo] += scores[name][gameNo]

print("%6s" % "Total", end = "")
for gameNo in range(no_of_games):
    print("%8s" % totalPoints[gameNo], end = "")
'''

#? Question 2

'''
no_of_stocks = int(input("Enter the number of stocks: "))

max = 0

names = [" "] * no_of_stocks
stocks = [[0 for x in range(9)] for y in range(no_of_stocks)]

for count in range(no_of_stocks):
    names[count] = input("Enter the name of the stock: ")

    for day in range(7):
        if day == 0:
            min = int(input("Enter the closing price: "))
            stocks[count][day] = min
            max = min
            
        elif day == 5:
            stocks[count][day] = min
            
        elif day == 6:
            stocks[count][day] = max
            
        else:
            stocks[count][day] = int(input("Enter the closing price: "))
            
            if stocks[count][day] < min:
                min = stocks[count][day]
                stocks[count][7] = day
                
            if stocks[count][day] > max:
                max = stocks[count][day]
                stocks[count][8] = day

print("%10s%6s%6s%6s%6s%6s%12s%12s" % ("Name", "Mon", "Tue", "Wed", "Thu", "Fri", "Minimum", "Maximum"))
for stock in range(no_of_stocks):
    print("%10s" % names[stock], end = "")
    for day in range(5):
        print("%6d" % stocks[stock][day], end = "")
    print("%12s" % (str(stocks[stock][5])+ " (Day: " + str(stocks[stock][7] + 1) + ")"), end = "")
    print("%12s" % (str(stocks[stock][6])+ " (Day: " + str(stocks[stock][8] + 1) + ")"))
'''

#? Question 3:

#! REMEMBER: To integrate while loop: 
#! Solicit first data b4 loop
#! In the while loop: increment counter var b4 for soliciting again

MAX_STUDENTS = 40

ave = 0.0
counter = 0
terminate = True

scores = [0.0] * MAX_STUDENTS

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

scores[counter] = input("Enter the next score or hit 'Enter' to stop: ")
ave += float(scores[0])

while terminate == True:
    counter += 1
    if counter >= MAX_STUDENTS:
        terminate = False

    student_score = input("Enter the next score or hit 'Enter' to stop: ")
    if isfloat(student_score):
        ave += float(student_score)
        scores[counter] = float(student_score)
    else:
        terminate = False

ave /= counter
print("Class average: " + str(round(ave, 1)))
print("Scores above average: ", end = "")

for mark in range(counter):
    if float(scores[mark]) > ave:
        print(str(scores[mark]) + " ", end = "")
