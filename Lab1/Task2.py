my_list = ['0', '1', '2', '3', '4', '5']
flag=True
print('Исходный список:\n')
print(my_list)
for i in range(len(my_list)-1):
    if my_list[i]>my_list[i+1]:
        flag=False
        break
print(flag)    
input("Press Enter to continue...")