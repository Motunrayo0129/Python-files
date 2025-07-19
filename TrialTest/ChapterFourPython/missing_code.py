def second_since_midnight(hour, minute, second):
    hour_in_seconds = hour * 3600
    minutes_in_seconds = 60 * minute
    return hour_in_seconds + minutes_in_seconds + second

print(second_since_midnight(13,30,45))

