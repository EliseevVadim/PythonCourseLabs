number=input('Введите номер карты:\n')
newline=''
for i in range(len(number)):
    if 3<i<12:
        newline+='*'
    else:
        newline+=number[i]
print(newline)
input("Press Enter to continue...")