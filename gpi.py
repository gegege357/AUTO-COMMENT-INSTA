from instagrapi import Client
from colorama import Fore, Style
import time
import os

# Clear screen
os.system("clear" if os.name != "nt" else "cls")

# Initialize Instagram client
client = Client()

print("\n=== Instagram Post ID Extractor ===\n")

# =========================
# INPUT URL
# =========================
post_url = input(
    f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Paste Instagram Post URL: "
)

while (
    not post_url.strip()
    or "instagram.com" not in post_url
    or not any(x in post_url for x in ["/p/", "/reel/", "/tv/"])
):
    print(f"{Fore.RED}Invalid Instagram POST URL. Try again.{Fore.RESET}")
    post_url = input(
        f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Paste Instagram Post URL: "
    )

# =========================
# GET POST ID
# =========================
print(f"{Fore.LIGHTGREEN_EX}\nGetting Post ID...{Fore.RESET}")
time.sleep(1)

try:
    post_id = client.media_pk_from_url(post_url)
except Exception as e:
    print(f"{Fore.RED}Error retrieving Post ID: {e}{Fore.RESET}")
    exit(1)

# =========================
# OUTPUT
# =========================
print(f"\n{Fore.YELLOW}Post ID:{Fore.RESET} {post_id}")
print(
    f"\n{Fore.LIGHTGREEN_EX}{Style.BRIGHT}"
    f"Copy the Post ID and run ./send_comment.sh"
    f"{Fore.RESET}\n"
)
