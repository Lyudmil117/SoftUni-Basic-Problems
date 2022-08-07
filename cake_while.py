cake_lenght = int(input())
cake_width = int(input())

cake_all = cake_lenght * cake_width
cake_taken = 0

while cake_all > 0:
    piece = input()
    cake_taken = cake_taken + int(piece)
    cake_left = cake_all - cake_taken

    if piece == "STOP":
        print(f"No more cake left! You need {cake_left} pieces more.")
        break

    if cake_left <= 0:
        cake_left = abs(cake_left)
        print(f"No more cake left! You need {cake_left} pieces more.")
        break
    else:
        print(f"{cake_left} pieces are left.")

