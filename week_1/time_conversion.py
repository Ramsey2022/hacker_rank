"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: 
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#Example
    s = '12:01:00PM'
        return '12:01:00'
    s = '12:01:00AM'
        return '00:01:00'
"""

# if time is 12am replace 12 with 00, if after 12pm add 12
def timeConversion(s):
    am = s[-2:]
    time = s[:-2]
    if am == 'AM':
        if (time.split(':')[0] == '12'):
            return '00' + time[2:]
        else:
            return time
    else:
        if(time.split(':')[0] == '12'):
            return time
        else:
            pm = int(time[:2]) + 12
            return str(pm) + time[2:]