# 🏋️ Gym Class Booking Bot

An automated gym class booking bot built with **Python** and **Selenium**. It logs into the gym website, scans the weekly schedule, and automatically books classes (or joins the waitlist) for your preferred days and time — so you never miss a spot.

---

## 📋 Features

- ✅ Auto-login to the gym portal
- 📅 Filters classes by target days (e.g. Tuesday & Thursday)
- 🕕 Filters classes by target time (e.g. 6:00 PM)
- 📌 Books available classes automatically
- ⏳ Joins the waitlist if a class is full
- 📊 Prints a detailed booking summary after each run

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Selenium** — browser automation
- **webdriver-manager** — auto-manages ChromeDriver versions

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/gym-booking-bot.git
cd gym-booking-bot
```

### 2. Install dependencies
```bash
pip install selenium webdriver-manager
```

### 3. Configure your details

Open `main.py` and update the constants at the top of the file:

```python
ACCOUNT_EMAIL = "your-email@example.com"
ACCOUNT_PASSWORD = "your-password"
GYM_URL = "https://your-gym-website.com/"
TARGET_DAYS = ("Tue", "Thu")   # Days to book
TARGET_TIME = "6:00 PM"        # Preferred class time
```

> ⚠️ **Security tip:** Avoid hardcoding credentials in the script. Use environment variables instead:
> ```python
> import os
> ACCOUNT_EMAIL = os.environ.get("GYM_EMAIL")
> ACCOUNT_PASSWORD = os.environ.get("GYM_PASSWORD")
> ```

### 4. Run the bot
```bash
python main.py
```

Chrome will open automatically, log in, process the schedule, and print results in the terminal.

---

## 🖥️ Sample Output

```
  Processed: Tuesday | Yoga Flow | Time: 6:00 PM | Booked
  Processed: Thursday | HIIT Burn | Time: 6:00 PM | Already booked

================================================================================
DETAILED BOOKING RESULTS
================================================================================
Tuesday   | Yoga Flow  | Time: 6:00 PM | Booked
Thursday  | HIIT Burn  | Time: 6:00 PM | Already booked

================================================================================
BOOKING SUMMARY
================================================================================
Classes Processed:         2
New Bookings Made:         1
Waitlists Joined:          0
Already Booked:            1
Already Waitlisted:        0
Available to Book:         1
Total Classes Checked:     2
================================================================================
```

---

## 📁 Project Structure

```
gym-booking-bot/
│
├── main.py        # Main script — all logic lives here
└── README.md      # Project documentation
```

---

## 🔍 How It Works

1. **Login** — Navigates to the gym URL and signs in using your credentials
2. **Scan Schedule** — Finds all day groups on the schedule page
3. **Filter** — Keeps only the target days and target time slot
4. **Act** — For each matching class:
   - If already booked → skips it
   - If available → books it
   - If full → joins the waitlist
5. **Report** — Prints a summary of all actions taken

---

## ⚠️ Notes

- The bot uses **CSS class selectors** from the gym website's HTML. If the website updates its layout, these selectors may need to be updated in `main.py`:
  ```python
  DAY_GROUP_CLASS = "Schedule_dayGroup__y79__"
  CLASS_CARD_CLASS = "ClassCard_card__KpCx5"
  BOOK_BUTTON_CLASS = "ClassCard_bookButton__DMM1I"
  ```
- Chrome must be installed on your machine. The `webdriver-manager` library handles ChromeDriver automatically.
- The `--no-sandbox` and `--disable-dev-shm-usage` flags are included for compatibility with Linux/server environments.

---

## 🚀 Future Improvements

- [ ] Load credentials from a `.env` file
- [ ] Add email/SMS notifications after booking
- [ ] Schedule the bot to run automatically (e.g. via cron job)
- [ ] Support multiple time slots per day
- [ ] Add a GUI for easy configuration

---

## 📄 License

This project is for educational purposes. Check your gym's terms of service before using automated tools on their platform.
