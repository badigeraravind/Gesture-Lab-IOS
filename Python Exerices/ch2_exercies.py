#Exercise 2-A Character Creator (warm-up)

player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

print (f"=== Welcome, {player_name} (Age {player_age}) ===")






#Exercise 2-B Lap-Time Difference

best_lap_sec = float(input('Enter your best lap in seconds: '))
curr_lap_sec = float(input('Enter your current lap in seconds: '))

differ = (curr_lap_sec - best_lap_sec) * 1000

print(f"Difference: {differ:+.0f} ms")              # “+” prints the sign, “.0f” drops decimals

if (curr_lap_sec < best_lap_sec):
    print("!!! NEW RECORD !!!")





#Exercise 2-C Boolean Flag Check

debug_mode = True
if debug_mode:
    print("Debug Overlay is OFF")
else:
    print("Debug Overlay is ON")



