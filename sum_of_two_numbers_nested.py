num1 = int(input())
num2 = int(input())
magic_number = int(input())
flag = False
combination_counter = 0

for x in range(num1, num2 + 1):
    for y in range(num1, num2 + 1):
        combination_counter = combination_counter + 1

        if x + y == magic_number:
            print(f"Combination N:{combination_counter} ({x} + {y} = {magic_number})")
            flag = True
            break

    if flag:
        break


if not flag:
    print(f"{combination_counter} combinations - neither equals {magic_number}")


