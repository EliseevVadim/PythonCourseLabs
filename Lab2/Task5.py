import re
line=input('Введите строку для поиска\n')
results=re.findall(r'\b[A-Z][a-z]*\d{2,4}\b', line)
for res in results:
    print(res)