import math
import random as r
length=r.randint(0, 10000)
rand_list=[r.randint(0, 1000) for _ in range(length)]
print('Исходный массив:')
print(rand_list)
print('Начальная длина - ', length)
new_pow=math.ceil(math.log2(length))
new_length=math.pow(2, new_pow)
print('Новая длина - ', int(new_length))
for _ in range(int(new_length)-length):
    rand_list.append(0)
print('Новый массив:')
print(rand_list)
input("Press Enter to continue...")