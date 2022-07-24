# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples

# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)





def find_outlier(integers):

    if integers[0] % 2 == 0 and integers[1] % 2 == 0:
        even = 1
    elif integers[0] % 2 == 0 and integers[2] % 2 == 0:
        even = 1
    elif integers[1] % 2 == 0 and integers[2] % 2 == 0:
        even = 1
    else:
        even = 0
    
    # i = 0
    
    if even == 1:
        # while i < len(integers):
        #     if integers[i] % 2 != 0:
        #         return integers[i] 
        #     else: 
        #         i += 1
        for i, v in enumerate(integers):
            if integers[v] % 2 != 0:
                return integers[v]
    else:
        i = 0
        while i < len(integers):
            if integers[i] % 2 == 0:
                return integers[i]
            else:
                i += 1

find_outlier([160, 3, 1719, 19, 11, 13, -21])