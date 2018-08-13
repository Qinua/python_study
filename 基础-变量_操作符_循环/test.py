
import datetime
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

gender = input("请输入性别：")
print("你输入的性别是：{0}".format(gender))
if gender == "nan":
    print("来，我们纪念一下今天，代码敲十遍")
else:
    print("发糖喽发糖喽")
    print("你是女生，特殊照顾喽")
print("开始上课喽")
