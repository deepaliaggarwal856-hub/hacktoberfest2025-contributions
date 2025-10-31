# Hacktoberfest 2025 💻✨
# Author: Deepali Agarwal
# A fun and motivational open-source contribution

import random
import datetime

# Get the current year
year = datetime.datetime.now().year

# List of unique motivational quotes
quotes = [
    "Dream big. Code bigger. 🚀",
    "Every commit brings you closer to mastery 💪",
    "Success starts with a single pull request 🌸",
    "Stay curious, stay open-source 🔥",
    "Hacktoberfest 2025 — where beginners become creators 💻",
    "Your code can change the world 🌍",
    "Keep pushing, even when it's hard 💫"
]

# Display a random quote
print(f"\n✨ Welcome to Hacktoberfest {year}! ✨\n")
print("Here’s your random motivation for today:\n")
print(f"💬 {random.choice(quotes)}\n")
print("Made with ❤️ by Deepali for open-source enthusiasts everywhere!")
