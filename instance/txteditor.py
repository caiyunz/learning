#/usr/bin/env python
#-*- coding:utf-8 -*-
def echo():
    print "Please input the selection:\
    1.取五个数的和;\
    2.取五个数的平均值;\
    X.退出"
    num=raw_input()
    return num
while(True):
    num=echo()
    if(num=='1'):
        print "取五个数的和:"
        print "1+2+3+4+5 is: %d" %(1+2+3+4+5)
    elif(num=='2'):
        print "取五个数的平均值:"
        print "(1+2+3+4+5)/5 is: %d" %((1+2+3+4+5)/5)
    elif(num=='X'):
        print "Exit"
        break
