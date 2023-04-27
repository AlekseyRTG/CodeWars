def solution(array_a, array_b):
    return sum((x - y) ** 2 for x, y in zip(array_a, array_b)) / len(array_a)

a1 = [1,2,3]
a2 = [4,5,6]
print(solution(a1, a2))