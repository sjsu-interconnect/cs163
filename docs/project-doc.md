# Proposal: Predicting Inflation in Food and Beverages industry using supply chain pass-through cost analysis

## Project Summary
<!--- Write a summary of your project including the project goals, broader impacts, and data sources -->
This project aims is to explore and create a model that predict the inflation of food and beverages price using the Food and Beverages Consumer Price Index. This model can be used for monitoring material price,
food price inflation, or market shifts that supports decision-making processes for companies in F&B as well as Agriculture industry. Moreover, it can give ordinary users 
forecasted changes (positive or negative) in food and beverages price for daily shopping routines. Ultimately, this project want to explore a new way to integrate more information
to the calculation of the F&B Price Index, which may result in more accurate result than the traditional method. 

The proposed model will be trained using historical data of Chained Consumer Price Index, Producer Price Indices, Consumer Expenditures from the Bureau of Labor Statistics (BLS). Another source of data is the Received Price Indices
data from the US Department of Agriculture (USDA) to provide insights about the amount of revenue that farmers received per an area of crop unit. By using the supply chain
pass-through cost model, we will predict the CPI by using PPI, CE, and RPI as the predictors.


## Data Sources
<!--- List data sources, including the existing datasets and anything you are going to collect by yourself. It is expected to combine two or more data sources in your project. -->
<!--- Each dataset should be briefly explained: what kinds of data are available, who collected the dataset, how the data was collected. -->

### Bureau of Labor Statistics Data API:
The main source that provide Food and Beverages Consumer Price Index, Producer Price Index, and Consumer Expenditures. The data is collected monthly by BLS agents, who are randomly
assigned to different places across the United States to monitor and report the daily change in item's price. BLS use CPI survey, which collects about 94,000 prices and 8,000 rental
housing units quotes each month. Those surveys are conducted within businesses and households.

### US Department of Agriculture Data API:
The Received Price Index from the USDA is gathered through surveys, offering a comprehensive look at the prices farmers receive for their products. Data is
collected both monthly and quarterly, providing timely insights into price trends. This index covers a wide geographic range, capturing data at both national
and regional levels, which helps reflect the diversity of agricultural markets across the country. These surveys are crucial for tracking the economic conditions
faced by agricultural suppliers.

## Expected Major Findings
<!--- List and explain what information you want to obtain in this project. Explain how valuable this project could be based on the objective discussion. You may want to list main claims and questions you want to answer through the project. -->
1. CPI Forecasting model:

A model that can forecast the inflation of Food and Beverages industry reflected via the CPI index. Santiago et al. (2024) suggested that firms use the price change along the supply chain
as evidence for their pricing strategy. Using the supply chain pass through cost analysis, we will create a model that use the changes in price received by agricultural suppliers (RPI),
manufacturers/retailers producer price (PPI), as well as the consumers substitution behavior (CCPI) to predict the inflation (CPI).

2. Which USDA sectors (e.g., LIVESTOCK, HORTICULTURE, VEGETABLES) have the largest impact on CPI?

By analyzing price trends across different agricultural sectors, we aim to determine which commodities contribute most to fluctuations in consumer prices. This insight 
can help policymakers and businesses understand the drivers of inflation in food markets and anticipate changes in consumer spending patterns. The analysis will also aid
in developing predictive models for better forecasting CPI movements.

3. The comparison of Timeseries and Machine Learning approach.

The objective is to compare the effectiveness of traditional time series forecasting methods, such as ARIMA or SARIMAX, with machine learning models, such as XGBoost or LSTM, in predicting the Consumer Price Index (CPI) for food and beverages. Time
series models rely on historical CPI data and account for seasonality and trends, while machine learning models can incorporate a broader set of features, such as
commodity prices, energy costs, and economic indices. This comparison will evaluate which approach provides more accurate predictions, handles complex relationships better,
and adapts more effectively to changing market conditions.

## Preprocessing Steps
<!--- List major preprocessing steps needed for the datasets and explain why. -->
1. Data Collection:

Collecting historical data from the 3 APIs using REST API provided from the BLS, BEA, and USDA official websites.

2. Cleaning and Formatting:

Clean the historical data to handle missing values, inconsistent formats, or outliers. Use aggregation, modification, and formatting to form a uniformed, final dataset with the index is the timeframe
of the timeseries.

4. Data Scaling and Normalization:

Normalize or scale the features (price, sentiment scores) to ensure that different features contribute equally to the model.

5. Model Training/Testing Split:

Split the dataset into training and testing sets, ensuring that the split maintains the time-series nature of the data.


## Basic Data Properties and Analysis Techniques
<!--- Based on the lectures on "Exploratory Data Analysis" and "Data and Sampling", list and explain what types of basic statistical analysis you plan to provide to give the meta information and overall picture of the datasets. -->
### Food and Beverages Price Index Data:
- Availability: 

The data is available across 236 monthly timeframes from January 2005 until present (August 2024). As a result, there are 236 entries for this data.
- Statistics:

<img alt="CPI_data.png" src="/Users/eddie/cs163/src/Plots/Original_CPI_and_CCPI.png"/>

<img alt="CPI vs CCPI plot" src="/Users/eddie/cs163/src/Plots/Differenced_CPI_and_CCPI.png">

- Both CCPI and CPI seem to increase over time throughout the observing period. However, when looking at the rate of changes, we witness a lot of drastic downward movement. We can investigate furthermore on 
what has happened at those periods of time. However, the mean of difference (t1 - t0) for CPI is 0.116, which shows the usual trend of inflation indicator to increase overtime.
- Even the two metrics have nearly identical trends, when we plot the differencing, we see that the degree of fluctuation are different. This
is due to the different in purpose of the metrics. CCPI is used for tracing the consumer's substitution behaviors when the item prices changed while CPI is used for
indicating change of item prices.

### Consumer Expenditures:

<img alt="Commodity Plot" src="/Users/eddie/cs163/src/Plots/CE.png">

- The total compensation of the groups seem to follow a general trend. However, the state and government workers
group seem to fluctuate very much. This may be explained by the adjustment of presidency and policy of each president. Other than that,
The private workers and civilian workers seem to always follow a harmonic trend. Though we will need to perform some analysis to see if 
they are influencing each others for feature selection.

### Producer Price Index Data:
<img alt="Commodity Plot" src="/Users/eddie/cs163/src/Plots/Commodity PPI.png">

- The PPI data was collected among 6 sectors: 
  - Frozen food manufacturing
  - Dehydrated food manufacturing
  - Seafood Production and Packaging manufacturing
  - Snack food manufacturing
  - Perishable food manufacturing
  - Food and Beverages retailers

- Similar to CPI, PPI tend to increase over time. However, Frozen food and Perishable food have some strange movement around the beginning of 2019 and 
late 2022. But in general, the PPI of sectors seem to have no influence on each others. We will need to confirm this anticipation using hypothesis testing
techniques later on.

### USDA RPI Data:
<img alt="Commodity RPI.png" src="/Users/eddie/cs163/src/Plots/Commodity RPI.png"/>

- The data contains Price Received Index of 8 different commodities: aquaculture, livestock, poultry, dairy, field crops, fruit
& nuts, horticulture, and vegetables. We need to perform imputation on the aquaculture and horticulture indices as they are
only available since 2018. After that, we should also check if the RPI of each commodity does not influence others.

## Automation, Scalability, and Portability
<!--- Assume that newer datasets will become available from the same source in the future, or you need to ask your colleague to inherit this project. What will be major challenges? List and explain technical and implementational practices you will use to enhance automation, scalability, and portability aspects of the project. -->
In the automation aspect, those data will always be published periodically by BLS, BEA, and USDA as they are major figures to monitor the economy. So by creating an automated pipeline, we can 
keep the project up to dated monthly with all the upcoming changes. For further exploration, we can expand the features to more than just the currently observed ones. There are multiple data that 
we can accounting for like oil prices, supply chain industry indices, weather, etc. For portability, we can deploy this analysis and model on a website using Dash. The automated pipeline can be
deployed using Airflow. Also, the machine learning model can be deployed via cloud computing services (AWS, Google Cloud, etc.) and transferring data to the website using API.



<!--- 
----------
The following sections should be used for the analysis planning. These are not required for the proposal document submission.
----------
-->



## Data Analysis and Algorithms
<!--- List and describe what types of (advanced) analysis you plan to conduct. This section should be tied back to the expected major findings. (If needed, you can update the findings section.) When selecting algorithms to obtain the analysis results, provide a brief explanation of the algorithmic properties and logic. You should clearly define the inputs and outputs of each algorithm. -->

- **Imputation for Food Fish and Horticulture RPI**: Due to the similarity in general RPI change over commodities,
I suspect KNN Imputer can be utilized to fill the those missing value. I will implement the KNN Imputer using Scikit_learn,
then optimize it with GridSearchCV. I will also check to see its correlation with other metrics (except CPI to prevent bias) then adjust
the features used for the imputation. Finally, we will compare the distribution to achieve the best result.
- **Difference in trends among groups for PPI, CE and RPI**: For this analysis, I want to corporate repeated ANOVA or regression analysis
to determine the differences in changes among groups. If the groups have significant differences, we can proceed to use them as features
for our predictors. Else, we have to investigate closely using pairwise comparison to figure out the left-out needed features.
- **Ranking the commodities on their effect to CPI**: For this analysis, we can use multiple regression analysis to check the 
correlation of the commodities RPI on CPI. We will use the coefficients to rank the importance of the commodity's effect on CPI. Moreover,
we can also do the same analysis on PPI sectors.
- **Feature importance**: Since I will use Tree-based algorithms XGBoost and Random Forest, I will use SHAPley value to 
figure out the feature importance for better interpreting the model.
- **Fitting Machine Learning models**: We will fit the data into XGBoost, Random Forest, and LSTM. After that we will optimize XGBoost
and Random Forest using GridSearchCV and hand-tune LSTM.
- **Lag and Correlation Computation of CPI for ARIMA model fitting**: From the plot above, we can see that CPI does not have seasonality. However, it does not 
have stationary. So, we will use differenced values of CPI to fit in the ARIMA model. In the preparation part, we will calculate correlation and
use ACF/PACF plots to determine feature lag. Then we will fit the data into ARIMA and produce predict some short term value for CPI.
- **Model comparison**: After the fitments, we will compare the results of the models to see which one performed best. I expect to use MSE, ROC AUC, and
Accuracy to evaluate and comparing the models. After finished comparing my models, I will use
LazyRegressor to further comparing them with other state-of-the-art algorithms.

<!--- 
----------
The following sections should be used for the analysis outcome presentation. These are not required for the analysis plan submission.
----------
-->
# Analysis Outcomes
<!--- Explain the analysis you conducted and show the results. Discuss how the data, your analysis, and/or visualization can support the claims or findings. What will be the recommendations or suggestions you can make based on the results? Use bullet points, tables, and figures (if possible) to increase the readability of the document. -->

- 


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