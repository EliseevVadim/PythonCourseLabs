def frange(start,end,step):
    l=[]
    while start<end-step:
        l.append(start)
        start+=step
    return l
for i in frange(1, 5, 0.1):
    print(i)
input("Press Enter to continue...")