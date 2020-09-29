def two_oldest_ages(ages):
    result = []
    a = max(ages)
    ages.remove(a)
    b = max(ages)
    result.append(b)
    result.append(a)

    return result

two_oldest_ages([1, 5, 87, 45, 8, 8])