weather = float(input())

if weather >= 5 and weather <= 11.9:
    print("Cold")
elif weather >= 12 and weather <= 14.9:
    print("Cool")
elif weather >= 15 and weather <= 20.00:
    print("Mild")
elif weather >= 20.1 and weather <= 25.9:
    print("Warm")
elif weather >= 26 and weather <= 35:
    print("Hot")
else:
    print("unknown")