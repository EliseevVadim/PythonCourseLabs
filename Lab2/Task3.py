import os
files = [file for file in os.listdir('WAV') if not file.endswith('txt')]
names=open('WAV/names.txt', 'r').readlines()
names=[name.rstrip() for name in names]
for filename in files:
    separated_name=filename.split('.')
    for name in names:
        if separated_name[0] in name:
            os.rename('WAV/'+filename, 'WAV/'+name+'.'+separated_name[1])
            print('Переименовано')