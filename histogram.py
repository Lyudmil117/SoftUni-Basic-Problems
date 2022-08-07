n = int(input())

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for i in range(1, n + 1):
    current_number = int(input())
    if current_number < 200:
        n1 = n1 + 1
    elif current_number < 400:
        n2 = n2 + 1
    elif current_number < 600:
        n3 = n3 + 1
    elif current_number < 800:
        n4 = n4 + 1
    else:
        n5 = n5 + 1

perc1 = (n1 / n) * 100
perc2 = (n2 / n) * 100
perc3 = (n3 / n) * 100
perc4 = (n4 / n) * 100
perc5 = (n5 / n) * 100

print(f'{perc1:.2f}%')
print(f'{perc2:.2f}%')
print(f'{perc3:.2f}%')
print(f'{perc4:.2f}%')
print(f'{perc5:.2f}%')


