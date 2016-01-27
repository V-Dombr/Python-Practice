fname = raw_input("Please, enter a file name: ")
words_list = list()

try:
    fhandle = open(fname)
except:
    print("Something is wrong with a file name")
    quit()

for line in fhandle:
    print line.rstrip()
    words_from_line = line.split()
    for word in words_from_line:
        if word not in words_list:
            words_list.append(word)

words_list.sort()

print
print words_list

