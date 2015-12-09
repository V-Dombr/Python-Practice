from datetime import datetime

now = datetime.now()
print now
print "Current month is %s" % now.month
print "Current day is %s" % now.day
print "Current year is %s" % now.year

print "%s/%s/%s" % (now.year, now.month, now.day)
print "Current time is %s:%s:%s" % (now.hour, now.minute, now.second)