password=input('Введите проверяемый пароль:\n')
good=False
if len(password)>12:
    good=any(map(str.isdigit, password)) and any(map(str.islower, password)) and any(map(str.isupper, password))
if good:
    print('Пароль надежен')
else:
    print('Пароль слабый')    
input("Press Enter to continue...")