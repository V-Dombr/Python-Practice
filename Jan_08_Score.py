try:
    inp = raw_input("Please, enter your score. It must be between 0.0 and 1.0: ")
    score = float(inp)
except:
    print "You must enter a number"
    quit()

if score < 0.0 :
    print "The value is out of range"
    quit()
elif score > 1.0 :
    print "The value is out of range"
    quit()

if score < 0.6:
    print "F"
elif score < 0.7:
    print "D"
elif score < 0.8:
    print "C"
elif score < 0.9:
    print "B"
else:
    print "A"