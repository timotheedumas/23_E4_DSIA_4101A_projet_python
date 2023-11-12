import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import webbrowser
import os

# Charger les données
ufo_data = pd.read_csv('cleandata.csv')

# Créer une application Dash
app = dash.Dash(__name__)

# defini les layout
app.layout = html.Div([
    html.H1("UFO Sightings Analysis", style={'textAlign': 'center'}),

    # slider pour la selection de l'année
    html.Div([
        html.Label("Select Year:", style={'textAlign': 'center'}),
        dcc.Slider(
            id='year-slider',
            min=ufo_data['Year'].min(),
            max=ufo_data['Year'].max(),
            value=ufo_data['Year'].min(),
            marks={str(year): str(year) for year in sorted(ufo_data['Year'].unique())},
            step=None
        )
    ], style={'margin': '20px'}),

    # Graphique linéaire des observations par année
    dcc.Graph(
        id='sightings-by-year-graph',
        figure=px.line(
            x=ufo_data['Year'].value_counts().sort_index().index,
            y=ufo_data['Year'].value_counts().sort_index().values,
            labels={'x': 'Year', 'y': 'Number of Sightings'},
            title='Total Number of UFO Sightings per Year'
        ),
        config={"staticPlot": True}  # Makes the plot non-interactive
    ),

    dcc.Graph(id='sighting-duration-histogram'),  

    html.Div([
        # Graphique camembert des saison
        dcc.Graph(id='season-pie-chart', style={'display': 'inline-block', 'width': '50%'}),

        # Graphique camembert des formes d'UFO
        dcc.Graph(id='ufo-shape-pie-chart', style={'display': 'inline-block', 'width': '50%'})
    ]),

    # Map
    dcc.Graph(id='ufo-sightings-map', style={'height': '90vh', 'width': '100%'})
])

# Callback
@app.callback(
    [Output('sighting-duration-histogram', 'figure'),
     Output('season-pie-chart', 'figure'),
     Output('ufo-shape-pie-chart', 'figure'),
     Output('ufo-sightings-map', 'figure')],
    [Input('year-slider', 'value')]
)

def update_charts(selected_year):

    filtered_data = ufo_data[ufo_data['Year'] == selected_year].copy()

    # Update the histogram
    histogram_figure = create_duration_histogram(filtered_data, selected_year)

    # Update the pie chart for seasons
    season_pie_figure = create_season_pie_chart(filtered_data)

    # Update the pie chart for UFO shapes
    ufo_shape_pie_figure = create_ufo_shape_pie_chart(filtered_data)

    # Update the map
    map_figure = create_map(filtered_data, selected_year)

    return histogram_figure, season_pie_figure, ufo_shape_pie_figure, map_figure

# fonction pour créer l'histogramme
def create_duration_histogram(filtered_data, selected_year):
    bins = [-1, 10, 60, 300, 1800, 7200, 86400, float('inf')]
    labels = ['< 10 sec', '10 sec - 1 min', '1 - 5 min', '5 - 30 min', '30 min - 2h', '2h - 1 day', '> 1 day']
    filtered_data['Duration_Category'] = pd.cut(
        filtered_data['length_of_encounter_seconds'], 
        bins=bins, 
        labels=labels,
        include_lowest=True
    )
    duration_counts = filtered_data['Duration_Category'].value_counts(sort=False)  # Make sure the labels order is kept

    histogram_figure = px.bar(
        x=duration_counts.index,
        y=duration_counts.values,
        labels={'x': 'Duration', 'y': 'Number of Sightings'},
        title=f'Distribution of UFO Sightings Durations in {selected_year}'
    )
    return histogram_figure

# camembert siasons
def create_season_pie_chart(filtered_data):
    season_counts = filtered_data['Season'].value_counts(normalize=True) * 100
    season_pie_figure = px.pie(
        filtered_data,
        names='Season',
        title='Seasonal Distribution of UFO Sightings'
    )
    return season_pie_figure

# camemebert formes
def create_ufo_shape_pie_chart(filtered_data):
    ufo_shape_counts = filtered_data['UFO_shape'].value_counts(normalize=True) * 100
    ufo_shape_pie_figure = px.pie(
        filtered_data,
        names='UFO_shape',
        title='UFO Shape Distribution'
    )
    return ufo_shape_pie_figure

# fonction pour creer la map
def create_map(filtered_data, selected_year):
    fig = px.scatter_geo(
        filtered_data,
        lat='latitude',
        lon='longitude',
        hover_name='Description',  # Affiche la description dans l'infobulle
        hover_data={
            'Date_time': True,    # Affiche la date
            'Country': True,      # Affiche le nom du pays
            'UFO_shape': True,    # Affiche la forme de l'UFO
            # Cachez la latitude et la longitude de l'infobulle
            'latitude': False,
            'longitude': False
        },
        title=f'UFO Sightings Around the World in {selected_year}'
    )
    fig.update_layout(
        geo=dict(
            projection_type='equirectangular',
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
            showcountries=True,
            showcoastlines=True,
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig

# ouvre automatiquement le browser
webbrowser.open_new('http://127.0.0.1:8050/')

# run l'appli
if __name__ == '__main__':
    app.run_server(debug=True)