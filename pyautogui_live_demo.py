import time
from datetime import datetime

import pyautogui
import pyperclip

now = datetime.now()
today = now.strftime("%Y-%m-%d")
date_and_time = now.strftime("%Y-%m-%d %H:%M:%S")
report_file = f"daily_report_{today}.txt"
screenshot_file = f"daily_report_{today}.png"

print("Step 1: Opening Python.org in Chrome...")
pyautogui.hotkey("win", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://www.python.org/")
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

print("Step 2: Copying information from the website...")
fetched_data = ""
for line in pyperclip.paste().splitlines():
    if len(line.strip()) > 20:
        fetched_data = line.strip()
        break

if not fetched_data:
    raise RuntimeError("No readable text was copied from Python.org.")
print("Copied information:", fetched_data)

comment = "Python is worth exploring today."
report_row = f"{date_and_time} | {fetched_data} | {comment}"

print("Step 3: Creating and saving the report in Notepad...")
pyautogui.hotkey("win", "r")
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(2)
pyperclip.copy(report_row)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.write(report_file)
pyautogui.press("enter")
time.sleep(2)

print("Step 4: Taking a screenshot...")
pyautogui.screenshot().save(screenshot_file)
print("Report saved as:", report_file)
print("Screenshot saved as:", screenshot_file)
print("Assignment complete!")
