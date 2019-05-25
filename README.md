# ScooterPy
Python script to obtain scooter data from the scootermap API.

# Usage
The purpose of the script is to obtain nearby Lime scooters based on your Lat/Long. We a querying the Scootermap API. Please do not spam. See comments in the try.py file. Lines 7 & 8 are where you enter your latitude, longitiude. The script will then get the number of scooters in your area. Calculate the distance from you to each scooter using haversine.py and print the info out in the terminal.

# Task Link
You'll need to edit the link on line 11 to get the scooters in your area.

```
https://scootermap.com/api/vehicles?user_location=45.563239893861635,-122.64168064688386&northeast_point=45.58034345683749,-122.63524334524811&southwest_point=45.54613112227501,-122.6481179485196&company=lime&mode=charge&randomize=false
```

Change user_location, northeast_point, and southwest_point to represent your general location.

# How to get your NE & SW Points
Using Google Chrome go to https://scootermap.com/map

Click the overflow menu (three dots top right)

Scroll down to more tools

Click developer tools

![developer tools](https://i.imgur.com/gVPSxzI.png)

Click on the network tab

Zoom out on the map to your desired range

Find the link that starts with vehicles? where company = lime

Click the link and go to the headers tab. Your location, NE & SW points will be there. Copy these into the task link.
