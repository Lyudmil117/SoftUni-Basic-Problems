n = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    current_number = int(input())
    if i % 2 == 0:
        odd_sum = current_number + odd_sum
    else:
        even_sum = current_number + even_sum

diff = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {diff}")

