n = [5, 7, 8]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print double_list(n)