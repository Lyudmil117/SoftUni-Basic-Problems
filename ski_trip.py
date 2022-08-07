days_to_stay = int(input()) - 1
room = input()
review = input()
total = 0


if room == "room for one person":
    if days_to_stay < 10:
        total = days_to_stay * 18.00
    elif 10 <= days_to_stay <= 15:
        total = days_to_stay * 18.00
    else:
        total = days_to_stay * 18.00
elif room == "apartment":
    if days_to_stay < 10:
        total = ((days_to_stay * 25.00) * 0.7)
    elif 10 <= days_to_stay <= 15:
        total = ((days_to_stay * 25.00) * 0.65)
    else:
        total = ((days_to_stay * 25.00) * 0.5)
else:
    if days_to_stay < 10:
        total = ((days_to_stay * 35.00) * 0.9)
    elif 10 <= days_to_stay <= 15:
        total = ((days_to_stay * 35.00) * 0.85)
    else:
        total = ((days_to_stay * 35.00) * 0.8)

if review == "positive":
    total = total + (total * 0.25)
else:
    total = total -(total * 0.1)


print(f"{total:.2f}")
