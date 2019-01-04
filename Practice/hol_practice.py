import random

LENGTH = 15
WIDTH = 8
NO_OF_FISH = 3

pond = []

def throw_pellet(): 
    x_coordinate = int(input("X coordinate <1 - 15> "))
    y_coordinate = int(input("Y coordinate <1 - 8> "))
    print()

    if pond[y_coordinate-1][x_coordinate-1] == "F":
        pond[y_coordinate-1][x_coordinate-1] = "H"
    else:
        pond[y_coordinate-1][x_coordinate-1] = "P"

def add_fish():
    for i in range(NO_OF_FISH):
        x_coor = random.randint(0, 14)
        y_coor = random.randint(0, 7)

        pond[y_coor][x_coor] = "F"

def print_pond():
    for row in range(WIDTH):
        for col in range(LENGTH):
            print(pond[row][col], end = "")
        print()

def main():
    #initialise an empty pond first
    for i in range(WIDTH):
        temp = []
        for j in range(LENGTH):
            temp.append(".")
        pond.append(temp)
    print(pond)

    add_fish()
    throw_pellet()
    print_pond()

main()