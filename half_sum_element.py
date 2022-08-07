import sys

n = int(input())
max_num = -sys.maxsize
sum_of_numbers = 0

for i in range(0, n):
    num = int(input())

    if max_num <= i:
        max_num = num
        sum_of_numbers = sum_of_numbers + num

if max_num == sum_of_numbers - max_num:
    print("Yes")
    print(f'Sum = {sum_of_numbers}')
else:
    print("No")
    sum_others = sum_of_numbers - max_num
    print(f"Dif = {abs(max_num - sum_of_numbers)}")


