def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(1, x):
            if x % i == 0:
                return False
            else:
                return True

print is_prime(3)