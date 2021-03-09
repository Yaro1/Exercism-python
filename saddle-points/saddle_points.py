def saddle_points(matrix):
    if not matrix:
        return []
    if sum([len(matrix[i]) for i in range(len(matrix))]) % len(matrix[0]):
        raise ValueError("Something wrong with size.")
    row = set()
    column = set()
    for i in range(len(matrix)):
        value = max(matrix[i])
        for j in range(len(matrix[0])):
            if matrix[i][j] == value:
                row.add((i, j))
    for i in range(len(matrix[0])):
        value = min([matrix[k][i] for k in range(len(matrix))])
        for j in range(len(matrix)):
            if matrix[j][i] == value:
                column.add((j, i))
    return [{"row": i[0] + 1, "column": i[1] + 1} for i in (row & column)]
