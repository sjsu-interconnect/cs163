# Proposal: Food and Beverages Price Analysis using Food item Price, Personal Consumption Expenditure and Agricultural Stocking Data

## Project Summary
<!--- Write a summary of your project including the project goals, broader impacts, and data sources -->
This project aims is to explore and analyze the impact of food item prices as well as consumer purchasing power on the Food and Beverages Price Index. Then, develop a machine-learning
model that predicts this index. This model can be used for monitoring material price, food price inflation, or market shifts that supports decision-making processes for companies in F&B as well as Agriculture industry. Moreover, it can give ordinary users 
forecasted changes (positive or negative) in food and beverages price for daily shopping routines. Ultimately, this project want to explore a new way to integrate more information
to the calculation of the F&B Price Index, which may result in more accurate result than the traditional method. 

The proposed model will be trained using historical data on monthly national selected average price from the Bureau of Labor Statistics (BLS). Also, Personal Consumption Expenditure Index (PCE) data from
the Bureau of Economics Analysis (BEA) will also be investigated to gain insights about inflation and customer budget for F&B expenditures. Another source may be included is the crop stock
data from the US Department of Agriculture (USDA) to provide insights about changes like shortage of supply or over production of agricultural products.


## Data Sources
<!--- List data sources, including the existing datasets and anything you are going to collect by yourself. It is expected to combine two or more data sources in your project. -->
<!--- Each dataset should be briefly explained: what kinds of data are available, who collected the dataset, how the data was collected. -->
### Bureau of Labor Statistics Data API:
The main source that provide Food and Beverages Price Index and the F&B prices. The data is collected monthly by BLS agents, who are randomly
assigned to different places across the United States to monitor and report the daily change in item's price. BLS use CPI survey, which collects about 94,000 prices and 8,000 rental
housing units quotes each month. Those surveys are conducted within businesses and households.
### Bureau of Economics Analysis Data API:
This is the source for PCE index. Similar to CPI and Item Prices, PCE is collected using survey within businesses and households. Unlike the CPI, which is based on 
a fixed basket of goods and services, the PCE Price Index is built on a dynamic basket. The weights in the PCE index come from business surveys and are updated
regularly based on shifts in consumer spending patterns. The collection frequency is monthly.
### US Department of Agriculture Data API:
The stocking data from USDA is collected using Grain Stock, Cold Storage, and Cattle on Feed reports. Most of them are collected both monthly and quarterly. Geographically, they are collected
on both national and regional scale. From this source, we can obtain the stocking data of almost all the agricultural products across the US.
## Expected Major Findings
<!--- List and explain what information you want to obtain in this project. Explain how valuable this project could be based on the objective discussion. You may want to list main claims and questions you want to answer through the project. -->
1. CPI Forecasting model:

A model that can forecast the health of Food and Beverages industry reflected via the CPI index. By accounting for various factors besides food item prices,
I expect to profound a new way to monitor this industry.

2. The elasticity of farmers and agricultural production company to demand changes: 

By looking closely to the consumer purchasing pattern and the stocking data, I expect to see how the demand side
of the agricultural industry response to the change in demand. By exploring this, we can see if there is any new data informing method needed for agricultural suppliers.

3. How F&B industry responded to inflation: 

Giving the Food and Beverages Price index as the inflation indicator, we can monitor how the market responded to it. By doing this, we can use reverse-engineer
method to predict the other way, which means how the changes in F&B industry will impact the F&B Price Index or the inflation.

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
![newplot.png](..%2Fnewplot.png)![newplot1.png](..%2Fnewplot1.png)

The CPI seems increased over time throughout the observing period. However, when looking at the rate of changes, we witness a lot of drastic downward movement. We can investigate furthermore on 
what has happened at those periods of time. However, the mean of rate of change is 0.116, which shows the usual trend of inflation indicator to increase overtime.

### Food and Beverages Item Price Data:
![newplot2.png](..%2Fnewplot2.png)
There are 672 series (item categories) that was obtained from the BLS. Due to the seasonal characteristic of food and beverages item, the BLS only selected some specific item to calculate the 
CPI for Food and Beverages. From 2005 to February 2022, the number of observations was stable at around 20 items per report cycle. However, maybe there was a change in report method from the BLS 
that decrease the number of observed item to only around 15 in the following periods. So, even though we have 672 series, we can only use around 16 items to calculate the CPI of F&B.

- Total entry: 1050
- Time covered: from January 2005 to August 2024

### Personal Consumption Expenditure Data:
- General:

The data is fully recorded in the period from January 2005 until now (July 2024). This data is 1 month later that the CPI index so maybe we have to cut the last month entry of the CPI data.
Other than that, there are 2 PCE indices that relates directly to F&B industry. The total number of observations are 470 with the mean expenditure falls around 9 million dollars per month.

- A quick peak:
![newplot7.png](..%2Fnewplot7.png)

The general trend is increasing as expected due to the inflation rule. However, in 2020,  which is the COVID-19 period, there is an
interesting sudden change. We can investigate this change later to see how this affect our CPI index. 

### USDA Stocking Data:

**In progress...**
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