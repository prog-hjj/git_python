#!/usr/bin/env python

class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hr, min):
        'Time60 constructor - takes hours and minutes'
        self.hr = hr
        dhr, self.min = divmod(min, 60)
        self.hr += dhr

    def __str__(self):
        'Time60 - string representation'
        return '%s:%02d' % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        'Time60 - overloading the addition operator'
        return self.__class__(self.hr + other.hr, self.min + other.min)

    def __iadd__(self, other):
        'Time60 - overloading in-place addition'
        self.min += other.min
        dhr, self.min = divmod(self.min, 60)
        self.hr += other.hr + dhr
        return self

mon = Time60(10, 30)
tue = Time60(11, 15)
print mon, tue
print mon + tue

# TypeError
# mon - tue

print id(mon)
mon += tue
print id(mon)
print mon

wed = Time60(12, 5)
print wed

thu = Time60(10, 30)
fri = Time60(8, 45)
print thu + fri

thu += fri
print thu
