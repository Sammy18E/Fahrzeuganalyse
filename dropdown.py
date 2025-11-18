from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

filepath = r"C:\Users\Admin\OneDrive\11 Datenvisualisierung mit Python\20250714 Praxisprojekt Fahrzeug\cleaned_data_vehicles.csv"
df = pd.read_csv(filepath, delimiter=';')

dimensions_list = df.columns.values

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "Scatterplot Matrix Korrelationen Fahrzeugtests",
            style={"textAlign": "center"},
        ),
        html.Div(
            [
                html.H3("Choose your dimensions:"),
                dcc.Dropdown(
                    id="dimension-dropdown",
                    options=dimensions_list,
                    value=["Fuel Type1", "Co2 Fuel Type1", "You Save/Spend"],
                    multi=True,
                ),
            ],
            style={"width": "50%", "marginLeft": "5em"},
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    Input("dimension-dropdown", "value"),
)
def update_graph(dimension_choice):
    fig = px.scatter_matrix(df, dimensions=dimension_choice)
    fig.update_layout(height=len(dimension_choice) * 166.667)
    return fig


if __name__ == "__main__":
    app.run(debug=True)