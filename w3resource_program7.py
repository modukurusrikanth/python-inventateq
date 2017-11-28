#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
s='The lyrics is not that poor!'
snot=s.find('not')
spoor=s.find('poor')
if snot<spoor:
    print(s.replace(s[snot:(spoor+4)],'good'))

# print(s.replace('not that poor','good',1))