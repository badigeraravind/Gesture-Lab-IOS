

# Exercise 8A: Basic Damage Calculator Function
#	Define a function called calculate_damage
#	•	It should accept two arguments:
#	•	base_damage (int or float)
#	•	multiplier (float, e.g., 1.0, 1.5, 2.0)
#	•	It should return the total damage as base_damage * multiplier
#	•	Outside the function, call it 2–3 times with different values and print the result.

def calc_damage(base: int, multiplier: int) -> int:
    result = base * multiplier
    damage = round(result, 2)   #roundoff the decimal value to 2 digits      
    return damage
    
print(calc_damage(3,2.5))
print(calc_damage(5.5,4.8))
print(calc_damage(199.23,6.96))

#========================================================================================================================================================================================================================

# Exercise 8B: Critical Hit Damage Function
# Define a function apply_crit_damage(base_damage: float, is_critical: bool) -> float
#	•	If is_critical is True, apply a 1.5× multiplier to base_damage
#	•	Otherwise, return base_damage as-is
#	•	Use round(..., 2) to keep the result clean
#	•	Test the function with both True and False cases and print the results

def apply_crit_damage(base_damage: float, is_critical: bool) -> float:
    if is_critical:
        result = round((base_damage * 1.5),2)
        return result
    else:
        return base_damage
    
# or the above 5 lines can be shorted to 2 lines as follows:
# multiplier = 1.5 if is_critical else 1.0
# return round((base_damage * multiplier),2)

print("True Scenario: ",apply_crit_damage(12.3,True))

print("False Scenario: ",apply_crit_damage(12.3,False))

#========================================================================================================================================================================================================================

# Exercise 8C: Damage with Weapon Modifier
# Create a function weapon_damage(base: float, modifier: float = 1.0) -> float:
# It should return:
# base_damage * weapon_modifier, rounded to 2 decimals
#	•	The weapon_modifier is optional — if not passed, it should default to 1.0
#	•	Test with:
#	•	Default weapon (no modifier)
#	•	A weapon with 1.25 modifier
#	•	A weapon with 0.75 modifier (weaker weapon)

def weapon_damage(base: float, modifier: float = 1.0) -> float:
    damage = round((base * modifier),2)
    return damage

print('Default Weapon: ',weapon_damage(12.3))

print('Modifier 1 Weapon: ',weapon_damage(12.3, 1.25))

print(f'Modifier 2 Weapon: {weapon_damage(12.3, 0.75)}')


#========================================================================================================================================================================================================================

# Exercise 8D: Critical Weapon Damage Combo
# Apply both:
#	•	Weapon modifier (multiply with base)
#	•	If is_critical is True, apply 1.5× to the result
#	•	Round the final output to 2 decimal places
#	•	Print test cases for:
#	1.	Default weapon, no crit
#	2.	Custom modifier, no crit
#	3.	Default weapon, critical
#	4.	Modifier + critical

def combo_calc(base, modifier = 1.0, is_critical = False):
    multiplier = 1.5 if is_critical else 1.0
    result = round((base * modifier * multiplier),2)
    return result
    
print("Default Weapon, No Crit: ",combo_calc(34.5))

print("Custom Modifier, No Crit: ",combo_calc(34.5, 2.3))

print("Default Weapon, Crit: ",combo_calc(34.5, is_critical = True))

print("Custom Modifier, Crit: ",combo_calc(34.5, 3.4, True))

#========================================================================================================================================================================================================================

# Exercise 8E: Health Threshold Alert System
# Define a function:
# If current HP is less than or equal to danger_threshold × max_hp, return: 'critical health', Otherwise, return: 'stable health'
# The danger_threshold is optional (default is 0.25, i.e., 25%)
#	•	Call the function with at least:
#	1.	Normal health
#	2.	HP at danger threshold
#	3.	HP below danger threshold


def check_health_status(current_hp, max_hp, danger_threshold = 0.25): 
    return (
        f"⚠️ Critical health! HP is below {danger_threshold * 100}%" 
        if current_hp <= (danger_threshold * max_hp) 
        else "HP is stable."
    )

# simpler code:
# if current_hp <= (danger_threshold * max_hp):
#        return f"⚠️ Critical health! HP is below {danger_threshold * 100}%"
#    else:
#        return "HP is stable."


print("Normal Health: ",check_health_status(40,100))

print(f"HP at Danger Threshold: {check_health_status(15,100,0.15)}")

print(f"HP below Danger Threshold: {check_health_status(30, 100, 0.45)}")


#========================================================================================================================================================================================================================

# Exercise 8F: XP Bar Function
# Define a function:
# The function should:
#	•	Calculate how full the XP bar is: fill_percent = (current_xp / xp_to_next_level) * 100
#	•	Return the percentage rounded to 2 decimal places
#	•	Test with:
#	1.	Halfway to next level (e.g. 50 / 100 → 50.0%)
#	2.	Just before leveling up (e.g. 99 / 100 → 99.0%)
#	3.	Overfilled XP (e.g. 120 / 100 → 120.0%)

def xp_bar_fill(current_xp, xp_to_next_level):
    return round(((current_xp / xp_to_next_level) * 100),2)

print('Halfway to next level: ',xp_bar_fill(50,150))

print('Just before levelling up: ',xp_bar_fill(99,150))

print('Overfilled XP: ',xp_bar_fill(170,150))


#========================================================================================================================================================================================================================

# Exercise 8G: Dynamic XP-to-Level Threshold Checker
# You need to build a check that tells you whether a player has enough XP to level up from their current level. This logic helps you write automated tests to validate:
#	•	Did the player earn enough XP to unlock the next level?
#	•	Or do they still need to grind more?

def levelup_calc(current_xp, xp_for_next_level):
    return (xp_for_next_level - current_xp) if current_xp < xp_for_next_level else 'Level should already be unlocked'
    
print(f'{levelup_calc(100,120)} XP is required to unlock next level')

print(levelup_calc(150,130))


#========================================================================================================================================================================================================================


        
    