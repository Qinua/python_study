'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass
# 定义一个对象
mingyue = Student()
# 再定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = 'Python'
    # 需要注意
    # 1.def doHomework的缩进层级
    # 2.系统默认出一个self参数
    def doHomework(self):
        print('I 在做作业')
        # 推荐在函数末尾使用return语句
        return None
# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()

class Student():
    name = 'dana'
    age = 18
Student.__dict__
yueyue = Student()
yueyue.__dict__
print(yueyue.name)
class A():
    name = 'dana'
    age = 18
print(A.name)
print(A.age)
print('*'*20)
# id可以鉴别一个变量是否和另一个变量是同一变量
print(id(A.name))
print(id(A.age))
a = A() # id 不变
print(id(a.name))
print(id(a.age))
a.name = 'yaona'
a.age = 16
print(id(a.name))
print(id(a.age))

class Student():
    name = 'dana'
    age = 18
    def say(self):
        self.name = 'aaaa'
        self.age = 200
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(self.age))

    def sayAgain(s):
        print('My name is {0}'.format(s.name))
        print('My age is {0}'.format(s.age))
yueyue = Student()
yueyue.say()
yueyue.sayAgain()

class Teacher():
    name = 'dana'
    age =19
    def say(self):
        self.name = 'yaona'
        self.age = 17
        print('My name is {0}'.format(self.name))
        print('My age is {0}'.format(self.age))
    def sayAgain(s):   #括号内若为空，则为绑定类函数，调用需要使用类名 Teacher.sayAgain()
        print('Hello,nice to see you again')
t =Teacher()
t.say()
t.sayAgain()
#私有变量实例：
class Persion():
    # name 是公有的成员
    name = 'liuying'
    # __age是私有成员
    __age = 18
p = Persion()
print(p.name)  # print(p.__age)会报错
print(Persion.__dict__) # 查看用法
p._Persion__age = 19 # name mangling技术
print(p._Persion__age)

# 继承的语法
# 在python中 ，任何类都有一个共同的父类叫object
class Persion():
    name = 'NoName'
    age = 18
    __score = 0 # 考试成绩是秘密，只要自己知道
    _petname = 'sec' # 小名，是保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping ... ...')
    def work(self):
        print('make some money')
# 父类写在括号内
class Teacher(Persion):
    teacher_id = '9527'
    age = 38
    def make_test(self): # 老师会考试
        print('attention')
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        Persion.work(self) # 扩充父类的方法，另一种方法：super().work() super代表得到父类
        self.make_test()
t = Teacher()
print(t.name)
print(Teacher.name)
print(t._petname)
t.sleep()
print(t.teacher_id)
t.make_test()
print(t.age)
t.work()

# 构造函数的概念
class Dog():
    # __init__就是构造函数
    # 每次实例化的时候，第一个被自动的调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I am init in dog')
class Animal():
    def __init__(self):
        print('Animal')
class PaxingAni(Animal):
    def __init__(self,name):
        print('Paxing Dongwu {0}'.format(name))
d = Dog()
class Cat(PaxingAni):
    pass
c = Cat(PaxingAni)

class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print('i am swimming....')
class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print('i am flying....')
class Persion():
    def __init__(self,name):
        self.name = name
    def work(self):
        print('Working....')
# 单继承
class Student(Persion):
    def __init__(self,name):
        self.name = name
stu = Student('yueyue')
stu.work()
# 多继承
class SuperMan(Persion,Bird,Fish):
    def __init__(self,name):
        self.name = name
s = SuperMan('yueyue')
s.fly()
s.swim()
s.work()

# Mixin案例
class Persion():
    name = 'liuying'
    age = 18
    def eat(self):
        print('EAT......')
    def drink(self):
        print('DRINK......')
    def sleep(self):
        print('SLEEP......')
class Teacher(Persion):
    def work(self):
        print('Work')
class Student(Persion):
    def study(self):
        print('Study')
class Tutor(Teacher,Student):
    pass
t = Tutor()
print(Tutor.__mro__)  # mro 多继承中用于保存继承顺序的一个列表
print(t.__dict__)
print(Tutor.__dict__)

# 类的相关函数
class A():
    pass
class B(A):
    pass
class C():
    pass
print(issubclass(B,A))  # issubclass 检测一个类是否是另一个类的子类
print(issubclass(C,A))
print(issubclass(B,object))
a = A()
print(isinstance(a,A))  # isinstance 检测一个对象是否是一个类的实例
class A():
    name = 'NoName'
a = A()
print(hasattr(a,'name')) # hasattr 检测一个对象是否有成员XXX
print(hasattr(a,'age'))
# 查看setattr的具体用法
help(setattr)

# property 案例：property(fget,fset,fdel,doc)
# 定义一个Persion类，具有name,age属性
# 对于任意输入的姓名，我们希望用大写方式保存
# 年龄，我们希望内部统一用整数保存
class Persion():
    '''
    这是一个人，一个高尚的人，一个脱离低级趣味的人
    他还有属性
    '''
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = 'NoName'
    name = property(fget,fset,fdel,'对name进行下操作啦')
p1 = Persion()
p1.name = 'Tuling'
print(p1.name)

# 类的内置属性
print(Persion.__dict__)
print(Persion.__doc__)
print(Persion.__name__)
print(Persion.__bases__)

# 类的常用魔法方法
class A():
    def __init__(self,name = 0): # __init__:构造函数
        print('哈哈哈哈我被调用了')
    def __call__(self): # __call__:
        print('我又被调用了')
    def __str__(self): # __str__:
        return '图灵学院的例子'
a = A()
a()
print(a)

# __getattr__案例
class A():
    name = 'NoName'
    age = 18
    def __getattr__(self, name):
        print('没找到呀没找到')
        print(name)
a = A()
print(a.name)
print(a.addr)

# __setattr__案例
class Persion():
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print('设置属性：{0}'.format(name))
        # 下面语句会导致问题，死循环
        # self.name = value
        # 此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name,value)
p = Persion()
print(p.__dict__)
p.age = 18

# __gt__ 案例
class Student():
    def __init__(self,name):
        self._name = name
    def __gt__(self, obj):
        print('哈哈，{0} 会比 {1} 大吗？'.format(self,obj))
        return self._name > obj._name
stu1 = Student('one')
stu2 = Student('two')
print(stu1 > stu2)

# 三种方法的案例
class Persion:
    # 实例方法
    def eat(self):
        print(self)
        print('Eating....')
    # 类方法：类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print('Playing....')
    # 静态方法：不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print('Saying....')
yueyue = Persion()
# 实例方法
yueyue.eat()
# 类方法
Persion.play()
yueyue.play()
# 静态方法
Persion.say()
yueyue.say()

# 类属性 property
# 对变量除了普通的赋值、读取、删除三种操作，还想增加一些附加的操作，那么可以通过property完成
class A():
    def __init__(self):
        self.name = 'haha'
        self.age = 18
    # 此功能对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print('我被读取了')
        return self.name
    # fset模拟的是对变量进行写操作
    def fset(self):
        print('我被写入了，但是还可以做好多事情')
        self.name = 'tulingxueyuan' + name
    # fdel模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass
    # property的四个参数顺序是固定的
    #第一个参数代表读取的时候需要调用的函数
    #第二个参数代表写入的时候需要调用的函数
    #第三个参数是删除
    name2 = property(fget,fset,fdel,'这是一个property的例子')
a = A()
print(a.name)
print(a.name2)

# 抽象类的实现
import abc
# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass
    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink(cls):
        pass
    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass
    # 定义非抽象的具体方法
    def sleep(self):
        print('Sleeping...')

# 自定义一个类
    # 借助于MethodType
from types import MethodType
class A():
    pass
def say(self):
    print('Saying......')
a = A()
a.say =MethodType(say,A)
a.say()

    # 借助于type
    #先定义类应该具有的成员函数
def say(self):
    print('Saying......')
def talk(self):
    print('Talking......')
    # 用type来创建一个类
A = type('AName',(object, ),{'class_say':say,'class_talk':talk})
    # 然后就可以像正常访问一样使用类
a = A()
a.class_say()
a.class_talk()

    # 元类案例
    # 元类写法是固定的，必须继承自type
    # 元类一般命名以MetaClass结尾
class TulingMetaClass(type):
    # 注意以下写法
    def __new__(cls,name,bases,attrs):
        # 自己的业务处理
        print('哈哈，我是元类呀')
        attrs['id'] = '000000'
        attrs['addr'] = '北京海淀区公主坟西翠路12号'
        return type.__new__(cls,name,bases,attrs)
    # 元类定义完就可以使用，使用注意写法
class Teacher(object,metaclass=TulingMetaClass):
    pass
t = Teacher()


