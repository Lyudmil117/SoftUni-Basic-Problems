gpu = 250

budget = float(input())
num_gpu = int(input())
num_cpu = int(input())
num_ram = int(input())

cpu = ((250 * num_gpu) * 0.35) * num_cpu
ram = ((250 * num_gpu) * 0.10) * num_ram

total = (num_gpu * gpu) + cpu + ram
left = budget  #защо като беше 0 джъдж не го приемаше?
gear_cost = total # pak zasto?

if num_gpu > num_cpu:
    gear_cost = total - (total * 0.15)

if budget >= gear_cost:
    left = budget - gear_cost
    print(f"You have {left:.2f} leva left!")
else:
    left = gear_cost - budget
    print(f'Not enough money! You need {left:.2f} leva more!')
