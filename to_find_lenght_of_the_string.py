#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
s=raw_input("Enter a string more than two words")
count = 0
for c in s:
    count += 1
print("length of the string {} is :{}".format(s,count))