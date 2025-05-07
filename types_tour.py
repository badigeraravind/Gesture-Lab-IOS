lives        = 3
pi           = 3.14159
name         = "Aravind Badiger"
is_game_over = False
scores       = [1200, 845, 990]
player       = {"id": 17, "rank": "Gold"}

# Take a snapshot so the dictionary size won't change while we iterate
vars_snapshot = [
    (k, v) for k, v in locals().items() if not k.startswith("__")
]

for label, value in vars_snapshot:
    print(f"{label:12} │ {value!r:18} │ {type(value).__name__}")

average = sum(scores) / len(scores)
print(f"\nAverage score: {average:.1f}")