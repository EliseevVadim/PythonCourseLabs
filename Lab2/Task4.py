import re
name=input('Введите название файла:\n')
file=open(name, 'r')
lines=file.readlines()
pattern=re.compile(r'\(\b\d{3}\)\d{3}\-?\d{2}\-?\d{2}\b')
for i in range(len(lines)):
    for match in pattern.finditer(lines[i]):       
        print ('Строка {}, позиция {} : найдено \'{}\''.format(i+1, match.start()+1, match.group()))