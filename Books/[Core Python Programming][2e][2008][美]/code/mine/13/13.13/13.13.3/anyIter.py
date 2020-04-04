#!/usr/bin/env python

class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

a = AnyIter(range(10))
i = iter(a)
for j in range(1,5):
    print j, ':', i.next(j)

# StopIteration
# i = iter(a)
# i.next(14)

a = AnyIter(range(10), True)
i = iter(a)
print i.next(14)
