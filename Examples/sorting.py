def swap(list, first, second):
    temp = list[first]
    list[first] = list[second]
    list[second] = temp
    return list

def selection_sort(list):
    for track in range(len(list) - 2):
        low = list[track]
        low_index = 0

        for i in range(track, len(list)):
            if list[i] < low:
                low = list[i]
                low_index = i
        
        swap(list, low_index, track)
        print(list)

    return list

def main():
    list = [21,332,43,12,45,32,42,34,37]
    list = selection_sort(list)
    print(list)

main()