import numpy as np
import torch
import torch.nn as nn


def custom_convolve(I, W, M, C, R_rows, R_cols, K_rows, K_cols):
    """This function does convolution of I and W given the below parameters

    Note: This function currently works for 3x3 kernels ONLY
    :param I:
    :param W:
    :param M:
    :param C:
    :param R_rows:
    :param R_cols:
    :param K_rows:
    :param K_cols:
    :return:
    """

    O = np.zeros((M, R_rows, R_cols), dtype=float)

    for m in range(M):
        for c in range(C):
            for r_rows in range(R_rows):
                for r_cols in range(R_cols):
                    for k_rows in range(-K_rows//2, K_rows//2 + 1):
                        for k_cols in range(-K_cols//2, K_cols//2 + 1):
                            O[m][r_rows][r_cols] += W[m][c][k_rows + K_rows//2][k_cols + K_cols//2] * I[c][r_rows + k_rows][r_cols + k_cols]

    return O


if __name__ == "__main__":
    np.random.seed(0)
    IFM = 3
    M = 2 #The output channels  == number of kernels
    H = 8
    W = 8
    I = np.random.randint(8, size=(IFM, H, W))

    # Weights = np.zeros((M, IFM, 3, 3), dtype=float)
    Weights = np.random.rand(M, IFM, 3, 3).astype('f')

    R_rows = H - 3 + 1
    R_cols = W - 3 + 1

    O = custom_convolve(I, Weights, M=M, C=IFM, R_rows=R_rows, R_cols=R_cols, K_rows=3, K_cols=3)
    print(O)

    input = torch.from_numpy(I)
    input = input.unsqueeze(0)
    input = input.type(torch.float32)


    # input = torch.randn(1, IFM, H, W)
    m = nn.Conv2d(IFM, M, 3, stride=1, bias=False)
    WT = torch.from_numpy(Weights)
    m.weight = torch.nn.Parameter(WT)
    output = m(input)
    print(output)
    a, b, c, d = output.shape
    output = output.reshape(b, c, d)


    output_numpy = output.detach().numpy()

    sub_result = np.subtract(O, output_numpy)
    print("Res: {}".format(np.sum(sub_result)))
