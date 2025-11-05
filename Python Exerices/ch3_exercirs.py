
#Exercise 3-A  Damage Calculator

base_damage = int(input("enter base damage: "))
crit_multiplier = float(input('enter critical hit multiplier: '))
crit_hit = input('Is it critical hit? (y/n): ').strip().lower()

if (crit_hit in ("y","yes")):
    damage_taken = base_damage * crit_multiplier
    print(f"Damage Dealt: {damage_taken} || Its a Critical Hit")
else:
    damage_taken = base_damage
    print(f"Damage Dealt: {damage_taken} || Not a Critical Hit")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-B  Low-Health Warning
hp = 111
max_hp = 123
low_health_check = max_hp * 0.30

if hp <= (low_health_check):
    print(f"Low Health ({hp}/{max_hp})")
else:
    print(f"Normal Health ({hp}/{max_hp})")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-C  Auto-Clicker Loop (v1)

ammo = int(input('Enter Starting Ammo: '))
shots_fired = 0

while ammo > 0 and shots_fired < 30 :
    shots_fired += 1
    ammo -= 1
    print(f"Shot #{shots_fired}  ||  Remaining Ammo: {ammo} ")

if shots_fired >= 30 :
    print("Simulation stopped after firing 30 shots.")

elif ammo == 0 :
    print("Simulation stopped: out of ammo.")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-D  Complex Condition Check
in_main_menu   = False
button_visible = True
network_ok     = True

if not in_main_menu and button_visible and network_ok :
    print('Start Match')
else :
    print('Match Not Started')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-E Frame-Budget Checker

budget_ms = float(input('Enter the Time Budget Per Frame (in milliseconds): '))
elapsed_ms = float(input('Enter the actual work time your code took this frame (in milliseconds): '))

diff_ms = budget_ms - elapsed_ms

status = "⚠ OVER BUDGET" if diff_ms < 0 else "✓ OK"
print(f"Frame budget diff: {diff_ms:+.1f} ms  {status}")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-F Cooldown-Ready Checker
# Ask the tester for three numbers—when the ability was last used (secs since match start), the current match time (seconds), and the cooldown duration. 
# Calculate how many seconds remain before the ability becomes usable again
# print either the remaining time or a “ready now” message—single-line output only.

last_ability_used = int(input("when the ability was last used (in sec): "))
curr_match_time = int(input("what is the current match time (in sec): "))
cooldown_time = int(input("what is the cooldown duration (in sec): "))

elapsed = abs(curr_match_time - last_ability_used)        
# seconds since the ability was last used.  
# "abs" treats the difference the same whether the match timer counts up or down.

rem_cooldown_time = cooldown_time - elapsed          
# time still needed to finish cooldown

status = "Ready Now" if rem_cooldown_time <= 0 else "Remaining Time"

print(f"{status}: {max(rem_cooldown_time, 0)} s")
# "max" is used to avoid printing negative values.



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-G FPS Drop Indicator
# Prompt for the target frame-rate cap and the observed average FPS;
# compute the percentage drop from target to observed; output one line showing that percentage (one decimal place)
# append “CRITICAL” if the drop is ≥ 10 %, otherwise “OK”.

target_fps = float(input('Enter Target FPS: '))
avg_fps = float(input('Enter the Average FPS: '))

drop_pct = (target_fps - avg_fps) / target_fps * 100    # percentage drop
status = "CRITICAL" if drop_pct >= 10 else "OK"
print(f"FPS drop: {drop_pct:.1f}%  {status}")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-H Spawn-Wave Timer
# Prompt for the total seconds elapsed in the match and the fixed spawn interval in seconds; 
# calculate how many seconds remain until the next spawn wave and print that single number on one line—if a spawn should trigger right now, print 0.

elapsed_time = int(input('Enter the total time elapsed in the match (in sec): '))
spawn_time = int(input('Enter the fixed spawn interval (in sec): '))

diff_time = (-elapsed_time) % spawn_time # [OR] spawn_interval - (elapsed_time % spawn_interval)

print(f"Remaining Time: {diff_time}")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-I Hit-Accuracy Tracker
# Ask for total shots fired and total hits landed. 
# Compute the hit accuracy as a percentage with one decimal place. 
# Print the percentage followed by “POOR” if accuracy is below 25 %, “AVERAGE” if it’s 25 %–74.9 %, and “EXCELLENT” if it’s 75 % or higher—single-line output only.

total_shots_fired = int(input('Enter the total shots fired: '))
total_shots_landed = int(input('Enter the total shots landed on the target: '))

accuracy = (total_shots_landed / total_shots_fired) * 100

if accuracy < 25:
    print('POOR')
elif accuracy > 75:
    print('EXCELLENT')
else:
    print('AVERAGE')



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-J Memory-Spike Alert
# Prompt for the game’s permitted memory budget in MB and the current process memory in MB; 
# calculate the percentage above budget (0 % if at or under),
# then print the percentage with one decimal place followed by “ALERT” if the excess is ≥ 5 %, else “STABLE”—single-line output only.

budget_mb = float(input("enter game’s permitted memory budget (in MB): "))
curr_mb = float(input("enter current process memory (in MB): "))

diff_mb = max((curr_mb - budget_mb) / budget_mb * 100, 0) # percentage

status = 'ALERT' if diff_mb >= 5 else 'STABLE'

print(f"Memory Spiked: {diff_mb:.1f}%   |   {status}")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-K Animation-Frame Selector
# Prompt for the current global tick count and the total frame count of a looping animation; 
# compute which animation frame should display right now (use 0-based indexing) and print just that frame number on one line.

global_tick = int(input("Enter current global tick count: "))
frame_count = int(input("Enter total frames in the loop: "))

# 0‑based frame index for the current tick
frame_index = global_tick % frame_count
print(frame_index)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-L XP-to-Level Calculator
# Prompt for the player’s current total XP and the fixed XP-per-level value; 
# compute the current level (levels start at 1) and how much XP is still needed to reach the next level; print a single line in the form

player_curr_xp = int(input("Enter player's current XP: "))
fixed_xp_per_lvl = int(input("Enter the fixed XP target to unlock the levels: "))

diff_xp = fixed_xp_per_lvl - (player_curr_xp % fixed_xp_per_lvl)

curr_lvl = (player_curr_xp // fixed_xp_per_lvl) + 1     # This operator: // means 'floor' which is better than using / and then converting to int.
next_lvl = curr_lvl + 1

print(f"Level {curr_lvl}  ->  {diff_xp} XP is required to reach Level {next_lvl}")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-M Checkpoint Timer Alignment
# Prompt for the game’s global tick count and the checkpoint interval in ticks. 
# Print the number of ticks remaining until the next checkpoint; if the checkpoint should trigger now, print 0—single-line output only.

global_tick = int(input("Enter game's global tick count: "))
chk_pt_interval = int(input("Enter check point interval (in ticks): "))

diff_tick = chk_pt_interval - (global_tick % chk_pt_interval)   # OR diff_tick = (-global_tick) % chk_pt_interval

print(f"Remaining ticks to next checkpoint: {diff_tick}")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3-N Bit-Mask Feature Toggle
# The game stores four debug overlays in a single integer bit-mask (bit 0 = FPS, bit 1 = Hitboxes, bit 2 = AI Paths, bit 3 = Network Stats). 
# Prompt for the current bit-mask value and a toggle bit number (0-3); flip that bit using an operator.
# print the new mask value—single line, no extra text.



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-O Timer Blink Scheduler
# Ask for the match time remaining in seconds and the blink interval;
# print the timestamp (in seconds remaining) when the next timer blink should occur—single line only.


curr_match_time = int(input("Enter current remaining match time (in sec): "))
blink_interval = int(input("Enter the blink interval (in sec): "))

remainder = curr_match_time % blink_interval

next_blink = curr_match_time if remainder == 0 else curr_match_time - remainder

print(f"Next blink happens at {next_blink}th sec")



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-P Power-Up Decay Calculator
# Prompt for the power-up’s initial strength value, the decay rate per second (as a percentage), and the elapsed time in seconds. 
# Compute the current strength of the power-up (strength × (1 − rate/100)^time) and print that value with two decimal places—single-line output only.


powerup_strength = float(input("Enter the initial powerup strength: "))
decay_rate = float(input("Enter the drop rate for every second (in %): "))
elapsed_time = int(input("Enter the elapsed time (in sec): "))


fraction_left = max(0.0, (1 - (decay_rate / 100)) ** elapsed_time)

# decay_rate / 100  -> Converts the user-entered percentage (e.g., 5) into a per-second fraction (0.05)
# 1-                -> Gives the portion that survives each second. With a 5 % decay rate, 1 – 0.05 = 0.95 → 95 % of the power-up remains after the first second.
# ** elapsed_time   -> ** is Python’s exponentiation operator. Raising the per-second survival factor to the power of elapsed_time compounds the decay over multiple seconds:  (0.95)^{3}=0.8574 means ~85.74 % is left after 3 s.
# max(0.0, …)       -> Guards against extreme inputs (decay_rate ≥ 100 for a positive time) that could yield a tiny negative due to floating-point rounding. We clamp the minimum to 0.0 because negative strength makes no sense.


remaining_strength = fraction_left * powerup_strength

# powerup_strength -> The initial magnitude the user typed (e.g., 100).
# fraction_left    -> Computed in the previous line (e.g., 0.8574).
# Multiplication   -> Gives the actual strength still active after the elapsed time:100 \times 0.8574 = 85.74.

print(f"Remaining {remaining_strength:.1f} strength is left from the powerup!")




#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-Q Latency Jitter Checker
# Prompt for three recent ping values (milliseconds), compute the absolute difference between the highest and lowest, and print that jitter value—single line only.

pings = [int(input("Last 3 pings: ping #1: ")),int(input("Last 3 pings: ping #2: ")),int(input("Last 3 pings: ping #3: "))]
jitter = abs(min(pings)-max(pings))
print(jitter)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-R Ammo-Clip Reload Counter
# Prompt for total rounds fired and the magazine size; print the number of full reloads that must have happened—single numeric output only.

bullets_fired = int(input("Enter the total bullets fired: "))
magazine_size = int(input("Enter the magazine size: "))

reloads = max(0,(bullets_fired - 1)) // magazine_size

print(reloads)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercise 3-S Frame-Drop Spike Detector
# Prompt for a sequence of five consecutive FPS readings. Count how many times an FPS value is at least 10 frames lower than the value immediately before it, and print that count—single numeric output only.

fps_values = [
    int(input("fps1: ")),
    int(input("fps2: ")),
    int(input("fps3: ")),
    int(input("fps4: ")),
    int(input("fps5: ")),
]

fps_drop_count = 0

# Count a spike whenever the current value is ≥ 10 FPS lower than the previous one
for prev, curr in zip(fps_values, fps_values[1:]):
    if prev - curr >= 10:
        fps_drop_count += 1

# The expression list[start:stop] returns a new list containing the items from index start up to but not including stop.
# Omitting stop means “go all the way to the end.”
# So 1: means “give me everything from index 1 onward”—i.e., the list without the very first element.
# We want to compare each reading to the one immediately after it. Having a “shifted” version of the list lets us line items up side-by-side:
# zip() – pairing two sequences item-by-item
	#•	zip(seq1, seq2) walks through both sequences together, yielding tuples (seq1[i], seq2[i]).
	#•	In the for prev, curr in ... loop, those tuples are unpacked directly into prev and curr variables.
	#•	fps_values gives the previous reading each loop.
	#•	fps_values[1:] gives the current reading (one step ahead).
	#•	zip pairs them (prev, curr).

# Single‑line numeric output
print(fps_drop_count)


#or
#fps_drop_count = 0
#for i in range(1, len(fps_values)):
#  prev = fps_values[i - 1]
#  curr = fps_values[i]
#  if prev - curr >= 10:
#       fps_drop_count += 1