name = input()
years = 0
sum_grades = 0
fired = 0

while True:
    yearly_grade = float(input())

    if yearly_grade >= 4:
        years = years + 1
        sum_grades = yearly_grade + sum_grades

    if years == 12:
        average_grade = sum_grades / 12
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break

    if yearly_grade < 4:
        fired = fired + 1
        if fired >= 2:
            all_years = (fired + years) - 1
            print(f"{name} has been excluded at {all_years} grade")
            break

