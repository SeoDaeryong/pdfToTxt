# -*- coding: utf-8 -*-
import sys

old = {}
for line in open(sys.argv[1]):
    line = line.strip()
    old[line] = 1

new = {}
for line in open(sys.argv[2]):
    line = line.strip()
    new[line] = 1
    if not line in old.keys():
        print("NEW %s" % (line))

for key in old.keys():
    if not key in new.keys():
        print("GONE %s" % (key))
