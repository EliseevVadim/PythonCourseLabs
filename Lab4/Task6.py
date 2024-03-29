import numpy as np
#Fisrt subtask
print('*'*80)
print('First subtask:')
a = np.random.randint(0, 50, 15).reshape(3, 5)
b=np.random.randint(0, 50, 10).reshape(5, 2)
result = a.dot(b)
print('Matrix A:\n{}'.format(a))
print('Matrix B:\n{}'.format(b))
print('Result:\n{}'.format(result))
#Second subtask
print('*'*80)
print('Second subtask')
matrixMultiplier = np.random.randint(0, 100, 15).reshape(5, 3)
vectorMultiplier = np.random.randint(0, 100, 3)
outputProduct = matrixMultiplier.dot(vectorMultiplier)
print('Matrix:\n{}'.format(matrixMultiplier))
print('Vector:\n{}'.format(vectorMultiplier))
print('Product:\n{}'.format(outputProduct))
#Third subtask
#Our system: x - y = 7
#            3x + 2y = 16
print('*'*80)
print('Third subtask:')
coeffs = np.array([[1, -1], [3, 2]])
results = np.array([7, 16])
print('System:')
print('x - y = 7\n3x + 2y = 16')
answers = np.linalg.solve(coeffs, results)
print('X = {}'.format(answers[0]))
print('Y = {}'.format(answers[1]))
#Fourth subtask
print('*'*80)
print('Fourth subtask:')
matrix = np.random.randint(0, 100, 25).reshape(5, 5)
print('Matrix:\n{}'.format(matrix))
determinant = np.linalg.det(matrix)
print('Determinant is {}'.format(determinant))
#Fifth subtask
print('*'*80)
print('Fifth subtask')
sourceMatrix = np.random.randint(0, 100, 25).reshape(5, 5)
print('Source matrix:\n{}'.format(sourceMatrix))
transposedMatrix = sourceMatrix.transpose()
print('Transposed matrix:\n{}'.format(transposedMatrix))
inversedMatrix = np.linalg.inv(sourceMatrix)
print('Inversed matrix:\n{}'.format(inversedMatrix))
#Sixth subtask
print('*'*80)
print('Sixth subtask')
otherRandomMatrix = np.random.randint(0, 100, 25).reshape(5, 5)
print('Matrix for test:\n{}'.format(otherRandomMatrix))
values = np.linalg.eig(otherRandomMatrix)
product = np.prod(values[0])
deter = np.linalg.det(otherRandomMatrix)
print('The difference between product and determinant is {}'.format(product - deter))
