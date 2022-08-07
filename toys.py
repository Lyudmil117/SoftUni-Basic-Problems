puzz = 2.60
doll = 3
bear = 4.10
mini = 8.20
car = 2

holiday = float(input())
num_puzz = int(input())
num_doll = int(input())
num_bear = int(input())
num_mini = int(input())
num_car = int(input())

toys = num_car + num_mini + num_doll + num_bear + num_puzz

order = (num_puzz * puzz) + (num_doll * doll) + (num_bear * bear) + (num_mini * mini) + (num_car * car)

discount = 0

if toys >= 50:
    discount = order * 0.25

petq_has = order - discount
za_more = petq_has - (petq_has * 0.1)

if za_more >= holiday:
    ostavat = za_more - holiday
    print(f'Yes! {ostavat:.2f} lv left.')
else:
    ostavat = holiday - za_more
    print(f'Not enough money! {ostavat:.2f} lv needed.')
