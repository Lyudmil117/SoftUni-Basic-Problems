import math


budget = float(input())
days_in_hotel = int(input())
hotel_per_day = float(input())
percent_of_budget = int(input())
hotel = days_in_hotel * hotel_per_day

extra_to_spend = budget * (percent_of_budget / 100)

if days_in_hotel > 7:
    hotel = hotel_per_day - (hotel_per_day * 0.05)
else:
    hotel = hotel

spend_per_holiday = (hotel_per_day * days_in_hotel) + extra_to_spend
money_left = (f'{budget - spend_per_holiday:.2f}')

money = abs(float(money_left)) # защо не мога да импортна math/abs или каквото и да е друго?

if spend_per_holiday < budget:
    print(f'Ivanovi still have {money} after the holidays')
else:
    print(f'Ivanovi will need {money}')