
name =input()
points_from_the_academy =float(input())
number_of_evaluators =int(input())
total_sum =0

for _ in range(1 ,number_of_evaluators +1):
    curr_name = input()
    curr_points = float(input())

    total = (len(curr_name ) *curr_points ) /2
    total_sum = total + total_sum

    if(total_sum + points_from_the_academy ) >1250.5:
        break

suma = total_sum + points_from_the_academy
difference =abs(1250.5 - suma)

if suma < 1250.5:
    print(f"Sorry, {name} you need {difference:.1f} more!")
else:
    print(f" Congratulations, {name} got a nominee for leading role with {(total_sum +points_from_the_academy):.1f}!")
