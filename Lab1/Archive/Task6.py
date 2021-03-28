line=input('Введите строку:\n')
dictionary={}
for i in range(len(line)):
    dictionary[line[i]]=dictionary.get(line[i], 0)+1
for key, value in dictionary.items():
    if value==1:
        print(key)
input("Press Enter to continue...")