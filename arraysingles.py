def repeats(arr):
    dup_list = []
    sum = 0
    for num in arr:
        if arr.count(num) == 1:
            dup_list.append(num)
        else:
            pass
    return (dup_list[0] + dup_list[1])


# another method, using list comprehensions
# def repeats(arr):
#     return sum([x for x in arr if arr.count(x) == 1])

repeats([4,5,7,5,4,8])
# repeats([9, 10, 19, 13, 19, 13])