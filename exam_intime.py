hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())

time_exam = minute_exam + (hour_exam * 60)
time_stud = min_arrival + (hour_arrival * 60)

time_difference = abs(time_exam - time_stud)

if time_stud > time_exam:
    print("Late")
    if time_difference >= 60:
        hours_late = time_difference // 60
        min_late = time_difference % 60
        print(f"{hours_late}:{min_late:02d} minutes before the start.")
    else:
        print(f"{time_difference:02d} minutes after the start")

elif time_stud <= time_exam and time_difference < 30:
    print("On time")
    if time_difference > 0:
        print(f"{time_difference} minutes before the start.")
        
else:
    print("Early")
    if time_difference >= 60:
        hours_early = time_difference // 60
        min_early = time_difference % 60

        print(f"{hours_early}:{min_early:02d} hours before the start.")
    else:
        print(f"{time_difference} minutes before the start.")

