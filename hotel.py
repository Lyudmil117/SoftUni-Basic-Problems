month = input()
nights_hotel = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    if nights_hotel > 14:
        studio = 50 * nights_hotel
        studio = studio - (studio * 0.3)
    elif nights_hotel > 7:
        studio = 50 * nights_hotel
        studio = studio - (studio * 0.05)

elif month == "June" or month == "September":
    if nights_hotel > 14:
        studio = nights_hotel * 75.20
        studio = studio - (studio * 0.2)
    else:
        studio = nights_hotel * 75.20

elif month == "July" or month == "August":
    studio = nights_hotel * 76



if month == "May" or month == "October":
    if nights_hotel > 14:
        apartment = nights_hotel * 65.00
        apartment = apartment - (apartment * 0.1)
    else:
        apartment = 65.00 * nights_hotel

elif month == "June" or month == "September":
    if nights_hotel > 14:
        apartment = 68.70
        apartment = apartment - (apartment * 0.1)
    else:
        apartment = 68.70 * nights_hotel

elif month == "July" or month == "August":
    if nights_hotel > 14:
        apartment = 77.00 * nights_hotel
        apartment = apartment - (apartment * 0.1)
    else:
        apartment = nights_hotel * 77.00

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
