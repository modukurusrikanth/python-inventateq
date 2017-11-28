#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
s=raw_input("Enter a string:")
l=list(s)
length=len(l)
i=length/2
if (length % 2) == 0:
    print("Entering to if:")
    print("The middle letters are:",l[(i-1):(i+1)])
else:
    print("Entering to else:")
    print("The middle letter is",l[i])

# print(l[(len(l)//2)])