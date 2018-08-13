def func():
    print('我是一个函数')
    print('我要完成一定功能')
print('我结束了')

func()

def hello(persion):
    print('{0}，你怎么了'.format(persion))
    print('Sir，你不理我就走啊')
    return '我已经和{0}打完招呼了，{1}不理我'.format(persion,persion)
p='明月'
rst = hello(p)
print(rst)

for row in range(1,10):
    for col in range(1,row+1):
        print(row,'*',col,'=',row * col,end='  ')
    print('')
def reg(name,age,gender='male'):
    if gender == 'male':
        print('{0} is {1},and he is a good student'.format(name,age))
    else:
        print('{0} is {1},and she is a good student'.format(name,age))
reg('liming',23)
reg('xiaojing',24,'female')

def stu_key(name='no name',age=0,addr='no addr'):  #关键字参数
    print('I am a student')
    print('我叫{0},我今年{1}岁了，我住{2}'.format(name,age,addr))
n ='jingjing'
a =18
addr = '我家'

stu_key(age=a,name=n,addr=addr)

# def func(*args):  #收集参数
def stu(*args):
    print('Hello 大家好，自我介绍一下：')
    print(type(args))  #type函数作用是检测变量的类型
    for item in args:
        print(item)
stu('liujing',18,'北京通州区','wangxiaojing','single')
stu('周大神')
stu()  #收集参数可以不带任何实参调用，此事收集参数为空tuple

''' 收集参数之关键字收集参数
   def func( **kwargs):
       func_body
    func(p1=v1,p2=v2,p3=v3,,,,,)
'''
def stu1(**kwargs):
    print('Hello 大家好，自我介绍一下：')
    print(type(kwargs))  #type函数作用是检测变量的类型
    # 对于字典的访问，python2和python3有区别
    for k,v in kwargs.items():
        print(k,'---',v)
stu1(name='liujing',age=18,addr='北京通州区',lover='wangxiaojing',woker='Teacher')
print('*'*50)
stu1(name='周大神')

def stu2(name,age,*args,hobby='没有',**kwargs):
    print('Hello 大家好，自我介绍一下：')
    print('我叫{0}，我今年{1}了，'.format(name,age))
    if hobby =='没有':
        print('我没有爱好，so sorry')
    else:
        print('我的爱好是{0}'.format(hobby))
    print('*' * 20)
    for i in args:
        print(i)
    print('#'* 30)
    for k,v in kwargs.items():
        print(k,'---',v)
name = 'liuying'
age =19
stu2(name,age)
stu2(name,age,hobby='游泳')
stu2(name,age,'王晓静','刘石头',hobby='游泳',hobby2='跑步')

def stu3(*args):   #收集参数的解包问题
    print('哈哈哈哈哈')
    n = 0 # n 用来表示循环次数
    for i in args:
        print(type(i))
        print(n)
        n += 1
        print(i)
l = ['liujing',18,'北京通州区','wangxiaojing']
stu3(*l)

'''返回值：
    函数和过程的区别（有无返回值）
    函数需要用return显示返回内容，如果没有返回，则默认返回None
    推荐写法，无论有无返回值，最后都要以return结束
'''
def func_1():
    print('有返回值')
    return 1
def func_2():
    print('没有返回值')
f1 = func_1()
print(f1)
f2 = func_2()
print(f2)

'''函数文档
    函数的文档的作用是对当前函数提供使用相关的参考信息
    文档的写法：在函数内部开始的第一行使用三引号字符串定衣符
                一般具有特定格式
    文档查看：使用help 函数，比如help(func)
                使用__doc__'''
def stu4(name,age,addr):
    '''
    这是文档的文字内容
    :param name: 表示学生的姓名
    :param age: 表示学生的年龄
    :param addr: 表示学生的地址
    :return: 此函数没有返回值
    '''
    pass
print(help(stu4))
print('*' * 20)
print(stu4.__doc__)

'''函数作用域：
            globals函数：全局变量
            locals函数：局部变量
    eval()函数：把一个字符串当成一个表达式来执行，返回表达式执行后的结果
    exec()函数：跟eval()功能类似，但是不返回结果
'''
x=100
y=200
z1 = x +y
z2 = eval('x+y')
z3 = exec('x+y')
z4 = exec("print('x+y:',x+y)")
print(z1)
print(z2)
print(z3)

'''递归函数：
            函数直接或者间接调用自身
            优点：简洁，理解容易
            缺点：对递归深度有限制，消耗资源大
            python对递归深度有限制，超过限制报错'''
x = 0
def fun():
    global x
    x += 1
    print(x) #函数自己调用自己
    return # 思考为何在后面加return才能正确执行，而不是报错
    fun()
fun() #调用函数

# 斐波那契数列：1,1,2,3,5,8,13,21，。。。。。
# f(1)=1,f(2)=1,f(n)=f(n-1)+f(n-2) n>=3

def fib(n):
    if n ==1:
        return 1
    if n ==2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(3))
print(fib(10))