from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table
import plotly.express as px

# Initialize the Dash app
app = Dash(__name__)

# Load the datasets into pandas DataFrames
weather_data = pd.read_csv('../data/weather_yearly.csv')
counties_data = pd.read_csv('../data/grouped_counties_by_region.csv')

# Handle any missing values in the counties_data for the Yield column
counties_data['Yield'] = pd.to_numeric(counties_data['Yield'], errors='coerce')
counties_data = counties_data.dropna(subset=['Yield'])

# Define the app layout
app.layout = html.Div([
    html.H1("Dataset Viewer and Plots"),
    
    # Dropdown for selecting dataset
    dcc.Dropdown(
        id="dataset-selector",
        options=[
            {'label': 'Weather Yearly Data', 'value': 'weather'},
            {'label': 'Grouped Counties by Region', 'value': 'counties'}
        ],
        value='weather',
        clearable=False
    ),
    
    # Data table display
    html.Div(id="table-container"),
    
    # Plot container
    html.Div(id="plot-container"),
    
    # Dropdown for selecting plot type
    dcc.Dropdown(
        id="plot-selector",
        options=[
            {'label': 'Line Plot - Average Temp by City', 'value': 'line_plot'},
            {'label': 'Bar Plot - Crop Yield by Region', 'value': 'bar_plot'}
        ],
        value='line_plot',
        clearable=False,
        style={'margin-top': '20px'}
    )
])

# Callback to update table based on dataset selected
@app.callback(
    Output("table-container", "children"),
    [Input("dataset-selector", "value")]
)
def display_table(selected_dataset):
    if selected_dataset == "weather":
        data = weather_data
    else:
        data = counties_data

    # Return the Dash DataTable for display
    return dash_table.DataTable(
        data=data.to_dict('records'),
        columns=[{"name": i, "id": i} for i in data.columns],
        page_size=10,
        style_table={'overflowX': 'auto'}
    )

# Callback to update plot based on plot type selected
@app.callback(
    Output("plot-container", "children"),
    [Input("plot-selector", "value")]
)
def display_plot(selected_plot):
    if selected_plot == "line_plot":
        # Line plot of average temperature by city over time
        fig = px.line(weather_data, x='year', y='temp', color='city_name', 
                      title='Average Temperature by City Over Time')
    else:
        # Bar plot of crop yield by region
        fig = px.bar(counties_data, x='Region', y='Yield', color='Crop Name', 
                     title='Crop Yield by Region')
    
    return dcc.Graph(figure=fig)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
