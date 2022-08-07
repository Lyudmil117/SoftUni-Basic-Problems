command = input()
steps_counter = 0

while command != "Going home":
    steps_per_day = int(command)
    steps_counter = steps_per_day + steps_counter

    if steps_counter >= 10000:
        break

    command = input()

if command == "Going home":
    steps_going_home = int(input())
    steps_counter = steps_going_home + steps_counter

if steps_counter >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{steps_counter - 10000} steps over the goal!")
else:
    print(f"{10000 - steps_counter} more steps to reach goal.")

