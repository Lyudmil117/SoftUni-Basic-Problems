

budjet = int(input())
season = input()
fisherman = int(input())
trip = 0

if season == "Spring":
    if fisherman <= 6:
        trip = 3000 - (3000 * 0.1)
    elif 7 <= fisherman <= 11:
        trip = 3000 - (3000 * 0.15)
    elif fisherman > 12:
        trip = 3000 - (3000 * 0.25)

elif season == "Autumn" or season == "Summer":
    if fisherman <= 6:
        trip = 4200 - (4200 * 0.1)
    elif 7 <= fisherman <= 11:
        trip = 4200 - (4200 * 0.15)
    elif fisherman > 12:
        trip = 4200 - (4200 * 0.25)


elif season == "Winter":
    if fisherman <= 6:
        trip = 2600 - (2600 * 0.1)
    elif 7 <= fisherman <= 11:
        trip = 2600 - (2600 * 0.15)
    elif fisherman > 12:
        trip = 2600 - (2600 * 0.25)

if fisherman % 2 == 0 and season != "Autumn":
    trip = trip - (trip * 0.05)
else:
    trip = trip

left = abs(budjet - trip)

if budjet >= trip:
    print(f"Yes! You have {left:.2f} leva left.")
else:
    print(f"Not enough money! You need {left:.2f} leva.")
