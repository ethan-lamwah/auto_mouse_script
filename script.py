import pyautogui
import sys
from datetime import datetime

import asyncio

async def move_mouse():
    interval_minute = 5 # default interval is 5 Minutes
    if (len(sys.argv) > 1 and sys.argv[1].isnumeric()):
        interval_minute = int(sys.argv[1])  # set interval if it is provided as sys argument

    print(f"Start auto-script to move your mouse at every {interval_minute} minutes.")
    screen_width, screen_height = pyautogui.size()
    
    pyautogui.moveTo(screen_width/2, screen_height/2)   # Move to central position of the screen

    while True:
        pyautogui.moveRel(0, 400, duration=1, tween=pyautogui.easeInOutQuad)    # move mouse relative to its current position with yOffset=400
        pyautogui.moveRel(0, -400, duration=1, tween=pyautogui.easeInOutQuad)   # move mouse relative to its current position with yOffset=400
        print(f"Move at {datetime.now().strftime('%b %d %I:%M %p')}")

        delay_in_sec = interval_minute * 60
        await asyncio.sleep(delay_in_sec)        

asyncio.run(move_mouse())