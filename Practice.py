choice = raw_input('Enjoying the course? (y/n)')

print choice

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

print "Passed"