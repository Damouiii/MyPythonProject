import numpy as np


def conv(image, small):
    for n in range(len(result[0])):
        for m in range(len(result)):
            e = 0
            for i in range(len(small)):
                for j in range(len(small[0])):
                    e += image[n + i][m + j] * small[i][j]

            result[n][m] = e

    return result


if __name__ == "__main__":
    # declare the arrays in numpy

    image = np.array([[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4],
                      [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])
    small = np.array([[1, 2, 0], [4, 5, 6], [0, 8, 9]], np.int32)
    result = np.zeros((3, 3), dtype=float)

    # and call the conv function

    res = conv(image, small)

    print(res)
