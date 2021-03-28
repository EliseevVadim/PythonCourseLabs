def extra_enumerate(x):
    cum=0
    frac=0
    elem=0
    for i in x:
        cum+=i
        frac=cum/sum(x)
        elem=i
        yield i, elem, cum, frac  
x=[1,3,4,2]
for i, elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac)
input("Press Enter to continue...")