from dash import Dash, dcc, html, Output, Input
import pandas as pd
import plotly.express as px

# CSV einlesen
filepath = r"C:\Users\Admin\OneDrive\11 Datenvisualisierung mit Python\20250714 Praxisprojekt Fahrzeug\cleaned_data_vehicles.csv"
df = pd.read_csv(filepath, delimiter=';')

# Daten vorbereiten: Anzahl Modelle pro Jahr
modelle_pro_jahr = df.groupby("Year")["Model"].nunique().reset_index()
modelle_pro_jahr.columns = ["Modelljahr", "Anzahl Modelle"]

# Jahre als Liste für Animation
jahre = sorted(modelle_pro_jahr["Modelljahr"].unique())

# App-Setup
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Animation: Entwicklung der Anzahl Fahrzeugmodelle pro Jahr", style={"textAlign": "center"}),

    dcc.Graph(id="animated-line"),

    dcc.Slider(
        id="jahr-slider",
        min=min(jahre),
        max=max(jahre),
        value=min(jahre),
        marks={str(j): str(j) for j in jahre if j % 5 == 0},
        step=None
    )
])

@app.callback(
    Output("animated-line", "figure"),
    Input("jahr-slider", "value")
)
def update_figure(selected_year):
    # Zeige alle Jahre bis einschließlich des ausgewählten Jahres
    df_filtered = modelle_pro_jahr[modelle_pro_jahr["Modelljahr"] <= selected_year]

    fig = px.line(
        df_filtered,
        x="Modelljahr",
        y="Anzahl Modelle",
        title="Anzahl Fahrzeugmodelle im Zeitverlauf",
        markers=True
    )

    fig.update_traces(line=dict(color="seagreen", width=3), marker=dict(size=7))
    fig.update_layout(
        xaxis_title="Modelljahr",
        yaxis_title="Anzahl Modelle",
        transition_duration=300
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)