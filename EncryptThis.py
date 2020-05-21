def encrypt_this(text):
    # split the string into a list of discrete words
    listOfWords = text.split()

    encryptedWordList = []
    for word in listOfWords:
        if len(word) < 3:
            encryptedWordList.append(word)
        else:
            newWord = word[0] + word[int(len(word)) - 1] + word[2:int(len(word)) - 1] + word[1]
            encryptedWordList.append(newWord)

    finalEncryptedWordList = []
    for word in encryptedWordList:
        asciiWord = str(ord(word[0])) + word[1:]
        finalEncryptedWordList.append(asciiWord)

    encryptedString = ''
    for word in finalEncryptedWordList:
        encryptedString += word + ' '

    encryptedString = encryptedString.rstrip(' ')

    return encryptedString