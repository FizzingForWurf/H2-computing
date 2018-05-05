#! CT1 practice

#? Question 1

'''
sum = 0 
counter = 0
max = 0

input_numbers = input("Enter a string of numbers: ")

for number in input_numbers:
    number = int(number)

    sum += number
    counter += 1

    if number > max:
        max = number

ave = sum / counter

print("")
print("Sum of digits:", sum)
print("Average of digits:", ave)
print("Maximum digit:", max)
'''

#? Question 2

'''
FILE_PATH = "C:\\Users\\tong\\Desktop\\Hwa Chong Institution\\Programming\\H2 computing\\Text\\" #? Only for vs code

terms = []
terminate = False

jargon_file = open(FILE_PATH + "JARGON.txt", "r")

for line in jargon_file:
    line = line.strip()
    terms.append(line)

def print_info():
    print("++++++++++++++++++")
    print("1. Exact Match")
    print("2. Start of Term")
    print("3. Within Term")
    print("++++++++++++++++++")

while terminate == False:
    print_info()

    user_input = input("Enter your choice or xxx to end: ")

    while user_input == "":                                 #! Checks if there isn't an input --> Presence check
        user_input = input("No input detected! Please input something: ")
    
    if user_input == "xxx":
        terminate = True
    else:
        while not user_input.isdigit():                     #! Checks if input is a digit --> Data type check
            user_input = input("Please enter an INTEGER instead: ")

        while len(user_input) > 1:                          #! Checks if only one digit is entered --> Length check
            user_input = input("Please ONLY 1 digit: ")

        while int(user_input) > 3 or int(user_input) < 1:   #! Checks if the input is 1, 2 or 3 --> Range check
            user_input = input("Please enter a digit from 1 - 3: ")

        term_input = input("Enter term to search for: ")
        print()

        counter = 0        
        if int(user_input) == 1:
            for element in terms:
                if term_input == element:
                    print(element)
                    counter += 1

        elif int(user_input) == 2:
            for element in terms:
                if element.startswith(term_input):
                    print(element)
                    counter += 1

        elif int(user_input) == 3:
            for element in terms:
                if term_input in element:
                    print(element)
                    counter += 1
        
        print("\nThere are", counter, "matching term(s).\n")
'''

#? Question 3

'''
FILE_PATH = "C:\\Users\\tong\\Desktop\\Hwa Chong Institution\\Programming\\H2 computing\\Text\\" #? Only for vs code

web_log_dict = {}

weblog_file = open(FILE_PATH + "weblog.txt", "r")

def readLog():
    for line in weblog_file:
        name, details = line.split(" - - ")
        details = details[1:12]

        if name in web_log_dict:    #! Address alrdy in the dictionary --> add one more entry
            l = web_log_dict[name]
            l.append(details)
            web_log_dict[name] = l
        else:                       #! Address NOT in dictionary --> add one entry
            l = [details]
            web_log_dict[name] = l

def processLog():
    summary_file = open(FILE_PATH + "summary.txt", "w")

    max_freq = 0
    max_addr = []

    for address in web_log_dict:
        summary_file.write("%-30s" % address)
        content = str(web_log_dict[address])
        content = content[1:-1]
        summary_file.write(content + "\n")

        counter = 0

        for date in web_log_dict[address]:
            counter += 1

        if counter >= max_freq:
            if counter == max_freq:
                max_addr.append(address)
            else:
                max_addr = [address]

            max_freq = counter

    print("Highest frequency (days):", max_freq, "\n")
    print("Accessed by: ")
    
    for addr in max_addr:
        print(addr)

    print()

    summary_file.close()

readLog()
processLog()

weblog_file.close()
'''

#? Question 4

import random

NO_OF_GAMES = 10
NO_OF_TRIES = 6

unsuccessful_games = 0
successful_games = 0
success_tries_sum = 0
games = {}

for num in range(1, NO_OF_TRIES + 1):
    games[num] = 0

for game in range(1, NO_OF_GAMES + 1):
    print("\nGame number " + str(game) + "\n")
    guess_number = random.randint(1, 50)
    #print(guess_number)

    end = False
    loop_counter = 0

    while end == False:
        input_number = input("Enter a number between 1 to 50: ")

        while not input_number.isdigit():
            input_number = input("Please enter an INTEGER: ")

        if int(input_number) > guess_number:
            print("Too HIGH!")
        elif int(input_number) < guess_number:
            print("Too LOW!")
        else:                               #! Successful game!
            print("Congratulations! You guessed it correctly!")

            games[loop_counter + 1] += 1

            successful_games += 1
            success_tries_sum += (loop_counter + 1)

            end = True
        
        loop_counter += 1
        if loop_counter == NO_OF_TRIES:     #! Unsuccessful game :(
            print("Sorry you did not get it right. The answer is", guess_number)
            unsuccessful_games += 1
            end = True

ave = success_tries_sum / successful_games

print("")
print("%-10s%-10s" % ("NumGuess", "NumGames"))

for key in games:
    print("%-10d%-10d" % (key, games[key]))

print("\nUnsuccessful games:", str(unsuccessful_games))
print("Average number of tries for successful games: %0.2f" % ave)