import sympy as sp
from sympy import *
from sympy.abc import x, y
from sympy.plotting import plot
#First subtask
print('*'*80)
function = x**2
integral = integrate(function)
derivative = diff(function)
print('The integral of {} is {}'.format(function, integral))
print('The derivative of {} is {}'.format(function, derivative))
plot(derivative, title='Производная функции {}'.format(function))
plot(integral, title='Интеграл функции {}'.format(function))
print('Построения произведены успешно')
#Second subtask
print('*'*80)
equation = [y**2+3*y-4, 0]
eqLine = 'y**2+3*y-4=0'
res = [pair[0] for pair in list(nonlinsolve(equation, (y, 0)))]
print('Корни уравнения {}:\n{}'.format(eqLine, res))
output = list(nonlinsolve((sp.sqrt(x-4*y)-2*sp.sqrt(x+3*y)-1, 7*sp.sqrt(x+3*y)+5*x+22*y-13), (x,y)))
print('Корни системы уравнений:\nsqrt(x-4y)-2sqrt(x+3y)=1\n7*sqrt(x+3y)+5x+22y=13:\n{}'.format(output[0]))
