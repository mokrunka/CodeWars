def comp(array1, array2):
    trueCount = 0
    if (array1 == []) and (array2 == []):
        return True
    elif (array1 == []) or (array2 == []) or (type(array1) == 'NoneType') or (len(array1) != len(array2)):
        return False
    for i in range(len(array1)):
        array1[i] = abs(array1[i])
    for i in range(len(array2)):
        array2[i] = abs(array2[i])
    array1.sort()
    array2.sort()
    zipped = zip(array1, array2)

    for x, y in zipped:
        if abs(x) ** 2 == y:
            trueCount += 1
        else:
            pass

    if trueCount == len(array1):
        return True
    else:
        return False

a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
a2 =  [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a1, a2)