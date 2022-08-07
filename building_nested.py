num_floors = int(input())
num_flats = int(input())

flat_number = 0
flat_name = ""

for floor in range(num_floors, 0, -1):
    for flat in range(num_flats):
        flat_number = floor * 10 + flat
        if floor == num_floors:

            flat_name = f"L{flat_number}"

        elif floor % 2 != 0:
            flat_name = f"A{flat_number}"

        else:
            flat_name = f"O{flat_number}"

        print(flat_name, end=" ")
    print()

