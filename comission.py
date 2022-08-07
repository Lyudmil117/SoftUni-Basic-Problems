city = input()
sales = float(input())
comm = 0
condition = True

if city == 'Sofia':
    if 0 <= sales <= 500:
        comm = 0.05
    elif 500 < sales <= 1000:
        comm = 0.07
    elif 1000 < sales <= 10000:
        comm = 0.08
    elif sales > 10000:
        comm = 0.12
    else:
        condition = False


elif city == "Varna":
    if 0 <= sales <= 500:
        comm = 0.045
    elif 500 < sales <= 1000:
        comm = 0.075
    elif 1000 < sales <= 10000:
        comm = 0.10
    elif sales > 10000:
        comm = 0.13
    else:
        condition = False


elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        comm = 0.055
    elif 500 < sales <= 1000:
        comm = 0.08
    elif 1000 < sales <= 10000:
        comm = 0.12
    elif sales > 10000:
        comm = 0.145
    else:
        condition = False

else:
    condition = False

if condition:
    print(f'{sales * comm:.2f}')
else:
    print('error')

