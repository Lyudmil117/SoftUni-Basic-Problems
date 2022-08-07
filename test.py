year = int(input())

if year % 4 == 0 and (year % 400 == 0 and year % 100 == 0):
    year = True
else:
    year = False
print(year)

