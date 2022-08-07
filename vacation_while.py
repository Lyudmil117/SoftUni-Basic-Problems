money_needed = float(input())
current_money = float(input())
days_spend = 0
action_spend = 0
action_saved = 0
days_counter = 0

while current_money < money_needed:
    action = input()
    money = float(input())
    days_counter = days_counter + 1

    if action == "spend":
        action_spend = action_spend + 1
        days_spend = days_spend + 1
        current_money = current_money - money

        if current_money < 0:
            current_money = 0

        if action_spend == 5:
            print("You can't save the money.")
            print(days_spend)
            break

    elif action == "save":
        current_money = current_money + money
        if current_money == money_needed:
            print(f"You saved the money for {days_counter} days.")
            break

