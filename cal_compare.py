calendarA = [["09:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
calendarB = [["10:00","11:30"],["12:30","14:30"],["14:30","15:00"], ["16:00","17:00"]]

#Task: Work out when A and B can have a meeting
#meetings can be between 09:00 and 18:30
#meeting lengths are minimum of 30 minutes
#sample output: [["11:30","12:00"],["15:00","16:00"],["18:00","18:30"]]

##array = []
##empty_time_slot = []
##time = "09:00"
##for time_slot in calendarA:
##    initial_time = 0
##    end_time = 1
##    hour = int(time[0:2])
##    minutes = time[3:5]
##    if hour >= int(time_slot[initial_time][0:2]):
##        if minutes >= int(time_slot[final_time][3:5]:
##            if len(empty_time_slot) == 0:
##                empty_time_slot.append(time)
##        
minutes_calendar = []

minutes_calendar_A = []
temp = []
for time_slot in calendarA:
    temp = []
    minutes = 0
    initial_time = time_slot[0]
    #print(initial_time)
    minutes = int(initial_time[0:2])*60 + int(initial_time[3:5])
    temp.append(minutes)
    #print()
    end_time = time_slot[1]
    #print(end_time)
    minutes = int(end_time[0:2])*60 + int(end_time[3:5])
    temp.append(minutes)
    minutes_calendar_A.append(temp)
    #print(minutes_calendar_A)

minutes_calendar_B = []
#print('B')
for time_slot in calendarB:
    temp = []
    minutes = 0
    initial_time = time_slot[0]
    #print(initial_time)
    minutes = int(initial_time[0:2])*60 + int(initial_time[3:5])
    temp.append(minutes)
    #print()
    end_time = time_slot[1]
    #print(end_time)
    minutes = int(end_time[0:2])*60 + int(end_time[3:5])
    temp.append(minutes)
    minutes_calendar_B.append(temp)
    #print(minutes_calendar_B)

#print(minutes_calendar)
##for a in minutes_calendar_A:
##    #print(a)
##    minutes_calendar.append(a)
##for b in minutes_calendar_B:
##    minutes_calendar.append(b)
##
##minutes_calendar = sorted(minutes_calendar)
##print(minutes_calendar)
##for i in range(540,1140,30):
##    for interval in minutes_calendar:
##        if i in range(interval[0],interval[1]):
##            print('time',i, interval)
##
##print()
#print(minutes_calendar_A)
#print(minutes_calendar_B)
arr = []
for a,b in zip(minutes_calendar_A, minutes_calendar_B):
    #print(a,b)
    if a[1] in range(b[0],b[1]):
        arr.append([a[0],b[1]])
    else:
        arr.append(min(a,b))
        arr.append(max(a,b))
#print(arr)

times = []
for i in range(len(arr)):
    if i == 0:
        continue
    num = min(arr[i])- max(arr[i-1])
    #print(num)
    if num > 0:
        times.append([max(arr[i-1]),min(arr[i])])
times.append([1080,1110])
#print(times)
    
def convertToTime(time):
    return ':'.join([str(time//60).zfill(2),str(time%60).zfill(2)])

for a,b in times:
    print(convertToTime(a),'-',convertToTime(b))
