##Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
s="srikanthsjgfhjfjhgkjhkgkgssssss"
s1=s[0]
for i in s[1:]:
    if i != s[0]:
        s1 = s1+i
    else:
        s1 = s1 + '$'
print(s,s1)
