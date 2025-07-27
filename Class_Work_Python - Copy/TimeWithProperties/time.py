class TimeWithProperties:
    def __init__(self, hour = 0, minute = 0, second= 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value < 0 or value > 23:
            raise ValueError("hour must be between 0 and 23")
        self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if value < 0 or value > 59:
            raise ValueError("minute must be between 0 and 59")
        self._minute = value

    @property
    def second(self):
        return self.second

    @second.setter
    def second(self, value):
        if value < 0 or value > 59:
            raise ValueError("second must be between 0 and 59")
        self._second = value

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

time1 = TimeWithProperties()
time1.hour = 12
print(time1)