import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from datetime import datetime, timedelta
import pytz
import smtplib

MIN = 60

smtp_server = "smtp.gmail.com"
smtp_port = 587
my_email = "sampagaellejun.dev@gmail.com"
my_password = "ydmw ahni plxz ndum"
recipients = "sampagaellejunit@gmail.com"

#LATITUDE
CURRENT_MY_LAT = 12.879721
POS_CURRENT_MY_LAT = 12.879721 + 200
NEG_CURRENT_MY_LAT = 12.879721 - 200
print(f"Latitude Range:  {NEG_CURRENT_MY_LAT} - {POS_CURRENT_MY_LAT}")

#LONGITUDE
CURRENT_MY_LONG = 121.774017
POS_CURRENT_MY_LONG = 121.774017 + 200
NEG_CURRENT_MY_LONG = 121.774017 - 200
print(f"Longitude Range:  {NEG_CURRENT_MY_LONG} - {POS_CURRENT_MY_LONG}")

print(f"LATITUDE RANGE : {CURRENT_MY_LAT}")
print(f"LATITUDE RANGE : {CURRENT_MY_LONG}")
philippines_timezone = pytz.timezone("Asia/Manila")

def send_email():
    try:
        msg = MIMEMultipart()
        msg["From"] = my_email
        msg['To'] = recipients
        msg['Subject'] = "ISS Incoming!"

        body = f"It's {formatted_date}, ISS is in your area. Please look up!"
        msg.attach(MIMEText(body, 'plain'))
        connection = smtplib.SMTP(smtp_server, smtp_port, timeout=30)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_email, recipients, msg.as_string())
        connection.close()
    except Exception as error:
        print(f"Failed to send an email: {error}")
    else:
        print("Email sent successfully!")

parameters = {
    "lat": CURRENT_MY_LAT,
    "lng": CURRENT_MY_LONG,
    "formatted": 0
}

# CHECK IF IT'S SUNSET OR SUNRISE
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(philippines_timezone)
formatted_date = time_now.strftime("%A, %d %B %Y")
time_now_hour = time_now.hour

print(f"Hour right now: {time_now_hour}")
print(sunrise)
print(sunset)

# GET THE LONG AND LAT FOR ISS POSITION
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


print(f"ISS CURRENT LATITUDE: {iss_latitude}")
print(f"ISS CURRENT LONGITUDE: {iss_longitude}")





def sent_every_min():
    for i in range(MIN):
        time_now + timedelta(minutes=i)
        if NEG_CURRENT_MY_LAT <= iss_latitude <= POS_CURRENT_MY_LAT and NEG_CURRENT_MY_LONG <= iss_longitude <= POS_CURRENT_MY_LONG:
            if time_now_hour <= sunset or time_now_hour != sunrise:
                send_email()
        time.sleep(60)

        time.sleep(1)

sent_every_min()

