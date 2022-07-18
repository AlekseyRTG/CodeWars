# def count_bits(n):
#     b = []
#     i = 0
#     count = 0
#     while n > 0:
#         a = str(n % 2)
#         b.append(a)
#         n = n // 2
#     while i < len(b):
#         if b[i] == '1':
#             count += 1
#         i += 1
#     print(count)
#     return count
def count_bits(n):
    print(bin(n).count("1"))
    return bin(n).count("1")
count_bits(1234)
