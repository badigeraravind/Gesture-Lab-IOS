
# 🧪 Exercise 10A: Player Name Validation
# In many games, player names must be valid (no numbers, not empty, no spaces). You need to write a function that checks if a player name is valid.
#	1.	Ask the player to enter their name.
#	2.	Use string methods to validate: Only alphabets allowed, Minimum length = 3, Maximum length = 12
# Print either: "Valid player name!" Or an error message explaining why it’s invalid.

name = str(input('enter player name: '))

if name.isalpha() and 3 < len(name) < 12 :
    print("Valid Player Name!")
elif not name.isalpha():
    print("INVALID ::: Only Alphabets Allowed, no Alphanumeric")
elif not 3 <= len(name) <= 12:
    print('INVALID ::: Name should be between 3 and 12')

#========================================================================================================================================================================================================================

# Exercise 10B: Match Log Keyword Search
# You’re testing logs after a multiplayer match. You need to find out whether certain keywords appear in the log string.
# Ask the tester to enter a match log string.
# Ask for a keyword to search.
# If the keyword exists in the log: Print "Keyword found at index X" Otherwise: Print "Keyword not found."

log = str(input('\nenter string: '))
keyword = str(input('enter keyword: '))

pos = log.find(keyword)
if pos != -1:           #found anywhere, even at index 0
    print(f'\nKeyword "{keyword}" found at index {pos} \n')
else:
    print(f'\nKeyword "{keyword}" not found')

#========================================================================================================================================================================================================================

# Exercise 10C: Scoreboard Formatter
# After a match, the game generates raw player-score strings like "Alice,1200" or "Bob,950". You need to parse and display them in a formatted scoreboard.
# Ask the tester how many player entries to input.
#	2.	Collect strings in the format "Name,Score".
#	3.	Use .split(",") to separate name and score.
#	4.	Print them formatted as shown below


player_count = int(input('how many players : '))
users_raw_list = []

for a in range(1, player_count + 1):
    print(f'player{a} info: ')
    name_score = str(input('enter name and score seperated by coma: '))
    splitted = name_score.split(",")
    users_raw_list.append(splitted)


print(users_raw_list)
print('Final Leaderboard')

for entry in users_raw_list:
    name, score = entry
    print(f'Player: {name.strip()}  |   Score: {score.strip()}')


#========================================================================================================================================================================================================================

# Exercise 10D: Chat Censorship
# You’re testing the in-game chat filter. Some words are banned (like “noob”, “cheat”, “hack”), and they must be replaced with *** when they appear in a message.
#Ask the tester to input a chat message.
#	2.	Replace all banned words with ***.
#	3.	Print the cleaned (censored) chat message.

msg = str(input('type your message: '))
banned = ["noob","fucker","asshole"]

for word in banned:
        msg = msg.replace(word,"***")
print(msg)

#========================================================================================================================================================================================================================

# Exercise 10E: Game Log Splitter
# Your game writes logs in a single line like this: 2025-09-10 | Player=Aravind | Event=LevelUp | XP=1500
# You need to split this line into parts and extract useful info.
#Ask the tester to enter a log line in the format above.
#	2.	Use .split("|") to break it into chunks.
#	3.	For each chunk, strip spaces and print it clearly

log = str(input("put your logline: "))

parts = log.split("|")

for a in parts:
    print(a.strip())

#========================================================================================================================================================================================================================

# Exercise 10F: Case-Insensitive Username Check
# You’re testing a login system. Player usernames should be treated the same whether typed in uppercase, lowercase, or mixed case
# Ask the tester to enter the registered username (stored in the system).
#	2.	Ask for the login attempt username.
#	3.	Compare them in a case-insensitive way (hint: use .lower() or .upper()).
#	4.	Print either:	•	"Login successful" if they match    OR     "Login failed" otherwise

reg_name = str(input('enter your registered uname: '))

login_name = str(input('enter your login uname: '))

if login_name.upper() == reg_name.upper():
    print('====Login Successful======')
else:
    print('====Login Failed======')


#========================================================================================================================================================================================================================

# Exercise 10G: Multi-Line Chat Log Parser
# Ask the tester to input a multi-line chat log (you can simulate by pasting 3–4 lines).
#	2.	Split the log into lines.
#	3.	For each line:	•	Print only the username and the message (ignore the timestamp).

chat_msg ="""[12:01] Alice: GG!
[12:02] Bob: Well played
[12:05] Alice: See you tomorrow"""

chat_msg = chat_msg.split("\n")

print('\n',chat_msg,'\n')

for line in chat_msg:
    # Remove timestamp
    _, rest = line.split("] ")
    # Separate username and message
    username, message = rest.split(": ",1)
    print(f"{username} → {message}")

# 🔎 Mini Cheat Sheet:
# 1. Using "_" in unpacking:
#    When splitting into multiple parts, "_" is often used to ignore values.
#    Example: _, rest = line.split("] ")  → ignores timestamp, keeps rest.
#
# 2. maxsplit in .split():
#    string.split(sep, maxsplit) will split only 'maxsplit' times.
#    Example: "Alice: GG: Extra".split(": ", 1) → ["Alice", "GG: Extra"]


#========================================================================================================================================================================================================================

# Exercise 10H: String Conversion (Numbers ↔ Strings)
# Sometimes game APIs return numbers as strings ("1200"), or you need to send numbers inside text logs. You should practice converting between strings and numbers.
# Ask the tester to enter a score as string input.
#	2.	Convert it into an integer and add 500 bonus points.
#	3.	Print the updated score.
#	4.	Then, convert it back into a string and print a message "Final Score: 1700"

score = str(input('score: '))

score = int(score) + 500

print("Integer Score: ",score)

print(f"String Score: {score}")      # you don’t actually need str(score) inside an f-string, because f-strings handle it automatically.


#========================================================================================================================================================================================================================

# Exercise 10I: Substring Replacement & Censoring (Advanced)
# You’re testing a game chat where not only whole words but also parts of words need to be censored. For example:
#	•	"hacker" → should still censor "hack"
#	•	"noobish" → should still censor "noob"
# Ask the tester to enter a chat message.
#	2.	Maintain a list of banned substrings (e.g., ["noob", "hack", "cheat"]).
#	3.	Replace every occurrence (even if inside another word) with "***".
#	4.	Print the final censored message.

chat = str(input('type your msg: '))
banned = ['noob','fuck','hack','loose']

clean_chat = chat
for word in banned:
    clean_chat = clean_chat.replace(word, "***")
print(clean_chat)

#========================================================================================================================================================================================================================

# Exercise 10J: String Validation in Logs
# Sometimes your game logs contain entries like:  Player=Aravind | XP=1500 | Level=5      You want to validate each part of the log to ensure it’s in the correct format.
# Ask the tester to enter a log line in the format above.
#	2.	Split the line by "|" and strip spaces.
#	3.	For each part:
#	•	Check if it contains "=".
#	•	Split into key and value.
#	•	Validate:
#	•	"Player" → value should be only letters (isalpha()).
#	•	"XP" and "Level" → values should be numbers (isdigit()).
#	4.	Print "Valid log" if all checks pass, otherwise print "Invalid log" with the reason.

log = input("Enter log line (format: Player=Aravind | XP=1500 | Level=5): ")

# Step 1: Split by "|" and strip spaces
parts = [p.strip() for p in log.split("|")]

valid = True   # assume log is valid unless a check fails

for part in parts:
    if "=" not in part:
        print(f"Invalid part (missing '='): {part}")
        valid = False
        continue

    key, value = part.split("=", 1)

    if key == "Player":
        if not value.isalpha():
            print(f"Invalid Player value: {value} (should be letters only)")
            valid = False

    elif key in ["XP", "Level"]:
        if not value.isdigit():
            print(f"Invalid {key} value: {value} (should be numbers only)")
            valid = False

    else:
        print(f"Unknown key: {key}")
        valid = False

# Final Result
if valid:
    print("✅ Valid log")
else:
    print("❌ Invalid log")


#========================================================================================================================================================================================================================

# Exercise 10K: Leaderboard Topper Finder
# After a match, you have a scoreboard dictionary like: {"Alice": 1200, "Bob": 950, "Charlie": 1600}
# You need to identify the top player and their score.
# Define a dictionary of players with their scores.
#	2.	Find the player with the highest score.
#	3.	Print their name and score like: Topper: Charlie with 1600 points

sb_dict = {"Alice": 1200, "Bob": 950, "Charlie": 1600}

topper = max (sb_dict, key = sb_dict.get)

print(f"Topper: {topper} with {sb_dict[topper]} points")


#========================================================================================================================================================================================================================

# Exercise 10L: Multi-Top Players (Tie Handling)
# Sometimes two or more players have the same top score. Your QA task is to correctly detect and display all toppers.
# Define a scoreboard dictionary: {"Alice": 1600, "Bob": 950, "Charlie": 1600, "Diana": 1200}
# Find the highest score.
# Collect all players who have that score.
# Print them clearly, e.g.: Toppers: Alice, Charlie with 1600 points

sb_dict = {"Alice": 1200, "Bob": 950, "Charlie": 1600, "Diana":1600}

max_score = max(sb_dict.values())

#topper = [name for name, score in sb_dict.items() if score == max_score]

# simpler code of above line
topper = []
for name, score in sb_dict.items():
   if score == max_score:
       topper.append(name) 

print(f"{','.join(topper)} with {max_score} points")

#========================================================================================================================================================================================================================

# Exercise 10M: Alphabetical First Player
# Sometimes you need to show the alphabetically first player name (for example, to break ties consistently or to display leaderboards in order).
# Define a scoreboard dictionary, e.g.: {"Zara": 1200, "Alice": 950, "Charlie": 1600, "Bob": 1200}
# Find the player whose name comes first alphabetically.
# Print it like: Alphabetically first player: Alice

dict = {"Zara": 1200, "Alice": 950, "Charlie": 1600, "Bob": 1200, "Abagel": 700}

name = min(dict.keys())
score = max(dict.values())

print(name)
print(score)

#---------------------------------------

for name, score in dict.items():
    name = min(dict.keys())
    tuples = (name, score)

print("Wohoo", tuples)

#========================================================================================================================================================================================================================








        
           
