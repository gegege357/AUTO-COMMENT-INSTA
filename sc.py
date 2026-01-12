from instagrapi import Client
import time
import getpass
import os
import sys
import random

bot = Client()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

print("\n=== Instagram Comment Tool ===\n")

# =========================
# LOGIN
# =========================
while True:
    username = input("Enter Instagram Username: ").strip()
    if username:
        break
    print("Username cannot be empty.")

while True:
    password = getpass.getpass("Enter Instagram Password: ").strip()
    if password:
        break
    print("Password cannot be empty.")

print("\nLogging in...")
try:
    bot.login(username, password)
    print(f"Login successful: {username}")
except Exception as e:
    print("Login failed:", e)
    sys.exit(1)

# =========================
# POST ID INPUT
# =========================
while True:
    POSTID = input("\nEnter Instagram Post ID: ").strip()
    if POSTID.isdigit():
        try:
            bot.media_info(POSTID)
            print("Post ID valid.")
            break
        except Exception:
            print("Invalid Post ID.")
    else:
        print("Post ID must be numeric.")

# =========================
# COMMENT SOURCE
# =========================
comment_types_input = input(
    "\nHow many comment templates? (ENTER = use comments.txt): "
).strip()

if not comment_types_input:
    if not os.path.exists('comments.txt'):
        print("comments.txt not found.")
        sys.exit(1)
    with open('comments.txt', 'r', encoding='utf-8') as f:
        comments = [x.strip() for x in f if x.strip()]
    if not comments:
        print("comments.txt is empty.")
        sys.exit(1)
else:
    comments = []
    try:
        count = int(comment_types_input)
        for i in range(1, count + 1):
            c = input(f"Enter comment {i}: ").strip()
            if c:
                comments.append(c)
    except ValueError:
        print("Invalid number.")
        sys.exit(1)

# =========================
# COUNT & DELAY
# =========================
while True:
    try:
        total = int(input("\nHow many comments to send: "))
        break
    except ValueError:
        print("Invalid number.")

while True:
    try:
        delay = int(input("Delay between comments (seconds, min 30): "))
        if delay >= 30:
            break
        print("Minimum delay is 30 seconds.")
    except ValueError:
        print("Invalid delay.")

# =========================
# EXECUTION
# =========================
print("\nPress CTRL+C to stop\n")
time.sleep(1)

sent = 0
for i in range(total):
    try:
        msg = random.choice(comments)
        bot.media_comment(POSTID, msg)
        sent += 1
        print(f"Sent {sent}/{total}: {msg}")
        if sent < total:
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nStopped by user.")
        break
    except Exception as e:
        print("Error:", e)
        break

print(f"\nDone. Total comments sent: {sent}")
