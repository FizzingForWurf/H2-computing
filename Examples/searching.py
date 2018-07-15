'''#? Sequential search'''

def seqSearch(A, start, n, key):
    for i in range(start, n):
        if A[i] == key:
            return i
    return -1

def binarySearch(A, low, high, key):
    A.sort()
    print(A)

    middle = high//2
    terminate = False

    while not terminate: 
        if A[middle] != key:
            if A[middle] < key:
                low = middle
            else:
                high = middle
            
            middle = (low + high)//2
            print(low, middle, high)
        else:
            terminate = True

        if high - low == 1:
            terminate = True
            middle = -1

    return middle

def binSearch(A, n ,key):
    found = False
    low = 0
    high = n - 1

    while not found and low <= high:
        mid = int(low + high) // 2
        if key == A[mid]:
            found = True
        if key < A[mid]:
            high = mid - 1
        if key > A[mid]:
            low = mid + 1

    if found: 
        return mid + 1
    else:
        return - 1

def recursiveSearch(list, key, low = 0, high = None):
    if high == None:
        high = len(list)

    middle = (high + low) // 2

    if high == low:
        return -1

    if list[middle] == key:
        return middle

    if key < list[middle]:
        return recursiveSearch(list, key, low, middle)

    if key > list[middle]:
        return recursiveSearch(list, key, middle + 1, high)

def main():
    list = []
    pos = 0 
    count = 0

    '''
    print("Enter a list of 10 integers:")
    for i in range(10):
        num = input("Enter an integer: ")
        list.append(num)
    print(list)
    '''

    list = [15,25,37,45,52,56,77,28,29]
    list.sort()
    print(list)

    key = input("Enter a key: ")
    pos = recursiveSearch(list, int(key))
    #pos = binarySearch(list, pos, 10, int(key))
    
    '''
    while pos != -1:
        count += 1
        pos += 1
        pos = seqSearch(list, pos, 10, key)

    print(key, "occurs", count, "times in the list.")
    '''
    
    if pos != -1:
        print("{0} is found at position {1}!".format(key, pos+1))
    else:
        print("{0} is not found!".format(key))

main()