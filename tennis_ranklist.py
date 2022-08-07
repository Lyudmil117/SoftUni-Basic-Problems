from math import floor
num_tournaments = int(input())
initial_points = int(input())
new_points = 0
tournaments_won = 0
final_points = 0

for _ in range(num_tournaments):
    position = input()
    if position == "W":
        new_points = 2000 + new_points
        tournaments_won = tournaments_won + 1
    elif position == "F":
        new_points = 1200 + new_points
    else:
        new_points = 720 + new_points

    final_points = new_points + initial_points

average_points_tour = new_points / num_tournaments
perc_tour_won = (tournaments_won / num_tournaments) * 100

print(f'Final points: {final_points}')
print(f"Average points: {floor(average_points_tour)}")
print(f"{perc_tour_won:.2f}%")

