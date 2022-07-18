def descending_order(num):
    result = []
    while num > 0:
        result.append(num % 10)
        num //= 10

        result.reverse()
    # print(result) 

    result.sort()
    result.reverse()

    num = 0
    for i, v in enumerate(reversed(result)):
        num += v * 10 ** i
    # print(num) 
    return num

print(descending_order(15))