def Matrix(matrix):
    m = len(matrix)
    matrix[:] = [[matrix[i][j] * 2 if i != j else matrix[i][j] for j in range(m)] for i in range(m)]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

Matrix(matrix)
print("Матрица увеличения в 2 раза:")
for row in matrix:
    print(row)
