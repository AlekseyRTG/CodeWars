def solution(number):
    answers = []
    for i in range(number):
        if (i%3==0 or i%5==0) and i<number and i>0:
            answers.append(i)
    return sum(answers)

print(solution(16))