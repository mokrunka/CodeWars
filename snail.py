def snail(snail_map):
    result = []
    num_rows = len(snail_map)
    num_cols = len(snail_map[0])
    i = 0
    j = 0
    while j < num_cols:
        result.append(snail_map[i][j])
        j += 1
    result.append(snail_map[i + 1][j])
    while i < num_rows:
        j = 0
        result.append(snail_map[i][j])
        j += 1
        i += 1
    print(result)








array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
snail(array)