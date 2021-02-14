import os
import hashlib
links=[]
codes=[]
duplicates=[]
path=input('Введите путь к директории, которую необходимо обработать:\n')
for root, folder, files in os.walk(path, topdown=True):
    for file in files:
        links.append(os.path.join(root, file))
for link in links:
    try:
        codes.append(hashlib.md5(open(link, 'rb').read()).hexdigest())
        print('Сделано')
    except:
        print('Не судьба')
for link in links:
    print(link)
for code in codes:
    idxs=[i for i, ltr in enumerate(codes) if ltr == code]
    if len(idxs)>1:
        for idx in idxs:
            duplicates.append(links[idx])
        print(duplicates)
        duplicates.clear()
        idxs.clear()
input('Press Enter to continue')