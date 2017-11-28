#!/usr/local/bin/python3.6
from __future__ import print_function
s={'1':['a','b','e'], '2':['c','d','f']}
# print(s.values())
# l=list(s.values())
l=s.values()
# for i in range(len(l)): # works for static string
#     print(l[i][0]+l[i][1])

for i in xrange(len(l)):
    for j in xrange(len(l[i])):
        print(l[i][j],end="")
    print()
