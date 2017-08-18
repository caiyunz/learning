#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
数据结构:数据结构是通过某种方式(例如对元素进行编号)组织在一起的数据元素的集合，这些数据元素可以是数字或者字符，甚至可以是其他数据结构。在Python中，最基本的数据结构是序列。序列中的每个元素被分配一个序号-即元素的位置，也称为索引。第一个索引是0,第二个则是1。
Python使用的编号机制可能看起来很奇怪，但这种方法其实非常自然。在后面的章节中可以看到，这样做的一个原因是也可以从最后一个元素开始计数:序列中的最后一个元素标记为-1，倒数第二个元素为-2，以此类推。这就意味着我们可以从第一个元素向前或者向后计数了，第一个元素位于最开始，索引为0。
Python包含6中内建的序列，主要介绍常用的两种类型:列表和元组。其他的内建序列类型有字符串，Unicode字符串，buffer对象和xrange对象。
列表和元组的主要区别在于，列表可以修改，元组则不能。也就是说如果要根据要求来添加元素，那么列表可能会更好用，而出于某些原因，序列不能修改的时候，使用元组则更为合适。一般来说，在几乎所有的情况下列表都可以替代元组(第四章将会介绍一个需要注意的例外情况:使用元组作为字典的键。在这种情况下，因为键不可修改，所以就不能使用列表)
序列也可以包含其他的序列。
Python之中还有一种名为容器的数据结构。容器基本上是包含其他对象的任意对象。序列（例如列表和元组)和映射(例如字典)是两类主要的容器。序列中的每个元素都有自己的编号，而映射中的每个元素择优一个名字(也称为键)。
所有序列类型都可以进行某些特定的操作。这些操作包括:索引(indexing),分片(sliceing),加(adding),乘(multiplying)以及检查某个元素是否属于序列的成员。除此之外，Python还有计算序列长度，找出最大元素和最小元素的内建函数。
"""
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year=raw_input('Year:')
month=raw_input('Month(1-12):')
day=raw_input('Day(1-31):')
month_number=int(month)
day_number=int(day)
month_name=months[month_number-1]
ordinal=day+endings[day_number-1]
print month_name +' '+ordinal+'. '+year
"""
分片操作对于提取序列的一部分是很有用的。而编号在这里显得尤为重要.分片操作的实现需要提供两个索引作为边界，第一个索引的元素是包含在分片内的，而第二个则不包含在分片内。
更大的步长
进行分片的时候，分片的开始和结束点需要进行指定(不管是直接还是间接)。而另外一个参数-步长-通常都是隐式设置的。
在普通的分片中，步长是1-分片操作就是按照这个步长逐个遍历序列的元素，然后返回开始和结束点之间的所有元素。
numbers[0:10:1]
numbers[0:10:2]
[1,3,5,7,9]
当然，步长不能为0-那不会向下执行-但步长可以是负数，即从右向左提取元素:
numbers[8:3:-1]
[9,8,7,6,5]
numbers[10:0:-2]
[10,8,6,4,2]
在这里要得到正确的分片结果需要动些脑筋。开始点的元素(最左边元素)包括在结果之中，而结束点的元素(最右边的元素)则不在分片之内。当使用一个负数作为步长时，必须让开始点(开始索引)大于结束点。在没有明确指定开始点和结束点的时候，正负数的使用可能会带来一些混淆。不过在这种情况下Python会进行正确的操作:对于一个正数步长，Python会从序列的头部开始向右提取元素，直到最后一个元素；而对于负数步长，则是从序列的尾部开始向左提取元素，直到一个元素。
"""
database = [
    ['albert','1234'],
    ['dilbert','4242'],
    ['smith','7524'],
    ['jones','9843']
]
username = raw_input('User name:')
pin = raw_input('PIN code:')
if [username,pin] in database:print 'Access granted'
"""
内建函数len,min和max非常有用。len函数返回序列中所包含元素的数量，min函数和max函数则分别返回序列中最大和最小的元素
基本的列表操作
列表可以使用所有适用于序列的标准操作，例如索引,分片，连接和乘法。有趣的是，列表是可以修改的。本节会介绍一些可以改变列表的方法:元素赋值，元素删除，分片赋值以及列表方法.
1.改变列表:元素赋值
不能为一个位置不存在的元素进行赋值，如果列表长度为2，那么不能为索引为100的元素进行赋值。如果要那样做，就必须创建一个长度为101的列表。
2.删除元素
从列表中删除元素也很容易:使用del语句来实现
names=['Alice','Beth','Cecil','Dee-Dee','Earl']
del names[2]
names
['Alice','Beth','Dee-Dee','Earl']
注意Cecil是如何彻底消失的,并且列表的长度也从5变为了4。除了删除列表中的元素，del语句还能用于删除其他元素。它可以用于字典元素甚至是其他变量的删除操作
3.分片赋值
分片是一个非常强大的特性，分片赋值操作则更加显现它的强大。
name=list('Perl')
name[1:]=list('ython')
name
['P','y','t','h','o','n']
程序可以一次为多个元素赋值了。一次一个地赋值吗？当然可以，但是在使用分片赋值时，可以使用与原序列不等长的序列将分片替换
name=list('Perl')
name[1:]=list('ython')
name
['P','y','t','h','o','n']
分片赋值语句可以在不需要替换任何原有元素的情况下插入新的元素
numbers=[1,5]
numbers[1:1]=[2,3,4]
numbers
[1,2,3,4,5]
这个程序只是"替换"了一个空的分片，因此实际的操作是插入了一个序列。以此类推，通过分片赋值来删除元素也是可行的。
numbers
[1,2,3,4,5]
numbers[1:4]=[]
numbers
[1]
方法是一个与某些对象有紧密联系的函数，对象可能是列表，数字，也可能是字符串或者其他类型的对象。一般来说，方法可以这样进行调用:
对象.方法(参数)
除了对象被放置到方法名之前，并且两者之间用一个点号隔开，方法调用与函数调用很类似。列表提供了几个方法，用于检查或者修改其中的内容。
1.append
append方法用于在列表末尾追加新的对象:
lst=[1,2,3]
lst.append(4_
lst
[1,2,3,4]
为什么我选择了如此糟糕的变量名lst,而不是使用list来表示一个列表呢？原因在于list是一个内建函数。如果使用list
"""