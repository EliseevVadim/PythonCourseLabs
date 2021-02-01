line=input('Введите строку:\n')
words=line.replace('.', ' ').replace('-', ' ').replace(',', ' ').split()
larger_then_seven=[]
from_four_to_seven=[]
others=[]
for word in words:
    if len(word)>7:
        larger_then_seven.append(word)
    elif 4<=len(word)<=7:
        from_four_to_seven.append(word)
    else:
        others.append(word)
print('Слова длиннее 7 букв:')
print(larger_then_seven)
print('Слова от 4х до 7 букв:')
print(from_four_to_seven)
print('Остальные слова:')
print(others)
input("Press Enter to continue...")