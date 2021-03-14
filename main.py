'''
from equiter.equiter import *

equiter = Equiter()


A = np.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]])
b = np.array([6, 10, 2])


solution = equiter.solve('jacobi', Parameters(
    A, b, 3, 0.0001))
'''
