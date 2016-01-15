xfile = open('test.txt')

"""#Search for a line and remove extra spaces as well as \n
for line in xfile:
    line = line.rstrip()
    if line.startswith("The"):
        print line"""

#Ignoring pattern
for line in xfile:
    line = line.rstrip()
    if not line.startswith("The"):
        print line


#Let's count number of lines
"""count = 0
for line in xfile:
    count = count + 1
print "There are %s lines in the file" % (count)"""

#Reading whole file
"""inp = xfile.read()

print "File contains the following:"
print inp

print "The length of the file is: %s" % (len(inp))
print inp[1:23]"""
