
# ISS Notification System

This Python script tracks the position of the International Space Station (ISS) and sends an email alert when the ISS is visible in a specific location during nighttime. The script utilizes the Sunrise-Sunset and Open Notify APIs for ISS location and sunrise/sunset data.

---

## Features

- Tracks the ISS's real-time position using the Open Notify API.
- Sends an email notification if the ISS is within a defined latitude and longitude range.
- Works only when it is dark (based on sunrise and sunset times).
- Scheduled to check ISS position every minute.

---

## Requirements

- Python 3.x
- Required Libraries:
  - `requests`
  - `email` (built-in)
  - `smtplib` (built-in)
  - `pytz`

---

## Setup

1. **Install Required Libraries**

   ```bash
   pip install requests pytz
   ```

2. **Email Configuration**

   Replace the following placeholders in the script with your details:

   - `my_email`: Your email address.
   - `my_password`: Your email app password (ensure you enable "App Password" in your email settings).
   - `recipients`: Recipient email address.

3. **Latitude and Longitude**

   Update the `CURRENT_MY_LAT` and `CURRENT_MY_LONG` variables with your current coordinates.

---

## How It Works

1. Fetches sunrise and sunset times for the given location.
2. Checks ISS position in real time every minute.
3. Sends an email notification when the ISS is visible and it is nighttime.

---

## Notes

- Make sure to enable "Less Secure App Access" in your email settings or use an App Password.
- Ensure a stable internet connection for API requests.

---

## Disclaimer

This script is for educational purposes only. Use responsibly and do not abuse email services.

---

## Author

- sampagaellejun.dev@gmail.com

---
