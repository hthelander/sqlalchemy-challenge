import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# import Flask
from flask import Flask, jsonify

# Create app
app = Flask(__name__)


# set home page
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the climate data API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-05-01<br/>"
        f"/api/v1.0/2016-04-30/2017-04-30<br/>"
        
    )


# 4. De
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'precipitation' page...")

    session = Session(engine)  
    
    # enddate = session.query(measurement.date).order_by(measurement.date.desc()).first()
    enddate ='2016-08-23'
    prcp_results = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date >= enddate).all()
    
    session.close()

    
    all_precipitation= []
    for date, prcp in prcp_results:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_precipitation.append(prcp_dict)

    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def station():
    print("Server received request for 'station' page...")

    session = Session(engine)  
    station_results = session.query(Station.station).all()
    
   
    session.close()

    all_stations = list(np.ravel(station_results))

    return jsonify(all_stations)


    
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received a request for TOBS page...")

    session = Session(engine)  
    tobs_results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281', Measurement.date >='2016-08-23').all()
    
   
    session.close()

    all_tobs = list(np.ravel(tobs_results))

    return jsonify(all_tobs)


@app.route("/api/v1.0/2017-05-01")
def start():
    print("Server received a request for 2017-05-01 page...")

    session = Session(engine)  
    startdate_results = session.query(func.min(Measurement.tobs), 
              func.avg(Measurement.tobs),
              func.max(Measurement.tobs)).filter(Measurement.station == 'USC00519281', Measurement.date >= '2017-05-01').all()
    session.close()

      
    startdate_sum = list(np.ravel(startdate_results))
   


    return jsonify(startdate_sum)




            

@app.route("/api/v1.0/2016-04-30/2017-04-30")
def start_end():
    session = Session(engine)
    start_end_results = session.query(func.min(Measurement.tobs), 
              func.avg(Measurement.tobs),
              func.max(Measurement.tobs)).filter(Measurement.station == 'USC00519281', Measurement.date >= '2016-04-30', Measurement.date <= '2017-04-30').all()
    session.close()

      
    start_end_sum = list(np.ravel(start_end_results))
   


    return jsonify(start_end_sum)




if __name__ == "__main__":
    app.run(debug=False)