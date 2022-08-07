import math

serial_name = input()
episod_time = int(input())
break_time = int(input())

time_for_lunch = break_time // 8
time_for_break = break_time // 4
time_left = break_time - time_for_break - time_for_lunch

free_time = math.ceil(time_left - episod_time)

if time_left >= episod_time:
    print(f"You have enough time to watch {serial_name} and left with {free_time} minutes free time.")

more_time = math.ceil(episod_time - time_left)

if episod_time > time_left:
    print(f"You don't have enough time to watch {serial_name}, you need {more_time} more minutes.")
