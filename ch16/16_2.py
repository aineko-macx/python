class Time(object):
    """Represents the time of day.
    
    attributes: hour, minute, second
    """


def print_time(Time):
    print("%.2d:%.2d:%.2d" %(time.hour, time.minute, time.second))




def is_after_if(Time1, Time2):
    #Returns true if time2 after time1, else returns false
    
    if Time2.hour > Time1.hour:
        return True
    elif Time2.hour == Time1.hour:
        if Time2.minute > Time1.minute:
            return True
        elif Time2.minute == Time1.minute:
            if Time2.second > Time1.second:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    

def time_hours(Time):
    return Time.hour + (Time.minute/60) + (Time.second/3600)

def is_after(Time1, Time2):
    return time_hours(Time2) > time_hours(Time1)






time1 = Time()
time1.hour = 1
time1.minute = 55
time1.second = 30

time2 = Time()
time2.hour = 10
time2.minute = 15
time2.second = 33

time3 = Time()
time3.hour = 1
time3.minute = 59
time3.second = 33

time4 = Time()
time4.hour = 1
time4.minute = 55
time4.second = 31


#print(time_hours(time1))
#print(time_hours(time2))
#print(time_hours(time3))
#print(time_hours(time4))
#print_time(Time)

print(is_after(time1, time2))
print(is_after(time1, time3))
print(is_after(time1, time4))

print(is_after(time4, time2))
print(is_after(time2, time4))
print(is_after(time3, time4))



