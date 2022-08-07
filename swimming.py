from math import floor

record_seconds = float(input())
meters = float(input())
time = float(input())

ivan_time = meters * time
met_sec = floor(meters // 15)
resist = (met_sec * 12.5)
total_time = ivan_time + resist
fail = abs(record_seconds - total_time)

if record_seconds < total_time:
    print(f'No, he failed! He was {fail:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
