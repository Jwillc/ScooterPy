import requests as re
import simplejson as json
import time
import datetime
import haversine
# Me
lat1 = 45.0000 # Put your latitude here
long1 = -122.0000 # Put your longitude here

# Generate a task from the API
response = re.get('https://scootermap.com/api/vehicles?user_location=45.563239893861635,-122.64168064688386&northeast_point=45.58034345683749,-122.63524334524811&southwest_point=45.54613112227501,-122.6481179485196&company=lime&mode=charge&randomize=false')
data = json.loads(response.text)
# Get the task_id
taskId = data['status_url'].split("/")[3].split("?")[1]
# Wait
time.sleep(2)

# Get the task-status from the API. Hopefully it's done.
responseFromApi = re.get('https://scootermap.com/api/tasks/task-status?' + str(taskId))
scooters = json.loads(responseFromApi.text)
content = scooters['task']['result']['vehicles']

# Get total number of scooters
numOfScoots = len(content)
# Print the date
print(datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S") + "\n")
# Print total number of scooters
print("Number of Scooters: " + str(numOfScoots) + "\n")

# Loop through each scooter
for item in content:
	# Get the lat/long for each scooter
    latty = item['latitude']
    longy = item['longitude']
	#Calculate distance from me to scooter
    fromMe = haversine.distance((lat1, long1), (latty, longy))
	# Print info
    print("Distance from Me: " + str(fromMe))
    print("Lat/Long: {}, {}\nvID: {}\n".format(item['latitude'],item['longitude'],item['vehicle_id_to_display']))