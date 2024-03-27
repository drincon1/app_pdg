import dash 
from dash import html, dcc, Input,Output, callback
import pandas as pd

df_ecosistemas = pd.read_excel(io="src/assets/recursos/ese_definiciones.xlsx", sheet_name='ecosistemas')
ecosistemas = df_ecosistemas[['ecosistema', 'definicion']]

df_servicios = pd.read_excel(io="src/assets/recursos/ese_definiciones.xlsx", sheet_name='ssee')


dash.register_page(__name__)

layout = html.Div(
    className="background",
    children=[
        html.Div(
            className="ad-layout",
            children=[
                html.Div(
                    className="panel-control",
                    children=[
                        html.Label("Código CIIU"),
                        dcc.Input(className="input-ciiu", id="ciiu", type="number", placeholder="####"),
                        html.Label("Sector(es)"),
                        dcc.Dropdown(className="select-sectores", options=['NYC', 'MTL', 'SF'], id='demo-dropdown'),
                        html.Label("Sub-Sector(es)"),
                        dcc.Dropdown(className="select-subsectores", options=['NYC', 'MTL', 'SF'], id='demo-dropdown'),
                        html.Button(className="btn-buscar",children="Buscar"),
                    ],
                ),
                html.Div(
                    className="categorias",
                    children=[
                        html.Div(
                            className="seleccion-categoria",
                            children=[
                                html.Button(className="btn-ctg", children="Ecosistema", id='btn-ecosistemas', n_clicks=0),
                                html.Button(className="btn-ctg", children="Servicios Eco", id='btn-servicios'),
                                html.Button(className="btn-ctg", children="Especies"),
                            ],
                        ),
                        html.Div(
                            className="elementos-categoria",
                            id = "elementos-categoria",
                            children=[
                                html.Div(
                                    className="elemento",
                                    
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)

@callback(
    Output('elementos-categoria','children', allow_duplicate=True),
    Input('btn-ecosistemas','n_clicks'),
    Input('btn-servicios','n_clicks'),
    prevent_initial_call=True
)
def update_elementos(n_clicks_ecosistemas, n_clicks_servicios):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'btn-ecosistemas' and n_clicks_ecosistemas:
        updated_content = [
            html.Div(
                className="elemento",
                children=[
                    html.H4(className="elemento-imagen", children=row['ecosistema'][0]),
                    html.Div(
                        className="elemento-informacion",
                        children=[
                            html.Div(
                                className="titulo-botones",
                                children=[
                                    html.H3(className="elemento-titulo", children=row['ecosistema']),
                                    html.Button(html.Img(src="../assets/imagenes/add.png", alt="+"), className="btn-add"),
                                    html.Button(html.Img(src="../assets/imagenes/information.png", alt="i"), className="btn-info"),
                                ],
                            ),
                            html.Div(
                                className="elemento-descripcion",
                                children=row['definicion']
                            ),
                        ],
                    ),
                ]) for index, row in ecosistemas.iterrows()
            ]
    elif button_id == 'btn-servicios' and n_clicks_servicios:
        updated_content = [
            html.Div(
                className="elemento",
                children=[
                    html.H4(className="elemento-imagen", children=row['categoria'][0]),
                    html.Div(
                        className="elemento-informacion",
                        children=[
                            html.Div(
                                className="titulo-botones",
                                children=[
                                    html.H3(className="elemento-titulo", children=row['subcategoria'] if row['subcategoria'] != 'na' else row['nombre']),
                                    html.Button(html.Img(src="../assets/imagenes/add.png", alt="+"), className="btn-add"),
                                    html.Button(html.Img(src="../assets/imagenes/information.png", alt="i"), className="btn-info"),
                                ],
                            ),
                            html.Div(
                                className="elemento-descripcion",
                                children=row['definicion']
                            ),
                        ],
                    ),
                ]) for index, row in df_servicios.iterrows()
            ]
    else:
        updated_content = []

    return updated_content