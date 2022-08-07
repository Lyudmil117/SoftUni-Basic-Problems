n = int(input())
counter = 1
is_ready = False

for row in range(1, n + 1):
    for col in range(1, row + 1):

        print(f"{counter}" + " ", end="")
        counter = counter + 1

        if counter > n:
            is_ready = True
            break

    if is_ready:
        break
    print()
