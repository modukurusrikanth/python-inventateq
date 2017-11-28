#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
########################## Tuples ##############################################
# s="srikanth"
# t=tuple(s)          # will convert given string/list to tuple
# print(s,t)


############# Dictionaries ######################
# d = {}
# print(dict)
# d = {'KA':'BLR','MH':'mum','AP':'AMR'} # first one is key and seocnd one value
# print(d)
# print(d['KA']) # accessing a dictionray value
# d = {'KA':'BLR','MH':'mum','AP':'AMR','noodles':['yippeee','maggi']} # when one key has multiple values
# print(d) # dictionary will not print in order that we define
# print(d.keys()) # prints all keys as a list
# print(d.values()) # prints all values as a list
# del d['KA']
# print(d)
# d.clear()   # it will just clear the data but structure will be as it is
# print(d)  # will print empty dict
# del(d)  # it will delete the structure also so when we try to print it it will tell like it's not defined
# print(d)
d = {'KA':'BLR','MH':'mum','AP':'AMR','noodles':['yippeee','maggi']}  # updating a dictionary values
# d['noodles'][0]="YIPPPEEEE"
# print(d)
# l=[1,2,3,d]
# print(l)
# print(l[3]['KA']) # asscessing a velue of dict inside a list
# print(d['K']) # gives Key Error Exception when we try to access a key that is nt present
# print(dict.fromkeys("Srikanth",5))
# print(d.get('Kerala',"trivendrum"))# retruns the key value if it is there it will return existing Value
# print(d.get('KA',"trivendrum"))
# print(d.items()) # retruns a tuples with each key and value as a pair
# print ("Value : {}" .format(d.setdefault('KA', None))) # similar to get but
# print (d)
# print ("Value : {}" .format(d.setdefault('Sex', '5')))
# print (d)

# d3 = {'Name': 'srikanth', 'Age': 23}
# d4 = {'Sex': 'male' }
#
# d3.update(d4) # adds d4 to d3
# # d3 = d3+d4  # dictionary concatination is not possible
# print ("updated dict : ", d3)
