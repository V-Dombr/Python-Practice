"""fname = raw_input("Please, enter a file name: ")
words = []

try:
    fhandle = open(fname)
except:
    print("Something is wrong with a file name")
    quit()

for line in fhandle:
    clean_line = line.rstrip()
    words_line = clean_line.split()
    words.append(words_line)

print words"""

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    print line.split()