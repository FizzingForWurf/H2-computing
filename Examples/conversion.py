letters = ["A", "B", "C", "D", "E", "F"]

def convert_decimal(key, original):
    decimal = 0
    count = len(key) - 1

    for i in range(len(key)):
        value = 0
        if key[i].isalpha():
            value = letters.index(key[i]) + 10
        else:
            value = int(key[i])
        decimal += value * original ** count
        count -= 1

    return decimal

def decimal_convert(key, final):
    quotient = int(key)
    result = ""

    while quotient > 0:
        remainder = quotient % final
        quotient = quotient // final
        if remainder > 9:
            remainder -= 10
            remainder = letters[remainder]

        result += str(remainder)
    
    return result[::-1]

def main():
    original = int(input("Original base: " ))
    while original not in [2, 8, 10, 16]: original = int(input("Please enter a valid base (2, 8, 10, 16): " ))
    key = input("Number to convert: ")
    final = int(input("Desired base: "))
    while final not in [2, 8, 10, 16]: final = int(input("Please enter a valid base (2, 8, 10, 16): " ))

    if original != final:
        if original != 10:
            key = convert_decimal(key, original)
        if final != 10:
            key = decimal_convert(key, final)
        print("The result is:", key)
    else:
        print("Enter a different original and final base!")

main()

'''
def binary_convert(key, final):
    limit = int(math.log(final, 2))
    count = 0
    temp = ""
    result = ""

    num = len(key) % limit
    for x in range(num):
        key = "0" + key

    for i in range(len(key) - 1, -1, -1):
        temp += key[i]
        if count < limit - 1:
            count += 1
        else:
            temp = temp[::-1]
            count = 0
            counter = 0

            value = 0
            for j in range(limit - 1, -1, -1):
                num = int(temp[j]) * 2 ** counter
                counter += 1
                value += num

            if value > 9:
                value = letters[value - 10]

            result += str(value)
            temp = ""

    return result[::-1]
'''