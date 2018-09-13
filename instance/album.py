#!/usr/bin/python3
def make_album(singer_name,album_name,number=''):
    album={'singer_name':singer_name,'album_name':album_name}
    if number:
        album['number']=number
    print(album)
make_album('zhangjie','wuwangxinan')
make_album('zhangliangyin','hhhhhhh',4)
while 1:
    print("Input the q to quit.")
    s_name=input("Please input the singer name:")
    if s_name == 'q':
        break
    print("Input the q to quit.")
    a_name=input("Please input the album name:")
    if a_name == 'q':
        break
    make_album(s_name,a_name)
