def find_missing_number(numbers):
    sorted_list = sorted(numbers)
    full_list = []
    for i in range(len(sorted_list)):
        full_list.append(i + 1)
    zipped = list(zip(full_list, sorted_list))
    for item in zipped:
        if item[0] != item[1]:
            return item[0]





find_missing_number([2, 3, 4])
find_missing_number([1, 3, 4, 6, 2, 9, 10, 8, 7])