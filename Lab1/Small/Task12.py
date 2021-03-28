from math import ceil
def get_frames(signal, size, overlap):
    step=ceil(size*overlap)
    pos=0
    length=len(signal)
    while pos<length:
        if pos==0:
            yield signal[:step]
        else:
            yield signal[pos:pos+size]
        pos+=step
x = [1,2,3,4,5,6,7,8]
for frame in get_frames(x, size=4, overlap=0.5):
    print(frame)
input("Press Enter to continue...")