import math
from math import ceil

ceil

number_em = int(input())
per_pers = float(input())
price_chairs = float(input())
price_umbrellas = float(input())

all_umbrellas = (number_em / 2)
all_chairs = (number_em * 0.75)
all_umbrellas = math.ceil(all_umbrellas) * price_umbrellas
all_chairs = math.ceil(all_chairs) * price_chairs

final_bill = (number_em * per_pers) + (all_chairs) + (all_umbrellas) # 115.5 + 70.4 + 68.20
print(f'{final_bill:.2f}')


