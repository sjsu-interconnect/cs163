# Proposal: Fresno Weather Data Analysis and Forecasting

## **Project Summary: Weather Data Analysis and Forecasting**

### **Project Goals:**
The primary goal of this project is to develop a basic and easy-to-implement system for forecasting short-term weather conditions in **Fresno County** and analyzing their correlation to **tomato and almond yields**. The project will apply time series analysis to predict daily weather patterns, such as temperature and precipitation, from **1979 to the present**, focusing on **Fresno County’s crop data**. By examining the relationship between weather and crop yield, the project aims to assist farmers in optimizing planting, irrigation, and harvesting schedules.

### **Specific Crops and Timeframe:**
The project will focus on the following crops, selected due to their economic importance in **Fresno** and the availability of historical yield data:
- **Almonds:** A major crop in Fresno, sensitive to temperature and water availability.
- **Tomatoes:** Widely grown and sensitive to temperature fluctuations, with high economic value.

The analysis will cover the period from **1979 to the present**, utilizing both historical crop yield data and weather data for each growing season in the Central California region, which includes Fresno County, and various other ``['Fresno', 'Sacramento', 'San Joaquin', 'Stanislaus', 'Merced', 'Madera', 'Kings', 'Tulare',
               'Kern', 'Yolo', 'Colusa', 'Sutter', 'Butte', 'Glenn', 'Tehama']``

### **Key Features:**

1. **Short-Term Weather Prediction:**
   - The system will predict daily weather conditions, focusing on key variables such as temperature, precipitation, and humidity, from 1979 to the present.
   - Time series analysis and simple machine learning models will generate these predictions, helping farmers anticipate weather conditions for upcoming days and plan agricultural activities accordingly.

2. **Correlation with Crop Yield:**
   - The project will analyze historical crop yield data for **almonds and tomatoes** alongside weather conditions to identify how short-term weather changes (e.g., heatwaves, rainfall) impact crop productivity.
   - The system will focus on identifying specific correlations between weather variables and crop yields, aiming to provide actionable insights for agricultural planning in Fresno.

---

### **User Implementation and Benefits:**

#### **1. Simple Web-Based Dashboard:**
   - **Implementation:** A straightforward web-based dashboard will provide daily weather forecasts and display visualizations (e.g., temperature trends, rainfall predictions) with a focus on crop yield impact.
     - Users can access real-time weather data and track how forecasted conditions might impact yields for **almonds** and **tomatoes**, based on historical correlations.
     - The dashboard will offer simple, easy-to-read graphs and alerts tailored to these two crops.
   - **Benefit:** Farmers will gain a **quick overview** of the predicted weather and its potential impact on specific crop yields, enabling better decision-making for daily agricultural activities.

#### **2. Basic Alerts for Critical Weather Conditions:**
   - **Implementation:** The system will send basic alerts via SMS or email when critical weather conditions (e.g., excessive heat or lack of rainfall) are forecasted.
     - Users can set preferences for receiving alerts based on conditions likely to affect **almonds** or **tomatoes**, such as heat alerts for almonds or drought warnings for tomatoes.
   - **Benefit:** The alerts will help farmers take **timely action** to protect crops from adverse weather conditions, such as adjusting irrigation or delaying planting during extreme heat.

#### **Data Sources:**
The project will utilize the following key data sources:

1. **NOAA Climate Data:** Provides comprehensive historical weather data, including temperature and precipitation records, essential for analyzing long-term climate trends and patterns in Fresno.

2. **OpenWeatherMap API:** Offers real-time weather data, including current temperature and precipitation, crucial for accurate short-term weather forecasts and anomaly detection.

3. **USDA Crop Yield Data:**
   - Data Available: Provides historical crop yield data for **almonds** and **tomatoes** in Fresno County.
   - Timeframe: Crop yield data from 1979 to the present.

---

### **Key Components:**

1. **Time Series Analysis:**
   - **Objective:** Analyze historical weather data specific to Fresno from **1979 to the present**, focusing on key variables such as temperature, precipitation, and humidity.
   - **Techniques:** 
     - Apply **time series decomposition** to separate the weather data into trend, seasonal, and residual components, helping to identify key patterns.
     - Focus on understanding short-term weather patterns, particularly during critical growing seasons for **almonds** and **tomatoes**.
     - Analyze the impact of weather trends on crop yield, such as how extreme temperature fluctuations or insufficient rainfall affect crop productivity.

2. **Correlation Analysis Between Climate and Crop Yield:**
   - **Objective:** Explore the correlation between short-term weather patterns and crop yield for **almonds** and **tomatoes** in Fresno.
   - **Techniques:**
     - Use **Pearson correlation** or **Spearman rank correlation** to assess the relationship between weather variables (e.g., temperature, rainfall) and crop yields.
     - Identify weather thresholds (e.g., maximum temperature or minimum rainfall) that significantly impact yield during critical phases of crop growth (e.g., flowering, harvesting).

3. **Machine Learning Models for Short-Term Weather Prediction and Crop Yield Forecasting:**
   - **Objective:** Develop and train a basic and easy-to-implement machine learning model to **simultaneously forecast short-term weather conditions** (e.g., up to 7 days ahead) **and predict potential impacts on crop yields** for **almonds** and **tomatoes** based on these forecasts.
   - **Model:** Utilize a **Long Short-Term Memory (LSTM)** model for predicting key weather variables and associating them with crop yield outcomes:
     - **Daily temperature fluctuations** (maximum and minimum temperatures) to anticipate heatwaves or frost events, which can negatively impact yields.
     - **Precipitation patterns** to forecast rain events, helping farmers optimize irrigation schedules and estimate crop water stress levels.
     - **Humidity levels** to predict changes that influence crop growth, such as fungal infections or evaporation rates.
   - **Training Data:**
     - The model will be trained on **NOAA historical weather data** from 1979 to the present, **OpenWeatherMap real-time data**, and **USDA crop yield data** for **almonds and tomatoes** in Fresno County.
     - By combining weather predictions with past crop yield data, the model will learn how weather conditions influence yield during key growth phases.
   - **Predictions:**
     - The LSTM model will not only predict short-term weather conditions but will also forecast potential impacts on crop yield based on expected weather changes.
     - For example, if a heatwave is predicted, the model will forecast the possible reduction in yield for sensitive crops like **almonds**, providing early warnings to farmers.


## **Expected Major Findings**

In this project, several key findings are anticipated, based on the analysis of historical and real-time weather data, as well as crop yield data for **Fresno County**. These findings will provide valuable insights into short-term weather patterns, crop yield predictions for **tomatoes** and **almonds**, and their correlation. Below are the main areas of exploration and the expected outcomes:

#### **1. Identification of Short-Term Weather Patterns and Their Impact on Crop Yield**
   - **Expected Finding:** 
     - Analyze historical weather data to identify short-term weather patterns, such as daily temperature fluctuations, precipitation trends, and humidity variations, particularly during critical growing seasons for **tomatoes** and **almonds**.
     - Identify how these weather patterns correlate with fluctuations in crop yield for **tomatoes** and **almonds**.
   - **Value:** 
     - Improved understanding of how specific weather conditions (e.g., heatwaves, rainfall patterns) affect the yields of **tomatoes** and **almonds**, helping farmers optimize agricultural practices based on short-term forecasts.

#### **2. Development of Accurate Short-Term Weather and Crop Yield Forecasts**
   - **Expected Finding:** 
     - Develop machine learning models (e.g., LSTM) to provide accurate short-term weather forecasts, including daily predictions for temperature, precipitation, and humidity in **Fresno County**.
     - Extend these forecasts to predict how upcoming weather conditions might impact yields of **tomatoes** and **almonds**, using historical correlations between weather patterns and yield outcomes.
   - **Value:** 
     - Farmers will be able to anticipate short-term weather impacts on **tomato** and **almond** yields, enabling them to make informed decisions on irrigation, planting, and harvesting to minimize potential losses. For example, if a heatwave is predicted, farmers can take early action to protect crops that are sensitive to temperature extremes.

### **Objective Discussion:**

- **Impact and Utility:**
  - This project aims to improve **short-term weather forecasts** and provide actionable insights into the correlation between weather conditions and **crop yield** for **tomatoes** and **almonds** in **Fresno County**. Accurate weather and crop yield predictions will benefit **agriculture** by enabling farmers to optimize irrigation, planting, and harvesting schedules. Additionally, early identification of critical weather conditions (e.g., heatwaves or droughts) will help farmers take timely actions to mitigate crop damage. The project will also provide value by contributing to **agricultural planning** and **disaster preparedness**.

- **Main Claims and Questions:**
  - *Claim 1:* The project will accurately predict short-term weather patterns (e.g., temperature and precipitation) using historical and real-time data for **Fresno County**, enhancing decision-making for farmers and agricultural stakeholders.
  - *Claim 2:* Machine learning models will provide accurate forecasts for how short-term weather patterns (e.g., heatwaves, rainfall) impact **tomato** and **almond** yields, validated through historical crop yield data.
  - *Claim 3:* The project will offer early warnings about potential yield losses based on forecasted critical weather conditions, allowing farmers to take preventive actions to protect crops.

  - *Question 1:* How do short-term weather patterns (e.g., temperature fluctuations, precipitation) influence **tomato** and **almond** yields, and what are the most critical weather variables affecting these yields?
  - *Question 2:* How effective are machine learning models (e.g., LSTM) in predicting short-term weather conditions and their impact on **tomato** and **almond** yields compared to traditional forecasting methods?

## Data Summary and Statistical Analysis

### **Weather-Only Focus:**

#### **1. Time Series Line Plot (Weather Variables Over Time)**
   - **Purpose:** Visualize trends and seasonal patterns in key weather variables over time.
   - **Variables:** Temperature, precipitation, humidity.
   - **Why it’s useful:** It will help you observe how weather conditions change over time and identify patterns, such as seasonal fluctuations or anomalies, across different regions.
   - **Implementation:** Create line plots for different regions in California to observe temperature, precipitation, and humidity trends.
   - **Tools:** Matplotlib, Plotly (for interactive exploration).

#### **2. Heatmap (Seasonal Variations by Region)**
   - **Purpose:** Show how weather variables (e.g., temperature, precipitation) vary across different regions and seasons.
   - **Variables:** Temperature, precipitation.
   - **Why it’s useful:** This will clearly show the regional and seasonal differences in weather patterns, making it easy to identify periods of extreme temperatures or rainfall.
   - **Implementation:** Create a heatmap showing how temperature or precipitation varies monthly across regions (e.g., Coastal, Inland, Central Valley).
   - **Tools:** Seaborn, Plotly.

#### **3. Geographic Map (Spatial Visualization of Weather Data)**
   - **Purpose:** Visualize the spatial distribution of weather data (e.g., average temperature or precipitation) across California.
   - **Variables:** Temperature, precipitation.
   - **Why it’s useful:** A geographic map will help you visualize how weather patterns vary spatially and highlight regional differences.
   - **Implementation:** Use a choropleth map to show the spatial distribution of temperature or precipitation across different agricultural regions.
   - **Tools:** Plotly, Folium, Geopandas.

### **Weather and Crop Yield Data:**

#### **4. Scatter Plot (Weather Variables vs. Crop Yield by Region)**
   - **Purpose:** Explore the relationship between key weather variables and crop yield.
   - **Variables:** Temperature, precipitation, crop yield.
   - **Why it’s useful:** This plot will help you identify how weather conditions (e.g., extreme heat or drought) impact crop yields in different regions.
   - **Implementation:** Plot temperature or precipitation against crop yield for different regions, using separate markers for each crop.
   - **Tools:** Matplotlib, Seaborn.

#### **5. Correlation Matrix Heatmap (Weather Variables and Crop Yield)**
   - **Purpose:** Show correlations between weather variables (e.g., temperature, precipitation) and crop yield.
   - **Variables:** Temperature, precipitation, humidity, crop yield.
   - **Why it’s useful:** This will help identify which weather factors have the strongest impact on specific crop yields, offering valuable insights into climate-crop relationships.
   - **Implementation:** Generate a heatmap to visualize correlations between weather variables and crop yields for selected crops (e.g., almonds, tomatoes, grapes, lettuce).
   - **Tools:** Seaborn, Plotly.

#### **6. Anomaly Detection Plot (Weather Extremes and Yield Impacts)**
   - **Purpose:** Identify and visualize extreme weather events (e.g., heatwaves, droughts) and their impact on crop yields.
   - **Variables:** Temperature, precipitation, crop yield.
   - **Why it’s useful:** This plot will help you highlight how extreme weather conditions directly impact crop productivity and identify patterns of risk.
   - **Implementation:** Use a time series plot to overlay weather anomalies (e.g., Z-scores for temperature) with crop yield data to show how extreme weather events affect yields.
   - **Tools:** Matplotlib, Plotly.

### Preprocessing Steps

**OpenWeatherMap API:**
- Retrieve real-time weather data for specified California regions, capturing key variables such as temperature, precipitation, humidity, and atmospheric pressure.
- Fetch historical weather data from 1979 to the present, allowing comparison with real-time data.
- No preprocessing will be done on dates; date parsing will remain flexible for time interval analysis.
- The data will be aggregated by date, city, and other relevant attributes such as temperature, humidity, and precipitation.

**NOAA Climate Data:**
- Download historical weather records focusing on temperature and precipitation from 1979 to the present for California’s agricultural regions.
- Include relevant seasonal indicators such as temperature patterns and rainfall amounts during critical crop growth periods.
- No specific date preprocessing; historical weather records will align with crop yield data for later correlation analysis.

**USDA Crop Yield Data:**
- Collect historical crop yield data for key crops (almonds, tomatoes, grapes, lettuce) from 1979 to the present.
- Align the crop yield data with the corresponding weather conditions in the same regions and timeframes for correlation analysis.
- Regions are assigned based on counties to facilitate regional crop yield comparisons with weather data.

**Region Assignment for Crop Yield Data:**
- Assign each county in the dataset to a predefined region (e.g., San Francisco, Riverside, Fresno) based on its geographical location.
- Use these regions to aggregate and filter crop data by year and region, grouping by crop name to derive relevant metrics such as harvested acres, yield, production, price per unit, and overall value.

**Weather Data Aggregation:**
1. **Daily Aggregation:**
   - Parse and clean the datetime column, removing unnecessary time zone information.
   - Aggregate weather data (temperature, pressure, humidity, etc.) daily, grouped by both date and city, to get a daily summary of weather conditions per city.

2. **Monthly Aggregation:**
   - Extract the year and month from the datetime column.
   - Group the weather data by city and month to generate monthly summaries for each location, including average temperature, humidity, and precipitation.

3. **Yearly Aggregation:**
   - Extract the year from the datetime column.
   - Group the weather data by city and year to produce yearly summaries, focusing on the same variables as daily and monthly aggregations.

Each step produces a CSV output that will serve as an input for the next phase of analysis. This approach maintains flexibility by not heavily preprocessing dates, enabling more dynamic analysis during the model-building phase. The preprocessing pipeline ensures consistent, clean data for later correlation and time-series analysis.

<!--- 
----------
The following sections should be used for the full proposal document. These are not required for the proposal draft discussion.
----------
-->


## **Basic Data Properties and Analysis Techniques**

### **1. Data Overview and Summary Statistics**

**Objective:**
To provide an initial understanding of both weather and crop yield datasets by summarizing key characteristics and overall distributions of the data.

**Techniques:**
- **Descriptive Statistics:**
  - **Mean, Median, and Mode:** Calculate these central tendency measures for continuous variables such as temperature, precipitation, humidity, and crop yield to understand the average conditions and productivity.
  - **Standard Deviation and Variance:** Measure the variability of weather variables and crop yield to assess the spread and dispersion of the data.
  - **Min and Max Values:** Identify the range of weather conditions and crop yield values to understand the extremes observed in the dataset.

- **Distribution Analysis:**
  - **Histograms:** Create histograms to visualize the frequency distribution of weather variables and crop yield (e.g., temperature distribution across regions or yield distribution for each crop).
  - **Box Plots:** Use box plots to visualize the spread, central tendency, and potential outliers in both weather data and crop yield data.

### **2. Temporal Analysis**

**Objective:**
To analyze how weather variables change over time and assess how these changes correlate with crop yield during different growing seasons.

**Techniques:**

- **Seasonal Decomposition (STL Decomposition):**
  - **Implementation Plan:** Use STL decomposition to break down weather data (e.g., temperature, precipitation) into seasonal, trend, and residual components.
    - Select appropriate timeframes for weather data (e.g., daily or monthly) and crop yield data (e.g., seasonal) to capture seasonal variations.
    - Apply **STL decomposition** to visualize and analyze how seasonal weather patterns correspond with crop productivity (e.g., rainfall during growing seasons correlating with higher yields).
    - Assess regional variations (e.g., Coastal, Inland, Central Valley) to determine how different regions experience unique seasonal patterns that impact crop yield.

- **Autoregressive Integrated Moving Average (ARIMA):**
  - **Implementation Plan:** Fit ARIMA models to forecast short-term weather conditions.
    - Conduct **exploratory data analysis (EDA)** to determine the appropriate differencing for stationarity of the time series data.
    - Use **ACF** and **PACF** plots to identify the optimal order for the ARIMA model (p, d, q).
    - Train the ARIMA model on historical weather data, focusing on short-term predictions of temperature and precipitation.
    - Validate the model’s performance using metrics like **Mean Absolute Error (MAE)** and compare predicted weather values with real-time data.
    - Integrate crop yield data into the model to predict how upcoming weather conditions might influence yields.

### **3. Anomaly Detection**

**Objective:**
To identify unusual or extreme weather events (e.g., heatwaves, droughts) that deviate significantly from historical norms and assess their impact on crop yield.

**Techniques:**

- **Z-Score Analysis:**
  - **Implementation Plan:** 
    - Calculate the mean and standard deviation of weather variables (e.g., temperature, precipitation) from historical data.
    - Compute **Z-scores** for each weather observation to measure the number of standard deviations away from the mean.
    - Identify anomalies (e.g., extreme temperatures or rainfall) by setting a threshold (e.g., Z-scores exceeding ±3).
    - Overlay weather anomalies with crop yield data to assess whether extreme weather events had significant effects on yield.

- **Interquartile Range (IQR) Method:**
  - **Implementation Plan:**
    - Calculate the **first (Q1)** and **third quartiles (Q3)** of weather data to compute the **IQR**.
    - Define upper and lower bounds (e.g., Q1 - 1.5 * IQR and Q3 + 1.5 * IQR) to detect weather outliers (e.g., extreme rainfall or drought).
    - Visualize outliers using box plots and examine how these anomalies correlate with crop yield drops during specific growing seasons.

### **4. Correlation Analysis Between Weather and Crop Yield**

**Objective:**
To explore the relationships between weather variables (e.g., temperature, precipitation) and crop yield to identify how short-term weather fluctuations affect agricultural productivity.

**Techniques:**
- **Pearson and Spearman Correlation Analysis:**
  - Use **Pearson correlation** to assess linear relationships and **Spearman correlation** for non-linear relationships between weather variables and crop yield.
  - Identify which weather factors (e.g., temperature, rainfall) most strongly influence yield for each crop (e.g., almonds, tomatoes, grapes).

- **Scatter Plots:**
  - Visualize relationships between weather variables (e.g., temperature vs. precipitation) and crop yield to detect patterns or thresholds where yield is significantly impacted.

### **5. Data Completeness and Integrity**

**Objective:**
To ensure the quality and consistency of weather and crop yield data for accurate analysis and predictions.

**Techniques:**
- **Missing Value Analysis:**
  - Analyze patterns of missing values in both weather and crop yield data to understand their distribution and potential impact on analysis.
  - Use appropriate **imputation strategies** (e.g., forward/backward fill for time series data) to handle missing data and minimize its effect on results.

- **Data Consistency Checks:**
  - Perform **data validation** by cross-referencing weather data with known historical trends and comparing crop yield data against established benchmarks for accuracy.
  - Ensure consistency across datasets (e.g., weather data from different sources or crop yield data for different regions) to avoid discrepancies in analysis.


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

In this project, we focus on predicting and analyzing temperature data across various cities using advanced machine learning algorithms, including **Prophet**, **LSTM (Long Short-Term Memory)**, and traditional regression models like **Linear Regression**, **Random Forest**, **Gradient Boosting**, and **K-Nearest Neighbors**. Each algorithm was chosen based on its strengths in handling time-series data and regression tasks. Below, I describe the types of analyses conducted and the specific algorithms used, their logic, inputs, and expected outputs.

### 1. **LSTM (Long Short-Term Memory) Neural Network**

- **Algorithmic Properties**: 
  LSTM is a type of recurrent neural network (RNN) that excels at modeling sequential data and capturing long-term dependencies. It is particularly suited for time-series forecasting due to its ability to retain information from previous time steps using its memory cells and gates (input, forget, and output).
  
- **Inputs**: 
  The input to the LSTM model consists of a series of temperature values for each city, prepared as sequences of 60 time steps. The input data is scaled using **MinMaxScaler** to ensure consistent training performance.

- **Outputs**: 
  The output is a predicted temperature value for the next time step in the sequence. For multi-step forecasting, the model iteratively uses predicted values to forecast future temperatures over several time steps.

- **Expected Analysis**: 
  The LSTM model was trained to predict the short-term temperature patterns for multiple cities. The performance of the model was evaluated using **Mean Absolute Error (MAE)**, **Root Mean Squared Error (RMSE)**, and **R-squared (R²)** metrics, achieving strong results on the test data. A key finding is the model’s ability to capture non-linear relationships and long-term dependencies in temperature patterns, providing highly accurate forecasts.

### 2. **Prophet Model for Time-Series Forecasting**

- **Algorithmic Properties**: 
  **Prophet** is an additive model developed by Facebook, designed specifically for forecasting time-series data with trends and seasonality. It is robust to missing data and can capture daily, weekly, and yearly seasonality with minimal parameter tuning. The model also handles holiday effects and trend changepoints automatically.

- **Inputs**: 
  The input data for Prophet consists of two columns: `ds` (date) and `y` (temperature). The model uses historical temperature data to learn the overall trend, daily patterns, and seasonal variations.

- **Outputs**: 
  Prophet outputs the predicted temperature for each future date, along with confidence intervals. Additionally, the model decomposes the forecast into **trend**, **yearly seasonality**, and **daily seasonality** components.

- **Expected Analysis**: 
  Prophet was used to detect long-term trends and seasonal patterns in the temperature data for each city. The analysis showed clear seasonal trends (e.g., higher temperatures during summer months) and identified potential changepoints where the overall temperature trend shifted. The performance metrics indicated that Prophet was effective in capturing both trends and short-term fluctuations in the data.

### 3. **Traditional Regression Models**

#### **Linear Regression**
- **Algorithmic Properties**: 
  **Linear Regression** models the relationship between the input features (e.g., temperature, visibility, dew point) and the target variable (future temperature) by fitting a linear equation. It assumes a linear relationship between the inputs and outputs.

- **Inputs**: 
  Features such as latitude, longitude, visibility, dew point, and previous temperature values were used as inputs for predicting future temperatures.

- **Outputs**: 
  The predicted temperature value at the next time step.

- **Expected Analysis**: 
  Linear regression provides a baseline performance for forecasting temperature. While it is less flexible than other models, it helps to understand the basic linear relationships in the data. However, due to the non-linear nature of temperature trends, this model showed lower performance compared to more advanced algorithms like LSTM.

#### **Random Forest and Gradient Boosting**
- **Algorithmic Properties**: 
  **Random Forest** and **Gradient Boosting** are ensemble learning methods that combine multiple decision trees to improve prediction accuracy. Random Forest works by averaging predictions from multiple independent decision trees, while Gradient Boosting trains trees sequentially, focusing on correcting the errors made by previous trees.

- **Inputs**: 
  Similar to linear regression, these models take in multiple weather-related features (e.g., latitude, visibility, temperature) as inputs to predict the next temperature value.

- **Outputs**: 
  The models output a predicted temperature value for each time step.

- **Expected Analysis**: 
  Both Random Forest and Gradient Boosting showed strong performance on the temperature prediction task, with lower errors compared to Linear Regression. These models are well-suited for capturing complex interactions between the input features and are robust to overfitting due to their ensemble nature. Gradient Boosting, in particular, demonstrated strong results with fine-tuned hyperparameters.

### 4. **K-Nearest Neighbors (KNN)**
- **Algorithmic Properties**: 
  **KNN** is a simple, non-parametric algorithm that makes predictions by averaging the outcomes of the K nearest neighbors in the feature space. It is a memory-based model that relies on the similarity between observations.

- **Inputs**: 
  The same set of weather-related features used in the other regression models (e.g., temperature, latitude, visibility) were input into the KNN algorithm.

- **Outputs**: 
  The predicted temperature value, based on the average temperature values of the nearest neighbors.

- **Expected Analysis**: 
  KNN performed reasonably well but was less accurate compared to ensemble models like Random Forest and Gradient Boosting. Its performance is highly dependent on the choice of `K` and the distance metric, and it tends to struggle with large datasets and high-dimensional feature spaces.


### Weather Data Model Usage

#### 1. **LSTM Model for Time-Series Forecasting**
- **Algorithmic Properties**: LSTM is a powerful recurrent neural network (RNN) that excels in learning long-term dependencies in sequential data. It’s particularly suited for time-series forecasting because it retains information over time, making it adept at handling historical weather patterns.
  
- **Process**:
    - Data was preprocessed using **MinMaxScaler** to normalize temperature values between 0 and 1.
    - We structured the data using a **lookback window of 60 time steps**, where each sequence of 60 past temperatures was used to predict the next temperature.
    - The data was reshaped into a 3D format to fit the LSTM model (samples, timesteps, features).
    - We trained the model using **LSTM layers** with 50 and 100 units, **Dropout layers** to prevent overfitting, and **Adam optimizer**. The model was trained over 20 epochs with a batch size of 32.
    - Predictions were scaled back to their original range, and performance metrics such as **MAE**, **RMSE**, and **R²** were computed. 

- **Input**: 60 past time steps of temperature data for each city.
- **Output**: Predicted temperature for the next time step.
- **Results**:
    - **MAE**: 1.6138, **RMSE**: 2.1238, **R²**: 0.9777.
    - These metrics indicate strong performance, with the model explaining 97.77% of the variance in temperature data.
  
- **Visualization**:
    - Loss curves were plotted to track the model’s training progress over epochs.
    - Predicted vs Actual temperatures were plotted, along with residual error plots to analyze discrepancies between predictions and actual values.

#### 2. **Prophet Model for Trend and Seasonality Analysis**
- **Algorithmic Properties**: Prophet is a time-series forecasting model developed by Facebook, specifically designed to handle data with clear seasonal patterns and trends. It is robust to missing data and can capture daily, weekly, and yearly seasonality.
  
- **Process**:
    - Data was reformatted into the `ds` (date) and `y` (target variable) format required by Prophet.
    - We trained a **Prophet model** with **daily seasonality** and saved the model for future use.
    - Future temperatures for the next 365 days were predicted for each city, and the model was evaluated on both training and test datasets.
    - **Performance metrics** such as **MAE**, **RMSE**, and **R²** were calculated to evaluate overfitting and generalization.

- **Input**: Historical temperature data formatted as (date, temperature) pairs.
- **Output**: Forecasted temperatures for the next 365 days, along with confidence intervals.
- **Results**:
    - **MAE**: 9.1447, **RMSE**: 11.6049, **R²**: 0.3705 for the test set, indicating reasonable accuracy for long-term trend predictions.
  
- **Visualization**:
    - Prophet’s built-in component plots (trend, yearly, and weekly seasonality) were used to visualize how different factors contribute to the model’s predictions.
    - Residual and actual vs predicted plots were also created to inspect the model’s performance.

#### 3. **Traditional Regression Models**
- **Algorithmic Properties**: We applied several traditional machine learning models to predict temperatures based on weather features like latitude, longitude, dew point, and visibility. These models include **Random Forest**, **Linear Regression**, **Gradient Boosting**, **K-Nearest Neighbors (KNN)**, and **Support Vector Regressor (SVR)**.
  
- **Process**:
    - Data was split into training and test sets, and relevant features were selected for temperature prediction.
    - Each model was trained on the training set, and their performance was evaluated on the test set.
    - Models were saved using **joblib** and later reloaded for further analysis and visualization.
  
- **Input**: Weather-related features such as latitude, longitude, dew point, visibility, etc.
- **Output**: Predicted temperature values.
- **Results**:
    - **Random Forest**: MAE = 0.1335, RMSE = 0.2126, R² = 0.9998 (some signs of overfitting).
    - **Linear Regression**: MAE = 0.2181, RMSE = 0.3161, R² = 0.9995.
    - **Gradient Boosting**: MAE = 0.2672, RMSE = 0.3536, R² = 0.9994.
    - **KNN**: MAE = 0.6308, RMSE = 1.3292, R² = 0.9912 (clear signs of overfitting).
  
- **Visualization**:
    - Performance metrics (MAE, RMSE) were plotted for each model.
    - Actual vs predicted plots and residual plots were created for all models, allowing comparison of the models' predictive accuracy.

#### 4. **Multi-City Prophet Forecasting**
- **Process**:
    - We extended the Prophet model to forecast temperatures for multiple cities individually.
    - For each city, the model was trained and used to predict the next 365 days of temperatures.
    - Cities with fewer than 30 observations were excluded to ensure reliable predictions.
    - Performance metrics for each city’s model were calculated, and all forecasts were combined into a single DataFrame for easy analysis.

- **Results**:
    - Detailed performance metrics were recorded for each city, providing insights into how the model performed across different geographical locations.
  
- **Visualization**:
    - Forecasts for each city were visualized using Prophet’s built-in plotting functions.

### Conclusion:
- **LSTM** performed exceptionally well on sequential temperature data, showing strong predictive capabilities and minimal overfitting.
- **Prophet** was useful for capturing long-term trends and seasonal patterns in city-specific temperature data, though its overall predictive accuracy was lower than LSTM.
- **Random Forest** and **Gradient Boosting** performed well, but Random Forest showed slight signs of overfitting, which could be improved with further tuning.
- **KNN** displayed significant overfitting, performing well on the training set but poorly on the test set.


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
