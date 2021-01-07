import numpy as np

Vektor = np.array([
    [8, -9, 1, -8, 80],
    [-3, -1, 5, 4, 7],
    [-2, -1, -3, 8, -30],
    [-2, -8, -1, 2, 18]
], float)


def main():
    [m, n] = np.shape(Vektor)
    for subscript1 in range (0, m - 1):
        for subscript2 in range (subscript1 + 1, m):
            Vektor[subscript2][:] = Vektor[subscript2][:] - Vektor[subscript1][:] * (Vektor[subscript2][subscript1] / Vektor[subscript1][subscript1])
            print(Vektor)
            print('------------------------------------------------------------')

    for subscript3 in range(m - 1, 0, -1):
        for subscript4 in range(subscript3 - 1, -1, -1):
           Vektor[subscript4][:] = Vektor[subscript4][:] - Vektor[subscript3][:] * (Vektor[subscript4][subscript3] / Vektor[subscript3][subscript3])
           print (Vektor)
           print ('------------------------------------------------------------')

    for subscript5 in range(0, m):
        Vektor[subscript5][:] = Vektor[subscript5][:] / Vektor[subscript5][subscript5]
        print (Vektor)
        print ('---------------------------------------------------------------')

main()