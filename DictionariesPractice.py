prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    print

total = 0

for item in prices:
    multiply = prices[item] * stock[item]
    print multiply
    total = total + multiply

print total