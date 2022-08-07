budjet = float(input())
season = input()
need = 0
destination = ""
where = ""

if budjet <= 100:
    if season == "summer":
        need = budjet * 0.3
    elif season == "winter":
        need = budjet * 0.7
elif 100 < budjet <= 1000:
    if season == "summer":
        need = budjet * 0.4
    elif season == "winter":
        need = budjet * 0.8

elif 1000 < budjet:
    need = budjet * 0.9



if budjet <= 100:
    destination = "Bulgaria"
elif 100 < budjet <= 1000:
    destination = "Balkans"
elif budjet > 1000:
    destination = "Europe"

if season == "summer":
    if destination == "Bulgaria":
        where = "Camp"
    elif destination == "Balkans":
        where = "Camp"
    else:
        where = "Hotel"

elif season == "winter":
    if destination == "Bulgaria":
        where = "Hotel"
    elif destination == "Balkans":
        where = "Hotel"
    else:
        where = "Hotel"



print(f"Somewhere in {destination}")
print(f"{where} - {need:.2f}")
