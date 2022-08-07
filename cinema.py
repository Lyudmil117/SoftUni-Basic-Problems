film = input()
row = int(input())
col = int(input())
income = 0

if film == 'Premiere':
    income = (row * col) * 12.00
elif film == "Normal":
    income = (row * col) * 7.50
elif film == "Discount":
    income = (row * col) * 5.00

print(f"{income:.2f} leva")



