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

![CPI_data.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/CPI_data.png)

- CPI seem to increase over time throughout the observing period. However, when looking at the rate of changes, we witness a lot of drastic downward movement.
We can investigate furthermore on what has happened at those periods of time. However, the mean
of difference (t1 - t0) for CPI is 0.116, which shows the usual trend of inflation indicator to increase overtime.

### Consumer Expenditures:

![Commodity Plot](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/CE.png)

- The total compensation of the groups seem to follow a general trend. However, the state and government workers
group seem to fluctuate very much. This may be explained by the adjustment of presidency and policy of each president. Other than that,
The private workers and civilian workers seem to always follow a harmonic trend. Though we will need to perform some analysis to see if 
they are influencing each others for feature selection.

### Producer Price Index Data:

![Commodity Plot](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/Commodity PPI.png)

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

![Commodity RPI.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/Commodity RPI.png)

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

## Imputation for FOOD FISH and HORTICULTURE RPI data
- After the imputation, although the distribution of both features remained similar, the data range shifted significantly

![KNN_Imputed_boxplot_for_FOOD FISH.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/KNN_Imputed_boxplot_for_FOOD_FISH.png)
![KNN_Imputed_boxplot_for_HORTICULTURE TOTALS.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/KNN_Imputed_boxplot_for_HORTICULTURE_TOTALS.png)

There are more outliers appear in the high value range. But, when we compare the imputed values to 
other RPI using the timeseries line plots, they follow the shift of other RPI closely.

![Imputed_RPI_timeseries.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/Imputed_RPI_timeseries.png)

So, the KNN Imputation can estimate the past values of FOOD FISH and HORTICULTURE RPI very well and successfully filled the NA values.

## Timeseries Analysis for CPI
### Stationary

![CPI_data.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/CPI_data.png)

Originally, Ad-Fuller test give out a test statistic of 0.75 with p-value of 0.99. This means that we cannot reject the null 
hypothesis, so there is no stationary in the CPI data. I applied differencing technique on the data with degree 1-4 to
test out. The result shows that at degree 1, CPI data is already station with p-value of 0.025. So we will proceed with ``d=1``

### Seasonality

To test the seasonality of CPI, I performed SLT Decomposition (Seasonal and Trend decomposition using Loess).

![Seasonality_decomposition.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/Seasonality_decomposition.png)

The decomposition shows that there is a trend in the CPI data and also seasonality by month. When double check it using the plot of true CPI value 
versus trend + seasonal data from the decomposition, the result is very promising.

![SLT_prediction.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/SLT_prediction.png)

The line can capture the general trend of the change of CPI. For extra information, I performed anamoly detection to identify the irregular changes of
CPI data in the dataset. 

![Anamolies_detection.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/Anamolies_detection.png)

![Anamolies_points.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/Anamolies_points.png)

The threshold that I used to classify anamolies is:
```
lower bound = residual mean - 3 x residual std
upper = residual mean + 3 x residual std
```
Based on the threshold, we notice that there are 3 anomolies points at April 2019, April 2020, and July 2020. 
- For April 2019, the negative spike can be explained by the impact of Organization of the Petroleum Exporting Countries policies changes 
earlier in 2019 as well as the tension between US and China on the tariff issue. This change impacted the supply chain, which might have caused the spike.
- For April 2020, this was the time when COVID-19 spread out on global-scaled and forced US government to issue the lockdown in the whole country. 
According to the news, people started to panic buy all food and beverages supply due to the concern of a long-lasting epidemic, which increased the CPI index sharply.
- For July 2020, the CPI spike was ease thanks to the reduced in consumer spending due to the lockdown as well as the assistance programs from the government.

## ARIMA and SARIMAX model

In this step, I will implement Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA with eXongeneous features (SARIMAX) to model the CPI data. Both model
require 
- p: Autoregressive lag order
- d: Difference degree
- q: Moving Average lag order

Additionally, for SARIMAX, it requires:
- P: Seasonal autoregressive lag order
- D: Seasonal difference degree
- Q: Moving Average lag order
- S: Seasonal frequency

As our data is monthly, we will use ``S=12``. Moreover, we use ``d=1`` as a result of Ad-Fuller test in the previous part.

### AR lag order and MA lag order

![ACF.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/ACF.png)

![PACF.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/PACF.png)

To identify p and q, I used ACF and PACF plots on CPI data with 1 level of differencing:

- In the ACF plot, we observe a log shape trend in the correlation data.
After 8 lags, we can see that the correlation started to fall inside the 95% confident interval, which indicates the cutoff. So, I decided to go with lag order of 8 (``q=8``)
- In the PACF plot, we can see that the cutoff is after lag 2. So, ``p=2`` is chosen. Notably, this plot shows a very interesting trend in correlation at lags that
are multiplication of 9. This indicate that there is a seasonality correlation every 9 months. So, I switched to ``S=9``
- For ``P`` and ``Q``, we will use grid search strategy to test out for the model with the best metrics (AIC, BIC, Ljung-Box p-value). The best model is 
**SARIMAX(1,1,3)(0,1,1)[9]** with

![sarimax_results.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/sarimax_results.png)

Some key results that we can tell from this model:

  - Frozen Food Manufacturing PPI has a coefficient of -0.0500 with a p-value of 0.000, indicating a significant negative impact on the target variable.
  - Dried and Dehydrated Food Manufacturing PPI is also significant with a positive coefficient (0.0480).
  - Poultry RPI has a negative coefficient (-0.0075) with a p-value of 0.028, indicating significance as well.
  - **Ljung-Box Test (Q)**: The result (0.01) and its probability (0.94) indicate that there is no significant autocorrelation in the residuals at lag 1, suggesting the model is well-fitted.
  - **Jarque-Bera Test (JB)**: A high value (68.12) with a very low probability (0.00) indicates that the residuals are not normally distributed, which may need further examination.
  - **Heteroskedasticity Test**: The H statistic (1.71) with a significant probability (0.02) suggests that there may be some level of heteroskedasticity in the model.

![SARIMAX_diagnosis.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/SARIMAX_diagnosis.png)

Since the data is relatively small, I retest the normality of the predicted CPI with Shapiro-Wilks test. However, the p-value received is way less than 0.05.
So, there is normality issue with the model. 

![QQ_plot_of_CPI.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/QQ_plot_of_CPI.png)

The plot shows a non-normal distribution of CPI. This is why the normality of the model is violated. So, I need to try new methods 
to transform the data to be normalized before retest the data. However, the current SARIMAX already yields very good prediction

![SARIMAX_prediction.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/SARIMAX_prediction.png)

![SARIMAX_prediction_whole_data.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/SARIMAX_prediction_whole_data.png)

### XGBoost Approach

For XGBoost, I used TimeSeriesSplit() to create time-splitting-based cross-validation dataset to feed into the model. I chose ``n_splits=10`` due to
the small sample size. I also tested other values but 10 gives the best performance in term of MSE and MAE.
So far, I used GridSearchCV to tune the model and the best model performance is as follows

![MSE_and_MAE_of_best_XGBoost_model.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/MSE_and_MAE_of_best_XGBoost_model.png)

As we can see, the MSE and MAE learning curve does not have a stable trend as expected. Moreover, MSE and MAE on test set is
very high, which suggest that the model did not capture any trend at all.

![XG_Boost_prediction.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/XG_Boost_prediction.png)

Since XGBoost does not require standardization, it means that the non-normality of CPI is not a factor contributes to the 
worst performance. Hence, I will try to create Window data of features as well as looking for new way to expand the dataset
to enhance the performance of the model. 

### Feature ranking

![SHAP_plot.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/SHAP_plot.png)

So far, the PPI indices are the ones that contribute the most to the XGBoost model using SHAPley values. However,
we cannot tell if this is true yet since the XGBoost model is not working properly. I will conduct this test again
after XGBoost has been finalized.

However, the huge impact of PPI on CPI is indeed a true fact based on the SARIMAX coefficients. Also based on these coefficient,
they have negative impact on the CPI value.

![Corr_heatmap.png](https://github.com/EddieNguyen2012/cs163/blob/af3f09d945a33c3db3351765d39696d417104589/src/Plots/Corr_heatmap.png)

Using pairwise correlation, we can also spot the impact clearer with PPI indices impact CPI more than RPI and CE indices. So,
I expect the completed SHAPley values will also yield similar result.

## Data Visualization Plan 
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