#!/usr/bin/env python
"read file and output content"
fname=open("/root/a.txt",'r+')
for content in fname:
    print content,
#在这个脚本中，实际上实现的功能很简单，但是有一个知识点需要了解，那就是，文件句柄可以应用到for,while中。
