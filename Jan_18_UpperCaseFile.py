file_name = raw_input("Enter file name: ")
file_data = open(file_name)

for line in file_data:
    print line.upper().rstrip()