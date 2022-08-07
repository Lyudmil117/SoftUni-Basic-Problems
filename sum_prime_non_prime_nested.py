from math import sqrt
from math import ceil

number = input()
sum_prime = 0
sum_non_prime = 0

while number != "stop":
    number = int(number)

    if number < 0:
        print("Number is negative.")
        number = input()
        continue

    if number <= 1:
        sum_non_prime = sum_non_prime + number

    else:
        is_prime = True
        for div in range(2, ceil(sqrt(number + 1) + 1)):
            if number % div == 0:
                is_prime = False
                break

        if is_prime:
            sum_prime = sum_prime + number
        else:
            sum_non_prime = sum_non_prime + number

    number = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")



