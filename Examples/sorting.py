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

    return array

def main():
    array = [21,332,43,12,45,32,42,34,37,90,324,1,4,56,365]
    array = selection_sort(array)
    print(array)

main()