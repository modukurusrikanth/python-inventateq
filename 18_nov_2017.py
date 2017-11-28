#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# s="srikanth"
# print(s)
# print(s.capitalize())   # capitalizes the first letter og the string provided
# print(s.ljust(30,"%")) # ljust() gives left most spaces for the width choosen with the character you gave
# print(s.rjust(30,"%")) # ljust() gives right most spaces for the width choosen with the character you gave
# s2="SRIKaNTh"
# print("Before converting:",s2)
# print(s2.lower()) #converts all the upper case letters to lower cases and remaming as it is
# s3= "    nbzjhc cs zj jz jz zczz z       "
# print(s3.strip())   #removes all the spaces
# print(s3.lstrip())
# print(s3.rstrip())
# s="Today is sdandwich day sdandwich day sssssssss"
# print(s.replace('s','a'))  # reaplces the old letter with new letter proposed
# print(s.replace('s','a',4)) # reaplces the old letter with new letter proposed with number of times you want like 3rd variable you're passing
# print(s.find('z'))  # gives the index of the letter first occurence in the string if it is there or else gives -1
# print(s.rfind('z'))  # gives the index of the letter first occurence in the string if it is there or else gives -1(backward search)
# print(s.index('z'))  # gives the index of the letter first occurence in the string if os there or else it throws an error
# print(s.rindex('s'))  # gives the index of the letter first occurence in the string if os there or else it throws an error(backward search)
# s4="modukuru.srikanth@gmail.com"
# print(s4.split('@'))  # splittig using '@' letter
# print(s4.split('@')[0]) # splitting and printing the first item
# print((s4.split('@')[0]).split('.')[0]) # splitting two times one '@' and second '.' and printing the first item
# print(s4.split('.')[0]) # smart way
# import sys
# for c in s4:
#     if c != '@':
#         print(c)
#     if c == '@':
#         break
# print(s4.startswith("modu"))  # retruns true if that string present or else retruns False
# print(s4.swapcase()) # changes the Lower to upper and vice versa
# s5="""nsjkdnvksndvlsdfkvnksfnvszfv
# vnnvsnvkjsfnvksfnvksflnvksf vkfsv
# nvkjs vks fjv sdfjvsd"""
# print(s4.title()) # Capitalize the first littetr of each word
# print(s5.splitlines()) # split the paragraphs into List of sentences with each new line as a element
# s6="1122017"
# print(s6.zfill(8)) # numbers when defined as string wants equal width we can use this one
# s7=14
# print(s7.isdecimal()) # check once agina have doubt working in idle
# xx=input("Entera string:") # need to check input() is not working
# s9="Weather is pleasant today"
# count=0
# for c in xx:
#     # count=count+1
#   count += 1
# print("the string '{}' has : {} letters".format(xx,count))

s=raw_input("Enter a string:")
if len(s) < 2:
    print("You've entered a single letter word \a")
else:
    print(s[:2]+s[-2:])