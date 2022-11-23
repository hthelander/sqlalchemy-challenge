# sqlalchemy-challenge
module 10 challenge

## INITIAL SQLITE EXPLORATION

Necessary libraries were imported and an engine was set up for querying sessions.  Classes/Tables were stored from data in the database.  Initial exploration of the data was performed in jupyter notebook.  A barchart was produced to track precipitation data from all weather stations for the last year in the dataset:
![](Images/barchart.png)

A histogram was also produced using the data from the most active weather station:
![](Images/histogram.png)

Then the queries initially created in jupyter notebook were used in flask to return JSonified lists and dictionaries for API data calls from the following URLs:

        "api/v1.0/precipitation"
        "api/v1.0/stations"
        "/api/v1.0/tobs"
        "/api/v1.0/2017-05-01"
        "/api/v1.0/2016-04-30/2017-04-30"

