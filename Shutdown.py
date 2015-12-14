def shut_down(s):

    if s.lower() == "yes":
        return "Shutting down"
    elif s.lower() == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

s = raw_input("Would you like to shut down the computer?")
print shut_down(s)