# Enter a number and program will count the sum
# let's say x = 3 then it returns 1+2+3

x_sum = []
i = 0

#TODO Check type of variable
x = int(raw_input("Please, enter a number: "))

# count from 1 to x
for i in range(x):
    i = i + 1
    x_sum.append(i)

# count from x to 1
for i in range(x, 1, -1):
    i = i - 1
    x_sum.append(i)

print
print x_sum
print "The sum is %s" % (sum(x_sum))