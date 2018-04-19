import sys
# https://tutorialspoint.com/python/python_command_line_arguments

# `sys.argv[1:]` returns a subset of the original array without first argument
# (which is the script name)

# First of all, in case the user enters the wrong time format, we'll wrap
# everything with `try` to except ValueError
try:
    # Let's break hour and minute values into separate parts to compare them
    # We'll check for a colon in the hour values (indicating it's a single digit)
    # Time 1
    if ":" in sys.argv[1][:2]:
        hour1 = int(sys.argv[1][:1])
    else:
        hour1 = int(sys.argv[1][:2])
    minute1 = int(sys.argv[1][-2:])

    # Time 2
    if ":" in sys.argv[2][:2]:
        hour2 = int(sys.argv[2][:1])
    else:
        hour2 = int(sys.argv[2][:2])
    minute2 = int(sys.argv[2][-2:])

    # Now we can figure out the number of hours between the two times by simply
    # subtracting the second hour value from the first. However, we need to account
    # for scenarios where the first minute value is higher than the second, in
    # which case the threshold between the hours need to be pulled back by 1.
    # My brain hurts trying to explain why.
    if minute1 > minute2:
        hourDuration = (hour2 - hour1) - 1
    else:
        hourDuration = (hour2 - hour1)

    # The duration in minutes is the number it takes to get the first value to 60
    # combined with the second value
    minuteDuration = (60 - minute1) + minute2

    # This is the opposite of the check we did above for when the first minute value
    # is high. In this case, if it's a small value, we need to remove an hour from
    # the calculation.
    if minuteDuration > 60:
        minuteDuration = minuteDuration - 60

    if hourDuration < 0:
        # Step to the next day
        if minuteDuration == 60:
            print str(hourDuration + 24) + "h "
        else:
            print str(hourDuration + 24) + "h " + str(minuteDuration) + "m"

    elif hourDuration == 0:
        # Drop the hour value altogether
        if minuteDuration == 60:
            print "You've entered the same times."
        else:
            print str(minuteDuration) + "m"
    elif minuteDuration == 60:
        # Drop the minute value altogether
        print str(hourDuration) + "h "

    else:
        print str(hourDuration) + "h " + str(minuteDuration) + "m"
except ValueError:
    print "Oh no, times not recognized! Please try again with hh:mm hh:mm"
