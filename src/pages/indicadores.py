import dash_bootstrap_components as dbc
import dash 
from dash import html, Output, Input, State, callback, dcc

dash.register_page(__name__)


layout = html.Div(children=[
    html.H1("Hello World")
])