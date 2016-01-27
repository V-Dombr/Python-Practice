fname = raw_input("Please, enter a file name: ")
words = list()
count = 0

try:
    fhandle = open(fname)
except:
    print("Something is wrong with a file name")
    quit()

for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        print words[1]
        count = count + 1
    else:
        continue

print "There were", count, "lines in the file with From as the first word"