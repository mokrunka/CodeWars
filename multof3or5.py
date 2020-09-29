def solution(number):
    result = []
    both = -1
    three_only = 0
    five_only = 0
    for i in range(number):
        if (i % 3) == 0 and (i % 5) == 0:
            both += 1
        elif (i % 3) == 0:
            three_only += 1
        elif (i % 5) == 0:
            five_only += 1
        else:
            pass
    answer = [three_only, five_only, both]
    # print(answer)
    return answer