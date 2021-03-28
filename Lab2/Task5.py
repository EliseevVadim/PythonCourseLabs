import re
line=input('Введите строку для поиска\n')
results=re.findall(r'\b[A-Z][a-z]*\d{2}\b|\b[A-Z][a-z]*\d{4}\b', line)
for res in results:
    print(res)