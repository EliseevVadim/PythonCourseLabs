import struct
import os
import sys
import argparse
def init_args(args=None):
    parser=argparse.ArgumentParser()
    parser.add_argument('-f', '--folder')
    parser.add_argument('-d', '--dump')
    parser.add_argument('-g', '--genre')
    parsed=parser.parse_args()
    return parsed.folder, parsed.dump, parsed.genre

if __name__=='__main__':
    folder, dump, genre=init_args(sys.argv[1:])
    files = os.listdir(folder)
    files = [f for f in files if f.endswith('.mp3')]
    dic = {}
    num = 1
    for file in files:
        path = os.path.join(folder, file)
        with open(path, 'rb') as f:
            size = os.path.getsize(path)
            f.seek(size - 128)
            mas = f.read(128)            
            header = struct.unpack('<3s30s30s30sI28sbbb', mas)
            dic[path] = []
            try:
                title = header[1].decode('utf-8')
                artist = header[2].decode('utf-8')
                album = header[3].decode('utf-8')
                print('{} - {} - {}'.format(artist, title, album))
                print('header[0] - {}'.format(header[0].decode('utf-8')))
                print('comment - {}'.format(header[5].decode('utf-8')))
                print('zero byte - {}'.format(header[6]))
                print('number - {}'.format(header[7]))
                print('genre idx - {}'.format(header[8]))                 
            except:
                print('Something wrong')
    if not dump is None:
        print('дампим')
