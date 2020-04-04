#!/usr/bin/env python

class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr__(self):
        return `self.file`

    def write(self, line):
        return self.file.write(line.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)

    def __iter__(self):
        return self.file

f = CapOpen('tmp.txt', 'w')
f.write('delegation example\n')
f.write('faye is good\n')
f.write('at delegating\n')
f.close()
print `f`

f = CapOpen('tmp.txt', 'r')
for eachLine in f:
    print eachLine,
f.close()

# clean tmp file
import os
os.remove('tmp.txt')
