import random

FILE_PATH = "C:\\Users\\tong\\Desktop\\Hwa Chong Institution\\Programming\\H2 computing\\Text\\"

def questionOne():
    MAX_PPL = 2
    round = 0

    star_name = ""
    star_steps = 0

    file = open(FILE_PATH + "STAR.txt", "r+")

    name = " "

    while round < MAX_PPL and name != "":
        name = input("Enter name of walker: ")
        step = int(input("Enter number of steps: "))
        print()
        
        if step > star_steps:
            star_steps = step
            star_name = name

        round += 1

    line = file.read()
    content = line.split("|")

    print("Last week, " + content[0] + " was 'Star of the Week' with " + content[1] + " steps taken.")
    print("This week, " + star_name + " is 'Star of the Week' with " + str(star_steps) + " steps taken.")

    file.truncate(0)
    file.close()

    new_file = open(FILE_PATH + "STAR.txt", "w")
    new_file.write(star_name + "|" + str(star_steps))
    new_file.close()

def QuickSort(scores):
    QuickSortHelper(scores, 0, len(scores) - 1)
    return scores

def QuickSortHelper(scores, first, last):
    if first < last:
        split_point = Partition(scores, first, last)
        QuickSortHelper(scores, first, split_point - 1) 
        QuickSortHelper(scores, split_point + 1, last)
    
    return scores

def Partition(scores, first, last):
    pivot_value = scores[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and pivot_value >= scores[left]:
            left += 1
        while pivot_value <= scores[right] and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = scores[left]
            scores[left] = scores[right]
            scores[right] = temp

    sub = scores[first]
    scores[first] = scores[right]
    scores[right] = sub

    return right

def questionTwo():
    initial_array = [15, 13, 489, 46, 456, 78, 32, 4]
    print(initial_array)
    final_array = QuickSort(initial_array)
    print()
    print(final_array)

def display_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end = " ")
        print()

def add_prize(maze):
    maze[5][4] = "O"
    exist = True
    while exist:
        column = random.randint(1, 8)
        row = random.randint(1, 9)

        if maze[row][column] == "." and row != 5 and column != 4:
            maze[row][column] = "P"
            exist = False

    return maze

def questionFour():
    maze = []

    file = open(FILE_PATH + "MAZE.txt", "r")
    for line in file:
        row = []
        for char in line:
            row.append(char)
        maze.append(row)

    display_maze(maze)
    new_maze = add_prize(maze)
    print("\n\n\n")
    display_maze(new_maze)

    result = ""
    while result != "P":
        command = input("Enter your input: ")
        while command not in "uUdDlLrR" or command != "":
            print("Invalid input!")
            command = input("Enter your input again: ")

        row = 5
        column = 4

        command = command.lower()
        if command == "u":
            pass

#questionFour()

def testing():
    NO_OF_PPL = 61
    PPL_PER_GRP = 12

    people = []
    people.append(list(range(1, PPL_PER_GRP+1)))

    group = []
    school = {}

    for i in range(PPL_PER_GRP+1, NO_OF_PPL+2):
        if i % (PPL_PER_GRP) == 0:
            group.append(i)
            people.append(group)
            group = []
        else:
            group.append(i)

    print(people)

questionFour()
