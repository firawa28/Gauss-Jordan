import numpy as np

def main():
    print ("Silahkan tentukan ukuran matriks yang diinginkan?:")
    m = int(input("Baris: " ))
    n = int(input("Kolom: "))
    
    matrix = np.zeros((m,n))
    
    for subscript1 in range (0, m):
        for subscript2 in range (0, n):
            print ("Berapakah nilai matriks pada baris {} dan kolom {}".format(subscript1 + 1, subscript2 + 1))
            matrix[subscript1][subscript2] = int(input())
            
    print ("Berikut merupakan matrix yang anda input\n", matrix)
    
    print ("=="*30)
    print ("Gauss Jordan Elimination")
    print ("=="*30)

    for subscript1 in range (0, m - 1):
        for subscript2 in range (subscript1 + 1, m):
            matrix[subscript2][:] = matrix[subscript2][:] - matrix[subscript1][:] * (matrix[subscript2][subscript1] / matrix[subscript1][subscript1])
            print(matrix)
            print('=='*30)

    for subscript3 in range(m - 1, 0, -1):
        for subscript4 in range(subscript3 - 1, -1, -1):
           matrix[subscript4][:] = matrix[subscript4][:] - matrix[subscript3][:] * (matrix[subscript4][subscript3] / matrix[subscript3][subscript3])
           print (matrix)
           print ('=='*30)

    for subscript5 in range(0, m):
        matrix[subscript5][:] = matrix[subscript5][:] / matrix[subscript5][subscript5]
        print (matrix)
        print ('=='*30)

main()