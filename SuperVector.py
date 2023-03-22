class SuperVector:
    vector = []

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        if len(self.vector) != len(other.vector):
            print("error: vectors must have same length")
            return []

        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] + other.vector[i])

        return SuperVector(result)

    def __sub__(self, other):
        if len(self.vector) != len(other.vector):
            print("error: vectors must have same length")
            return []

        result = []
        for i in range(len(self.vector)):
            result.append(self.vector[i] - other.vector[i])

        return SuperVector(result)

    def __mul__(self, other):
        result = [0]
        for i in range(len(self.vector)):
            result[0] = result[0] + self.vector[i] * other.vector[i]
        return SuperVector(result)

    def __len__(self):
        return len(self.vector)

    def __str__(self):
        result = ""
        for value in self.vector:
            result = result + str(value) + " "
        return result


v1 = SuperVector([1, 1, 1, 1, 1])

v2 = SuperVector([2, 2, 1, 1, 1])

print(v1 + v2)
print(v1 - v2)
print(v2 * v1)
