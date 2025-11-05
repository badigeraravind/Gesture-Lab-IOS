
# Exercise 4‑A  Auto‑Screenshot Timer
# 	1.	Prompt for a start time (seconds_remaining) and an interval in seconds.
#	2.	Use a while loop that counts down by 1 s each iteration:
#	•	When the remaining time is a multiple of the interval, print SNAP  <t> , where <t> is the current seconds remaining, 
#   .   Stop when the timer hits 0.

seconds_remaining = int(input("Enter remaining seconds: "))
snap_interval     = int(input("Enter the snap interval (in sec): "))

while seconds_remaining > 0:
    if seconds_remaining % snap_interval == 0:
        print(f"SNAP {seconds_remaining}")
    seconds_remaining -= 1

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4‑B  Timed Health Potion Loop
# Start with an initial HP value and a potion heal amount. Use a while loop that heals the player once every 5 seconds until HP reaches or exceeds 100. 
# After each heal, print one line showing the new HP and the time stamp (seconds elapsed). End the loop when HP ≥ 100.

initial_hp     = 13
potion_heal    = 10
heal_interval  = 5        # seconds between heals
elapsed_time   = 0        # seconds elapsed since start

while initial_hp < 100:
    elapsed_time += heal_interval            # wait for the next heal tick
    initial_hp   += potion_heal              # apply the heal

    # Cap HP at 100 so we don't print 103, 112, etc.
    if initial_hp > 100:
        initial_hp = 100

    print(f"new HP: {initial_hp}  ||  Elapsed Time: {elapsed_time}")



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-C Enemy Patrol Scanner
# Prompt for a patrol route length in waypoints and a waypoint index where an enemy is spotted; 
# use a for loop that steps through the route from 0 upward, printing each waypoint number visited, but terminate the loop immediately with break once the enemy’s waypoint is reached.

patrol_route = int(input('Enter total length of waypoints: '))
enemy_waypoint = int(input('Enter the waypoint index: '))

for waypoint in range(patrol_route):
    if enemy_waypoint == waypoint:
        print(f'Enemy Spotted in waypoint: {waypoint}')
        break
    else:
        print(f'no enemy in waypoint: {waypoint}')



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-D Early-Exit Screenshot Loop
# Start a for loop that iterates 1 … 30 (inclusive) to represent frames. On each frame, prompt for a Boolean “glitch detected?” input (1 / 0). 
# If a glitch is reported, print "GLITCH at frame <n>" and break; otherwise, continue until the loop finishes. If no glitch occurs, print "All clear" after the loop ends.

total_frames = 5

for a in range(1, total_frames + 1):
    is_glitching = int(input(f"Frame {a} – glitch? (1/0): "))
    if is_glitching == 1:
        print(f"GLITCH at frame {a}")
        break
else:
    print("All clear")



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-E Timed Bomb Defusal Loop
# Begin with a countdown timer value and a defusal code input interval (in seconds). Use a while loop that decrements the timer by 1 s each pass; 
# every time the remaining seconds are a multiple of the interval, prompt the tester for a “code entered?” flag (1 / 0). 
# If the correct code is entered, print "DEFUSED at <t>s" and break; if the timer reaches 0 first, print "BOOM" and exit.

countdown_time = 13
defusal_code_interval = 5

while countdown_time:
    print(countdown_time)
    if countdown_time % defusal_code_interval == 0 :
        prompt = int (input ('code entered? (1/0): '))
        if prompt == 1:
            print(f'DEFUSED !! @ {countdown_time}s')
            break
    countdown_time -= 1
if countdown_time == 0:
    print('BOOM !!')



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-F Even-Frame Processor
# Start a for loop over frames 1 through 20. If a frame number is odd, use continue to skip all work for that frame; otherwise print Processing frame <n>.

frames = 20
for a in range(1, frames + 1):
    if a % 2 != 0:
        continue
    print(f"Processing Frame @ {a}")



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-G  Nested Wave Scanner
# Create a nested loop: the outer for cycles through levels 1 → 5, the inner for cycles through waves 1 → 3 for each level. 
# Print "Level <L>, Wave <W>" for every wave except wave 2 on level 3 (skip it with continue). 
# If the loop reaches wave 3 on level 5, print "Termination at Level 5, Wave 3" and use break to exit both loops immediately—no further output.

terminated = False

for level in range(1, 6):          # Levels 1 → 5
    for wave in range(1, 4):       # Waves 1 → 3
        if level == 3 and wave == 2:
            continue                           # skip Wave 2 on Level 3
        if level == 5 and wave == 3:
            print(f"Termination at Level {level}, Wave {wave}")
            terminated = True
            break                              # exit inner loop
        print(f"Level {level}, Wave {wave}")
    if terminated:
        break                                  # exit outer loop once flagged

    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-H Score Milestone Notifier
# Prompt for a starting score and a score-increment value. Use a while loop that keeps adding the increment to the score until it exceeds or equals 10 000. 
# Each time the score becomes a multiple of 2 500, print "Milestone <score>". When the loop finishes, print "Goal reached at <score>" on one line.

start_score = 1000
score_multiplier = 500


while start_score < 10000:
    start_score += score_multiplier           # add points

    if start_score % 2500 == 0:               # milestone reached?
        print(f"Milestone {start_score}")

print(f"Goal reached at {start_score}")



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-I Rolling Average FPS Monitor
# Prompt for six consecutive FPS readings. Starting with the third reading, print the average of the current reading and the two previous readings (a three-frame rolling average) on one line. 
# Continue doing this for each new input until all six readings are processed. Single-line numeric output for each average—no extra text.

fps =   [int(input("FPS 1 : ")),
        int(input("FPS 2 : ")),
        int(input("FPS 3 : ")),
        int(input("FPS 4 : ")),
        int(input("FPS 5 : ")),
        int(input("FPS 6 : "))]


for prev_1, prev, curr in zip(fps, fps[1:], fps[2:]):
    avg = (prev_1 + prev + curr) / 3
    print(f"avg of {prev_1} - {prev} - {curr} ==  {avg:.1f}")




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
# Exercise 4-J Server-Retry Loop
# Ask for a maximum retry count N. Use a while loop that attempts to “connect” once per iteration (simulate with input(1 = success / 0 = fail)). 
# If a connection succeeds, print "Connected on attempt <k>" and break; if all N attempts fail, print "Connection failed after <N> attempts" after the loop ends—single-line output either way.

max_retry = int(input('what is the max retry count: '))
attempt = 1

while attempt <= max_retry:
    is_connection_success = int(input(f"Attempt {attempt}: Is it connected? (1=success / 0=fail): "))
    if is_connection_success == 1:
        print(f"Connected on attempt {attempt}")
        break
    attempt += 1
else:
    # executes only if loop exhausted without break
    print(f"Connection failed after {max_retry} attempts")



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
# Exercise 4-K Input-Lag Watchdog
# Start a while True loop that asks the tester for a frame number and its measured input-lag in milliseconds. 
# If lag exceeds 100 ms, print "LAG spike at frame <n>" and break; if the tester enters -1 for the frame number, print "Session complete — no spikes" and break. 
# Otherwise the loop continues, accepting more frame/lag pairs.

while True:
    frame_num = int(input('enter frame number:'))
    if frame_num == -1 :
        print(f"Session complete — no spikes")
        break
    input_lag = float(input('enter input lag (in ms): '))
    if input_lag > 100 :
        print(f"LAG spike at frame {frame_num}")
        break
    
# frame_num, lag = map(float, input("Frame and lag (e.g., 123 , 87.5): ").split(","))
# .split()  >>> Splits the string on whitespace by default, giving a list ["123", "87.5"].
# map(float, …) >>> Assigns the first converted value to frame_num and the second to lag.     



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-L Menu-Driven Command Loop
# Write an infinite while True loop that shows this mini-menu each cycle:
# 	•	Keep two variables in memory: score (starts at 0) and hp (starts at 100).
#	•	When the tester enters 1, prompt for the amount to add and increase score.
#	•	When they enter 2, prompt for damage amount and subtract it from hp (but not below 0).
# 	•	When they enter 3, print Score: <s>  |  HP: <h>.
#	•	When they enter 0, break the loop and print "Session ended"—single-line output.
# No other menu options are allowed; any unrecognised input should simply re-display the menu and wait for the next choice.

score = 0
hp = 100
while True : 
    print(f"\n0 – Quit\n1 – Add score\n2 – Take damage\n3 – Show status")
    menu = int(input("What's your choice? - "))
    if menu == 0:
        print (f"Session Ended")
        break
    if menu == 1:
        add_score = int(input('Enter the value to be added to score: '))
        score += add_score
    if menu == 2:
        del_score = int(input('Enter the value to be removed from hp: '))
        hp = max(0, hp - del_score)
    if menu == 3:
        print(f"Score: {score}  ||  HP: {hp}")




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-M Random-Loot Drop Loop
# Keep looping until the tester enters a loot rarity value of 5 (legendary). Each iteration prompts for the rarity pulled (1–5) and increments a counter. 
# When rarity 5 appears, print "Legendary after <n> pulls" and stop.

pull_counter = 0

while True:
    rarity_pulled = int(input('enter the rarity type pulled (1-5):'))
    pull_counter += 1
    if rarity_pulled == 5:
        print(f"Legendary after {pull_counter} pulls")
        break



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Exercise 4-N HP + Score Fail-Safe Loop
# Start an infinite while True loop that prompts for damage taken and score gained each tick. Subtract the damage from hp and add the score to score.
# 	•	If hp falls to 0 or below, print "PLAYER DOWN at score <s>" and break.
# 	•	If score reaches or exceeds 20 000, print "VICTORY with hp <h>" and break.
#	•	Otherwise continue looping.

hp = 100
score = 100

while True:
    damage = int(input('enter the damage taken: '))
    gained = int(input('enter the score gained: '))
    hp = max(0, hp-damage)
    score += gained 
    if hp <= 0:
        print(f">>> player down at score {score} <<<")
        break
    if score >= 20000:
        print(f">>> victory with hp {hp} <<<")
        break



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Exercise 4-O Checkpoint-Retry Timer
# Start a countdown at 120 seconds. Every 15 seconds, attempt a “checkpoint save” (simulate with 1 = success, 0 = fail). 
# If a save succeeds, print Saved at <t>s and stop. If the timer reaches 0 without a successful save, print Abort after 120 s.

countdown = 120
chkpt_interval = 15
while countdown > 0:
    if countdown % chkpt_interval == 0:
        attempt = int(input(f"timer:{countdown} ::: attempting checkpoint save (1 = success, 0 = fail): "))
        if attempt == 1:
            print(f"checkpoint saved at {countdown}s")
            break
    countdown -= 1
    if countdown <= 0:
        print(f"Abort after 120s")
    
        

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-P Damage-Over-Time (DoT) Tracker
# Prompt for an initial HP value and a per-second DoT amount. Use a while loop that subtracts the DoT each second. 
# Every 4 seconds, print "Tick <t>s – HP <h>". Stop the loop and print "KO after <t>s" the moment HP falls to 0 or below.

initial_hp = int(input("whats the initial hp: "))
dot = int(input("whats the damage over time (in sec): "))
timer = 0
while True:
    timer += 1
    initial_hp = max(0, initial_hp-dot)
    if timer % 4 == 0:
        print(f"Tick {timer}s - HP {initial_hp}")
    
    if initial_hp <= 0:
        print(f"Knock Out after {timer}s")
        break



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-Q Shield-Recharge Cool-down
# Start with shield = 0 and a cooldown = 8 s. Use a for loop that simulates 40 seconds, one second per iteration. 
# Each second, prompt for incoming damage. If no damage occurs (enter 0) for the entire cooldown span, set shield = 100 and print Shield recharged at <t>s, then break. 
# If any damage arrives before the cooldown completes, the cooldown timer resets. If the loop ends without a full recharge, print Shield never recharged—single-line output.

shield = 0
COOLDOWN = 8                 # seconds of no damage required
cooldown_remaining = COOLDOWN

for tick in range(1, 41):    # simulate 40 seconds, tick = elapsed seconds
    dmg = int(input(f"Second {tick} – incoming damage (0 for none): "))

    if dmg > 0:
        cooldown_remaining = COOLDOWN      # reset the cooldown
        print("Cooldown reset")
    else:
        cooldown_remaining -= 1            # count a damage‑free second
        if cooldown_remaining == 0:
            shield = 100
            print(f"Shield recharged at {tick}s")
            break
else:
    # loop finished without achieving a full recharge window
    print("Shield never recharged")



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-R Multi-Stage Retry Pipeline
# Implement two nested loops: the outer loop represents levels 1 → 4, the inner loop represents up to 3 retries for each level. Prompt for a “stage success?” flag (1 = success, 0 = fail) on each retry.
#	•	If a retry succeeds, print "Level <L> passed on retry <R>" and proceed to the next level.
#	•	If all three retries for a level fail, print "Abort at Level <L>" and stop the whole script immediately.
#	•	If every level passes within its retries, print "Pipeline complete" after the outer loop ends.

for level in range (1,5):
    for retry in range(1,4):
        prompt = int(input(f"Level {level} :: Retry {retry} ::: stage success? (1=success, 0=fail): "))
        if prompt == 1:
            print(f"Lvl {level} passed on retry {retry}")
            break
    else:                                           # inner loop exhausted → all 3 retries failed
        print(f'abort at level {level}')
        break                                       # break outer loop
else:                                               # outer loop finished - no aborts
    print(f"pipeline complete")


        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 4-S Dynamic Respawn Countdown
# Begin with a respawn timer set to 30 seconds. Every second, prompt for a “team-mate revived?” flag (1 = yes, 0 = no).
#	•	If a revive happens, cut the remaining timer in half (rounded down) and continue counting.
# 	•	Print Respawn in <t>s on each tick.
#	•	When the timer reaches 0, print Player respawned and stop.

respawn_timer = 30

while respawn_timer > 0:
    print(f"Respawn in {respawn_timer}s")
    is_revived = int(input(f'Is Teammate Revived? (1=success / 0=fail):'))
    respawn_timer -= 1
    if is_revived == 1:
        respawn_timer = respawn_timer // 2
else:
    print('player respawned')



