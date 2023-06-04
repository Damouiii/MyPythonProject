import numpy as np


def smaller_matrix(matrix, row, column):
    result = np.delete(matrix, column, 1)
    result = np.delete(result, row, 0)
    return result


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Error: Matrix is not square")
        return None
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        answer = 0
        for i in range(len(matrix[0])):
            answer += ((-1) ** i) * matrix[0][i] * determinant(smaller_matrix(matrix, 0, i))
        return answer


np.random.seed(1)
matrix = np.random.rand(10, 10)

# Testing determinant function.
a = determinant(matrix)

# Running the numpy det function so that we can compare our results
np_det = np.linalg.det(matrix)

print(a)
print(np_det)
print(a-np_det)