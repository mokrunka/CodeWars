def reject(seq, predicate):
    result_list = []
    boolean_test = (predicate)
    for value in seq:
        if not boolean_test(value):
            result_list.append(value)
    return result_list

reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0)
reject(['a', 'b', 3, 'd'], lambda x: type(x)==int)
reject(['a', 'b', 3, 'd'], lambda x: type(x)==str)

