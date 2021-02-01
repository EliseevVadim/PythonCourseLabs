sum=float(input());
try:
    if sum<0:
        raise Exception('Число отрицательное')    
    else:
        rubbles=int(sum);
        pennyes=int(sum*100-rubbles*100);
        print(rubbles, 'руб.', pennyes, 'коп.', sep=' ');
        input("Press Enter to continue...");
except Exception:
    print('Некорректный формат')
    input("Press Enter to continue...");