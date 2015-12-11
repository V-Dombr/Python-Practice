def cube(number):
    """Returns the cube of a number"""
    cube_number = number ** 3
    print "The cube of %d is %d" % (number, cube_number)
    return cube_number

print cube(2)