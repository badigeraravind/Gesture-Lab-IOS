from datetime import datetime          # ➊ pulls in date & time utilities
from pathlib import Path               # ➋ modern, OS-safe paths

log_file = Path("log_setup.txt")      # ➌ choose (or create) a log file
timestamp = datetime.now().isoformat() # ➍ current time like 2025-05-08T19:02:11.123456

with log_file.open("a", encoding="utf-8") as f:  # ➎ open in **a**ppend mode
    f.write(f"\nSetup finished at {timestamp}\n")  # ➏ add one line to the end

print(f"\nLogged to: {log_file.resolve()}\n")         # ➐ show the absolute path