#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
list_1 = [9, 8, 1, 6, 3, 2, 10, 12, 11, 201, 209, 99, 203,4,-5]
max_num = list_1[0]
min_num = list_1[0]
print("The list is:", list_1)
for i in xrange(len(list_1)):
    if list_1[i] > max_num:
        max_num = list_1[i]
    elif list_1[i] < min_num:
        min_num = list_1[i]
print("max_num is :", max_num)
print("min_num is :", min_num)