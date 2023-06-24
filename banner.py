from colorama import Fore, just_fix_windows_console,init
import os

just_fix_windows_console()
init(autoreset=True)
width, heigth = os.get_terminal_size()
offset1 = int((width - 93) /2 )
offset2 = offset1 + 70



print("-"*width)
banner = r"""
  _____   ___   _____        ___   __  __ ______  ____    __  ___   ___  ______  ____    ___ 
 / ___/  / _ \ / ___/       / _ | / / / //_  __/ / __ \  /  |/  /  / _ |/_  __/ / __ \  / _ \
/ (_ /  / ___// (_ /       / __ |/ /_/ /  / /   / /_/ / / /|_/ /  / __ | / /   / /_/ / / , _/
\___/  /_/    \___/       /_/ |_|\____/  /_/    \____/ /_/  /_/  /_/ |_|/_/    \____/ /_/|_| 
"""

for line in banner.splitlines():
    print(Fore.CYAN+" "*offset1+line) 

print(Fore.CYAN+"\n"+" "*offset2+"version: v0.1.0-beta1")
print(Fore.CYAN+" "*offset2+"Source: www.github.com/LunaOzma")
print("-"*width)