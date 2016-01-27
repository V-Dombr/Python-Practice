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
        if word in words_list:
            continue
        else:
            words_list.append(word)

words_list.sort()
print words_list
