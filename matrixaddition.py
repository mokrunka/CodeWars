def matrix_addition(m1, m2):
    sum_matrix = []
    add_rows = zip(m1, m2)
    for x, y in add_rows:
        size = len(x)
        for i in range(len(x)):
            placeholder = x[i] + y[i]
            i += 1
            sum_matrix.append(placeholder)

    # creating a template for the solution using the input
    result = m1
    k = 0

    for i in range(size):
        for j in range(size):
            result[i][j] = sum_matrix[k]
            k += 1

    return result