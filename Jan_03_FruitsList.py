fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
# Check the first letter to use proper article: 'a', 'an'
    if f[0] == 'a' or f[0] == 'o':
        print 'An', f
    else:
        print 'A', f
else:
    print 'A fine selection of fruits!'