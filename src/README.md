# Source Codes
<!--- This directory stores all source codes used in this project -->


## Webpage Generation Instructions
#### Sample query: 
- http://127.0.0.1:5000/current-weather?lat=37.7749&lon=-122.4194
- http://127.0.0.1:5000/current-weather?city_name=Los%20Angeles

## List of Endpoints for OpenWeather API
### **Types of Data to Collect from the OpenWeather API**

1. **Current Weather Data:**
   - **Temperature:** Current temperature in Celsius or Fahrenheit.
   - **Humidity:** Percentage of humidity in the air.
   - **Pressure:** Atmospheric pressure in hPa.
   - **Wind Speed and Direction:** Wind speed in meters per second and wind direction in degrees.
   - **Weather Conditions:** Descriptions (e.g., clear sky, rain) and corresponding weather icons.
   - **Precipitation:** Rainfall or snowfall in the last hour or day, measured in millimeters.
   - **Cloud Coverage:** Percentage of the sky covered by clouds.

2. **Historical Weather Data:**
   - **Temperature:** Historical daily temperature data (min, max, and average).
   - **Precipitation:** Historical daily precipitation data.
   - **Humidity:** Historical daily humidity data.
   - **Wind Speed:** Historical wind speed data.
   - **Pressure:** Historical atmospheric pressure data.
   - **Weather Conditions:** Historical weather condition descriptions.

3. **Forecast Data:**
   - **Short-term Forecasts:** Hourly forecasts for the next 48 hours, including all variables listed in current weather data.
   - **Medium-term Forecasts:** Daily forecasts for the next 7 days, including temperature (min/max), humidity, wind speed, and precipitation.
   - **Long-term Forecasts:** If available, forecast data for the next 16 days.

4. **Geographic Data:**
   - **Location Data:** Latitude and longitude coordinates for specific locations within California.
   - **Elevation Data:** Elevation of the location, which can impact weather patterns.

5. **Anomaly Detection Data:**
   - **Extreme Weather Events:** Data on historical and real-time extreme weather events (e.g., heatwaves, heavy rainfall, droughts).
   - **Deviation from Norm:** Data showing deviation from historical norms for temperature, precipitation, etc.

6. **Climatic Data for Long-term Analysis:**
   - **Seasonal Averages:** Long-term averages of temperature, precipitation, and other variables for seasonal trend analysis.
   - **Climate Normals:** 30-year averages for comparison with current weather conditions.

### **Feasible List of Endpoints to Implement**

1. **Current Weather Data Endpoint:**
   - **Endpoint:** `/current-weather`
   - **Method:** `GET`
   - **Parameters:** `city_name`, `lat`, `lon`
   - **Description:** Retrieves the current weather data for a specific city or coordinates.

2. **Historical Weather Data Endpoint:**
   - **Endpoint:** `/historical-weather`
   - **Method:** `GET`
   - **Parameters:** `lat`, `lon`, `start_date`, `end_date`
   - **Description:** Retrieves historical weather data for a specific location between the specified start and end dates.

3. **Short-term Forecast Endpoint:**
   - **Endpoint:** `/forecast/hourly`
   - **Method:** `GET`
   - **Parameters:** `lat`, `lon`
   - **Description:** Provides an hourly weather forecast for the next 48 hours for a specific location.

4. **Medium-term Forecast Endpoint:**
   - **Endpoint:** `/forecast/daily`
   - **Method:** `GET`
   - **Parameters:** `lat`, `lon`
   - **Description:** Provides a daily weather forecast for the next 7 days for a specific location.

5. **Long-term Forecast Endpoint:**
   - **Endpoint:** `/forecast/long-term`
   - **Method:** `GET`
   - **Parameters:** `lat`, `lon`
   - **Description:** Provides a long-term weather forecast for the next 16 days if supported by the API.

6. **Extreme Weather Events Endpoint:**
   - **Endpoint:** `/anomalies/extreme-weather`
   - **Method:** `GET`
   - **Parameters:** `lat`, `lon`, `start_date`, `end_date`
   - **Description:** Retrieves data on extreme weather events for a specific location during the specified period.

7. **Climate Trends Analysis Endpoint:**
   - **Endpoint:** `/climate/trends`
   - **Method:** `GET`
   - **Parameters:** `lat`, `lon`, `variable` (e.g., temperature, precipitation)
   - **Description:** Analyzes long-term trends in specific weather variables for a given location.

8. **Data Collection Scheduler Endpoint:**
   - **Endpoint:** `/data-collection/schedule`
   - **Method:** `POST`
   - **Parameters:** `interval` (e.g., hourly, daily)
   - **Description:** Allows the scheduling of automated data collection at specified intervals.

9. **Data Aggregation and Summary Endpoint:**
   - **Endpoint:** `/data/summary`
   - **Method:** `GET`
   - **Parameters:** `lat`, `lon`, `period` (e.g., last 7 days, last month)
   - **Description:** Provides a summary of weather data for the specified period, useful for initial analysis or reporting.