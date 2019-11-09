
def print_header(header):
    for day in header:
        print(day, end = '  ')
    print()

def print_calendar(startday, num_of_days, header):
    index = header.index(startday)
    print('     '*index, end = '')
    index += 1
    i = 1
    while i <= num_of_days:
        print('{0:<5}'.format(i), end = '')
        if index % 7 == 0:
            print('')
        i += 1
        index += 1
            
    
def main():
    startday = input('Day: ')
    num_of_days = int(input('Number of days: '))
    header = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    print_header(header)
    print_calendar(startday, num_of_days, header)
    
main()
