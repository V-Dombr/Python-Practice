numbers = [131, 23, 14, 135, 56, 72, 55, 57, 44, 33, 50]

smallest = None

for i in numbers:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i

print ("The lowest is"), smallest