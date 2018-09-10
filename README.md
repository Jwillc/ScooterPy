# ScooterPy
Python script to obtain scooter data from the scootermap API.

# Usage
The purpose of the script is to obtain nearby Lime scooters based on your Lat/Long. We a querying the Scootermap API. Please do not spam. See comments in the try.py file. Lines 7 & 8 are where you enter your latitude, longitiude. The script will then get the number of scooters in your area. Calculate the distance from you to each scooter using haversine.py and print the info out in the terminal.

# Task Link
You'll need to edit the link on line 11 to get the scooter in your area.

```
https://scootermap.com/api/vehicles?user_location=45.563239893861635,-122.64168064688386&northeast_point=45.58034345683749,-122.63524334524811&southwest_point=45.54613112227501,-122.6481179485196&company=lime&mode=charge&randomize=false
```

Change user_location and southwest_point to represent your general location.
