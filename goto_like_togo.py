def togo(linenum):
    global line
    line = linenum

line = 1
while True:
    if line == 1:
        response = raw_input("yes or no? ")
        if response == "yes":
            togo(2)
        elif response == "no":
            togo(3)
        else:
            togo(100)
    elif line == 2:
        print "Thank you for the yes!"
        togo(20)
    elif line == 3:
        print "Thank you for the no!"
        togo(20)
    elif line == 20:
        break
    elif line == 100:
        print "You're annoying me - answer the question!"
        togo(1)