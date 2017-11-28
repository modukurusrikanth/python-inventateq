#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
def togo(linenum):
    global line
    line = linenum
line = 1
while True:
    if line == 1:
        s = raw_input("Enter a string more than two letters:")
        if len(s) >= 2:
            togo(2)
        else:
            togo(100)
    elif line == 2:
        print(s[:2]+s[-2:])
        togo(20)
    elif line == 20:
        break
    elif line == 100:
        print("You're annoying me - Enter a string more than two letters")
        togo(1)