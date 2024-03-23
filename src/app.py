import dash
from dash import html, dcc, callback, Input, Output

app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.Div(className="background", children=[
        html.Div(className="home-page", children=[
            html.Div(className="title-buttons", children=[
                html.H2(className="home-title", children="Autodiagnóstico: Dependencias e impactos"),
                html.Div(className="home-buttons", children=[
                    html.Button(className="btn-comenzar", children="Comenzar"),
                    html.Button(className="btn-informacion", children="Información")
                ])
            ]),
            html.Img(className="home-image", src="assets/home-image.jpg")
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
