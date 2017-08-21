函数是可以调用(可能包含参数，也就是放在圆括号中的值),它执行某种行为并且返回一个值。一般来说，内建的callable函数可以用来判断函数是否可调用：
>>> import math
>>> x=1
>>> y=math.sqrt
>>> callable(x)
False
>>> callable(y)
True
>>> 
注意：函数callable在Python 3.0中不再可用，需要使用表达式hasattr(func,__call__)代替。

记录函数
如果想要给函数写文档，让后面使用该函数的人能理解的话，可以加入注释(以# 开头)。另外一个方式就是直接写上字符串。这类字符串在其他地方可能会非常有用，比如在def语句后面(以及在模块或者类的开头).
如果在函数的开头写下字符串，它就会作为函数的一部分进行存储，这称为文档字符串。
>>> def square(x):
...     'Calculates the square of the number x.'
...     return x*x
... 
>>> square.__doc__
'Calculates the square of the number x.'

注意：__doc__是函数属性。属性名中的双下划线表示它是个特殊属性。属性名中的双下划线表示它是个特殊属性。
内建的help函数是非常有用的。在交互式解释器中使用它，就可以得到关于函数，包括它的文档字符串的信息：

字符串(以及数字和元组)是不可变的，即无法被修改(也就是说只能用新的值覆盖)。所以它们做参数的时候也就无需多做介绍。
当两个变量同时引用一个列表的时候，它们的确是同时引用一个列表。就是这么简单。如果想避免出现这种情况，可以复制一个列表的副本。当在序列中做切片的时候，返回的切片总是一个副本。因此，如果你复制了整个列表的切片，就会得到一个副本。

注意：字典的键并没有具体的顺序，所以当字典打印出来的时候，顺序是不同的。如果读者在自己的解释器中打印出的顺序不同，请不要担心，这是很正常的。

目前为止我们所使用的参数都叫做位置参数，因为它们的位置很重要-事实上比它们的名字更加重要。本节中引入的这个功能可以回避位置问题，当你慢慢习惯使用这个功能以后，就会发现程序规模越大，它们的作用也就越大。

位置参数和关键字参数

def print_params(*params):
    print params
参数前的星号将所有值放置在同一个元组中。可以说是将这些值收集起来，然后使用。不知道能不能用来联合普通参数。
def print_params_2(title,*params):
    print title
    print params
print_params_2('Params',1,2,3)
Params
(1,2,3)
>>> print_params_2('Params',1,2,3)
Params
(1, 2, 3)
没问题！所以星号的意思就是"收集其余的位置参数".如果不提供任何供收集的元素，params就是个空元组：
>>> print_params_2('Nothing:')
Nothing:
()
>>> 
的确如此，很有用。那么能不能处理关键字参数(也是参数)呢？
>>> print_params_2('Hmm...',something=43)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_params_2() got an unexpected keyword argument 'something'
看来不行。所以我们需要另外一个能处理关键字参数的"收集"操作。那么语法应该怎么写呢？会不会是"**"?
>>> def print_params_3(**params):
...     print params
... 
>>> print_params_3(x=1,y=2,z=3)
{'y': 2, 'x': 1, 'z': 3}
>>> 
返回的是字典，而不是元组。
>>> def print_params_4(x,y,z=3,*pospar,**keypar):
...     print x,y,z
...     print pospar
...     print keypar
... 
>>> print_params_4(1,2,3,5,6,7,foo=1,bar=3)
1 2 3
(5, 6, 7)
{'foo': 1, 'bar': 3}

反转过程：
如何将参数收集为元组和字典已经讨论过了，但是事实上，如果使用*和**的话，也可以执行相反的操作。
>>> def add(x,y):return x+y
... 
>>> params=(1,2)
>>> add(*params)
3
这个过程或多或少有点像我们上一节中介绍的方法的逆方法。不是要收集参数，而是分配它们在"另一端"。使用*运算符就简单了-不过是在调用而不是在定义时使用：

对于参数列表来说工作正常，只要扩展的部分是最新的就可以。可以使用同样的技术来处理字典--使用双星号运算符。
在定义或者调用函数时使用星号(或者双星号)仅传递元组或字典,所以可能没遇到什么麻烦：
>>> def with_stars(**kwds):
...     print kwds['name'],'is',kwds['age'],'years old'
... 
>>> def without_start(kwds):
...     print kwds['name'],'is',kwds['age'],'years old'
... 
>>> args={'name':'Mr.Gumby','age':42}
>>> with_stars(**args)
Mr.Gumby is 42 years old
提示：使用拼接操作符"传递"参数很有用，因为这样一来就不用关心参数的个数之类的问题，例如：

嵌套作用域
Python的函数是可以嵌套的，也就是说可以将一个函数放在另一个里面。
def foo():
    def bar():
        print "Hello,world!"
    bar()
嵌套一般来说并不是那么有用，但它有一个很突出的应用，例如需要用一个函数"创建"另一个。也就意味着可以像下面这样(在其他函数内)书写函数：
def multiplier(factor):
    def multiplyByFactor(number):
        return number*factor
    return multiplyByFactor
一个函数位于另外一个里面，外层函数返回里层函数。也就是说函数本身被返回了--但并没有被调用。重要的是返回的函数还可以访问它的定义所在的作用域。换句话说，它"带着"它的环境(和相关的局部变量).
每次调用外层函数，它内部的函数都被重新绑定，factor变量每次都有一个新的值。由于Python的嵌套作用域，来自外部作用域的这个变量
>>> def multiplier(factor):
...     def multiplyByFactor(number):
...         return number*factor
...     return multiplyByFactor
... 
>>> double=multiplier(2)
>>> double(5)
10
>>> triple=multiplier(3)
>>> triple(3)
9
>>> multiplier(5)(4)
20
类似multiplyByFactor函数存储自封闭作用域的行为叫做闭包
外部作用域的变量一般来说是不能进行重新绑定的。nonlocal关键字被引入。它和global关键字的使用方式类似，可以让用户对外部作用域的变量进行赋值。

递归
def recursion():
    return recursion()
这类递归叫做无穷递归，类似于while True开始的无穷循环，中间没有break或者return语句。因为(理论上讲)它永远不结束。我们想要的是能做一些有用的事情的递归函数。有用的递归函数包含以下几部分:
当函数直接返回值时有基本实例(最小可能性问题);
递归实例，包括一个或者多个问题最小部分的递归调用。
这里的关键就是将问题分解为小部分，递归不能永远继续下去，因为它总是以最小可能性问题结束，而这些问题又存储在基本实例中的。

