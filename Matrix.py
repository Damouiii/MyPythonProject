class Matrix:
    matrix = []

    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        result = []
        for i in range(len(self.matrix[0])):
            result.append([])
            for j in range(len(self.matrix)):
                result[i].append(0)

        for n in range(len(self.matrix)):

            for m in range(len(self.matrix[0])):
                result[m][n] = self.matrix[n][m]

        return result

    def __str__(self):
        result = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result = result + str((self.matrix[i][j])) + " "
            result = result + "\n"

        return result

    def __add__(self, other):
        result = []
        for n in range(len(self.matrix)):
            result.append([])
            for m in range(len(self.matrix[0])):
                result[n].append(self.matrix[n][m] + other.matrix[n][m])

        return result


m1 = Matrix([[0, 2, 3], [4, 5, 6]])
m2 = Matrix([[0, 2, 1], [0, 0, 0]])

print(m1 + m2)
