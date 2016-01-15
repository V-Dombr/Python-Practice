fname = raw_input("Enter the file name:")
fhand = open(fname)
count = 0

for line in fhand:
    count = count + 1
print "Count lines:", count
