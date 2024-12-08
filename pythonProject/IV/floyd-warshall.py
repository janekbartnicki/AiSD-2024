def floyd_warshall(matrix):
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    return matrix


matrix_representation = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]

print(f'Macierz wynikowa: ')
for row in floyd_warshall(matrix_representation):
    print(row)
