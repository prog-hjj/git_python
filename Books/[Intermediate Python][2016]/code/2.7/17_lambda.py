add = lambda x, y: x + y
print add(4,6)


# 列表排序
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print a

# 列表并⾏排序
import random
list1 = [random.randint(1,10) for x in range(5)]
list2 = [random.randint(1,20) for x in range(5)]
print list1
print list2
data = list(zip(list1, list2))
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
print 'After parallel sort:'
print list1
print list2
