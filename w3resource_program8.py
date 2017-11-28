# Write a Python function that takes a list of words and returns the length of the longest one
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
l=['cnxvjxnlkxnlxc','kjgnfxkjvkfjnvklxnv','xkjvbfkjbvjkxznvkjxcnvkjzcxnvjzxcnv','jfvjcgcb','ggg']
max_s=l[0]
for i in l:
    if len(max_s) < len(i):
        max_s=i
print("The maximum length string is: '{}'".format(max_s))


### we can still do like
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    print(word_len)
    word_len.sort()
    print(word_len)
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))