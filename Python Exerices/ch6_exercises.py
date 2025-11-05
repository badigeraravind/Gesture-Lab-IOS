

# exercise 6a - Killfeed Analyzer
# Write a script that:
#	1.	Uses this fixed list: killfeed = ["P1", "P2", "P3", "P1", "P1", "P2", "P4"]
#   2.  Prompts the tester to enter a player name
#	3.	Prints how many kills that player got in total (i.e., how many times their name appears in the list)

killfeed = ["a","b","c","d","a","b","a","c","a","b"]

def kill_analyzer(name):
    return killfeed.count(name)

name = input("enter player name: ")
print(f"player {name} got a total of {kill_analyzer(name)} kills.")

#=========================================================================================================================================================================================================================

# ✅ Exercise 6-B – Most Kills Winner
#	1.	Reuse this list: killfeed = ["P1", "P2", "P3", "P1", "P1", "P2", "P4"]
#	2.	Write code that finds and prints:
#	•	The name of the player with the most kills
#	•	Their kill count
#	•	You’ll need to loop through the list.
#	•	Use either:
#	•	A dictionary to count kills per player, or
#	•	A set to find unique players, then .count() each.

killfeed = ["P1", "P2", "P3", "P1", "P1", "P2", "P4", "P4", "P4", "P4", "P4"]
killcounts = {}

for killer in killfeed:
    if killer in killcounts:
        killcounts[killer] += 1
    else:
        killcounts[killer] = 1 

top_killer = max(killcounts, key = killcounts.get)
top_kills = killcounts[top_killer]

print(f"Top Killer: {top_killer} :: {top_kills} kills")

#=========================================================================================================================================================================================================================

# Exercise 7A — Skip Broken Frames
# You have a list of frame render times (in milliseconds).
# Some frames are marked -1, which means they’re corrupted and should be skipped.
# Write a loop that:
# Goes through the list
# Skips over the corrupted frames (-1)
# Prints only the render times of valid frames

frame_time = [12,27,-3,34,102,-23.5,-213.23]

for a in frame_time:
    if a > 0 :
        print(a)
    else :
        continue


#=========================================================================================================================================================================================================================

# ✅ Exercise 7B — Stop After First Crash Frame
# You’re analyzing a game replay log that lists frame durations in milliseconds.
# If a frame has a negative value, it means the engine crashed at that point.
# Write a loop that:
# Goes through the list of frame durations
# Prints each frame until the first crash
# Then stops execution immediately (do not print anything after that)

frame_time = [12,27,-3,34,102,-23.5,-213.23]

for a in frame_time:
    if a > 0 :
        print(a)
    else :
        break

#=========================================================================================================================================================================================================================

# ✅ Exercise 7C — Did We Finish All Frames?
# You’re analyzing frame render times again.
# If all frames are valid (no negative values), print "All frames processed successfully!"
# But if any frame crashes (negative value), you should stop printing and instead show "Crash detected!"
# You must use:
# A for loop
# An else: clause on the loop (yes, Python allows this!)

frame_time_a = [12,27,-3,34,102,-23.5,-213.23]
frame_time_b = [33,29,123,69,12,32,908,23,56,90]


for a in frame_time_a:
    if a > 0 :
        print(a)
    else :
        print("Crash Detected!")
        break
else:
    print("All frames processed successfully!")
print('===============')
for b in frame_time_b:
    if b > 0 :
        print(b)
    else:
        print('Crash Detected!')
        break
else:
    print("All frames processed successfully!")


#=========================================================================================================================================================================================================================

# ✅ Exercise 7D — Nested Waves & Early Termination
# You’re simulating enemy waves in a level.
# Each level has multiple waves, and each wave contains a list of enemy HP values.
# Write code that:
#	•	Loops through levels (a list of waves)
#	•	For each wave (a list of HPs), print "Wave started" and print all HPs
#	•	If you encounter an enemy with HP of 0, immediately terminate the entire level (not just the wave) and print "Level failed!"
# You will need:
#	•	Nested loops (loop inside a loop)
#	•	A break and a flag to exit both loops

level = [
    [100, 90, 80],
    [120, 110, 0, 95],
    [150, 160, 170]
]
flag = False

for l in level:
    print ('wave started')
    for w in l:
        if w > 0:
            print (w)
        else:
            print('level failed')
            flag = True
            break
    if flag == True:
        break


#=========================================================================================================================================================================================================================

# ✅ Exercise 7E — Full Clear with Loop Else
# You’re still working with levels and waves of enemy HP values.
# This time:
#	•	Print "Wave started" for each wave
#	•	Print each enemy’s HP
#	•	If any enemy has HP = 0, print "Level failed!" and exit the level
#	•	But if the level finishes with no 0 HPs, print "Level cleared!" at the end
# This time, you must use a for ... else: clause to detect if the loop finished normally without a crash.


level = [
    [100, 90, 80],
    [120, 110, 10, 95],
    [150, 160, 170]
]
flag = False

for l in level:
    print ('wave started')
    for w in l:
        if w > 0:
            print (w)
        else:
            print('level failed')
            flag = True
            break
    if flag:
        break
else:
    print('level cleared')


#=========================================================================================================================================================================================================================

# ✅ Exercise 7G — Frame Drift Monitor
# You’re testing a game mode where each level has several waves. Each wave is a list of enemy HPs.
#	•	For each wave:
#	•	Print "Wave X started" (X = wave number starting from 1)
#	•	Count how many enemies are above 50 HP (i.e., strong enemies)
#	•	If more than 3 strong enemies exist in any wave, print "Warning: Overpowered wave!"
#	•	Continue processing all waves.

level = [
    [10, 25, 90, 75, 10],    # 2 strong
    [65, 80, 95, 100, 55],   # 5 strong → warning!
    [30, 45, 20, 10],        # 0 strong
    [30, 95, 80, 70, 69]     # 4 strong → warning!
]
wave_num = 1

for l in level:
    print (f"Wave {wave_num} started")
    count = 0
    for w in l:
        if w > 50:
            count += 1    
    if count > 3:
       print('warning! overpowered wave')
    print('strong enemies: ',count)
    wave_num += 1

#=========================================================================================================================================================================================================================

# ✅ Exercise 7G — Frame Drift Monitor
# You are checking if frame times are becoming inconsistent.
# Given a list of frame render times in milliseconds, compare each frame to the previous one:
#	•	If the difference is greater than 10 ms, print "Frame spike detected at index X!"
#	•	If all frames are smooth, print "All frames smooth!"


frame_time_a = [50,45,60,65,50]

for i in range(1, len(frame_time_a)):        # range(1, len(...)): starts from second frame
    prev = frame_time_a[i-1]                # i - 1 is the previous frame
    curr = frame_time_a[i]
    diff = abs(curr - prev)                   # abs() ensures you catch spikes in either direction
    if diff > 10:
        print(f"Frame spike detected at index {i}!")
        break
else:
    print("All frames smooth!")


#=========================================================================================================================================================================================================================

# ✅ Exercise 7H — Retry Until Success
# You’re testing an in-game “data fetch” API that may return either "success" or "fail".
#	•	Loop through the results
#	•	As soon as you find a "success", print "Success on attempt X" and break
#	•	If you loop through all and never find "success", print "Test failed: No success found"


api_results = ["fail", "fail", "fail", "fail", "success","fail"]
attempt = 0

for a in api_results:
    attempt += 1
    if a == "success":
        print(f'success on attempt {attempt}')
        break
else:
    print('Test failed: No success found')    


#=========================================================================================================================================================================================================================

# ✅ Exercise 7I — Retry With Cooldown (Simulation)
# You’re testing a login system under load. The system allows 3 retries, but there must be a cooldown wait after each failed attempt.
#Your task:
#	•	Loop through login attempts
#	•	After each "fail":
#	•	Print: "Attempt X failed. Cooling down..."
#	•	After a "success":
#	•	Print: "Login succeeded on attempt X" and exit
#	•	After 3 "fail"s without success, print: "Account locked after 3 failed attempts"
# Rules:
#	•	You must stop checking after 3 total failures, even if there’s a "success" later
#	•	Do not use sleep/timers — just simulate the messages


login_attempts = ["fail", "fail", "fail", "success"]
attempt = 0
fail_count = 0
for a in login_attempts:
    attempt += 1
    if a == 'success':
        print(f'Login succeeded on attempt {attempt}')
        break
    elif a == 'fail':
        print(f"attempt {attempt} failed, cooling down...")
        fail_count += 1
        if fail_count == 3:
            print('Account locked after 3 failed attempts')
            break
   

#=========================================================================================================================================================================================================================

# 🕹️ Chapter 7J — Final Boss Exercise: Survival Mode Tracker
# You’re testing a game’s “Survival Mode.” Each level contains several waves. Each wave contains several enemies, and each enemy has an HP value.
# You are to:
#	1.	Print "Level X Started" for each level
#	2.	For each wave:
#	•	Print "  Wave Y Started"
#	•	Print all enemy HPs in that wave (just the numbers)
#	3.	If the level is completed (i.e., no failed wave), print "Level X Cleared!"
#	4.	Finally, print how many total waves were fully completed (i.e., didn’t fail)



levels = [
    [[100, 90, 80], [110, 0, 95], [100, 10, 98]],       # Level 1 – Wave 2 fails
    [[120, 130, 140], [100, 100, 100]],                  # Level 2 – Cleared
    [[150, 150, 0], [130, 120], [140, 150]],             # Level 3 – Wave 1 fails
    [[110, 115], [120, 110], [130, 120]]                 # Level 4 – Cleared
]
lvl_no = 0


for level_num in levels:
    lvl_no += 1
    wave_no = 1
    flag = False
    print('=========================')
    print(f'Level {lvl_no} started')
    
    for wave_num in level_num:
        print(f'wave {wave_no} started')
        print(wave_num)

        for enemy_hp in wave_num:
            if enemy_hp == 0:
                print(f'Wave {wave_no} Failed!')
                flag = True
                break
        if flag:
            break
        wave_no += 1



#=========================================================================================================================================================================================================================

ammo = 10

while ammo:
    ammo -= 1
    print('bullet fired, left:',ammo)
else:
    print("Out of ammo!")  
#----------------------------------------------------
import random
flag = True

while flag :
    hit = random.randint(1,10)
    if hit in (9,9,10):
        print('Hit Taken: ',hit)
        print('Critical Hit Landed!')
        break
    else:
        print('Hit Taken: ',hit)

#----------------------------------------------------
                
import random
import time
failcount = 1

while failcount <= 3:
    server = random.randint(1,10)
    if server in (8,9,10):
        print(f'Login Successfull on server {server}')
        break
    else:
        print(f'Login Failed on server {server}\nCooling Down...\n')
        failcount += 1
        time.sleep(2)
else:
    print('Account locked')   

#-----------------------------------------------------
# Wave Retry System
# Simulate 3 waves using a for loop.
#	•	Each wave can be retried up to 3 times using a while loop inside it.
#	•	Each attempt has a 50% success chance (use random.choice([True, False]))
#	•	On success: print "Wave X cleared on attempt Y" and move to next wave
#	•	On 3 consecutive failures: print "Wave X failed after 3 attempts", stop the level (break the outer loop)

import random
       
for waves in range(1,4):
    retry = 0
    attempt = 0
    while retry < 3:
        match_result = random.choice([True, False])
        attempt += 1
        if match_result:
            print(f'wave {waves} cleared on {attempt} attempt\n')
            break
        else:
            print(f'wave {waves} failed on {attempt} attempt')
            retry += 1
    else:
        print('All attempts exhausted for this wave\n')
        break
else:
    print(f'all waves cleared successfully')

#----------------------------------------------------

#   You have a list of enemies with their cooldown timers in seconds:
#   Loop through the list. For each:
#   If the cooldown is 0 or less, print:
#   "Enemy X is ready to attack!"
#   If the cooldown is positive, print:
#   "Enemy X cooling down for Ys..." and continue to the next enemy.
#   Print the index (1-based) of each enemy being checked

import time

cooldowns = [0, 3, -1, 5, 0, 2]

for x, y in enumerate(cooldowns, start=101):            # The enumerate() function, Instead of looping through just the values, you also get the index of each item.
    print(f'Enemy #{x}')                                # By default, enumerate starts from 0 (like most Python indexing), hence start = 101
    if y <= 0:
        print('Enemy is ready to attack!\n')
    else:
        print(f'Enemy is cooling down...for {y} seconds\n')
        time.sleep(y)
        continue

#----------------------------------------------------


            
        













