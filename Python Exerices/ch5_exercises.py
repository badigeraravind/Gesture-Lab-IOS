
# Exercise 5-A Critical-Hit Damage Function
# 	1.	Write a function calc_damage(base, crit_multiplier, is_crit) that
#	    •   takes an int base, a float crit_multiplier, and a bool is_crit;
#	    •   returns the damage as an int (rounded down).
#	    •   If is_crit is True, multiply base by crit_multiplier; otherwise use base.
#	2.	Prompt the tester for the three inputs, call the function once, and print only the returned value—single-line numeric output.

def calc_damage(base, crit_multiplier, is_crit):
    if is_crit == "1":
        base *= crit_multiplier
        return base                         # we can also convert to int here: return int(base) , instead of doing at line 13

base_value = int(input('Enter the base value: '))
critical_multiplier = float(input('Enter the value of critical hit multiplier: '))
is_critical = input('Is It Critical Hit? (1=yes/0=no): ')

damage = calc_damage (base_value, critical_multiplier, is_critical)

print(f"Your Final Damage Taken Is:{int(damage)}")

========================================================================================================================================================================================================================

# Exercise 5-B Area-of-Effect Hit Scan
# Write a function named get_targets_hit(center_x, radius) that returns a list of all enemies hit by an area-of-effect attack.
#	1.	Use this fixed list of enemy positions (don’t prompt for input): enemies = [(5, 3), (10, 0), (4, 4), (7, 6), (3, 2)]
#	2.	The center_x is an int (you can assume y = 0).
#	3.	The radius is a positive float — any enemy with a distance ≤ radius from (center_x, 0) should be returned.
#	4.	Use Euclidean distance: distance = sqrt((ex - center_x)² + (ey - 0)²)
#	5.	Return a list of tuples representing the enemies hit.
#	6.	At the bottom, call the function once using tester input for center_x and radius, and print the result.

from math import sqrt

enemies = [(5, 3), (10, 0), (4, 4), (7, 6), (3, 2)]

def get_targets_hit(center_x, radius):
    hit_enemies = []
    for ex, ey in enemies:
        distance = sqrt((ex - center_x) ** 2 + ey ** 2)     #Euclidean distance formula: distance = sqrt((ex - center_x)² + (ey - 0)²)
        if distance <= radius:
            hit_enemies.append((ex, ey))
    return hit_enemies

cx = int(input("Enter AoE center x: "))
r = float(input("Enter AoE radius: "))
print("Targets Hit List",get_targets_hit(cx, r))

=========================================================================================================================================================================================================================

# Exercise 5-C Friendly Fire Filter
# You already wrote get_targets_hit(center_x, radius) which returns all enemies in range.
#	1.	Add a second function called filter_enemies(hit_list, avoid_list)
#	    It takes:
#		    hit_list: list of coordinates (like [(5, 3), (4, 4)])
#		    It returns only those entries in hit_list not found in avoid_list.
#	2.	At the bottom of the file:
#		    Prompt the user to enter one friendly coordinate (e.g. 5 3)
#		    Call get_targets_hit() as before
#		    Then pass the result into filter_enemies() with the single friendly you got
#		    Print the final filtered hit list

from math import sqrt

enemies = [(5, 3), (10, 0), (4, 4), (7, 6), (3, 2)]
ally_x = int(input('Enter ally X coordinates : '))
ally_y = int(input('Enter ally Y coordinates : '))
allies = [(ally_x,ally_y)]

def get_targets_hit(center_x, radius):
    hit_enemies = []
    for ex, ey in enemies:
        distance = sqrt((ex - center_x) ** 2 + ey ** 2)     #Euclidean distance formula: distance = sqrt((ex - center_x)² + (ey - 0)²)
        if distance <= radius:
            hit_enemies.append((ex, ey))
    return hit_enemies

cx = int(input("Enter AoE center x: "))
r = float(input("Enter AoE radius: "))
print("Targets Hit List",get_targets_hit(cx, r))


def filter_enemies(hit_list, avoid_list):
    filtered = []
    for enemy in hit_list:
        if enemy not in avoid_list:
            filtered.append(enemy)
    return filtered

filtered_hit = filter_enemies(get_targets_hit(cx,r),allies)
print("Filtered Hit List",filtered_hit)

=========================================================================================================================================================================================================================

# Exercise 5-D Random Enemy Spawn Selector
# Write a function spawn_random_enemy(zone_list) that:
#	1.	Accepts a list of zone names as input (e.g., ["forest", "desert", "cave"])
#	2.	Returns a randomly selected zone name from the list
#	3.	Use Python’s random.choice() to pick one
#	4.	At the bottom of the script:
#	        Prompt the tester to enter 3 zone names (one at a time)
#	        Call the function and print the selected spawn zone

from random import choice

def spawn_random_enemy(zone_list):
    spawned_zone = choice(zone_list)
    return spawned_zone

zone1 = input("Enter the zone 1 name: ")
zone2 = input("Enter the zone 2 name: ")
zone3 = input("Enter the zone 3 name: ")
zones = [zone1,zone2,zone3]

print("Spawned Zone: ",spawn_random_enemy(zones))

=========================================================================================================================================================================================================================

# Exercise 5-E Ability Cooldown Function
# Write a function can_use_ability(last_used_time, cooldown, current_time) that:
# Takes 3 inputs:
#	•	last_used_time → integer (e.g., seconds since match start)
#	•	cooldown → integer (number of seconds the ability is locked)
#	•	current_time → integer (current time in match)
# Returns True if the ability can be used now, else False
# At the bottom:
#	•	Prompt for all 3 values
#	•	Call the function and print only "Ready" or "On Cooldown" depending on the result 

def can_use_ability(last_used_time, cooldown, current_time):
    if (current_time - last_used_time) > cooldown:                          # to avoid next 3 lines, we can directly use:  return (current_time - last_used_time) > cooldown
        return True
    else:
        return False

last_used_time = int(input('Enter the time the ability was last used: '))
cooldown = int(input('Enter the cooldown period of the ability: '))
current_time = int(input('Enter the current time of the match: '))

if can_use_ability(last_used_time, cooldown, current_time) == True:         # here, no need of  "==true" if we use above suggestion
    print("READY")
else:
    print("ON COOLDOWN")

=========================================================================================================================================================================================================================

# Exercise 5-F Time-to-Next-Use Calculator
# Write a function called time_to_ready(last_used, cooldown, now) that:
#	1.	Takes:
#	•	last_used: int (when the ability was last used)
#	•	cooldown: int (cooldown duration in seconds)
#	•	now: int (current time)
#	2.	If the ability is still cooling down, return the number of seconds remaining (i.e., last_used + cooldown - now)
#	3.	If it’s already ready, return 0
#	4.	At the bottom, prompt for all 3 inputs, call the function, and print:
#	•	"Ready now" if result is 0
#	•	"Wait Xs" if result is > 0

def time_to_ready(last_used, cooldown, now):
    if (now-last_used) > cooldown:
        return 0
    else:
        return cooldown - (now-last_used)
        

last_used = int(input('Enter the time the ability was last used: '))
cooldown = int(input('Enter the cooldown period of the ability: '))
now = int(input('Enter the current time of the match: '))

rem_time = time_to_ready(last_used, cooldown, now)

if rem_time == 0:
    print("READY")
else:
    print(f"WAIT for {rem_time}s")

=========================================================================================================================================================================================================================

# Exercise 5-G Dynamic XP-to-Level Function
# Write a function get_level(xp, xp_per_level) that:
#	1.	Takes:
#   	•	xp: an integer (total experience points earned by the player)
#   	•	xp_per_level: int (how much XP is needed to gain one level)
#	2.	Returns the current level as an integer (starting from level 1)
#	3.	At the bottom:
#   	•	Prompt the tester for both values
#   	•	Call the function and print "Current Level: X"

def get_level(xp, xp_per_level):
    return xp // xp_per_level + 1           
# adding "+1" means if user's total XP earned is less than target XP, so it returns lvl 1 instead of lvl 0, when Level 1 means “you started playing”, and not “you’ve completed one full level’s XP.

total_xp = int(input('Enter the total XP earned by the player so far: '))
xp_target = int(input('Enter the total XP required to unlock a level: '))

print(f"Your Current Level Is: {get_level(total_xp, xp_target)}")

=========================================================================================================================================================================================================================

# Exercise 5-H XP Remaining for Next Level
# Write a function xp_to_next_level(current_xp, xp_per_level) that:
#	1.	Takes:
#	    • 	current_xp: integer (total XP earned so far)
#	    •	xp_per_level: integer (XP needed to unlock each new level)
#	2.	Returns the XP needed to unlock the next level
#	3.	At the bottom:
#	    •	Prompt the user for XP values
#	    •	Print either: XP needed for next level: X or Level cap reached if player has hit a fixed max level (assume max XP = 100000 for this exercise)

def xp_to_next_level(current_xp, xp_per_level):
    rem_xp =  xp_per_level - (current_xp % xp_per_level)
    curr_lvl =  (current_xp // xp_per_level) + 1 
    next_lvl = (current_xp // xp_per_level) + 2     # 
    return rem_xp, curr_lvl, next_lvl

total_xp = int(input('Enter the total XP earned by the player so far: '))
xp_target = int(input('Enter the total XP required to unlock a level: '))

rem_xp, curr_lvl, next_lvl = xp_to_next_level(total_xp, xp_target)

if total_xp >= 10000:
    print("Level Cap Reached!")
else:
    print(f"Current Level:{curr_lvl} ====> {rem_xp} XP is required to unlock level {next_lvl}")

=========================================================================================================================================================================================================================

# Extra Exercise 5-I – Weapon Heat Tracker
# Create a function is_overheated(heat, max_heat) that:
#	1.	Takes:
#	    •	heat: a float representing the weapon’s current heat
#	    •	max_heat: the float threshold at which the weapon overheats
#	2.	Returns True if the weapon is overheated, else False
#   3.  At the bottom:
#	    •	Prompt for both values (heat and max_heat)
#	    •	Print:
#	    •	"Weapon safe to fire" otherwise

def  is_overheated(heat, max_heat):
    return heat > max_heat

heat = float(input('Enter the current heat of the weapon: '))
max_heat = float (input('Enter the threshold heat of the weapon: '))

if is_overheated(heat, max_heat):
    print("Weapon Overheated! Cooldown in progress...")
else:
    print("Weapon safe to fire")

=========================================================================================================================================================================================================================

# Extra Exercise 5-J – Score Milestone Notifier
# Create a function check_score_milestone(score, milestone) that:
#	1.	Takes:
#   	•	score: integer (current player score)
#   	•	milestone: integer (target milestone score, like 5000)
#	2.	Returns:
#   	•	"Milestone reached!" if the score is equal to or exceeds the milestone
#   	•	"Keep going..." otherwise
#   3.  At the bottom:
#	    •	Prompt the user for score and milestone
#	    •	Call the function and print its return value directly

def check_score_milestone(score, milestone):
    if score < milestone:
       return "Keep Going.."
    else:
        return "Milestone Reached"

score = int(input('Enter the player current score: '))
milestone = int(input('Enter the milestone target: '))

print(check_score_milestone(score, milestone))

=========================================================================================================================================================================================================================

# Extra Exercise 5-K – Combo Multiplier Calculator
# Write a function calc_combo_score(base_score, combo_count) that:
#   1.	Takes:
#   	•	base_score: int – the score for a single action
#   	•	combo_count: int – number of consecutive actions without a miss
#	2.	Returns the total score using this formula: total = base_score × (1 + 0.1 × (combo_count - 1)) (In other words, every combo after the first adds +10% bonus per action)
#   3.  At the bottom:
#	    •	Prompt the tester for base score and combo count
#	    •	Print: Total Combo Score: <rounded_score> (round the final value to nearest whole number)

def calc_combo_score(base_score, combo_count):
    return int(base_score * (1 + 0.1 * (combo_count - 1)))

base = int(input('Enter the base score: '))
combo = int(input('Enter the combo hits: '))

print(f"Your Total Score Is: {calc_combo_score(base,combo)}")

=========================================================================================================================================================================================================================



