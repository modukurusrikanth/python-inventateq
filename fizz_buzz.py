#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# list_all = []
# list_3 = []
# list_5 = []
# list_3_and_5 = []
# list_normal = []
# for i in xrange(1,100):
#     if i%3 == 0:
#         if i%5==0:
#             print("fizzbuzz")
#             # list_3_and_5.append(i)
#         else:
#             print("fizz")
#             # list_3.append(i)
#     elif i%5 == 0:
#         print("buzz")
#         # list_5.append(i)
#     else:
#         print(i)
        # list_normal.append(i)
# print("All the elements list those are only divisble by 3: {}".format(list_3))
# print("All the elements list those are only divisble by 5: {}".format(list_5))
# print("All the elements list those are divisble by 3 and 5 are: {}".format(list_3_and_5))
# print("All the elements list those are not divisble by 3 and 5 are: {}".format(list_normal))
for i in xrange(1,100):
    if i%3 == 0 and i%5 ==0:
            print("fizzbuzz")
    elif i% 3 == 0:
            print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)