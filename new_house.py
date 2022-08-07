#⦁	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
#⦁	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
#	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
#	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
#	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.



flower = input()
flo_number = int(input())
budjet = int(input())

total = 0


if flower == "Roses":
    if flo_number > 80:
        total = (flo_number * 5) - ((flo_number * 5) * 0.10)
    else:
        total = flo_number * 5
elif flower == 'Dahlias':
    if flo_number > 90:
        total = (flo_number * 3.80) - ((flo_number * 3.80) * 0.15)
    else:
        total = flo_number * 3.80
elif flower == "Tulips":
    if flo_number > 80:
        total = (flo_number * 2.80) - ((flo_number * 2.80) * 0.15)
    else:
        total = flo_number * 2.80
elif flower == "Narcissus":
    if flo_number < 120:
        total = (flo_number * 3) * 1.15
    else:
        total = flo_number * 3
elif flower == "Gladiolus":
    if flo_number < 80:
        total = (flo_number * 2.50) * 1.2
    else:
        total = flo_number * 2.50

left = abs(total - budjet)

if total <= budjet:
    print(f"Hey, you have a great garden with {flo_number} {flower} and {left:.2f} leva left.")
else:
    print(f'Not enough money, you need {left:.2f} leva more.')





