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
为什么我选择了如此糟糕的变量名lst,而不是使用list来表示一个列表呢？原因在于list是一个内建函数。如果使用list作为变量名，我就无法调用list函数了。根据给定的应用程序可以定义更好的变量名，像lst这样的变量名是毫无意义的。
注意，下面的内容很重要:append方法和其他一些方法类似,只是在恰当位置修改原来的列表。这意味着，它不是简单地返回一个修改过的新列表-而是直接修改原来的列表。
2.count
count方法统计某个元素在列表中出现的次数:
['to','be','or','not','to','be'].count('to')
2
x=[[1,2],1,1,[2,1,[1,2]]]
x.count(1)
2
3.extend
extend方法可以在列表的末尾一次性追加另一个序列中的多个值。换句话说，可以用新列表扩展原有的列表:
a=[1,2,3]
b=[4,5,6]
a.extend(b)
a
[1,2,3,4,5,6]
这个操作看起来很像连接操作，两者最主要区别在于:extend方法修改了被扩展的序列(在这个例子中，就是a)。而原始的连接操作符则不然，它会返回一个全新的列表:
4.index
index方法用于从列表中找出某个值第一个匹配项的索引位置:
knights=['We','are','the','knights','who','say','ni']
knights.index('who')
5.insert
insert方法用于将对象插入到列表中:
numbers=[1,2,3,5,6,7]
numbers.insert(3,'four')
numbers
[1,2,3,'four','5','6','7']
6.pop
pop方法会移除列表中的一个元素(默认是最后一个),并且返回该元素的值:
x=[1,2,3]
x.pop()
注意:pop方法是唯一一个既能修改列表又返回元素值的列表方法
使用pop方法可以实现一种常见的数据结构-栈。栈的原理就像堆放盘子那样。只能在顶部放一个盘子，同样，也只能从顶部拿走一个盘子。最后被放入堆栈的最先被移除(这个原则称为LIFO,即后进先出)。
对于上述两个栈操作(放入和移出),它们有大家都认可的称谓-入栈(push)和出栈(pop).Python没有入栈方法，但可以使用append方法来代替。pop方法和append方法的操作结果恰好相反，如果入栈(或者追加)刚刚出栈的值，最后得到的结果还是原来的栈。

如果需要实现一个先进先出(FIFO)的队列，那么可以使用insert(0,...)来代替append方法。或者，也可以继续使用append方法，但必须用pop(0)来代替pop()。更好的解决方案是使用collection模块中的deque对象).
7.remove
remove方法用于移除列表中某个值的第一个匹配项:
5.insert
insert方法用于将对象插入到列表中:
numbers=[1,2,3,5,6,7]
numbers.insert(3,'four')
numbers
[1,2,3,'four','5','6','7']
6.pop
pop方法会移除列表中的一个元素(默认是最后一个),并且返回该元素的值:
x=[1,2,3]
x.pop()
注意:pop方法是唯一一个既能修改列表又返回元素值的列表方法
使用pop方法可以实现一种常见的数据结构-栈。栈的原理就像堆放盘子那样。只能在顶部放一个盘子，同样，也只能从顶部拿走一个盘子。最后被放入堆栈的最先被移除(这个原则称为LIFO,即后进先出)。
对于上述两个栈操作(放入和移出),它们有大家都认可的称谓-入栈(push)和出栈(pop).Python没有入栈方法，但可以使用append方法来代替。pop方法和append方法的操作结果恰好相反，如果入栈(或者追加)刚刚出栈的值，最后得到的结果还是原来的栈。

如果需要实现一个先进先出(FIFO)的队列，那么可以使用insert(0,...)来代替append方法。或者，也可以继续使用append方法，但必须用pop(0)来代替pop()。更好的解决方案是使用collection模块中的deque对象).
7.remove
remove方法用于移除列表中某个值的第一个匹配项:
5.insert
insert方法用于将对象插入到列表中:
numbers=[1,2,3,5,6,7]
numbers.insert(3,'four')
numbers
[1,2,3,'four','5','6','7']
6.pop
pop方法会移除列表中的一个元素(默认是最后一个),并且返回该元素的值:
x=[1,2,3]
x.pop()
注意:pop方法是唯一一个既能修改列表又返回元素值的列表方法
使用pop方法可以实现一种常见的数据结构-栈。栈的原理就像堆放盘子那样。只能在顶部放一个盘子，同样，也只能从顶部拿走一个盘子。最后被放入堆栈的最先被移除(这个原则称为LIFO,即后进先出)。
对于上述两个栈操作(放入和移出),它们有大家都认可的称谓-入栈(push)和出栈(pop).Python没有入栈方法，但可以使用append方法来代替。pop方法和append方法的操作结果恰好相反，如果入栈(或者追加)刚刚出栈的值，最后得到的结果还是原来的栈。

如果需要实现一个先进先出(FIFO)的队列，那么可以使用insert(0,...)来代替append方法。或者，也可以继续使用append方法，但必须用pop(0)来代替pop()。更好的解决方案是使用collection模块中的deque对象).
7.remove
remove方法用于移除列表中某个值的第一个匹配项:
5.insert
insert方法用于将对象插入到列表中:
numbers=[1,2,3,5,6,7]
numbers.insert(3,'four')
numbers
[1,2,3,'four','5','6','7']
6.pop
pop方法会移除列表中的一个元素(默认是最后一个),并且返回该元素的值:
x=[1,2,3]
x.pop()
注意:pop方法是唯一一个既能修改列表又返回元素值的列表方法
使用pop方法可以实现一种常见的数据结构-栈。栈的原理就像堆放盘子那样。只能在顶部放一个盘子，同样，也只能从顶部拿走一个盘子。最后被放入堆栈的最先被移除(这个原则称为LIFO,即后进先出)。
对于上述两个栈操作(放入和移出),它们有大家都认可的称谓-入栈(push)和出栈(pop).Python没有入栈方法，但可以使用append方法来代替。pop方法和append方法的操作结果恰好相反，如果入栈(或者追加)刚刚出栈的值，最后得到的结果还是原来的栈。

如果需要实现一个先进先出(FIFO)的队列，那么可以使用insert(0,...)来代替append方法。或者，也可以继续使用append方法，但必须用pop(0)来代替pop()。更好的解决方案是使用collection模块中的deque对象).
7.remove
remove方法用于移除列表中某个值的第一个匹配项:
5.insert
insert方法用于将对象插入到列表中:
numbers=[1,2,3,5,6,7]
numbers.insert(3,'four')
numbers
[1,2,3,'four','5','6','7']
6.pop
pop方法会移除列表中的一个元素(默认是最后一个),并且返回该元素的值:
x=[1,2,3]
x.pop()
注意:pop方法是唯一一个既能修改列表又返回元素值的列表方法
使用pop方法可以实现一种常见的数据结构-栈。栈的原理就像堆放盘子那样。只能在顶部放一个盘子，同样，也只能从顶部拿走一个盘子。最后被放入堆栈的最先被移除(这个原则称为LIFO,即后进先出)。
对于上述两个栈操作(放入和移出),它们有大家都认可的称谓-入栈(push)和出栈(pop).Python没有入栈方法，但可以使用append方法来代替。pop方法和append方法的操作结果恰好相反，如果入栈(或者追加)刚刚出栈的值，最后得到的结果还是原来的栈。

如果需要实现一个先进先出(FIFO)的队列，那么可以使用insert(0,...)来代替append方法。或者，也可以继续使用append方法，但必须用pop(0)来代替pop()。更好的解决方案是使用collection模块中的deque对象).
7.remove
remove方法用于移除列表中某个值的第一个匹配项:
x=['to','be','or','not','to','be']
x.remove('be')
x
['to','or','not','to','be']
x.remove('bee')
报错
可以看到:只有第一次出现的值被移除了，而不存在于列表中的值(比如例子中的"bee")是不会移除的。
值得注意的是,remove是一个没有返回值的原位置改变方法。它修改了列表却没有返回值，这与pop方法相反。
8.reverse
reverse方法将列表中的元素反向存放：
x=[1,2,3]
x.reverse()
x
[3,2,1]
请注意:该方法也改变了列表但不返回值(就像remove和sort)
提示:如果需要对一个序列进行反向迭代，那么可以使用reversed函数。这个函数并不返回一个列表，而是返回一个迭代器对象。
9.sort
sort方法用于在原位置对列表进行排序。在"原位置排序"意味着改变原来的列表，从而让其中的元素能按一定的顺序排序，而不是简单地返回一个已排序的列表副本。
x=[4,6,2,1,7,9]
x.sort()
x
[1,2,4,6,7,9]
前面介绍过了几个改变列表却不返回值的方法，在大多数情况下这样的行为方式是很合常理的。但是，sort方法的这种行为方式需要重点讲解一下，因为很多人都被sort方式弄糊涂了。当用户需要一个排好序的列表副本，同时又保留原有列表不变的时候，问题就出现了。为了实现这个功能，我们自然而然就想到了如下的做法:
x=[4,6,2,1,7,9]
y=x.sort()#Don't do this!
print y
None
因为sort方法修改了x却返回了空值，那么最后得到的是已排序的x以及值为None的y。实现这个功能的正确方法是，首先把x的副本赋值给y,然后对y进行排序，如下例所示:
x=[4,6,2,1,,7,9]
y=x[:]
y.sort()
x
[4,6,2,1,7,9]
y
[1,2,4,6,7,9]
再次调用x[:]得到的是包含了x所有元素的分片，这是一钟很有效率的复制整个列表的方法。只是简单地把x赋值给y是没用的，因为这样做就让x和y都指向同一个列表了。
y=x
y.sort()
x
[1,2,4,6,7,9]
y
[1,2,4,6,7,9]
这个函数实际上可以用于任何序列，却总是返回一个列表:
sorted('Python')
['P','h','n','o','t','y']
如果想把一些元素按相反的排序排列，可以先使用sort(或者sorted),然后再调用reverse方法，或者也可以使用reverse参数。
10.高级排序
如果希望元素能按照特定的方式进行排序(而不是sort函数默认的方式，即根据Python的默认排序规则按升序排列元素),那么可以通过compare(x,y)的形式自定义比较函数。compare(x,y)函数会在x<y是返回负数，在x>y时返回正数，如果x=y则返回0(根据你的定义)定义好该函数之后，就可以提供给sort方法作为参数了。内建函数cmp提供了比较函数的默认实现方式：
sort方法有另外两个可选的参数-key和reverse。如果要使用它们，那么就要通过名字来指定。参数key和参数cmp类似-必须提供一个在排序过程中使用的函数。然而，该函数并不是直接用来确定对象的大小，而是为每个元素创建一个键，然后所有元素根据键来排序。因此，如果要根据元素的长度进行排序，那么可以使用len作为键函数:
x=
2.4元组：不可变序列
元组与列表一样，也是一种序列。唯一的不同是元组不能修改。(你可能注意到了，字符串也是如此。)创建元组的语法很简单:如果你用逗号分隔了一些值，那么你就自动创建了元组。
1,2,3
(1,2,3)
元组也是(大部分时候是)通过圆括号括起来的:
(1,2,3)
(1,2,3)
空元组可以用没有包含内容的两个圆括号表示:
()
那么如何实现包括一个指的元组呢。实现方法有些奇特-必须加个逗号，即使只有一个值:
(42,)
最后两个例子生成了一个长度为1的元组，而第一个例子根本不是元组。逗号是很重要的，只添加圆括号也是没用的：（42)和42是完全一样的。但是，一个逗号却能彻底地改变表达式的值:
3*(40+2)
126
3*(40+2,)
(42,42,42)

2.4.1tuple函数
tuple函数的功能与list函数基本上是一致的:以一个序列作为参数并把它转换为元组。如果参数是元组，那么该参数就会被原样返回：
tuple([1,2,3])
(1,2,3)
tuple('abc')
('a','b','c')
tuple((1,2,3))
(1,2,3)
2.4.2基本元组操作
元组其实并不复杂--除了创建元组和访问元组元素之外，也没有太多其他操作，可以参照其他类型的序列来实现:
x=1,2,3
x[1]
2
x[0:2]
(1,2)
元组的分片还是元组，就像列表的分片还是列表一样。
2.4.3那么，意义何在
现在你可能会想到底有谁会需要像元组那样的不可变序列呢？难道就不能在不改变其中内容的时候坚持只用列表吗？一般来说这是可行的。但是由于以下两个重要的原因，元组是不可替代的:
  元组可以在映射中当作键使用-而列表则不行
  元组作为很多内建函数和方法的返回值存在，也就是说你必须对元组进行处理。只要不尝试修改元组，那么，'处理'元组在绝大多数情况下就是把它们当作列表来进行操作(除非需要使用一些元组没有的办法，如index和count)
一般来说，列表可能更满足对序列的所有需求。
"""
