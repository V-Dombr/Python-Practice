def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

x = int(raw_input("Please, enter a number: "))

print is_even(x)

