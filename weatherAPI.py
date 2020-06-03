#!/usr/bin/python3
import flask
from flask import jsonify
import mysql.connector
from datetime import date

# Specify database credentials
config = {
        "host": "ip_address",
        "port": "3306",
        "user": "username",
        "passwd": "password",
        "database": "database"
}

# Create a flask app object with this filename as name
app = flask.Flask(__name__)
# Set debug mode to False
app.config["DEBUG"] = False


def getDictFromRow(row) -> dict:
    """
    Convert a database row to a dictionary
    :param row: The row to parse to a dict
    :return: The parsed row as a dictionary
    """
    return {"location": row[1],
            "date": str(row[2]),
            "time": str(row[3]),
            "weather_id": int(row[4]),
            "description": row[5],
            "icon": row[6],
            "temp": float(row[7]),
            "temp_min": float(row[8]),
            "temp_max": float(row[9]),
            "pressure": int(row[10]),
            "humidity": int(row[11]),
            "wind_speed": float(row[12]),
            "wind_direction": int(row[13]),
            "cloudiness": int(row[14])
            }


@app.route('/', methods=['GET'])
def home():
    return "<h1>Weather proxy API</h1><p>This site is a prototype API for weather data</p>"


# A route to return all of the available entries in the database.
@app.route('/api/v1/weather/all', methods=['GET'])
def api_all():
    # Connect to the database
    cnx = mysql.connector.connect(**config)
    # Get the cursor object
    cursor = cnx.cursor()
    # Execute sql statement that gets weather data from the current date
    cursor.execute("SELECT * FROM weather WHERE date like %s", (str(date.today()),))
    # Fetch all results
    results = cursor.fetchall()
    # Create a response list
    response = []
    for row in results:
        # Convert the current row and append it to the response list
        response.append(getDictFromRow(row))
    # Close the cursor object
    cursor.close()
    # Close the connection
    cnx.close()
    # Return and encode the response as JSON
    return jsonify(response)


# A route to return the most recent entry in the database.
@app.route('/api/v1/weather/recent', methods=['GET'])
def api_recent():
    # Connect to the database
    cnx = mysql.connector.connect(**config)
    # Get the cursor object
    cursor = cnx.cursor()
    # Execute sql statement that gets the most recent entry
    cursor.execute("SELECT * FROM weather ORDER BY id DESC LIMIT 1")
    # Fetch all results
    result = cursor.fetchall()
    # Close the cursor object
    cursor.close()
    # Close the connection
    cnx.close()
    # Return and encode the response as JSON
    return jsonify(getDictFromRow(result[0]))


if __name__ == "__main__":
    app.run()
