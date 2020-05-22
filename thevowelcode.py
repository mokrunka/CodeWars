def encode(st):
    letterList = list(st)
    for i in range(len(letterList)):
        if letterList[i] == 'a':
            letterList[i] = 1
        elif letterList[i] == 'e':
            letterList[i] = 2
        elif letterList[i] == 'i':
            letterList[i] = 3
        elif letterList[i] == 'o':
            letterList[i] = 4
        elif letterList[i] == 'u':
            letterList[i] = 5

    encode_result = ''

    for letter in letterList:
        encode_result += str(letter)
    return encode_result

def decode(st):
    letterList = list(st)
    for i in range(len(letterList)):
        if letterList[i] == '1':
            letterList[i] = 'a'
        elif letterList[i] == '2':
            letterList[i] = 'e'
        elif letterList[i] == '3':
            letterList[i] = 'i'
        elif letterList[i] == '4':
            letterList[i] = 'o'
        elif letterList[i] == '5':
            letterList[i] = 'u'
    encode_result = ''

    for letter in letterList:
        encode_result += str(letter)
    return encode_result

decode('h2ll4')