
budget = float(input())
actors = int(input())
clothes = float(input())


decor = budget * 0.1
per_actor = float(actors * clothes)
discount = 0

if actors > 150:
    discount = per_actor * 0.1
else:
    per_actor = per_actor

money_needed = decor + (per_actor - discount)
extra_money = money_needed - budget
enough_money = budget - money_needed

extra_money = abs(extra_money)
enough_money = abs(enough_money)

if budget < money_needed:
    print(f'Not enough money!')
    print(f'Wingard needs {enough_money:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {extra_money:.2f} leva left.')
