def is_leap_year(year):
    print(year, end = ' ')
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print('True')
    else:
        print('False')

is_leap_year(2000)
is_leap_year(1800)
is_leap_year(2004)

