import math

athlete1 = int(input())
athlete2 = int(input())
athlete3 = int(input())

total_time = athlete1 + athlete2 + athlete3
min = total_time / 60
sec = total_time % 60
min = math.floor(min)

if sec < 10:
    print(f'{min}:0{sec}')
else:
    print(f'{min}:{sec}')
