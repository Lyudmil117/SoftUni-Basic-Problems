num_people = int(input())
season = input()
price = 0

if num_people <= 5:
    if season == "spring":
        price = num_people * 50
    elif season == "summer":
        price = num_people * 48.50
    elif season == "autumn":
        price = num_people * 60.00
    else:
        price = num_people * 86.00
else:
    if season == "spring":
        price = num_people * 48.00
    elif season == "summer":
        price = num_people * 45.00
    elif season == "autumn":
        price = num_people * 49.50
    else:
        price = num_people * 85.00

if season == "summer":
    price = price - (price * 0.15)
elif season == "winter":
    price = price + (price * 0.08)

print(f"{price:.2f} leva.")