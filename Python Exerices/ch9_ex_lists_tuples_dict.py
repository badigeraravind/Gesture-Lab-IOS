
# Exercise 9A: Damage Tracker per Wave
# You’re testing a wave-based game where enemies spawn in multiple waves. You want to track how much damage the player deals in each wave and calculate the total damage at the end.
# 1.	Create a list to store damage values per wave
#	2.	Ask the user how many waves were played
#	3.	Use a for loop to:
#     Prompt the user for the damage dealt in each wave
#		  Store each damage value in the list
#	4.	After all waves:
#	   	Print the damage list
#	    Print the total damage dealt across all waves

def damage_tracker():
    damage = []
    waves = int(input('How many waves were played:'))
    
    for a in range(1, waves+1) :
        print(f'Wave #{a}')
        dmg = int(input('Enter the damage dealt by the player in this wave: '))
        damage.append(dmg)
    
    return damage

print('List of Damage taken by the player across all waves:',damage_tracker())


#=======================================================================================================================================================================================================================

# Exercise 9B: Position Tracker using Tuples
# You’re testing a 2D game where a player moves across a map. You want to track the player’s (x, y) position after every move and store those positions in a list.
# Ask the user how many moves the player made.
# For each move:
#	•	Ask for the new x and y positions
#	•	Store them as a tuple like (x, y)
#	•	Append the tuple to a list of positions
# At the end: Print all stored positions like: [(0, 0), (1, 2), (2, 2)]


def position_tracker():
    pos = []
    moves = int(input('Enter how many moves the player made: '))

    for a in range(1, moves+1):
        print(f'Move #{a}')
        coords = (float(input('Enter X coordinate: ')),float(input('Enter Y coordinate: ')))
        pos.append(coords)
    return pos

print('Positions list: ',position_tracker())


#=======================================================================================================================================================================================================================

# Exercise 9C: Scoreboard Tracker using Dictionary
# You’re testing a multiplayer match where each player earns a score. Your job is to build a scoreboard that maps each player’s name to their score using a dictionary.
# Ask how many players participated.
# For each player:
#	•	Ask for their name (string)
#	•	Ask for their score (integer)
#	•	Store the entry as {"player_name": score}
# After all inputs, Print the full scoreboard dictionary


def scoreboard():
    players = int(input('How many players participated: '))
    sb = {}
    for a in range(1, players + 1):
        print(f'Player #{a}')
        player_name = str(input('Enter player name: '))
        player_score = int(input('Enter player score: '))
        sb[player_name] = player_score
    return sb

print('Leaderboard Dictionary: ', scoreboard())


#=======================================================================================================================================================================================================================

# Exercise 9D: Top Scorer Finder (Dictionary + Loop)
# You’re testing the final match leaderboard and want to identify which player scored the highest using the scoreboard dictionary you already built.
# Reuse or re-ask the player names and scores.
# Loop through the dictionary to: Track the player with the highest score
# At the end: Print the name and score of the top scorer

def scoreboard():
    players = int(input('How many players participated: '))
    sb = {}
    for a in range(1, players + 1):
        print(f'Player #{a}')
        player_name = str(input('Enter player name: '))
        player_score = int(input('Enter player score: '))
        sb[player_name] = player_score
    return sb

def scoreboard_topper(sb):
    topper =  max (sb, key=sb.get)
    return topper, sb[topper]

sb_data = scoreboard()
print('Leaderboard Dictionary: ', sb_data)
print('Leaderboard Topper: ',scoreboard_topper(sb_data))

#=======================================================================================================================================================================================================================

# Exercise 9E: Score Brackets Using Dictionary Lookup
# You’re validating how players are categorized into score brackets (e.g., Bronze, Silver, Gold) based on their final match score. These brackets are mapped using a dictionary.
#	1.	Define a dictionary.
#	2.	Ask the user to enter a score.
#	3.	Loop through the dictionary to figure out which bracket the score falls into.
#	4.	Print something like: "Your rank is: Silver"

brackets = {
    "Bronze": range(0, 1000),
    "Silver": range(1000, 2000),
    "Gold": range(2000, 3000),
    "Platinum": range(3000, 5000)
}

score = int(input("enter user's score: "))

for a, b in brackets.items():
    if score in b:
        print('your rank is: ',a)
        break
else:
    print('Score does not match any defined bracket.')


#=======================================================================================================================================================================================================================

# 🧪 Exercise 9F: Player Loadout Tracker (Using Dictionary of Lists)
# You’re testing a shooter game where each player can equip multiple items (like weapons, grenades, perks, etc.). You need to track what each player has equipped — and verify that it matches the backend configuration.
# Ask how many players participated.
#	2.	For each player:
#   	•	Ask for the player’s name
#   	•	Ask how many loadout items they have equipped
#   	•	Then, in a loop, collect each item name into a list
#	3.	Store it in a dictionary
#	4.	After collecting all player data, print the final loadout dictionary.


users = int(input('how many users participated: '))
inventory_dict = {}

for a in range(1, users + 1):
    user_bag = []
    print(f'\nuser #{a}')
    name = str(input('whats the player name: '))
    items = int(input('how many loadout items this user carry: '))
    for b in range(1, items + 1):
        user_bag.append(str(input(f'Item #{b}: ')))
    inventory_dict[name] = user_bag                     #assign after bag is ready

print(inventory_dict)


#=======================================================================================================================================================================================================================

# Exercise 9G: Reverse Lookup – Who Has This Item?
# Imagine you’re testing a “Search by Equipment” feature in the game. Given a specific item name (like “Sniper” or “Armor”), you need to identify all players who have that item equipped.
# Reuse the inventory_dict from the last exercise (player → list of items) and use functions concept.
#	2.	Ask the tester (you) to input an item name to search.
#	3.	Loop through the dictionary:
#	•	If the item exists in that player’s loadout, add their name to a results list.
#	4.	After the loop, print the names of players who have that item.
#   5.  If no one has it, print "No players found with that item."

def loadout_logic():
    users = int(input('how many users participated: '))
    loadout_dict = {}

    for a in range(1, users + 1):
        print(f'\nuser #{a}')
        user_bag = []
        name = str(input('player name: '))
        items = int(input('how many loadout items does this user has: '))
        for b in range(1, items + 1):
            user_bag.append(str(input(f'item #{b}: ')))
        loadout_dict[name] = user_bag
    
    return loadout_dict

def find_item(Dictionary):
    find = str(input('\nwhich item to be searched: '))
    found = []
    for name, items in Dictionary.items():
        if find in items:
            found.append(name)
    if not found:
        return f'No players in the dictionary has your item "{find}"'
    return found


Dictionary = loadout_logic()
print(f'Current Loadout Dictionary: ',Dictionary)

Found_Item = find_item(Dictionary)
print(Found_Item)


#=======================================================================================================================================================================================================================

# Exercise 9H: Weapon Usage Frequency (Dictionary + Count)
# You’re testing weapon balancing in a game. After a play session, you’re given a list of weapon names used by the player during the match. Your task is to count how many times each weapon was used.
# Ask the tester how many weapons were used in total.
#	2.	In a loop:
#	•	Ask for each weapon name (e.g., "Sniper", "Pistol", "Grenade")
#	•	Store and count how many times each weapon appears using a dictionary.
#	3.	After the loop:
#	•	Print the final dictionary showing weapon names and their usage counts.


# Step 1: Ask for total number of weapons used
weapon_count = int(input("How many weapons were used in the match? "))

# Step 2: Dictionary to store weapon usage
usage = {}

# Step 3: Loop through weapon entries
for i in range(1, weapon_count + 1):
    weapon = input(f"Weapon #{i}: ")

    # Step 4: Count occurrences
    if weapon in usage:
        usage[weapon] += 1
    else:
        usage[weapon] = 1

# Step 5: Print result
print("\nWeapon Usage Summary:")
for weapon, count in usage.items():
    print(f"{weapon}: {count} times")


#=======================================================================================================================================================================================================================

# Exercise 9I: Tuple-Based Spawn Points
# You’re testing spawn locations for NPCs in a battle royale game. The level designer has given you fixed (x, y) spawn coordinates, and you need to test their placement order and usage.
# Create a list of tuples, where each tuple represents an NPC’s spawn point:
# Ask the tester how many spawn points to input.
# Let them enter each coordinate.
# After collecting all points:
#	•	Print each coordinate and its spawn index (1-based)
#	•	Print the first and last spawn locations separately
#	•	Print all unique spawn locations used    

spawn_count = int(input('enter how many spawn points: '))

NPC_spawn_pos = []

for a in range(1, spawn_count + 1):
    print(f'Enter the coordinates of spawn count {a}: ')
    xy_pos = (float(input('enter x value: ')), float(input('enter y value: ')))
    NPC_spawn_pos.append(xy_pos)

print('All NPCs Spawn Positions: ',NPC_spawn_pos)

print('First NPC position: ',NPC_spawn_pos[0])

print('Last NPC Position: ',NPC_spawn_pos[-1])

unique_pos =set()
for b in NPC_spawn_pos:
    if b not in unique_pos:
        unique_pos.add(b)
        
print('Unique NPC Position: ', unique_pos)


#=======================================================================================================================================================================================================================

# Exercise 9J: Merge Two Leaderboards (Dictionaries)
# Sometimes a game merges results from two matches or two servers into one leaderboard. You need to combine two dictionaries of player scores.
#	•	If a player exists in both leaderboards, their scores should be added together.
#	•	If a player exists in only one leaderboard, keep their score as is.
# Define two dictionaries
# Merge them into a final dictionary

match1 = {"Alice": 1200, "Bob": 1500, "Eve": 1000}
match2 = {"Bob": 1700, "Charlie": 900, "Alice": 800}

final = {}

for name, score in match1.items() :
    if name in match2:
        final[name] = score + match2[name]
    else:
        final[name] = score

for name, score in match2.items() :
    if name not in final:
        final[name] = score

print('Final Leaderboard: ',final)


#=======================================================================================================================================================================================================================


