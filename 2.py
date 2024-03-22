def el(matrix):
    return any(element > 0 for row in matrix for element in row)

matrix = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, 8, -9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

result = el(matrix)
print("Есть ли положительные элементы в матрице?", result)

