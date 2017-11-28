#!/usr/bin/python3.6
s = 'xyz\t12345\tabc  aba'
print(s)
result = s.expandtabs() #default tab size 8
print(result)

result1 = s.expandtabs(4) # definfing tab size to 4
print(result1)