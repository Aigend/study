# 1.5个python标准库
# os, date,datetime,re,math,re,sys,
#
# 2.匿名函数lambda的使用
# lambda x, y: x*y；函数输入是x和y，输出是它们的积x*y
# lambda:None；函数没有输入参数，输出是None
# lambda *args: sum(args); 输入是任意个数的参数，输出是它们的和(隐性要求是输入参数必须能够进行加法运算)
# lambda **kwargs: 1；输入是任意键值对参数，输出是1
# filter函数。此时lambda函数用于指定过滤列表元素的条件。
# 例如filter(lambda x: x % 3 == 0, [1, 2, 3])指定将列表[1,2,3]中能够被3整除的元素过滤出来，其结果是[3]。
# sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。
# 例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]
# 按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]
#
# 3.random 模块
