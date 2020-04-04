#!/usr/bin/env python

class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), "Value must be a float!"
        self.value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__

# AssertionError
# rfm = RoundFloatManual(42)

rfm = RoundFloatManual(5.5964)
print `rfm`
print rfm
