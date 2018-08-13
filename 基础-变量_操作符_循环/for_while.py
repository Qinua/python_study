

for name in ['zhangsan','lisi','wanglaowu','jingjing']:
    print(name)
    if name == 'jingjing':
        print('我的最爱{0}出现了'.format(name))
    else:
        print('同学我们不约，不约，同学请自重')
else:
    print('别的都不是我同学，不会再爱了')

for i in range (1,11):
    if i%2==1:
        continue
    print('{0}是偶数'.format(i))
    break
for i in range(1,100):
    pass

benqian = 1000000
year =0
while benqian <2000000:
    benqian = benqian*(1+0.067)
    year += 1
    print('第{0}年拿了{1}块钱'.format(year,benqian))
else:
    print('大爷的，终于翻倍了')
    print('当年可以买房，现在只能买个卫生间')
