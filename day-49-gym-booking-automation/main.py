from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"
TARGET_DAYS = ("Tue", "Thu")
TARGET_TIME = "6:00 PM"

CHROME_PREFS = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
}

CHROME_ARGS = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-software-rasterizer",
]

DAY_GROUP_CLASS = "Schedule_dayGroup__y79__"
CLASS_CARD_CLASS = "ClassCard_card__KpCx5"
BOOK_BUTTON_CLASS = "ClassCard_bookButton__DMM1I"


def create_driver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("prefs", CHROME_PREFS)
    for arg in CHROME_ARGS:
        chrome_options.add_argument(arg)

    service = Service(ChromeDriverManager().install(), log_path="/tmp/chromedriver.log")
    return webdriver.Chrome(service=service, options=chrome_options)


def login(driver: webdriver.Chrome, wait: WebDriverWait) -> None:
    driver.get(GYM_URL)
    driver.maximize_window()

    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "email-input"))).send_keys(ACCOUNT_EMAIL)
    wait.until(EC.presence_of_element_located((By.ID, "password-input"))).send_keys(ACCOUNT_PASSWORD)
    wait.until(EC.element_to_be_clickable((By.ID, "submit-button"))).click()
    wait.until(lambda d: "/schedule" in d.current_url)


def parse_class_card(card: webdriver.remote.webelement.WebElement) -> tuple[str, str, webdriver.remote.webelement.WebElement]:
    card_lines = [line.strip() for line in card.text.splitlines() if line.strip()]
    class_name = card_lines[0] if card_lines else "Unknown"
    class_time = next((line for line in card_lines if "Time:" in line), "Time: Unknown")
    book_button = card.find_element(By.CLASS_NAME, BOOK_BUTTON_CLASS)
    return class_name, class_time, book_button


def get_button_state(book_button: webdriver.remote.webelement.WebElement) -> str:
    button_text = book_button.text.strip()
    button_classes = book_button.get_attribute("class")

    if "booked" in button_classes:
        return "booked"
    if "Join Waitlist" in button_text or "waitlist" in button_classes:
        return "waitlist"
    if "available" in button_classes or "Book Class" in button_text:
        return "available"
    return "unknown"


def process_schedule(driver: webdriver.Chrome, wait: WebDriverWait) -> tuple[dict, list[str]]:
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, DAY_GROUP_CLASS)))

    counts = {
        "bookings_made": 0,
        "waitlists_joined": 0,
        "already_booked": 0,
        "already_waitlisted": 0,
        "available_to_book": 0,
        "classes_processed": 0,
    }
    processed_details: list[str] = []

    for day_group in driver.find_elements(By.CLASS_NAME, DAY_GROUP_CLASS):
        day_text = day_group.text
        if not any(day in day_text for day in TARGET_DAYS):
            continue

        for card in day_group.find_elements(By.CLASS_NAME, CLASS_CARD_CLASS):
            if TARGET_TIME not in card.text:
                continue

            counts["classes_processed"] += 1
            class_name, class_time, book_button = parse_class_card(card)
            state = get_button_state(book_button)

            if state == "booked":
                counts["already_booked"] += 1
                status = "Already booked"
            elif state == "waitlist":
                book_button.click()
                counts["waitlists_joined"] += 1
                status = "Joined waitlist"
            elif state == "available":
                counts["available_to_book"] += 1
                book_button.click()
                counts["bookings_made"] += 1
                status = "Booked"
            else:
                status = f"Unknown status ({book_button.text.strip()})"

            processed_details.append(f"{day_text.splitlines()[0]} | {class_name} | {class_time} | {status}")
            print(f"  Processed: {processed_details[-1]}")

    return counts, processed_details


def print_summary(counts: dict, details: list[str]) -> None:
    print("\n" + "=" * 80)
    print("DETAILED BOOKING RESULTS")
    print("=" * 80)
    for detail in details:
        print(detail)
    print("\n" + "=" * 80)
    print("BOOKING SUMMARY")
    print("=" * 80)
    print(f"Classes Processed:         {counts['classes_processed']}")
    print(f"New Bookings Made:        {counts['bookings_made']}")
    print(f"Waitlists Joined:         {counts['waitlists_joined']}")
    print(f"Already Booked:           {counts['already_booked']}")
    print(f"Already Waitlisted:       {counts['already_waitlisted']}")
    print(f"Available to Book:        {counts['available_to_book']}")
    print(f"Total Classes Checked:    {counts['classes_processed']}")
    print("=" * 80)


if __name__ == "__main__":
    driver = create_driver()
    wait = WebDriverWait(driver, 10)
    login(driver, wait)
    time.sleep(2)
    counts, details = process_schedule(driver, wait)
    print_summary(counts, details)




