while True:
    num = raw_input("Enter your number:" )

    if num == 'done':
        break

    try:
        num = int(num)
    except:
        print ("Only integer numbers should be entered!")
        continue

