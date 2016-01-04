# Let's take 623. The program will return the sum 6 + 2 + 3

def digit_sum(n):
    sum_n = 0

    len_n = len(str(n))
    n = str(n)

    for i in range(len_n):
        sum_n = sum_n + int(n[i])

    return sum_n

print digit_sum(999)