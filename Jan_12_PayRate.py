def computepay(h,r):
    if h <= 40:
        pay = h * r
        return pay
    else:
        pay = 40 * r + (1.5 * r * (h - 40))
        return pay

inp_hrs = raw_input("Enter Hours: ")
hrs = float(inp_hrs)

inp_pay_rate = raw_input("Enter Rate per 1 hour: ")
pay_rate = float(inp_pay_rate)

p = computepay(hrs, pay_rate)
print "Pay",p