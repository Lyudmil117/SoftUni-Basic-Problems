
name = input()
record_goals = 0
record_name = ""

while name != "END":
    goals = int(input())
    if goals > record_goals:
        record_goals = goals
        record_name = name

    if record_goals >= 10:
        break

    name = input()

print(f"{record_name} is the best player!")

if record_goals >= 3:
    print(f"He has scored {record_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {record_goals} goals.")

