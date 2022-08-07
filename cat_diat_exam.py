percent_fat = int(input()) / 100
percent_protein = int(input()) / 100
percent_cabs = int(input()) / 100
calories = int(input())
water = int(input())

fat_per_day = ((calories * percent_fat) / 9)
protein_per_day = ((calories * percent_protein) / 4)
carbs_per_day = ((calories * percent_cabs) / 4)

food = fat_per_day + protein_per_day + carbs_per_day
calories_per_day = calories / food

water_in_food = calories * (calories_per_day / 100)
result = calories_per_day * ((100 - water) / 100)

print(f'{result:.4f}')
