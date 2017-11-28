# Write a Python program to remove the nth index character from a nonempty string
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
s=raw_input("enter a string:")
s1=None
n=eval(raw_input("Enter the index of the letter to be removed:"))
if len(s) == 0 :
    print("Please enter a non-empty string, next time!!")
elif n > len(s):
    print("Please enter proper index value in the range in next runtiime")
else:
    s1 = s.replace(s[n],'')
    print(s,s1)

