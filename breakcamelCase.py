def solution(s):
    result_list = []
    prev_i = 0
    for i in range(len(s)):
        if ord(s[i]) < 97:
            result_list.append(s[prev_i:i])
            prev_i = i
    result = ' '.join(result_list)
    temp = result.replace(' ','')
    # print(result)
    last_word_start_index = len(temp)
    result += ' ' + s[last_word_start_index:len(s)]
    # print(result)
    return result

#alternative solution
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

solution("helloWorld")
solution("breakCamelCaseStuff")
solution("camelCase")
solution("camelCaseStuff")