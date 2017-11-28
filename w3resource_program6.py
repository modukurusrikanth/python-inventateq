#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
s=raw_input("Enter a string:")
# s="st"
l=len(s)
if l<3:
    print(s)
elif s.endswith('ing'):
    print(s+'ly')
else:
    print(s+'ing')