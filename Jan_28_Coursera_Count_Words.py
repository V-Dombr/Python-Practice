counts = dict()
# words = list()

# Ask for a text to process
print 'Enter a line of text: '
line = raw_input('>>')

# Split text into words
words = line.lower().split()
print "Words: ", words

print "Counting..."

# Count words
for word in words:
    counts[word] = counts.get(word, 0) + 1

print "Counts: ", counts

# Get rid of words which appear only 1 time and print the rest
for key in counts:
    if counts[key] != 1:
        print key, counts[key]
