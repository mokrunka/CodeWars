def decipher_this(string):
    # count the number of words
    numwords = 1
    for char in string:
        if char == ' ':
            numwords += 1

    # create a list of the words
    listofwords = string.split(sep=' ')
    # empty list to contain deciphered words as we manipulate them
    newlistofwords = []
    # print(listofwords)
    for word in listofwords:
        numstoppos = 0
        for letter in word:
            if ord(letter) < 58:
                numstoppos += 1
        letter = chr(int(word[:numstoppos]))
        newword = letter + word[numstoppos:]
        newlistofwords.append(newword)
    # print(newlistofwords)

    finalwordlist = []
    for word in newlistofwords:
        if len(word) == 1:
            finalwordlist.append(word)
        elif len(word) == 2:
            finalwordlist.append(word)
        else:
            swappedword = word[0] + word[-1] + word[2:-1] + word[1]
            finalwordlist.append(swappedword)

    cipher = ''
    for word in finalwordlist:
        cipher = cipher + word + ' '
    cipher = cipher.rstrip()

    return cipher

    return finalwordlist