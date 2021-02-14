import argparse
import sys
import os
import datetime
def init_args(args=None):
    parser=argparse.ArgumentParser()
    parser.add_argument('-s', '--source', help='source directory')
    parser.add_argument('-d', '--days', help='minimal change difference')
    parser.add_argument('-sz', '--size', help='minimal file size')
    parsed=parser.parse_args()
    return parsed.source, parsed.days, parsed.size

if __name__=='__main__':
    source, date, size=init_args(sys.argv[1:])
    files=os.listdir(source)
    archive=[]
    small=[file for file in files if os.path.getsize(os.path.join(source, file))<int(size)]
    for file in files:
        now=datetime.datetime.now()
        mod=datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(source, file)))
        sb=now-mod
        if sb.days>int(date):
            archive.append(file) 
    if(len(archive)>0):
        os.mkdir(os.path.join(source, 'Archive'))
        for file in archive:
            os.rename(os.path.join(source, file), os.path.join(source, 'Archive', file))
    if(len(small)>0):
        os.mkdir(os.path.join(source, 'Small'))
        for file in small:
            try:
                os.rename(os.path.join(source, file), os.path.join(source, 'Small', file))
            except:
                print('Файл уже перемещен')
    print('Готово')