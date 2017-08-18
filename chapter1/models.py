#!/usr/bin/python
#--coding: utf-8 --
"""
注意模块是怎么起作用的：用import 导入了模块，然后按照"模块.函数"的格式使用这个模块的函数
import math
math.sqrt(9)
在确定自己不会导入多个同名函数(从不同模块导入)的情况下，你可能不希望每次调用函数的时候，都要写上模块的名字。
那么，可以使用import命令的另外一种形式：
from math import sqrt
sqrt(9)
在使用了"from 模块import 函数"这种形式的import命令之后，就可以直接使用函数，而不需要模块名作为前缀。
"""
temp=42
print "The temperature is "+`temp`
"""
如果不加反引号，则会报错。因为连接的是字符串，而不是数字
"""
print "The temperature is "+str(temp)

print "The temperature is "+repr(temp)
"""
简而言之，str,repr和反引号是将python值转换为字符串的3种方法。函数str让字符串更易于阅读，而repr(和反引号)则把结果字符串转换为合法的python表达式
"""
