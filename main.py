import requests
from datetime import datetime

# MY_LAT = 14.612034
# MY_LONG = 121.086786

MY_LAT = -33.612034  # For testing purposes only +5 -5
MY_LONG = -69.859  # For testing purposes only +5 -5

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
iss_data = response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])
my_latitude = float(MY_LAT)
my_longitude = float(MY_LONG)

if (iss_latitude - 5 <= my_latitude <= iss_latitude + 5) and (iss_longitude - 5 <= my_longitude <= iss_longitude + 5):
    print("Your position is within +5 or -5 degrees of the ISS latitude and longitude.")

print(f"ISS Latitude: {iss_latitude}")
print(f"ISS Longitude: {iss_longitude}")
print(f"My Latitude: {my_latitude}")
print(f"My Longitude: {my_longitude}")

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now)
print(iss_data)

# If the ISS is close to my current position
# And it is currently dark
# Then send an email to look up.
# BONUS: run the code every 60 seconds.
