def solution(s):
    result_list = []
    for i in range(len(s)):
        if len(s) % 2 == 0:
            if i % 2 == 0:
                result_list.append(s[i] + s[i + 1])
            else:
                pass
        elif len(s) % 2 != 0:
            if (i % 2 == 0) and i != (len(s) - 1):
                result_list.append(s[i] + s[i + 1])

    if len(s) % 2 != 0:
        result_list.append(s[-1] + '_')

    return (result_list)

solution('asadfadd')

# alternate solution
# def solution(s):
#     result = []
#     if len(s) % 2:
#         s += '_'
#     for i in range(0, len(s), 2):
#         result.append(s[i:i+2])
#     return result