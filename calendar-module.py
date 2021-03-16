import calendar

def get_day_name(year, month, day):
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    weekday = calendar.weekday(year, month, day)
    # print(weekday)
    return days[weekday]


if __name__=="__main__":
    month, day, year = map(int, input().split())
    print(get_day_name(year, month, day))
