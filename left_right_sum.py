n = int(input())
left_sum = 0
right_sum = 0

for _ in range(1, n + 1):
    left_sum = left_sum + int(input())
for _ in range(1, n + 1):
    right_sum = right_sum + int(input())

diff = abs(right_sum - left_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {right_sum}')
else:
    print(f'No, diff = {diff}')
