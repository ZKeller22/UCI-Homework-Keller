import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})


Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

measurement = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

#weather app
app = Flask(__name__)


# Design a query to retrieve the last 12 months of precipitation data and plot the results
latest_date = (session.query(measurement.date)
              .order_by(measurement.date.desc())
              .first())

#Get string from query object
latest_date= list(np.ravel(latest_date))[0]

#Convert string to date Object
latest_date = dt.datetime.strptime(latest_date, '%Y-%m-%d')

#Get Year, Month, Date
year = int(dt.datetime.strftime(latest_date, '%Y'))
month = int(dt.datetime.strftime(latest_date, '%m'))
day = int(dt.datetime.strftime(latest_date, '%d'))

# Calculate the date 1 year ago from the last data point in the database
year_prior = dt.date(year, month,day)- dt.timedelta(days=365)




@app.route("/")
def home():
    return (f"Welcome to Surf's Up!: Hawai'i Climate API<br/>"
            f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>"
            f"Available Routes:<br/>"
            f"/api/v1.0/stations ~~~~~ a list of all weather observation stations<br/>"
            f"/api/v1.0/precipitaton ~~ the latest year of preceipitation data<br/>"
            f"/api/v1.0/temperature ~~ the latest year of temperature data<br/>"
            f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>"
            f"~~~ datesearch (yyyy-mm-dd)<br/>"
            f"/api/v1.0/datesearch/2015-05-30  ~~~~~~~~~~~ low, high, and average temp for date given and each date after<br/>"
            f"/api/v1.0/datesearch/2015-05-30/2016-01-30 ~~ low, high, and average temp for date given and each date up to and including end date<br/>"
            f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<br/>"
            f"~ data available from 2010-01-01 to 2017-08-23 ~<br/>"
            f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(station.name).all()
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/precipitaton")
def precipitation():
    
    results = (session.query(measurement.date, measurement.prcp, measurement.station)
                      .filter(measurement.date > year_prior)
                      .order_by(measurement.date)
                      .all())
    
    precip_data = []
    for result in results:
        precip_dict = {result.date: result.prcp, "Station": result.station}
        precip_data.append(precip_dict)

    return jsonify(precip_data)

@app.route("/api/v1.0/temperature")
def temperature():

    results = (session.query(measurement.date, measurement.tobs, measurement.station)
                      .filter(measurement.date > year_prior)
                      .order_by(measurement.date)
                      .all())

    temp_data = []
    for result in results:
        temp_dict = {result.date: result.tobs, "Station": result.station}
        temp_data.append(temp_dict)

    return jsonify(temp_data)

@app.route('/api/v1.0/datesearch/<startDate>')
def start(startDate):
    sel = [measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]

    results =  (session.query(*sel)
                       .filter(func.strftime("%Y-%m-%d", measurement.date) >= startDate)
                       .group_by(measurement.date)
                       .all())

    dates = []                       
    for result in results:
        date_dict = {}
        date_dict["Date"] = result[0]
        date_dict["Low Temp"] = result[1]
        date_dict["Avg Temp"] = result[2]
        date_dict["High Temp"] = result[3]
        dates.append(date_dict)
    return jsonify(dates)

@app.route('/api/v1.0/datesearch/<startDate>/<endDate>')
def startEnd(startDate, endDate):
    sel = [measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]

    results =  (session.query(*sel)
                       .filter(func.strftime("%Y-%m-%d", measurement.date) >= startDate)
                       .filter(func.strftime("%Y-%m-%d", measurement.date) <= endDate)
                       .group_by(measurement.date)
                       .all())

    dates = []                       
    for result in results:
        date_dict = {}
        date_dict["Date"] = result[0]
        date_dict["Low Temp"] = result[1]
        date_dict["Avg Temp"] = result[2]
        date_dict["High Temp"] = result[3]
        dates.append(date_dict)
    return jsonify(dates)

if __name__ == "__main__":
    app.run(debug=True)