import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

pyautogui.moveTo(150, 100, duration=1)
pyautogui.dragTo(300, 300, duration=1, button='left')
pyautogui.click(400, 400)
pyautogui.scroll(500)
pyautogui.scroll(-500)
pyautogui.doubleClick(500, 500)
pyautogui.rightClick(600, 600)