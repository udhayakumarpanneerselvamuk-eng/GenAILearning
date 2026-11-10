from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright


url = "https://www.bbc.com/sport/cricket/scores-fixtures"
output_folder = Path(__file__).resolve().parent
timestamp = datetime.now()
date_and_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
score_file = output_folder / f"live_score_{timestamp:%Y-%m-%d_%H-%M-%S}.txt"
screenshot_file = output_folder / f"live_score_{timestamp:%Y-%m-%d_%H-%M-%S}.png"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    try:
        page = browser.new_page()
        response = page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        if response is None or response.status >= 400:
            status = response.status if response else "no response"
            raise RuntimeError(f"The score website returned {status}: {url}")

        main_content = page.locator("main")
        main_content.wait_for(state="visible", timeout=15_000)
        page_text = main_content.inner_text()

        score = "\n".join(line.strip() for line in page_text.splitlines() if line.strip())
        if not score:
            raise RuntimeError("No cricket score information was found on the page.")

        page.screenshot(path=str(screenshot_file), full_page=True)
        score_file.write_text(
            f"Date and time: {date_and_time}\nScore information:\n{score}\n",
            encoding="utf-8",
        )

        print(f"Score information:\n{score}")
        print(f"Text file saved: {score_file}")
        print(f"Screenshot saved: {screenshot_file}")
    finally:
        browser.close()
