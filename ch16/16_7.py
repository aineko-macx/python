from datetime import datetime


import copy

class Time(object):
    """Represents a time in hours, minutes, and seconds.
    """

def print_time(Time):
    print("%.2d: %.2d: %.2d" %(Time.hour, Time.minute, Time.second))


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

def secs(Time):
    return Time.hour*3600 + Time.minute*60 + Time.second



def increment(Time, seconds):
    
    newTime = copy.deepcopy(Time)

    initial = secs(Time)
    total = initial + seconds

    hours = total//3600
    rem = total%3600

    minutes = rem//60
    sec = rem%60

    newTime.hour = hours
    newTime.minute = minutes
    newTime.second = sec
    
    return newTime

def time_to_int(Time):
    minutes = Time.hour*60 + Time.minute
    seconds = minutes *60 + Time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)

    return time

def incr(Time, seconds):
    
    int = time_to_int(Time)
    temp = int + seconds
    
    newTime = int_to_time(temp)

    return newTime


def mul_time(Time, num):
    
    intTime = secs(Time)

    product = intTime*num

    result = int_to_time(product)

    return result


def pace(Time, dist):

    pace = mul_time(Time, 1/dist)

    return pace


#16_7

def print_weekday_str(day):
    weekday = day.weekday()
    if weekday == 0:
        print("Monday")
    elif weekday == 1:
        print("Tuesday")
    elif weekday == 2:
        print("Wednesday")
    elif weekday == 3:
        print("Thursday")
    elif weekday == 4:
        print("Friday")
    elif weekday == 5:
        print("Saturday")
    else:
        print("Sunday")

def print_age(birthday):
    today = datetime.today()
    
    age = today.year - birthday.year - 1

    if today.month > birthday.month:
        age +=1 
    elif  today.month == birthday.month:
        if today.day >= birthday.day:
            age +=1
            
    print(age)


def print_next_bday(birthday):
    today = datetime.today()

    next_bday = datetime(today.year, birthday.month, birthday.day)

    if today > next_bday:
        next_bday = datetime(today.year+1, birthday.month, birthday.day)

    print("Next bday: ", next_bday, "is in ", next_bday-today)



def days_old(birthday, date):

    
    delta = date - birthday
    
    return delta.days


def double_day(birthday1, birthday2):

    if birthday1 > birthday2:
        birthday1, birthday2 = birthday2, birthday1

    delta = birthday2 - birthday1
    doubleDay = delta + birthday2

    return doubleDay


def n_day(birthday1, birthday2,n):

    if birthday1 > birthday2:
        birthday1, birthday2 = birthday2, birthday1

    delta = birthday2 - birthday1
    
    nDay = birthday2 + delta / (n-1)

    
    return nDay

#Main

today = datetime.today()
#birthday = datetime(2018,12,1)
#birthday1 = datetime(2018, 11, 1)

print_weekday_str(today)

#date = datetime(2018, 12,25)
#print_weekday_str(today)
#print_age(birthday)
#print_next_bday(birthday)


#print(days_old(birthday, date))
#print(days_old(birthday1, date))
#print(double_day(birthday, birthday1))
#print(n_day(birthday, birthday1, 3))
"""
myTime = Time()
myTime.hour = 0
myTime.minute = 10
myTime.second = 30

print_time(pace(myTime, 1.5))

newTime = increment(myTime, 9999)
print_time(newTime)

ans = int_to_time(time_to_int(myTime))
print_time(ans)

newTime1 = incr(myTime, 9999)
print_time(newTime1)

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)
"""
