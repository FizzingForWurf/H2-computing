#! Assignment 5

#? Question 1

'''
def multiply(x, y):
    if x == 1:
        return y
    else:
        return y + multiply(x - 1, y)

print(multiply(2, 4))
'''

#? Question 2

'''
def print_stars(number, count = 1):
    if count == number:
        print("*" * number)
    else:
        print("*" * count)
        return print_stars(number, count + 1)
'''

#? Question 3

'''
def find_sum(number):
    if number == 1:
        return number
    else:
        return number + find_sum(number - 1)
'''

#? Question 4

my_list = []

def myRange(stop):
    if stop == 0:
        my_list.insert(0, 0)
        return my_list
    else:
        my_list.insert(0, stop)
        return myRange(stop - 1)

my_second_list = []

def my_range(start, stop, step = 1):
    if start == stop:
        return my_second_list
    else:
        my_second_list.append(start)
        return my_range(start + step, stop, step)

