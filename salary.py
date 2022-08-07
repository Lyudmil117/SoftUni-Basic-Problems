n = int(input())
salary = int(input())

globa1 = 0
globa2 = 0
globa3 = 0
globa4 = 0

for i in range(n):
    site = input()
    if site == "Facebook":
        globa1 = globa1 + 150
    elif site == "Instagram":
        globa2 = globa2 + 100
    elif site == "Reddit":
        globa3 = globa3 + 50
    else:
        globa4 = globa4

globite = globa1 + globa2 + globa3 + globa4
ostavat = salary - globite

if ostavat > 0:
    print(f"{ostavat:.0f}")
else:
    print("You have lost your salary")
