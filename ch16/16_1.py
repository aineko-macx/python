class Time(object):
    """Represents the time of day.
    
    attributes: hour, minute, second
    """


def print_time(Time):
    print("%.2d:%.2d:%.2d" %(time.hour, time.minute, time.second))







time = Time()
time.hour = 1
time.minute = 59
time.second = 30



print_time(Time)

