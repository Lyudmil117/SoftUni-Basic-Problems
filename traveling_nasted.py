destination = input()
total_saved = 0


while destination != "End":
    min_bud = float(input())
    while total_saved <= min_bud:
        new_save = float(input())
        total_saved = total_saved + new_save

        if total_saved >= min_bud:
            total_saved = 0
            print(f"Going to {destination}!")
            destination = input()

            if destination == "End":
                break
            min_bud = float(input())
    break


