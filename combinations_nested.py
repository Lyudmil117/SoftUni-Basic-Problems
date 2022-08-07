number = int(input())

combination_counter = 0

# x1 + x2 + x3 = n
for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            if x1 + x2 + x3 == number:
                combination_counter = combination_counter + 1

print(combination_counter)
