file_name = raw_input("Enter file name: ")

#Make sure that everything is OK with a file name
try:
    file_data = open(file_name)
except:
    print ("Something is wrong with the file name")
    exit()

print file_data

spam_confidence_sum = 0
count_line = 0

for line in file_data:
    if line.startswith("X-DSPAM-Confidence:"):
        count_line = count_line + 1
        line = line.rstrip()

        spam_confidence_sum = spam_confidence_sum + float(line[20:26])

print "Number of lines", count_line
print "Spam sum", spam_confidence_sum
print "The average spam confidence", spam_confidence_sum/count_line

# Close file and verify if we do this correctly
file_data.close()
print file_data
