def move_zeros(lst):
    for x in lst:
        if x == 0:
            lst.remove(x)
            lst.append(0)
    return lst

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))