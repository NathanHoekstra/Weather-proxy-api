#!/usr/bin/python3
import requests
from datetime import datetime
import mysql.connector

# Connect to mysql database with the following params
db = mysql.connector.connect(
    host="ip_address",
    port="3306",
    user="username",
    passwd="password",
    database="database"
)

# Create cursor object
cursor = db.cursor()

# Specify parameters for the api
# Docs: https://openweathermap.org/current
parameters = {"id": 999999, "units": "metric", "lang": "nl", "appid": "API_KEY"}

# Perform an API request
response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parameters)

# Retreive the JSON encoded data
data = response.json()

# SQL statement to insert the api data into the database table
sql = "INSERT INTO weather (city_id, date, time, weather_id, description, icon, temp, temp_min, temp_max, pressure, " \
      "humidity, wind_speed, wind_direction, cloudiness) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

# Corresponding values for the sql statement
val = (data['id'],
       datetime.fromtimestamp(data['dt']).date(),
       datetime.fromtimestamp(data['dt']).time(),
       data['weather'][0]['id'],
       data['weather'][0]['description'],
       data['weather'][0]['icon'],
       data['main']['temp'],
       data['main']['temp_min'],
       data['main']['temp_max'],
       data['main']['pressure'],
       data['main']['humidity'],
       data['wind']['speed'],
       data['wind']['deg'],
       data['clouds']['all'])

# Execute the sql statement with the corresponding values
cursor.execute(sql, val)
# Commit the values into the database table
db.commit()
# Close connection
db.close()
