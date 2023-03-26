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

    def symmetric(self):
        return self.transpose() == self.matrix

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

    def __sub__(self, other):
        result = []
        for n in range(len(self.matrix)):
            result.append([])
            for m in range(len(self.matrix[0])):
                result[n].append(self.matrix[n][m] - other.matrix[n][m])

    def __mul__(self, other):
        result = []
        if len(self.matrix[0]) != len(other.matrix):
            print("Error: Number of columns of the first matrix and number of rows of second matrix must be the same!")

        for n in range(len(self.matrix)):
            result.append([])
            for m in range(len(other.matrix[0])):
                result[n].append(0)
                for k in range(len(other.matrix)):
                    result[n][m] += self.matrix[n][k] * other.matrix[k][m]

        return result


m1 = Matrix([[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]])

m2 = Matrix([[5, 8, 1, 2],
             [6, 7, 3, 0],
             [4, 5, 9, 1]])

m3 = Matrix([[0, 0],
             [0, 0]])

print(m3.symmetric())
