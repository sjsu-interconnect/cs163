from dash import html

def render_home_page():
    return html.Div([
        html.H1("Welcome to the California Weather Data and Crop Yield Analysis"),
        html.Img(src='/assets/illustration.png', style={'width': '60%', 'margin': 'auto', 'display': 'block'}),
        html.P("This site provides a comprehensive analysis of historical and real-time weather data in California "
               "along with crop yield trends. The goal is to offer insights for agricultural planning, climate studies, "
               "and prediction of future weather and crop yield patterns."),
        html.Hr(),
        html.H2("Site Navigation"),
        html.P("Use the tabs above to explore the following sections:"),
        html.Ul([
            html.Li("Weather Data: Explore detailed weather data for different regions in California."),
            html.Li("Crop Data: Examine trends and insights related to crop yield."),
            html.Li("Prediction: See predictions for future weather patterns and crop yields based on machine learning models."),
            html.Li("Analysis: Dive deeper into data analysis, including anomaly detection and correlation between climate factors and crop yields.")
        ]),
        html.P("This project applies data science techniques such as time series analysis, anomaly detection, and machine learning "
               "to provide valuable insights into California's agricultural and climate trends.")
    ])
