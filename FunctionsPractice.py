def wages(hours):
    # If I make $80/hour
    wage = 80 * hours
    return wage


hours = float(raw_input("Enter hours:"))
print type(hours)
print wages(hours)
