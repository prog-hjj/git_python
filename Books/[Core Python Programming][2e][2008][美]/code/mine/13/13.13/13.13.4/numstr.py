#!/usr/bin/env python

class NumStr(object):

    def __init__(self, num=0, string=''):
        self.__num = num
        self.__string = string

    def __str__(self):  # define for str()
        return '[%d :: %r]' % (self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):  # define for s+o
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num,
                                  self.__string + other.__string)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __mul__(self, num):  # define for o*n
        if isinstance(num, int):
            return self.__class__(self.__num * num,
                                  self.__string * num)
        else:
            raise TypeError, 'Illegal argument type for built-in operation'

    def __nonzero__(self):  # False if both are
        return self.__num or len(self.__string)

    def __norm_cval(self, cmpres):  # normalize cmp()
        return cmp(cmpres, 0)

    def __cmp__(self, other):  # define for cmp()
        return self.__norm_cval(cmp(self.__num, other.__num)) + \
            self.__norm_cval(cmp(self.__string, other.__string))

a = NumStr(3, 'foo')
b = NumStr(3, 'goo')
c = NumStr(2, 'foo')
d = NumStr()
e = NumStr(string='boo')
f = NumStr(1)
print 'a:', a
print 'b:', b
print 'c:', c
print 'd:', d
print 'e:', e
print 'f:', f
print 'a < b:', a < b
print 'b < c:', b < c
print 'a == a:', a == a
print 'b * 2:', b * 2
print 'a * 3:', a * 3
print 'b + e:', b + e
print 'e + b:', e + b
if d: print 'd not false'  # also bool(d)
if e: print 'e not false'  # also bool(e)
print cmp(a,b)
print cmp(a,c)
print cmp(a,a)
