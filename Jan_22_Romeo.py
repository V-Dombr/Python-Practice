fname = raw_input("Please, enter a file name: ")
words_list = []

try:
    fhandle = open(fname)
except:
    print("Something is wrong with a file name")
    quit()

for line in fhandle:
    words = line.split()
    words_list.append(word)
    for word in words_list:
        if

print words

