from datetime import datetime
from pathlib import Path
import shutil
import subprocess
import time

import pyautogui
import pyperclip


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

website = "https://www.python.org/"
output_folder = Path(__file__).resolve().parent
timestamp = datetime.now()
report_path = output_folder / f"daily_report_{timestamp:%Y-%m-%d}.txt"
screenshot_path = output_folder / f"daily_report_{timestamp:%Y-%m-%d}.png"

# Open Chrome and copy the page text.
pyautogui.hotkey("win", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("ctrl", "l")
pyautogui.write(website, interval=0.03)
pyautogui.press("enter")
time.sleep(6)
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
time.sleep(1)

page_text = pyperclip.paste()
page_lines = [line.strip() for line in page_text.splitlines() if len(line.strip()) >= 25]
if not page_lines:
    raise RuntimeError("Could not copy readable text from the Python website.")

fetched_data = page_lines[0]
report_row = (
    f"{timestamp:%Y-%m-%d %H:%M:%S} | "
    f"{fetched_data} | Python is worth exploring today."
)

# Open Notepad++ when installed, otherwise use Windows Notepad.
notepad_plus_plus = shutil.which("notepad++")
if notepad_plus_plus is None:
    common_paths = (
        Path(r"C:\Program Files\Notepad++\notepad++.exe"),
        Path(r"C:\Program Files (x86)\Notepad++\notepad++.exe"),
    )
    notepad_plus_plus = next((str(path) for path in common_paths if path.exists()), None)

subprocess.Popen([notepad_plus_plus or "notepad.exe"])
time.sleep(3)
pyperclip.copy(report_row)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "s")
time.sleep(2)
pyperclip.copy(str(report_path))
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(2)

# Capture the report as it appears in the editor.
pyautogui.screenshot().save(screenshot_path)
print(f"Saved report: {report_path}")
print(f"Saved screenshot: {screenshot_path}")
