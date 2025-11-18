from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px


vehicles_df = pd.read_csv(r"C:\Users\Admin\OneDrive\11 Datenvisualisierung mit Python\20250714 Praxisprojekt Fahrzeug\cleaned_data_vehicles.csv", delimiter=';')
vehicles_data = vehicles_df.to_dict('records')

# App instantiieren (App-Objekt erstellen):
app = Dash()

vehicles_hist = px.histogram(vehicles_df,
                             x='Year',
                             y='Time to charge at 240V',
                             histfunc='avg')

app.layout = [
    html.Center(html.H1('Data Science vehicles')),
    html.Hr(),
    dcc.Graph(figure=vehicles_hist),
    dash_table.DataTable(data=vehicles_data,
                         page_size=5,
                         style_cell={'textAlign': 'center'}),
]

if __name__ == '__main__':
    app.run(debug=True)

# app.run_server has been replaced by app.run
