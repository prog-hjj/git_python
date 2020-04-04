#!/usr/bin/env python

import os
import pickle

class FileDesc(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDesc.saved:
            raise AttributeError, "%r used before assignment" % self.name

        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.PicklingError, IOError, EOFError,
                AttributeError, ImportError, IndexError), e:
            raise AttributeError, "could not read %r: %s" % (self.name, e)

    def __set__(self, obj, val):
        f = open(self.name, 'w')
        try:
            try:
                pickle.dump(val, f)
                FileDesc.saved.append(self.name)
            except (TypeError, pickle.PicklingError), e:
                raise AttributeError, "could not pickle %r: %s" % (self.name, e)
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDesc.saved.remove(self.name)
        except (OSError, ValueError), e:
            pass

class MyFileVarClass(object):
    foo = FileDesc('foo')
    bar = FileDesc('bar')

fvc = MyFileVarClass()
# Error
# print fvc.foo

fvc.foo = 42
fvc.bar = 'leanna'
print fvc.foo, fvc.bar
del fvc.foo
# Error
# print fvc.foo, fvc.bar

# Error
# fvc.foo = __builtins__

# clean tmp file
del fvc.foo
del fvc.bar
