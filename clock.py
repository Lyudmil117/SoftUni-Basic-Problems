# ⦁	Време + 15 минути
# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.

hour = int(input())
min = int(input())

min = min + 15
if hour == 24:
    hour = hour - 24

if min >= 60:
    min = min - 60
    hour = hour + 1
if min >= 10:
    print(f'{hour}:{min}')
else:
    print(f'{hour}:0{min}')



