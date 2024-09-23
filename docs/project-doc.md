# Proposal: California Weather Data Analysis and Forecasting

## **Project Summary: Weather Data Analysis and Forecasting**

### **Project Goals:**
The primary goal of this project is to develop a robust system for forecasting weather conditions in California using historical weather data from 1970. Specifically, the project will focus on applying time series analysis to predict weather patterns and detect anomalies that may indicate significant shifts in climate or unexpected weather events. The system will be designed to support disaster preparedness efforts by providing early warnings for extreme weather events such as wildfires and droughts.

### **Early Warning System:**

The early warning system will be a core feature of the weather forecasting platform, designed to alert users of potential extreme weather events or anomalies, such as wildfires, heatwaves, droughts, and floods, based on historical and real-time weather data. The goal is to make this system **simple and user-friendly**, so individuals and organizations can easily implement it in their day-to-day operations.

#### **How the Early Warning System Works:**
1. **Anomaly Detection:** 
   - The system will continuously monitor weather data and compare current conditions with historical patterns to identify potential anomalies.
   - Anomalies may include significant deviations in temperature, precipitation, humidity, or wind speed—indicators of extreme weather events.
   
2. **Threshold-Based Alerts:**
   - The system will define thresholds for various weather variables (e.g., heat levels, rainfall amounts, humidity) based on historical data and regional climate trends.
   - When these thresholds are exceeded (e.g., unusually high temperatures that could indicate wildfire risk or sudden drops in precipitation signaling potential drought), the system will trigger an alert.

3. **Prediction of Extreme Events:**
   - Using machine learning models such as LSTM, the system can predict short-term weather conditions (e.g., the likelihood of a wildfire or extreme rainfall within the next few days).
   - The model will provide probabilistic forecasts for extreme events and anomalies, helping users make informed decisions.

### **User Implementation and Benefits:**

The system’s early warning functionality will be delivered through a **simple, accessible interface** that can be customized for different user needs. Here’s how users can implement and benefit from the early warning system:

#### **1. Web-Based Dashboard:**
   - **Implementation:** Users can access a web-based dashboard that provides real-time weather forecasts and displays alerts for extreme weather events.
     - Users can configure their preferences by setting the types of alerts they want to receive (e.g., heatwave alerts, wildfire risk alerts) and the regions they are monitoring.
     - The dashboard will provide visualizations such as time series plots of temperature and precipitation, heatmaps for regional anomalies, and notifications of potential extreme events.
   - **Benefit:** This provides a **centralized, real-time overview** of the weather conditions and predictions for specific regions, helping users stay updated on potential risks.

#### **2. SMS/Email Notifications:**
   - **Implementation:** The system can send **automated notifications** via SMS or email when an anomaly is detected or when there is a high probability of extreme weather.
     - Users can subscribe to receive notifications for specific events, such as drought warnings, flooding risks, or fire hazards, tailored to their region and risk tolerance.
     - Alerts can include key information such as predicted weather conditions, probability of the event, and suggested actions (e.g., prepare for potential water restrictions or wildfire evacuation plans).
   - **Benefit:** Users can **receive timely alerts directly to their phones or inboxes**, allowing them to take action even if they are not actively monitoring the dashboard.

#### **Broader Impacts:**

### **1. Integration of Historical and Real-Time Data**
- **Existing Systems:** Many existing models prioritize real-time weather data and focus on short-term predictions without deeply leveraging historical data for long-term trends or anomaly detection.
- **Your Project:** Your project integrates **50+ years of historical weather data** (NOAA) with **real-time data** (OpenWeatherMap), allowing for robust time series analysis and the detection of long-term weather trends and anomalies.
  - **Benefit:** Enhanced ability to identify seasonal patterns and climate shifts that could signal important long-term changes, providing valuable insights for climate research and future planning.

### **2. Anomaly Detection for Extreme Weather Events**
- **Existing Systems:** While current weather systems can forecast extreme events (e.g., storms, heatwaves), they often rely on short-term meteorological data without detecting patterns that deviate significantly from historical norms.
- **Your Project:** By applying **anomaly detection techniques** (Z-score, IQR), the system can detect **unusual weather events** that are outliers compared to historical patterns. This can give **early warnings** for events like droughts, extreme heat, or irregular rainfall that may not be immediately visible through traditional forecasts.
  - **Benefit:** Proactive identification of extreme or unusual weather conditions, enabling earlier preparation and better resource management.

### **3. Tailored for Agriculture and Disaster Preparedness**
- **Existing Systems:** Traditional weather forecasts are generalized and often not optimized for specific industries like agriculture or sectors focused on disaster preparedness.
- **Your Project:** The system is explicitly designed to cater to the needs of **agriculture** (e.g., planting schedules, irrigation management) and **disaster preparedness** (e.g., predicting wildfires, floods). The forecasts will consider both **short-term predictions** and **long-term climate trends**, which are critical for these sectors.
  - **Benefit:** Targeted insights that provide practical value to farmers, policymakers, and emergency responders, offering decision-making tools that are directly applicable to their specific needs.

#### **Data Sources:**

The project will utilize the following key data sources:

1. **NOAA Climate Data:** Provides comprehensive historical weather data, including temperature and precipitation records, essential for analyzing long-term climate trends and patterns in California.

2. **OpenWeatherMap API:** Offers real-time weather data, including current temperature and precipitation, crucial for accurate short-term weather forecasts and anomaly detection.

#### **Key Components:**
1. **Time Series Analysis:** Analyze historical weather data specific to California from 1970 to the present, focusing on key variables such as temperature, precipitation, and humidity. This analysis will identify long-term trends and seasonal patterns unique to different regions of California, such as coastal, inland, and mountainous areas. By understanding these patterns, we can establish a solid foundation for developing predictive models that account for California's diverse climate variations.

2. **Machine Learning Models:**
   - Develop and train an LSTM (Long Short-Term Memory) model to forecast future weather conditions for California based on the identified trends and seasonal patterns. The model will specifically predict:
     - **Daily temperature fluctuations** (maximum and minimum temperatures) to assist in understanding heatwaves or cold spells.
     - **Precipitation patterns** to forecast the likelihood and intensity of rain, which is critical for water resource management and agriculture.
     - **Humidity levels** to predict changes that may impact comfort levels and agricultural practices.
   - The model will be trained on historical data, focusing on short-term predictions (e.g., up to 7 days ahead) while incorporating features such as time lags, seasonality indicators, and geographical information to enhance forecast accuracy tailored to specific regions within California.

#### **Possible Geographical Division**
1. **Coastal Region:**
- **San Francisco, CA**
  - **Reason:** San Francisco is well-known for its coastal fog, mild temperatures, and proximity to the Pacific Ocean, making it an ideal location for studying the climate of the coastal region.   - Characterized by mild temperatures, higher humidity, and frequent coastal fog.
   - Influenced by the Pacific Ocean, with distinct seasonal variations.

2. **Inland Empire:**
- **Riverside, CA**
  - **Reason:** Riverside is located in the heart of the Inland Empire, featuring a semi-arid climate with hot summers and cooler winters, and is less influenced by coastal weather patterns.   - Features a semi-arid climate with hotter summers and cooler winters.
   - Less influenced by coastal weather patterns, leading to more pronounced temperature fluctuations.

3. **Central Valley:**
- **Fresno, CA**
  - **Reason:** Fresno is a major city in the Central Valley and represents the region’s hot summers and agricultural significance, as well as its Mediterranean climate with dry summers and wet winters.   - Known for its agricultural productivity and hot summers.
   - Experiences a Mediterranean climate with dry summers and wet winters.

4. **Mountain Region:**
- **South Lake Tahoe, CA**
  - **Reason:** Located in the Sierra Nevada range, South Lake Tahoe experiences cold winters with heavy snowfall, making it a key area for understanding the mountain climate.   - Characterized by colder temperatures and significant snowfall in winter.
   - Seasonal variations are pronounced, with temperature changes depending on elevation.

5. **Desert Region:**
- **Palm Springs, CA**
  - **Reason:** Palm Springs is a well-known desert city with extremely hot summers, mild winters, and minimal precipitation, representing the unique desert climate.   - Features extreme temperatures, with very hot summers and mild winters.
   - Receives low precipitation and has unique weather patterns compared to other regions.

6. **Northern California:**
- **Eureka, CA**
  - **Reason:** Located on the Redwood Coast, Eureka experiences significant seasonal precipitation and diverse microclimates, including coastal fog and inland heat, making it ideal for representing Northern California’s climate.   - Known for its diverse microclimates, from coastal fog to inland heat.
   - Experiences significant seasonal variation, particularly in precipitation.

7. **Southern California:**
- **Los Angeles, CA**
  - **Reason:** Los Angeles is a major city in Southern California, characterized by a warm Mediterranean climate with dry summers and variable weather patterns between coastal and inland areas.   - Characterized by a warm Mediterranean climate with dry summers.
   - Weather patterns can vary significantly between coastal and inland areas.


## **Data Sources**

For this project, the data will be sourced from both existing datasets provided by established weather data providers and potentially some data that will be collected or integrated manually. The project will combine data from at least two sources to enhance the robustness and accuracy of the analysis and forecasts.

#### **Data Sources:**

1. **NOAA Climate Data**
   - **Data Available:** Provides comprehensive historical weather data, including temperature and precipitation records crucial for analyzing long-term climate trends.
   - **Collected By:** NOAA, using a network of ground-based stations, satellites, and ocean buoys.
   - **Data Collection Method:** Historical records are collected from various observational platforms to ensure accuracy and consistency.

2. **OpenWeatherMap API**
   - **Data Available:** Offers real-time weather data, including current temperature and precipitation, essential for short-term weather forecasting and anomaly detection.
   - **Collected By:** OpenWeatherMap, aggregating data from weather stations and satellites.
   - **Data Collection Method:** Real-time data is collected through a global network of weather stations and sensors, complemented by satellite imagery.


## **Expected Major Findings**

In this project, several key findings are anticipated, based on the analysis of historical and real-time weather data. These findings will provide valuable insights into weather patterns, forecasting accuracy, and potential climate trends. Below are the main areas of exploration and the expected outcomes:

#### **1. Identification of Seasonal Weather Patterns**
   - **Expected Finding:** 
     - Analyze historical weather data to identify consistent seasonal patterns, such as typical temperature and precipitation trends throughout the year.
   - **Value:** 
     - Improved seasonal weather forecasts will support agricultural planning and preparation for seasonal climate variations.

#### **2. Development of Accurate Short-Term Weather Forecasts**
   - **Expected Finding:** 
     - Develop machine learning models to provide accurate short-term weather forecasts, including temperature and precipitation for the next few days.
   - **Value:** 
     - Enhanced short-term forecasts will aid day-to-day decision-making in sectors like transportation and emergency management.

### **Objective Discussion:**

- **Impact and Utility:**
  - This project aims to improve short-term weather forecasts and enhance understanding of seasonal weather patterns. Accurate forecasts will benefit agriculture, emergency management, and daily decision-making. Additionally, identifying seasonal trends will provide insights into climate variations and inform broader climate research.

- **Main Claims and Questions:**
  - *Claim 1:* The project will accurately predict seasonal weather patterns using historical data, enhancing the reliability of seasonal forecasts.
  - *Claim 2:* Machine learning models will provide accurate short-term weather predictions, validated through comparison with real-time and historical data.
  - *Claim 3:* Anomaly detection will identify unusual weather events, offering early warnings for extreme conditions.

  - *Question 1:* What are the key seasonal weather patterns in California, and how can they be predicted with high accuracy?
  - *Question 2:* How effective are machine learning models in forecasting short-term weather conditions compared to traditional methods?

## Data Summary and Statistical Analysis

### **1. Time Series Line Plot (Weather Variables Over Time)**
   - **Purpose:** Visualize trends and seasonal patterns in weather data over time for each region.
   - **Variables:** Temperature, precipitation, humidity.
   - **Details:**
     - Create a **line plot** to show the evolution of these variables (temperature, precipitation, humidity) over time for each location (e.g., San Francisco, Fresno, Palm Springs).
     - Overlay the variables for comparison and look for patterns like seasonal fluctuations or anomalies.
   - **Why it’s useful:** It will help you observe trends over time and highlight seasonal changes, showing how different regions (coastal vs. desert) experience varying weather patterns.
   - **Tools:** Matplotlib, Plotly (for interactive exploration).

### **2. Heatmap (Seasonal Variations by Region)**
   - **Purpose:** Show how weather variables (e.g., temperature, precipitation) vary across different regions and seasons.
   - **Variables:** Temperature, precipitation.
   - **Details:**
     - Create a **heatmap** with months on the x-axis and regions (e.g., San Francisco, Riverside, South Lake Tahoe) on the y-axis.
     - Use color gradients to show the magnitude of the weather variable (e.g., average temperature or precipitation).
   - **Why it’s useful:** This will clearly illustrate regional and seasonal differences in weather conditions, making it easy to identify periods of extreme temperatures or precipitation.
   - **Tools:** Seaborn, Plotly.

### **3. Box Plot (Weather Variability Across Regions)**
   - **Purpose:** Compare the variability in key weather variables (e.g., temperature, precipitation) across regions.
   - **Variables:** Temperature, precipitation.
   - **Details:**
     - Use a **box plot** to show the spread, median, and outliers for temperature and precipitation across different regions.
     - This will help identify which regions experience more extreme weather variability (e.g., higher temperatures in Palm Springs vs. cooler conditions in South Lake Tahoe).
   - **Why it’s useful:** This will allow for a visual comparison of the range and variability of weather conditions across regions, highlighting extremes.
   - **Tools:** Matplotlib, Seaborn.

### **4. Geographic Map (Spatial Visualization of Weather Data)**
   - **Purpose:** Visualize the spatial distribution of weather data (e.g., average temperature, precipitation) across the state of California.
   - **Variables:** Temperature, precipitation.
   - **Details:**
     - Use a **choropleth map** to show the average temperature or precipitation for each region (e.g., San Francisco, Riverside, Fresno).
     - Alternatively, use **bubble maps** to display weather extremes (larger bubbles for higher values).
   - **Why it’s useful:** A geographic map will allow you to visualize how weather patterns vary spatially across California and identify regional differences in temperature or precipitation.
   - **Tools:** Plotly, Folium, Geopandas.

### **5. Scatter Plot (Temperature vs. Precipitation by Region)**
   - **Purpose:** Examine the relationship between temperature and precipitation in different regions.
   - **Variables:** Temperature, precipitation.
   - **Details:**
     - Use a **scatter plot** to display temperature on one axis and precipitation on the other.
     - Add different colors or markers to represent each region (e.g., San Francisco, Palm Springs) to see how regions differ in the relationship between temperature and precipitation.
   - **Why it’s useful:** This plot will allow you to see if regions with higher temperatures (e.g., Palm Springs) have less precipitation, and vice versa.
   - **Tools:** Matplotlib, Seaborn.

### **6. Anomaly Detection Plot (Highlighting Extreme Weather Events)**
   - **Purpose:** Visualize anomalies in the weather data to identify extreme events (e.g., heatwaves, heavy rainfall).
   - **Variables:** Temperature, precipitation, humidity.
   - **Details:**
     - Use a **time series plot** with annotations to highlight anomalies, such as periods where temperature or precipitation significantly deviates from the norm.
     - Use **Z-scores** or **IQR method** to detect and mark these anomalies on the plot.
   - **Why it’s useful:** This will allow you to identify and visually highlight extreme weather events (e.g., record heatwaves in Palm Springs, or unusual rainfall in Eureka), which are important for understanding regional climate variability.
   - **Tools:** Matplotlib, Plotly.


### **Why These Plots are Informative:**
- **Time Series Line Plot:** Helps track changes over time, essential for understanding long-term trends and seasonal patterns.
- **Heatmap:** Offers a clear visualization of seasonal and regional variations, making it easier to compare different times and locations.
- **Box Plot:** Highlights variability and extremes, which are key to understanding regional climate behavior.
- **Geographic Map:** Provides spatial context, essential for a project covering different geographical regions.
- **Scatter Plot:** Explores relationships between key variables like temperature and precipitation.
- **Anomaly Detection Plot:** Focuses on outliers and extreme events, critical for identifying climate anomalies.


## **Preprocessing Steps**

1. **Data Collection:**
   - **OpenWeatherMap API:**
     - Retrieve real-time weather data for specified locations, including temperature, humidity, wind speed, precipitation, and atmospheric pressure.
     - Fetch historical weather data for the same locations to facilitate comparison with real-time data.

   - **NOAA Climate Data:**
     - Download historical weather records, focusing on temperature and precipitation data from specified time periods.
     - Ensure data includes relevant climatic indicators for California, such as long-term temperature trends and seasonal variations.

2. **Data Cleaning:**
   - **Handling Missing Values:**
     - Identify and address any missing or null values in the dataset. Employ interpolation methods for missing numerical values and imputation techniques for categorical variables.
     - Remove or flag incomplete records that cannot be accurately imputed.

   - **Outlier Detection:**
     - Detect and investigate outliers using statistical methods (e.g., Z-scores, IQR). Determine if they result from data entry errors or represent genuine anomalies.
     - Apply appropriate transformation or correction methods to handle outliers.

   - **Data Consistency:**
     - Standardize units of measurement (e.g., temperature in Celsius or Fahrenheit, precipitation in millimeters or inches) across datasets.
     - Ensure consistency in timestamp formats and time zones for accurate time series analysis.

3. **Data Integration:**
   - **Combining Data Sources:**
     - Merge datasets from OpenWeatherMap and NOAA by aligning timestamps and geographic locations.
     - Create a unified dataset that integrates real-time and historical data for comprehensive analysis.

   - **Resampling and Aggregation:**
     - Aggregate data to appropriate time intervals (e.g., daily, weekly) to match the analysis requirements.
     - Resample data to ensure uniform time intervals and handle any discrepancies in the temporal resolution.

4. **Feature Engineering:**
   - **Creating New Features:**
     - Generate additional features such as moving averages, seasonal indicators, and anomaly flags based on historical weather patterns.
     - Create features that capture interactions between different weather variables (e.g., humidity-temperature interactions).

   - **Normalization and Scaling:**
     - Normalize or scale numerical features to ensure they are on a comparable scale, which is important for machine learning model performance.
     - Apply methods such as Min-Max scaling or Standardization as appropriate.

5. **Data Validation:**
   - **Verification:**
     - Cross-check the preprocessed data with source data to ensure accuracy and completeness.
     - Validate the consistency and integrity of the dataset by comparing with known benchmarks or historical records.

   - **Exploratory Data Analysis (EDA):**
     - Perform initial exploratory analysis to understand data distributions, correlations, and patterns.
     - Use visualization techniques to identify trends, seasonality, and potential data issues.


<!--- 
----------
The following sections should be used for the full proposal document. These are not required for the proposal draft discussion.
----------
-->




## Basic Data Properties and Analysis Techniques

### **1. Data Overview and Summary Statistics**

**Objective:**
To provide an initial understanding of the datasets by summarizing key characteristics and overall distributions of the data.

**Techniques:**
- **Descriptive Statistics:**
  - **Mean, Median, and Mode:** Calculate these central tendency measures for continuous variables such as temperature, precipitation, and humidity to understand the average conditions.
  - **Standard Deviation and Variance:** Measure the variability of weather variables to assess the spread and dispersion of the data.
  - **Min and Max Values:** Identify the range of weather conditions to understand the extremes observed in the dataset.

- **Distribution Analysis:**
  - **Histograms:** Create histograms to visualize the frequency distribution of continuous variables (e.g., temperature, precipitation).
  - **Box Plots:** Use box plots to visualize the spread, central tendency, and potential outliers in the data.

### **2. Temporal Analysis**

**Objective:**
To analyze how weather variables change over time and identify notable patterns or trends.

**Techniques:**

- **Seasonal Decomposition (STL Decomposition):**
  - **Implementation Plan:** Use the STL decomposition method to break down the historical weather data into seasonal, trend, and residual components. This will involve:
    - Selecting a suitable time frame (e.g., daily or monthly data) to capture seasonal variations accurately.
    - Applying the STL decomposition function from libraries such as `statsmodels` in Python to visualize and analyze each component. 
    - Assessing the seasonal patterns across different regions in California to identify variations in temperature and precipitation that align with specific seasons.

- **Autoregressive Integrated Moving Average (ARIMA):**
  - **Implementation Plan:** Fit ARIMA models to forecast future weather conditions by:
    - Conducting exploratory data analysis (EDA) to determine the appropriate differencing needed for stationarity.
    - Using autocorrelation function (ACF) and partial autocorrelation function (PACF) plots to identify the optimal order of the ARIMA model (p, d, q).
    - Training the ARIMA model on the historical data, focusing on key weather variables such as temperature and precipitation.
    - Validating the model’s performance using metrics like Mean Absolute Error (MAE) and comparing predicted values against actual observations for accuracy.


### **3. Anomaly Detection**

**Objective:**
To identify unusual or extreme weather events that deviate significantly from historical norms.

**Techniques:**

- **Z-Score Analysis:**
  - **Implementation Plan:** 
    - Calculate the mean and standard deviation of key weather variables (e.g., temperature, precipitation) using historical data from California.
    - For each data point in the dataset, compute the Z-score using the formula.
    - Identify anomalies as data points with Z-scores exceeding a threshold (e.g., ±3), indicating significant deviations from normal weather conditions. 
    - Visualize the results using time series plots to highlight the identified anomalies and their corresponding dates.

- **Interquartile Range (IQR) Method:**
  - **Implementation Plan:**
    - Calculate the first (Q1) and third quartiles (Q3) of the weather data distribution to determine the IQR.
    - Define lower and upper bounds for detecting outliers:
    - Flag any data points that fall outside these bounds as potential anomalies. 
    - Apply this method to each weather variable and visualize the identified outliers using box plots or scatter plots to provide context for the extreme values.

### **4. Data Completeness and Integrity**

**Objective:**
To assess the quality of the data and identify any issues related to missing or inconsistent entries.

**Techniques:**
- **Missing Value Analysis:**
  - **Missingness Patterns:** Analyze patterns of missing values to understand their distribution and potential impact on the analysis.
  - **Imputation Strategies:** Evaluate and apply appropriate imputation methods to address missing data, ensuring minimal disruption to the analysis.

- **Data Consistency Checks:**
  - **Data Validation:** Verify data integrity by comparing against known benchmarks or historical data to ensure accuracy and consistency.


## Automation, Scalability, and Portability

### **1. Automation**

**Objective:**
To streamline data processing and minimize manual intervention, allowing for efficient updates and analysis.

**Techniques:**
- **Scheduled Data Retrieval:** Utilize Heroku Scheduler or cron jobs to automate the regular fetching of new weather data from APIs, ensuring the system is continuously updated with the latest information.
- **Automated Data Processing Pipelines:** Implement ETL processes using MongoDB to efficiently manage and transform incoming data, ensuring consistency and reducing processing time.
- **Error Handling:** Establish comprehensive logging and alert systems to monitor data processing activities, enabling rapid identification and resolution of any issues that arise.

### **2. Scalability**

**Objective:**
To design the system to handle increasing data volumes and user demands without compromising performance.

**Techniques:**
- **Cloud Services:** Leverage Heroku’s scalable infrastructure to dynamically adjust resources based on user demand and data volume, ensuring optimal performance during peak usage.
- **Database Optimization:** Utilize MongoDB's flexible schema and indexing capabilities to manage large datasets efficiently, allowing for quick queries and data retrieval.
- **Load Balancing:** Implement load balancing techniques to distribute incoming traffic evenly across multiple instances, ensuring consistent performance and responsiveness under heavy loads.

### **3. Portability**

**Objective:**
To ensure the system can be easily adapted to various environments with minimal modifications.

**Techniques:**
- **Containerization:** Use Docker to containerize the application and its dependencies, ensuring consistent behavior across development, staging, and production environments.
- **Configuration Management:** Utilize environment variables and configuration files to manage environment-specific settings, facilitating easy deployment in different contexts without hardcoding values.
- **Documentation:** Maintain detailed documentation of the system architecture, setup procedures, and dependencies, alongside version control (e.g., Git), to streamline knowledge transfer and adaptation for future developers.

### **4. Future Considerations**

**Objective:**
To prepare for ongoing enhancements and the integration of new features as project requirements evolve.

**Techniques:**
- **Modular Design:** Structure the system with modular components that can be independently updated or replaced, allowing for easy integration of new features without disrupting existing functionality.
- **Extensible Architecture:** Develop well-defined APIs and interfaces that facilitate the addition of new data sources or analytical methods, ensuring the system can adapt to emerging needs and technologies.

<!--- 
----------
The following sections should be used for the analysis planning. These are not required for the proposal document submission.
----------
-->



## Data Analysis and Algorithms
<!--- List and describe what types of (advanced) analysis you plan to conduct. This section should be tied back to the expected major findings. (If needed, you can update the findings section.) When selecting algorithms to obtain the analysis results, provide a brief explanation of the algorithmic properties and logic. You should clearly define the inputs and outputs of each algorithm. -->




<!--- 
----------
The following sections should be used for the analysis outcome presentation. These are not required for the analysis plan submission.
----------
-->
# Analysis Outcomes
<!--- Explain the analysis you conducted and show the results. Discuss how the data, your analysis, and/or visualization can support the claims or findings. What will be the recommendations or suggestions you can make based on the results? Use bullet points, tables, and figures (if possible) to increase the readability of the document. -->



<!--- 
----------
The following sections should be used for the visualization planning. These are not required for the analysis outcome presentation.
----------
-->


# Visualization
## Visualization Plan
<!--- List and explain what types of plots you plan to provide and what you are trying to show through the diagrams. You should explore the best way to visualize the information and message based on the lectures on visualization and related topics. It is required to have at least two interactive graphing and five static plots. -->

## Web Page Plan
<!--- Explain how many pages you will have in total and what content will be shown in each page. (Each diagram discussed above should be given a proper location in this section. Also, it is required to have (1) "Project Objective" page, which explains the main goals and data sources, and (2) "Analytical Methods" page, where you explain the major techniques used in the project and provide further references. -->
