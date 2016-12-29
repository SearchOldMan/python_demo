#!/usr/bin/env python
import sys

count = 1
while True:
    line = sys.stdin.readline()
    if not line:
        break
    print '%s:%s' % (count,line)
    count += 1