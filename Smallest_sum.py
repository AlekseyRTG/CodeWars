# smallest possible sum of all numbers in Array
def solution(a):
    if len(a) < 2:
        smallest_sum = a[0]
    else:
        a.sort()
        if a[len(a)-1] != a[len(a) - 2]:
            while a[len(a)-1] != a[len(a) - 2]:
                a[len(a)-1] = a[len(a)-1] - a[len(a)-2]
                a.sort()
            smallest_sum = sum(a)
        else:
            if a[len(a)-1] == a[len(a)-2]:
                a[len(a)-2] = a[len(a)-2] - a[len(a)-3]
                a.sort()
                while a[len(a)-1] != a[len(a) - 2]:
                    a[len(a)-1] = a[len(a)-1] - a[len(a)-2]
                    a.sort()
                    smallest_sum = sum(a)
    return smallest_sum

print(solution([21, 1, 55]))