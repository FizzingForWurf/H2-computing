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

def print_stars(number):
    if number == 1:
        print("*")
    else:
        return print_stars()
print_stars(5)