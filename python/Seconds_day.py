no_days = int(input("How many days do you want to use to culculate the no of seconds? "))
seconds_minute = 60
minutes_day = 60
hours_day = 24 
seconds_day = seconds_minute * minutes_day * hours_day
seconds_days = no_days * seconds_day

print("Seconds in that many days:",seconds_days)
