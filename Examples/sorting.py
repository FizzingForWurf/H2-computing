import random

def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp
    return array

def selection_sort(array):
    for track in range(len(array) - 1):
        low = array[track]
        low_index = track

        for i in range(track + 1, len(array)):
            if array[i] < low:
                low = array[i]
                low_index = i
        
        swap(array, low_index, track)
        print(array)

    return array

def bubble_sort(array):
    pointer = None

    while pointer != 0:
        pointer = 0

        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                swap(array, i, i - 1)
                pointer += 1

        print(array)

    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        
        if array[i - 1] > array[i]:
            for j in range(i, 0, -1):
                if array[j - 1] > array[j]:
                    swap(array, j, j - 1)
            print(array)

    return array

A = []

def quick_sort(A, low, high):
    mid = (low + high) // 2
    pivot = A[mid]
    swap(A, low, mid)
    print(pivot, A)

    left = low + 1
    right = high

    while(left < right):
        while(A[left] < pivot and left != high):
            left += 1
        while(A[right] > pivot and right != low):
            right -= 1
        if left < right:
            if(A[left] > A[right]):
                print("SWAP!", left, right)
                swap(A, left, right)

        print(A, left, right)

    swap(A, low, right)
    print(A, left, right)
    print()

    if right - low > 1:
        quick_sort(A, low, right)
    if high - right > 2: 
        quick_sort(A, right + 1, high)

def merge(firstArr, secondArr):
    array = []
    if (str(firstArr).isdigit()):
        if firstArr < secondArr:
            return [firstArr, secondArr]
        else:
            return [secondArr, firstArr]
    else:
        firstArr.append(1000)
        secondArr.append(1000)

        count1, count2 = 0, 0
        while count1 < len(firstArr)-1 or count2 < len(secondArr)-1:
            if firstArr[count1] < secondArr[count2]:
                array.append(firstArr[count1])
                count1 += 1
            elif firstArr[count1] > secondArr[count2]:
                array.append(secondArr[count2])
                count2 += 1
            else:                                 #if both entries are equal --> just add both to the list
                array.append(firstArr[count1])
                array.append(secondArr[count2])
                count1 += 1
                count2 += 1

    return array

def merge_sort(array):
    while len(array) != 1:
        mid = len(array) // 2
        firstArr = array[0:mid]
        secondArr = array[mid:]

        array = []
        for x in range(len(firstArr)):
            newArr = merge(firstArr[x], secondArr[x])
            array.append(newArr)

        if len(firstArr) != len(secondArr):
            extraArr = secondArr[len(secondArr) - 1]
            if str(extraArr).isdigit():
                extraArr = [extraArr]
                
            tempArr = merge(array[len(array) - 1], extraArr)
            array[len(array) - 1] = tempArr

    return array[0]

def main():
    A = []

    for i in range(9):
        A.append(random.randint(1, 50))

    #A = [1, 10, 11, 13, 34, 46, 39, 46]

    print("Initial array:" + str(A))
    print()

    A = merge_sort(A)

    print()
    print(A)

main()

'''

array = [[], [], []]
sorted_array = []

def min(a, b, c):
    if a < b and a < c:
        return 1
    elif b < a and b < c:
        return 2
    elif c < a and c < b:
        return 3

def create_array():
    numbers = list(range(1, 1001))

    for x in range(3):
        for i in range(100):
            num = random.randint(1, 1001)
            while num not in numbers:
                num = random.randint(1, 1001)
            array[x].append(num)
            numbers.remove(num)

        array[x].sort()
        array[x].append(2000)

def sorting():
    count1, count2, count3 = 0, 0, 0
    while count1 < 100 or count2 < 100 or count3 < 100:
        value = min(array[0][count1], array[1][count2], array[2][count3])
        if value == 1:
            sorted_array.append(array[0][count1])
            count1 += 1

        elif value == 2:
            sorted_array.append(array[1][count2])
            count2 += 1

        elif value == 3:
            sorted_array.append(array[2][count3])
            count3 += 1

create_array()
sorting()

print(sorted_array)
print(len(sorted_array))

'''