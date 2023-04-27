def sort_array(source_array):
    l = 0
    odd_numbers = []
    while len(source_array) > l:
        if source_array[l] != 0 and source_array[l] % 2 == True:
            odd_numbers.append(source_array[l])
        l += 1
    
    odd_numbers.sort()
    l = 0
    index = 0
    sorted = []

    while len(source_array) > l:
        if source_array[l] != 0 and source_array[l] % 2 == True:
            sorted.append(odd_numbers[index])
            index += 1
        else:
            sorted.append(source_array[l])
        l += 1

    return sorted

sort_array([5, 3, 2, 8, 1, 4])
