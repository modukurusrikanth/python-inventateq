#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
d = {'KA':'BLR','MH':'mum','AP':'AMR','noodles':['yippeee','maggi']}
for k,v in d.items():
    print(" the capital of {} is: {}".format(k,v))
for k in d.values():
    print("All the values of dictionary is:{}".format(k))