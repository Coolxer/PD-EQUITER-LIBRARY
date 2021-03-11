

import numpy as np

from methods.stationary.jacobi.method import jacobi_method

'''
a = np.arange(15).reshape(3, 5)

print(a.shape[1])

'''

# jacobi_validator(np.empty((0)), 1, 2, 3, 4)
# jacobi_validator(np.arange(6).reshape(2, 3), 1, 2, 3, 4)

# A = np.arange(9).reshape(3, 3)
'''
print(A)
print('\n------------\n')
print(np.diag(A))
print('\n------------\n')
print(np.diagflat(np.diag(A)))
print('\n------------\n')
# print(np.linalg.inv(A))

x = np.array([[1, 2], [3, 4]])
y = np.linalg.inv(x)
print(y)
'''

'''
## TWO WAYS TO GET L + U ##

# FIRST WAY
L = np.tril(A, -1)
U = np.triu(A, 1)
# D = np.diagflat(np.diag(A))
L_plus_U = L + U

# SECOND WAY
D = np.diagflat(np.diag(A))
L_plus_U = A - D
'''

'''
A = np.array([[1., 2.], [3., 4.]])
A_inv = np.linalg.inv(A)

print(A)
print('\n------------\n')
print(A_inv)
print('\n------------\n')
print(np.dot(A, A_inv))

'''

A = np.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]])
b = np.array([6, 10, 2])

# i, x = jacobi_method(A, b, 100, 1)

# print(i)
# print('\n------\n')
# print(x)

# print(A.sum(axis=1)[0])
# print(np.diag(A)[0])

print(A)
print('\n-=----=\n')


def dd(X):
    D = np.diag(np.abs(X))  # Find diagonal coefficients
    S = np.sum(np.abs(X), axis=1)  # Find row sum without diagonal

    print(D)

    print('\n--------\n')
    print(S)

    if np.all(D > S):
        print('matrix is diagonally dominant')
    else:
        print('NOT diagonally dominant')
    return


dd(A)
