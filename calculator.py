n1 = int(input())
n2 = int(input())
choise = input()
result = 0

if choise == "+":
    result = n1 + n2
    if result % 2 == 0:
        print(f'{n1} {choise} {n2} = {result} - even')
    else:
        print(f'{n1} {choise} {n2} = {result} - odd')
elif choise == "-":
    result = n1 - n2
    if result % 2 == 0:
        print(f'{n1} {choise} {n2} = {result} - even')
    else:
        print(f'{n1} {choise} {n2} = {result} - odd')
elif choise == "*":
    result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} {choise} {n2} = {result} - even')
    else:
        print(f'{n1} {choise} {n2} = {result} - odd')
elif choise == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {choise} {n2} = {result:.2f}")
elif choise == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {choise} {n2} = {result}")


