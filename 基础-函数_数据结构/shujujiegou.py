'''内置数据结构：
            list（列表）：[] 一组有顺序的数据的组合 [] = list()
            tuple（元组）：() 可看成是一个不可更改的list
            set（集合）：{} 一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素
            dict（字典）：无序
            '''
l2 = [1,2,3,4,5,23,1,34,12,4]
l3=l2[:]  # l3通过分片重新生成一个列表
l4=l3      # l4还是和l3同一个列表
print(id(l2))
print(id(l3))
print(id(l4))

l2[1]=100
print(l2)
print(l3)

l3[1]=100
print(l3)
print(l4)

a = [['one',1],['two',2],['three',3]]
for k,v in a:
    print(k,'---',v)

b = [i for i in range(1,10)]
print(b)
c = [i*10 for i in b if i% 2 == 0]
print(c)

b.append(100)  #append 插入一个内容，在末尾追加
print(b)
b.insert(3,666)  # insert(index,data),插入位置是index前面
print(b)
last_ele = b.pop() # del 删除    pop 从对位拿出一个元素，即把最后一个元素取出来
print(last_ele)
print(b)
b.remove(666)  #  remove 在列表中删除指定的值的元素
print(b)
b.clear()
print(b)

a = [1,2,3,4,5]
print(a)
print(id(a))
a.reverse()  # reverse 原地翻转 id不变
print(a)
print(id(a))

a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)  # extend 扩展列表，id不变
print(a)
a_len = a.count(10) # count 查找列表中指定值或元素的个数
print(a_len)
b = a    # id相同
b[3]=100
print(a)
print(b)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a.copy() # copy 拷贝（浅拷贝） 列表赋值 id不同
print(b)
b[3]=100
print(a)
print(b)

'''tuple 元组():
            是序列表，有序
            元组的数据值可以访问，不能修改，不能修改，不能修改
            元组数据可以是任意类型
            总之，list所有特性，除了可修改外，元组都具有
            也就意味着，list具有的一些操作，比如索引、分片、序列相加、相乘，成员操作等等，一模一样
            '''
# 索引操作
t = (1,2,3,4,5) # t[1] =100 会报错
print(t[4])
#成员检测
if 2 in t:
    print('YES')
else:
    print('NO')
# 元组遍历，一般采用for
# 1.单层元组遍历
t = (1,2,3,'wangxiaojing','i','love')
for i in t:
    print(i,end=' ')
print(t)
# 2.双层元组的遍历
t = ((1,2,3),(2,3,4),('i','love','wangxiaojing'))
for i in t:
    print(i)
for k,m,n in t:
    print(k,'--',m,'--',n)

# 关于元组的函数
# len 获取元祖的长度 Max min 最大最小值
# 转化或创建元组
l = [1,2,3,4,5]
t = tuple(l)
print(t)
# count :计算指定数据出现的次数
t = (2,3,45,2,1,2,5,2,8,2)
print(t.count(2))
# index:求指定元素在元组中的索引位置，如果元素有多个则返回第一个
print(t.index(45))
# 元组变量交换法
a = 1
b = 3
a,b = b,a
print(a)
print(b)

'''set（集合）：{} 无序，
            一堆确定的无序的唯一的数据，集合中每一个数据成为一个元素
            大括号内一定要有值，否则定义出的是一个dick类型'''
# set ：生成一个集合
l = {1,2,3,4,5,3,2,23,4,6}
s = set(l)
print(s)
# len,max,min:跟其他基本函数一样
# add ：向集合内添加元素
s.add(222)
print(s)
# clear :清空，id不变
# copy : 拷贝
# remove : 移除指定的值，直接改变原有值，如果删除的值不存在，报错
# discard : 移除集合中指定的值，和remove一样，但删除值不存在不报错
# pop ：随机移除一个元素
# 集合函数：intersection(交集），difference（差集），union（并集）
         # issubset（检查一个集合是否为另一个子集）
         # issuperset（检查一个集合是否为另一个超集）
# frozenset : 冰冻集合，不可以进行任何修改的集合

'''dict（字典）：是序列类型，但是无序，所以没有分片和索引
                字典中的数据每个都有键值对组成，即kv对
                        key：必须是可哈希的值，比如int,string,float,tuple,但是list,set,dict不行
                        value：任何值
'''
d = {'one':1,'two':2,'three':3}
print(d['one'])
d['one'] = '一'
print(d)
del d['one']
print(d)
# 遍历字典
d = {'one':1,'two':2,'three':3}
for k in d:
    print(k,d[k])
for k in d.keys():
    print(k,d[k])
for v in d.values():
    print(v)
for k,v in d.items():
    print(k,'--',v)
# 字典生成式：
dd = {k:v for k,v in d.items()}
print(dd)
dd = {k:v for k,v in d.items() if v%2 ==0}
print(dd)
# 字典相关函数：len,max,min,dict,clear,items,values,get
v = d.values()
print(type(v))
print(v)
print(d.get('one333')) # get：根据指定键返回相应的值，如果没有则返回none，不用get会报错
print(d.get('one',100)) #get：根据指定键返回相应的值，好处是可以设置默认值
print(d.get('one333',100))
# fromkeys：使用指定的序列作为键，使用一个值作为字典的所有的键的值
l = ['one','two','three']
d = dict.fromkeys(l,'hahhhaahhaah')
print(d)
