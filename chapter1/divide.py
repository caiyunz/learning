#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
一个整数被另外一个整数除，计算结果的小数部分被截出了，只留下整数部分。有些时候，这个功能很有用，但通常情况只需要普通的除法。要用实数而不是整数进行运算，或者让python改变出发的执行方式。
#如果希望python只执行普通的除法，那么可以在程序前加上 from __future__ import division
"""
#a=1/2
#print a

from __future__ import division
b=1/2
print b
"""导入代码要放到代码执行的最上面。在这里a和b不能同时运行，运行一个的时候需要注释另外一个"""
