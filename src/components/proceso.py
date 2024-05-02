import dash
from dash import html, dcc, callback, Output,Input


layout = html.Div([
    html.Div(id='main-display',className="main-display",children=[
        html.H1(className="page-title", children="Elección de Proceso"),
        html.P(children="Seleccione verdadero o falso. Si selecciona verdadero una nueva pregunta aparecerá"),
        dcc.RadioItems(id="options-TF",options=["Verdadero","Falso"]),
        html.P(id="siguiente-pregunta")
    ]),
])

# Callback para ir a la dirección URL /arbol-decision
@callback(
    Output('siguiente-pregunta', 'children'),
    [Input('options-TF', 'value')]
)
def change_layout(radio_value):
    if radio_value == "Verdadero":
        return "Esta es la siguiente pregunta"
    else:
        return ""