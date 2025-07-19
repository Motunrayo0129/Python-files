class TimeWithProperties:
    def __init__(self, hour = 0, minute = 0, second= 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def second(self):
        return self._second

    @second.setter
    def seconds(self, value):
        if value < 0 and value > 59:
            raise ValueError('seconds must be between 0 and 59')
        self._seconds, = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minutes(self, value):
        if value < 0 and value > 59:
            raise ValueError('minutes must be between 0 and 59')
        self._minute = value

    @property
    def hour(self):
        return self._hour


    @hour.setter
    def hours(self, value):
        if 0 > value > 23:
            raise ValueError('hours must be between 0 and 23')
        self._hour = value

    def __str__(self):
        return f'Time({self.hour}:{self.minute:02}:{self.second:02})'


time1 = TimeWithProperties()
time1.hour = 12
print(time1)