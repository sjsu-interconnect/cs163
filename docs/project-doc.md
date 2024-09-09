# Proposal: Using Machine Learning to predict Groceries Price using Historical Data and News Sentiment

## Project Summary
<!--- Write a summary of your project including the project goals, broader impacts, and data sources -->
This project aims to develop a machine-learning model that predicts grocery prices by leveraging historical pricing data and news sentiment 
analysis. By combining these two data sources, the model aims to capture market trends and external factors, such as news events, 
that may influence price fluctuations. This solution is designed to empower businesses to optimize pricing strategies and enable consumers to make confident, informed decisions.

The proposed model will be trained using historical data on grocery prices, as well as sentiment scores derived from news articles or social media. 
This hybrid approach aims to enhance the accuracy of price predictions, especially during times of market volatility, economic shifts, 
or disruptions such as global pandemics.

## Data Sources
<!--- List data sources, including the existing datasets and anything you are going to collect by yourself. It is expected to combine two or more data sources in your project. -->
<!--- Each dataset should be briefly explained: what kinds of data are available, who collected the dataset, how the data was collected. -->
Walmart API, Newspaper API, Web Scraping
## Expected Major Findings
<!--- List and explain what information you want to obtain in this project. Explain how valuable this project could be based on the objective discussion. You may want to list main claims and questions you want to answer through the project. -->
1. Price Trends Correlated with Sentiment: A strong correlation between the sentiment of news related to food production, 
supply chain, or market events and the fluctuation of grocery prices.

2. Seasonal or Regional Price Fluctuations: Evidence of seasonal price changes or regional variations in grocery prices that align with historical
data and economic factors.

3. Predictive Power of News Sentiment: News sentiment may have predictive power in identifying price shifts, especially during market disruptions,
natural disasters, or sudden changes in consumer behavior.

## Preprocessing Steps
<!--- List major preprocessing steps needed for the datasets and explain why. -->
1. Data Collection:

Collect historical grocery price data from online APIs or grocery databases.
Scrape or source news articles related to the economy, food production, or relevant industries. Use a web scraper for news sources or access public news APIs.

2. Cleaning and Formatting:

Clean the historical data to handle missing values, inconsistent formats, or outliers.
For news data, remove irrelevant content (e.g., stopwords, non-informative articles) and standardize text formats.

3. Sentiment Analysis:

Apply natural language processing (NLP) techniques like sentiment analysis on the news data. Tools
like VADER, TextBlob, or custom-built models can be used to assign sentiment scores to each article.

3. Feature Engineering:

Create time-lagged features from historical grocery prices (e.g., price shifts over the past week/month).
Aggregate news sentiment over the same period (e.g., average sentiment over the past week).
Generate additional features like seasonality, regional identifiers, or economic indicators (if used).

4. Data Scaling and Normalization:

Normalize or scale the features (price, sentiment scores) to ensure that different features contribute equally to the model.
Model Training/Testing Split:

Split the dataset into training and testing sets, ensuring that the split maintains the time-series nature of the data (i.e., training on past data, testing on future periods).



<!--- 
----------
The following sections should be used for the full proposal document. These are not required for the proposal draft discussion.
----------
-->




## Basic Data Properties and Analysis Techniques
<!--- Based on the lectures on "Exploratory Data Analysis" and "Data and Sampling", list and explain what types of basic statistical analysis you plan to provide to give the meta information and overall picture of the datasets. -->



## Automation, Scalability, and Portability
<!--- Assume that newer datasets will become available from the same source in future, or you need to ask your colleague to inherit this project. What will be major challenges? List and explain technical and implementational practices you will use to enhance automation, scalability, and portability aspects of the project. -->




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