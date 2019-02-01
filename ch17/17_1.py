class Time(object):
    """Represents the time of day.
    """


    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print("%.2d: %.2d %.2d" %(self.hour, self.minute, self.second))

    def time_to_int(self):
        return self.hour*3600 + self.minute*60 + self.second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

def int_to_time(seconds):

    time = Time()
    
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)

    return time



start = Time()
start.hour = 9
start.minute = 45
start.second = 00


end = start.increment(1337)


start.print_time()
end.print_time()
