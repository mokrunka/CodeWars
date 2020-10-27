def moving_average(values, n):
    """Computes the moving average of a list of values 'values', of window size 'n'."""
    moving_average_list = []
    sum = 0
    test_sum = 0
    average = 0
    counter = 0
    for num in values:
        test_sum += num
    if len(values) == 0 or len(values) < n or n == 0:
        return None
    for i in range(len(values)):
        if (i + n - 1) < len(values):
            for j in range(i, i + n):
                sum += values[j]
                average = sum / n
            moving_average_list.append(average)
            sum = 0
        else:
            break
    return (moving_average_list)



# moving_average([40, 30, 50, 46, 39, 44], 3)
#
# test.describe("Basic Tests")
# test .assert_equals(moving_average([40, 30, 50, 46, 39, 44],3),[40.0, 42.0, 45.0, 43.0])
# test.assert_equals(moving_average([40, 30, 50, 46, 39, 44],2),[35.0, 40.0, 48.0, 42.5, 41.5])
# test.assert_equals(moving_average([40, 30, 50, 46, 39, 44],4),[41.5, 41.25, 44.75])
# test.assert_equals(moving_average([40, 30, 50, 46, 39, 44],0),None)