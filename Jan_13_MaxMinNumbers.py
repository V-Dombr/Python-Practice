# I am proud about this one!

lowest = None
highest = None

while True:
    num = raw_input("Enter your number:" )

    if num == 'done':
        break

    try:
        num = int(num)
    except:
        print ("Only integer numbers should be entered!")
        continue

    if lowest is None:
        lowest = num

    if highest is None:
        highest = num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print ('The highest number is: '), highest
print ('The lowest number is: '), lowest