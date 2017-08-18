#!/usr/bin/python
#-*-coding:utf-8 -*-
"""
name=input("What is your name?")
input会假设用户输入的是合法的Python表达式(或多或少有些与repr函数相反的意思).如果以字符串做为输入的名字，程序运行是没有问题的:
What is your name?"Gumby"
然而，要求用户带着符号输入他们的名字有点过分,因此，这就需要raw_input函数，它会把所有的输入当作原始数据，然后将其放入字符串中:
raw_input("Enter a number:")
'3'
除非对input有特别的需要，否则应该尽可能使用raw_input函数
"""
