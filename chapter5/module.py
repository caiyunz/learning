从模块导入函数的时候，可以使用：
import somemodule
或者
from somemodule import somefunction
或者
from somemodule import somefunction,anotherfunction,yetanotherfunction
或者
from somemodule import *
只有确定自己想要从给定的模块导入所有功能时，才应该使用最后一个版本。但是如果两个模块都有open函数，那又该怎么办？只需使用第一种方式导入，然后像下面这样使用函数:
module1.open(...)
module2.open(...)
但还有另外的选择：可以在语句末尾增加一个as子句，在该子句后给出名字，或为整个模块提供别名：
>>> import math as foobar
>>> foobar.sqrt(4)
2.0
也可以为函数提供别名：
>>> from math import sqrt as foobar
>>> foobar(4)
2.0
对于open函数，可以像下面这样使用:
from module1 import open as open1
from module2 import open as open2
注意：有些模块，例如os.path是分层次安排的(一个模块在另一个模块的内部).
就算是不起眼的赋值语句也有一些特殊的技巧
序列解包
赋值语句的例子已经给过不少，其中包括对变量和数据结构成员的(比如列表中的位置和分片以及字典中的槽)赋值。但赋值的方法还不止这些。比如，多个赋值操作可以同时进行：
>>> x,y,z=1,2,3
>>> print x,y,z
1 2 3
>>> x,y=y,x
>>> print x,y,z
事实上，这里所做的事情叫做序列解包或可选代解包-将多个值的序列解开，然后放到变量的序列中。更形象一点的表示出来就是：
>>> values=1,2,3
>>> values
(1, 2, 3)
>>> x,y,z=values
>>> print x,y,z
1 2 3
当函数或者方法返回元组(或者其他序列或可迭代对象)时，这个特性尤其有用。假设需要获取(和删除)字典中任意的键-值对，可以使用popitem方法，这个方法将键-值作为元组返回。那么这个元组就可以直接赋值到两个变量中：
>>> scoundrel={'name':'Robin','girlfriend':'Marion'}
>>> key,value=scoundrel.popitem()
>>> key
'girlfriend'
>>> value
'Marion'
它允许函数返回一个以上的值并且打包成元组，然后通过一个赋值语句很容易进行访问。所解包的序列中的元素数量必须和放置在赋值符号=左边的变量数量完全一致，否则Python会在赋值时引发异常：
>>> x,y,z=1,2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: need more than 2 values to unpack
>>> x,y,z=1,2,3,4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack
>>> 
注意:Python 3.0中有另外一个解包的特性：可以像在函数的参数列表中一样使用星号运算符。例如，a,b,rest*=[1,2,3,4]最终会在a和b都被赋值之后将所有其他的参数都收集到rest中。本例中，rest的结果将会是[3,4].使用星号的变量也可以放在第一个位置，这样它就总会包含一个列表。右侧的赋值语句可以是可迭代对象。

链式赋值
链式赋值是将同一个值赋给多个变量的捷径。它看起来有些像上节中的并行赋值，不过这里只处理一个值：
x=y=somefunction()
y=somefunction()
x=y
注意上面的语句和下面的语句不一定等价：
x=somefunction()
y=somefunction()

增量赋值
这里没有将赋值表达式写为x=x+1,而是将表达式运算符放置在赋值元素符=的左边，写成x+=1.这种写法叫做增量赋值，对于*,/,%等标准运算符都适用：
>>> x=2
>>> x+=1
>>> print x
3
>>> x*=2
>>> x
6
对于其他数据类型也适用(只要二元运算符本身适用于这些数据类型即可)：
>>> fnord='foo'
>>> fnord+='bar'
>>> fnord
'foobar'
>>> fnord*=2
>>> fnord
'foobarfoobar'
增量赋值可以让代码更加紧凑和简练
语句块:缩排的乐趣
语句块并非一种语句，而是在掌握后面两节的内容之前应该了解的知识。
语句块是在条件为真(条件语句)时执行或者执行多次(循环语句)的一组语句。在代码前放置空格来缩进语句即可创建语句块。
注意：使用tab字符也可以缩进语句块。Python将一个tab字符解释为到下一个tab字符位置的移动，而一个tab字符位置为8个空格，但是标准且推荐的方式是只用空格，尤其是在每个缩进需要4个空格的时候。
块中的每行都应该缩进同样的量。下面的伪代码展示了缩进的工作方式：
很多语言使用特殊单词或者字符来表示一个语句块的开始，用另外的单词或者字符(比如end或者})表示语句块的结束。在Python中，冒号(:)用来标识语句块的开始，块中的每一个语句都是缩进的(缩进量相同).当回退到和已经闭合的块一样的缩进量时，就表示当前块已经结束了

布尔变量的作用：
真值是接下来内容的主角
下面的值在作为布尔表达式的时候，会被解释器看作假：
False None 0 "" () [] {}
换句话说，也就是标准值False和None,所有类型的数字0(包括浮点型，长整型和其他类型),空序列(比如空字符串，元组和列表)以及空的字典都为假。其他的一切都被解释为真，包括特殊值True.
也就是说Python中的所有值都能被解释为真值，"标准的"真值为True和False.标准的真值为0(表示假)和1(表示真)。事实上，True和False只不过是1和0的一种"华丽"的说法而已.
如果某个逻辑表达式返回1或0，那么它实际的意思是返回True或False。
布尔值True和False属于布尔类型，bool函数可以用来转换其他值。

比较不兼容类型
理论上，对于相对大小的任意两个对象x和y都是可以使用比较运算符(例如,<和<=)比较的，并且都会得到一个布尔值结果。但是只有在x和y是相同或者近似类型的对象时，比较才有意义。
正如将一个整形数添加到一个字符串中是没有意义的，检查一个整形是否比一个字符串小，看起来也是毫无意义的。
在Python中比较运算和赋值运算一样是可以连接的-几个运算符可以连在一起使用，比如：0<age<100

相等运算符
如果想要知道两个东西是否相等，应该使用相等运算符，即两个等号==：
单个相等运算符是赋值运算符，是用来改变值的，而不能用来比较。
is:同一性运算符
这个运算符比较有趣。它看起来和==一样，事实上却不同：
>>> x=y=[1,2,3]
>>> z=[1,2,3]
>>> x==y
True
>>> x==z
True
>>> x is y
True
>>> x is z
False
一切看起来都很好，但是最后一个结果很奇怪，x和z相等却不等同，因为is运算符是判定同一性而不是相等性的。变量x和y都被绑定到同一列表上，而变量z被绑定在另外一个具有相同数值和顺序的列表上。它们的值可能相等，但是却不是同一个对象。
>>> x=[1,2,3]
>>> y=[2,4]
>>> x is not y
True
>>> del x[2]
>>> y[1]=1
>>> y.reverse()
>>> y
[1, 2]
>>> x==y
True
>>> x is y
False
>>> 
总结一下：使用==运算符来判定两个对象是否相等，使用is判定两者是否等同(同一个对象)
警告：避免将is运算符用于比较类似数值和字符串这类不可变值。由于Python内部操作这些对象的方式的原因，使用is运算符的结果是不可预测的。

in：成员资格运算符
字符串和序列比较
字符串可以按照字母顺序排列进行比较：
>>> "alpha"<"beta"
True
如果字符串内包括大写字母，那么结果就会有点乱(实际上，字符是按照本身的顺序值排列的。一个字母的顺序值可以用ord函数查到，ord函数与chr函数功能相反).如果要忽略大小写字母的区别，可以使用字符串方法upper和lower.

布尔运算符
返回真值的对象已经介绍过许多(事实上，所有值都可以解释为真值，所有的表达式也都返回真值).但有时想要检查一个以上的条件。例如，如果需要编写读取数字并且判断该数字是否位于1-10之间的程序，可以像下面这样做：

短路逻辑和条件表达式
布尔运算符有个有趣的特性：只有在需要求值时才进行求值。举例来说，表达式x and y需要两个变量都为真时才为真，所以如果x为假，表达式就会立刻返回false,而不管y的值。实际上，如果x为假，表达式会返回x的值-否则它会返回y的值。这种行为被称为短路逻辑或惰性求值：布尔运算符通常被称为逻辑运算符，在表达式x or y中，x为真时，它直接返回x值，否则返回y值。注意，这意味着在布尔运算符之后的所有代码都不会执行。

if语句有个非常有用的"近亲",它的工作方式多少有点像下面这样(伪代码):
if not condition:
    crash program
究竟为什么会需要这样的代码呢？就是因为与其让程序在晚些时候崩溃，不如在错误条件出现时直接让它崩溃。一般来说，你可以要求条件必须为真(例如，在检查函数参数的属性时，或者作为初期测试和调试过程中的辅助条件).语句中使用的关键字是assert
如果需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert语句就有用了，他可以在程序中置入检查点。

在Python中迭代序列时，一些函数非常有用。
并行迭代
程序可以同时迭代两个序列。比如有下面两个列表：
names=['anne','beth','george','damon']
ages=[12,45,32,102]
for i in range(len(names)):
    print names[i],'is',ages[i],'years old'
这里i是循环索引的标准变量名。
而内建的zip函数可以用来进行并行迭代,可以把两个序列"压缩"在一起，然后返回一个元组的列表：
zip(names,ages)
[('anne',12),('beth',45),('george',32),('damon',102)]
现在我可以在循环中解包元组：
for name in zip(names,ages):
    print name,'is',age,'years old'
zip函数也可以作用于任意多的序列。关于它很重要的一点是zip可以应付不等长的序列：当最短的序列"用完"的时候就会停止：
>>> zip(range(5),xrange(100000))
[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
>>> 
在上面的代码中，不推荐用range替换xrange-尽管只需要前5个数字，但range会计算所有的数字，这要花费很长的时间。而使用xrange就没这个问题了，它只计算前5个数字。

编号迭代
有些时候想要迭代序列中的对象，同时还要获取当前对象的索引。例如，在一个字符串列表中替换所有包含'xxx'的子字符串。实现的方法肯定有很多,假设你想象下面这样做：

reversed和sorted:它们同列表的reverse和sort(sorted和sort使用同样的参数)方法类似，但作用于任何序列或可迭代对象上，不是原地修改对象，而是返回翻转或排序后的版本:

列表推倒式--轻量级循环
列表推倒式是利用其他列表创建新列表的一种方法。它的工作方式类似于for循环，也很简单：
>>> [x*x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
也可以增加更多for语句的部分：
>>> [(x,y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
作为对比，下面的代码使用两个for语句创建了相同的列表：
>>> result=[]
>>> for x in range(3):
...     for y in range(3):
...         result.append((x,y))
... 
>>> result
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
>>> 
也可以和if子句联合使用，像以前一样：
>>> girls=['alice','bernice','clarice']
>>> boys=['chris','arnold','bob']
>>> [b+'+'+g for b in boys for g in girls if b[0]==g[0]]
['chris+clarice', 'arnold+alice', 'bob+bernice'
这样就得到了那些名字首字母相同的男孩和女孩

注意：使用普通的圆括号而不是方括号不会得到"元组推导式"。

使用del删除
一般来说，Python会删除那些不再使用的对象(因为使用者不会再通过任何变量或者数据结构引用它们):
>>> scoundrel={'age':42,'first name':'Robin','last name':'of Lucksley'}
>>> robin=scoundrel
>>> scoundrel
{'first name': 'Robin', 'age': 42, 'last nam': 'of Lucksley'}
>>> robin
{'first name': 'Robin', 'age': 42, 'last nam': 'of Lucksley'}
>>> scoundrel=None
>>> robin
{'first name': 'Robin', 'age': 42, 'last nam': 'of Lucksley'}
>>> 
首先，robin和scoundrel都被绑定到同一个字典上。所以当设置scoundrel为None的时候，字典通过robin还是可用的。但是当我把robin也设置为None的时候，字典就"漂"在内存里面了，没有任何名字绑定到它伤民。没有办法获取和使用它，所以Python解释器直接删除了那个字典。注意：也可以使用None之外的其他值。字典同样会"消失不见"

另外一个方法就是使用del语句,它不仅会移除一个对象的引用，也会移除那个名字本身。

5.7.3使用exec和eval执行和求值字符串
有些时候可能会动态地创造Python代码，然后将其作为语句执行或作为表达式计算，这可能接近于"黑暗魔法"-在此之前，一定要慎之又慎，仔细考虑。
警告：会学到如何执行存储在字符串中的Python代码。这样做会有很严重的潜在安全漏洞。如果程序将用户提供的一段内容中的一部分字符串作为代码执行，程序可能会失去对代码执行的控制，这种情况在网络应用程序--比如CGI脚本中尤其危险

exec
执行一个字符串的语句是exec:
>>> exec "print 'Hello,world!'"
Hello,world!
但是，使用简单形式的exec语句绝不是好事。很多情况下可以给它提供命名空间-可以放置变量的地方。你想这样做，从而使代码不会干扰命名空间，比如，下面的代码中使用了名称sqrt:
注意：命名空间的概念，或称为作用域，是非常重要的知识。但是现在可以把它想象成保存变量的地方，类似于不可见的字典。所以在程序执行x=1这类赋值语句时，就将键x和值1放在当前的命名空间内，这个命名空间一般来说都是全局命名孔家，但这并不是必须的。

>>> from math import sqrt
>>> exec "sqrt=1"
>>> sqrt(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

>>> from math import sqrt
>>> scope={}
>>> exec 'sqrt=1' in scope
>>> sqrt(4)
2.0
>>> scope['sqrt']
1

eval
eval(用于'求值')是类似于exec的内建函数。exec函数会执行一系列Python语句，而eval会计算Python表达式(以字符串形式书写),并且返回结果值，(exec语句并不返回任何对象，因为它本身就是语句).例如，可以使用下面的代码创建一个Python计算器:
>>> eval(raw_input("Enter an arithmetic expression:"))
Enter an arithmetic expression:16*3+2
50
注意：表达式eval(raw_input(...))事实上等于input(...).
跟exec一样，eval也可以使用命名空间。尽管表达式几乎不像语句那样为变量重新赋值(事实上，可以给eval语句提供两个命名空间,一个全局的一个局部的。全局的必须是字典，局部的可以是任何形式的映射)。
警告：尽管表达式一般不给变量重新赋值，但它们的确可以(比如可以调用函数给全局变量重新赋值)。所以使用eval语句对付一些不可信任的代码并不比exec语句安全。目前，在Python内没有任何执行不可信任代码的安全方式。一个可选的方案是使用Python的实现

断言：断言简单来说就是肯定某事(布尔表达式)为真，也可在后面跟上这么认为的原因。如果表达式为假，断言就会让程序崩溃。比起让错误潜藏在程序中，知道你不知道它源于何处，更好的方法是尽早找到错误。

