tshirt = float(input())
money_to_win = float(input())

shorts = tshirt * 0.75
socks = shorts * 0.2
shoes = (tshirt + shorts) * 2
total = tshirt + shorts + socks + shoes
after_disc = total - (total * 0.15)
win = after_disc - money_to_win
lost = abs(money_to_win - after_disc)

if after_disc >= money_to_win:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {after_disc:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {lost:.2f} lv. more.")
