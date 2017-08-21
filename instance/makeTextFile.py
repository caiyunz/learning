#!/usr/bin/env python
import sys
'input and write into a file'
fname='/root/a.txt'
if os.path.exists(fname):
    print "ERROR:'%s' already exists" % fname
    sys.exit(0)
else:
    print "The program is working!"
fopen=open(fname,'w+')
while True:
    entry=raw_input("Please input the content:")
    if(entry == "."):
        break
    else:
        fopen.writelines(entry+'\n')
#append()方法不能用于文件句柄中，文件句柄中不支持appaen()追加。append()方法适合于列表，元组
#文件句柄中适合用writelines,但是需要注意writelines不会自动添加换行符。需要手动添加。
fopen.close()
