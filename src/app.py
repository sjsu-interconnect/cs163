import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load datasets (you would replace these paths with your actual dataset paths)
crops_data_path = '../data/grouped_fresno_crops.csv'
weather_data_path = '../data/weather_yearly.csv'

crops_data = pd.read_csv(crops_data_path)
weather_data = pd.read_csv(weather_data_path)

# Convert 'date' column to datetime
weather_data['date'] = pd.to_datetime(weather_data['year'].astype(str), format='%Y')

# Get the list of unique cities
cities = weather_data['city_name'].unique()

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Weather Data Visualization"),
    dcc.Dropdown(
        id='city-dropdown',
        options=[{'label': city, 'value': city} for city in cities],
        value=cities[0]  # Default value
    ),
    dcc.Graph(id='weather-graph'),
])

# Define callback to update graph
@app.callback(
    Output('weather-graph', 'figure'),
    [Input('city-dropdown', 'value')]
)
def update_graph(selected_city):
    # Filter the dataset for the selected city
    city_data = weather_data[weather_data['city_name'] == selected_city]

    # Create traces for temperature, precipitation, and humidity
    traces = []

    # Temperature trace
    traces.append(go.Scatter(
        x=city_data['date'],
        y=city_data['temp'],
        mode='lines',
        name='Temperature',
        line=dict(color='orange')
    ))

    # Precipitation trace (rain_1h)
    if 'rain_1h' in city_data.columns:
        traces.append(go.Scatter(
            x=city_data['date'],
            y=city_data['rain_1h'].fillna(0),
            mode='lines',
            name='Precipitation (1h)',
            line=dict(color='blue')
        ))

    # Humidity trace if it exists
    if 'humidity' in city_data.columns:
        traces.append(go.Scatter(
            x=city_data['date'],
            y=city_data['humidity'],
            mode='lines',
            name='Humidity',
            line=dict(color='green')
        ))

    # Return the figure
    return {
        'data': traces,
        'layout': go.Layout(
            title=f'Weather Variables Over Time for {selected_city}',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Value'},
            margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
            hovermode='closest'
        )
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
