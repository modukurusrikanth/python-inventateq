#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
s="srikanths"
# for c in s:
#     # j=s.count(c)
#     # print(j,c)
#     # print("the character '{}' peresent in string '{}': {} times".format(c,s,j))
#     print("{}' : {} ".format(c,j))
# d={}
# for x in s:
#     d[x] = s.count(x)
# print(d)

a = "google.com"
y = {i: a.count(i) for i in a}
print(y)
