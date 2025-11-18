# pip install dash im Terminal
from dash import Dash, html, dash_table, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Die benötigten Daten:
vehicles_df = pd.read_csv(r"C:\Users\Admin\OneDrive\11 Datenvisualisierung mit Python\20250714 Praxisprojekt Fahrzeug\cleaned_data_vehicles.csv", delimiter=';')
vehicles_data = vehicles_df.to_dict('records')

# App instantiieren (App-Objekt erstellen):
app = Dash()

# Layout der App festlegen:
app.layout = [
    html.Center(html.H1('Data Science vehicles')),
    html.Hr(),
    dcc.RadioItems(options=['avg', 'min', 'max', 'count'],
                   value='avg',
                   id='radio-items'),
    dcc.Graph(id='histogram-graph'),
    dash_table.DataTable(data=vehicles_data,
                         page_size=5,
                         style_cell={'textAlign': 'center'}),
]

# Histogramm-Funktion:
@app.callback(
    Output('histogram-graph', 'figure'),
    Input('radio-items', 'value')
)
def make_histogram(agg_func):
    histogram = px.histogram(vehicles_df,
                             x='Year',
                             y='Time to charge at 240V',
                             histfunc=agg_func)
    return histogram


# Dient dem Starten der App:
if __name__ == '__main__':
    app.run(debug=True)

# app.run_server has been replaced by app.run
