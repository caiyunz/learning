class语句会在函数定义的地方创建自己的命名空间。一切看起来都挺好，但是那个self参数看起来有点奇怪。它是对于对象自身的引用。
>>> class Person:
...     def setName(self,name):
...         self.name=name
...     def getName(self):
...         return self.name
...     def greet(self):
...         print "Hello,world! I'm %s."%self.name
... 
>>> foo.setName('Luke Skywalker')
>>> bar.setName('Anak in Skywalker')
>>> foo.greet()
Hello,world! I'm Luke Skywalker.
>>> bar.greet()
Hello,world! I'm Anak in Skywalke.
在调用foo的setName和greet函数时，foo自动将自己作为第一个参数传入函数中--因此形象地命名为self.对于这个变量，每个人可能都会有自己的叫法，但是因为它总是对象自身，所以习惯上总是叫做self.

>>> foo=Person()
>>> foo.name="Yokr"
>>> foo.getName
<bound method Person.getName of <__main__.Person instance at 0x7fe2a62b60e0>>
>>> foo.setName("York")
>>> foo.getName
<bound method Person.getName of <__main__.Person instance at 0x7fe2a62b60e0>>
>>> foo.getName()
'York'
>>> foo.name="New"
>>> foo.getName
<bound method Person.getName of <__main__.Person instance at 0x7fe2a62b60e0>>
>>> foo.getName()
'New'
>>> foo.setName()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: setName() takes exactly 2 arguments (1 given)

继承：
class 子类名(父类名):
这就是继承的格式。

为了让方法或者特性变为私有(从外部无法访问),只要在它的名字前面加上双下划线即可：
class Secretive:
    def __inaccessible(self):
        print "Bet you can't see me..."
    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()
现在__inaccessible从外界是无法访问的，而在类内部还能使用访问：
尽管双下划线有些奇怪，但是看起来像是其他语言中的标准的私有方法。真正发生的事情才是不标准的。类的内部定义中，所有以双下划线开始的名字都被"翻译"成前面加上单下划线和类名的形式。
在了解了这些幕后的事情后，实际上还是能在类外访问这些私有方法，尽管不该这么做：
s._Secretive__inaccessible()

调查继承
如果想要查看一个类是否是另一个的子类，可以使用内建的issubclass函数：
issubclass(SPAMFilter,Filter)
True
issubclass(Filter,SPAMFilter)
False
如果想要知道已知类的基类,可以直接使用它的特殊特性__bases__:
SPAMFilter.__bases__

同样，还能用使用isinstance方法检查一个对象是否是一个类的实例：
s=SPAMFilter()
isinstance(s,SPAMFilter)
True
isinstance(s,Filter)
True
isinstance(s,str)
Flase
如果只想知道一个对象属于那个类，可以使用__class__特性：
s.__class__

class 子类名(父类名1,父类名2,...):
这种行为称为多重继承，是个非常有用的工具。但除非读者特别熟悉多重继承，否则应该尽量避免使用。
当使用多重继承时，有个需要注意的地方。如果一个方法从多个超类继承(也就是说你有两个具有相同名字的不同方法),那么必须要注意一下超类的顺序(在class语句中):先继承的类中的方法会重写后继承的类中的方法。所以就是说父类1中有talk方法，父类2中也有talk方法，那么子类在使用父类中的talk方法的时候，父类1中的talk方法会重写父类2中的talk方法。


