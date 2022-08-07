from math import ceil
days = int(input())
kilometers = float(input())
sum_of_kilometers = kilometers

for _ in range(1, days + 1):
    increase_prec_kilom = int(input())
    kilometers += kilometers * (increase_prec_kilom / 100)
    sum_of_kilometers += kilometers


if sum_of_kilometers >= 1000:
    print(f"You've done a great job running {ceil(sum_of_kilometers - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - sum_of_kilometers)} more kilometers")
