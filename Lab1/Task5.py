line=input('Введите строку:\n')
words=line.split()
for i in range(len(words)):
    if words[i].istitle():
        words[i]=words[i].upper()
output=' '.join(words)
print(output)
input("Press Enter to continue...")