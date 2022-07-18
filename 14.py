# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 *  ... * N

# Be careful 1000! has 2568 digits...

# For more info, see: http://mathworld.wolfram.com/Factorial.html

# Examples

# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros



def zeros(n):
    if n > 0:
        spam = list(range(1, n+1))
        factorial = spam[0] * spam[1]
        i = 1
        zeros = 0
        while i != n-1:
            factorial = factorial * spam[i + 1]
            # print(factorial)
            i += 1
        while factorial % 10 < 1:
            zeros += 1
            factorial = factorial / 10
    else:
        zeros = 0
    return zeros

print(zeros(30))