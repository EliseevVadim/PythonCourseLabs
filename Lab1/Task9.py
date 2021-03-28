bank={5000:10, 1000:15, 500:20, 100:50, 50:100, 10:15}
withdraw=int(input('Введите сумму, которую необходимо снять:\n'))
withdraw_dict={}
count=0
if withdraw>0:
    for knote in bank.keys():
        count=int(withdraw/knote)
        if count<=bank[knote] and count!=0  and bank[knote]>0:
            withdraw_dict[knote]=count
            withdraw-=knote*count
            bank[knote]-=count
        elif count>bank[knote] and count!=0 and bank[knote]>0:
                withdraw_dict[knote]=bank[knote]
                withdraw-=knote*bank[knote]
                bank[knote]=0        
    if withdraw!=0:
        print('Операция не может быть выполнена')
        input("Press Enter to continue...")
    else:
        out=''
        for knote in withdraw_dict.keys():
            out+=str(withdraw_dict[knote])+'*'+str(knote)+'+'
        out=out[0:-1]
        print(out)
        input("Press Enter to continue...")
else:
    print('Некорректный ввод')
    input("Press Enter to continue...")