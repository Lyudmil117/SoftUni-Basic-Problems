
the_number = int(input())
bonus = 0
extra_bonus = 0

if the_number < 100:
    bonus = 5
elif the_number > 1000:
    bonus = the_number * 0.1
else:
    bonus = the_number * 0.20


if the_number % 2 == 0:
    extra_bonus = 1

elif the_number % 10 == 5:
    extra_bonus = 2

bonus_points = bonus + extra_bonus

print(bonus_points)
print(the_number + bonus_points)


