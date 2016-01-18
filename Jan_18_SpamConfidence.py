file_name = raw_input("Enter file name: ")
file_data = open(file_name)

spam_confidence_sum = 0
count_line = 0

for line in file_data:
    if line.startswith("X-DSPAM-Confidence:"):
        count_line = count_line + 1
        