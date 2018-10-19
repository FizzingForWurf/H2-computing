import math

def isPrime(number):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True

def find_primes(limit):
    count = 0
    numbers = list(range(1, limit+1))

    for i in range(2, int(math.sqrt(limit)+1)):
        for j in numbers:
            if j%i == 0 and j != i:
                numbers.remove(j)
                count += 1

    print(limit - count)
    print(numbers)

def no_of_primes(number):
    result = [1]
    counter = 1
    test = 2

    while counter < number:
        if isPrime(test):
            result.append(test)
            counter += 1
        test += 1

    print(result)
    return result

def main():
    limit = int(input("Enter number of primes: "))
    no_of_primes(limit)

main()