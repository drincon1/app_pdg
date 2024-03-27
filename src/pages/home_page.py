import dash_bootstrap_components as dbc
import dash 
from dash import html, Output, Input, State, callback, dcc

dash.register_page(__name__,path='/')

layout = html.Div(children=[
    html.Div(className="background", children=[
        html.Div(className="home-page", children=[
            html.Div(className="title-buttons", children=[
                html.H2(className="home-title", children="Autodiagnóstico: Dependencias e impactos"),
                html.Div(className="home-buttons", children=[
                    html.Button(className="btn-comenzar", children="Comenzar", id='comenzar-button'),
                    dcc.Location(id='url', refresh=True),
                    # html.Button(className="btn-informacion", children="Información", id="open", n_clicks=0),
                ])
            ]),
            html.Img(className="home-image", src="assets/imagenes/home-image.jpg")
        ])
    ])
])

# Callback para ir a la dirección URL /arbol-decision
@callback(
    Output('url', 'pathname'),
    [Input('comenzar-button', 'n_clicks')]
)
def change_layout(n_clicks):
    if n_clicks is not None and n_clicks > 0:
        return '/arbol-decision'
    else:
        raise dash.exceptions.PreventUpdate