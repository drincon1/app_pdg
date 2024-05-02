import dash 
from dash import html, dcc, Input,Output, State, callback, ALL
import pandas as pd


df_sectores = pd.read_excel(io="src/assets/recursos/sectores.xlsx", sheet_name='sectores')
df_industrias = pd.read_excel(io="src/assets/recursos/sectores.xlsx", sheet_name='industrias')

sectores = df_sectores['nombre']
industrias = df_industrias['nombre']

df_ecosistemas = pd.read_excel(io="src/assets/recursos/ese_definiciones.xlsx", sheet_name='ecosistemas')
ecosistemas = df_ecosistemas[['id','ecosistema', 'definicion']]

df_servicios = pd.read_excel(io="src/assets/recursos/ese_definiciones.xlsx", sheet_name='ssee')

btn_elementos = []

dash.register_page(__name__)

#TODO: 
layout = html.Div(
    className="background",
    children=[
        html.Div(
            className="ad-layout",
            children=[
                html.Div(
                    className="panel-control",
                    children=[
                        # html.Label("Código CIIU"),
                        # dcc.Input(className="input-ciiu", id="ciiu", type="number", placeholder="####"),
                        html.Div(
                            className="label-clear",
                            children=[
                                html.Label("Sector"),
                                html.Button(className="btn-clear",children="x", id="btn-clear-sector", n_clicks=0)
                            ]
                        ),
                        dcc.Dropdown(className="select-sectores", options=sectores, id='dropdown-sectores', clearable=False, optionHeight=45),
                        html.Label("Industrias"),
                        dcc.Dropdown(className="select-industrias", options=industrias, id='dropdown-industrias', clearable=False, optionHeight=45),
                        html.Button(className="btn-buscar",children="Buscar"),
                    ],
                ),
                html.Div(
                    className="categorias-continuar",
                    children=[
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
                        html.Div(
                            className="div-continuar",
                            children=[
                                html.Button("Continuar",id="btn-continuar",className="btn-continuar",disabled=True),
                                ]
                            ),
                    ]
                    ),
                
            ],
        ),
    ],
)

# ----------------CALLBACKS----------------

# Callback -> Cuando se selecciona un sector en particular, aparecen las industrias respectivas
@callback(
    Output('dropdown-industrias','options'),
    [Input('dropdown-sectores','value')]
)
def update_industrias(nombre_sector):
    if not nombre_sector:
        return industrias
    
    # Buscar el id del sector que fue seleccionado
    id_sector = df_sectores[df_sectores["nombre"] == nombre_sector]["id"].iloc[0]
    
    opciones_industrias = df_industrias[df_industrias["id_sector"] == id_sector]
    
    opciones = [{'label': row['nombre'], 'value': row['nombre']} for index, row in opciones_industrias.iterrows()]
    
    return opciones

# Callback -> Cuando se presiona la 'x' se limpia el dropdown sector
@callback(
    [Output('dropdown-sectores','value'),
        Output('dropdown-industrias','value')],
    [Input('btn-clear-sector','n_clicks')],
    prevent_initial_call=True
)
def update_sectores(num_clicks):
    if num_clicks:
        return None, None
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    return sectores, industrias



# Callback -> Cuando se quiere seleccionar un elemento
@callback(
    Output('ciiu','value'),
    Input({'type':'btn-add-ecosistema','index':ALL}, 'n_clicks')
)
def select_elemento(num_clicks):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0][9:10]
    print(button_id)


# Callback -> Cuando se preciona el boton 'Ecosistema' o 'Servicios Eco' aparecen los respectivos elementos
@callback(
    Output('elementos-categoria','children'),
    [Input('btn-ecosistemas','n_clicks'),
     Input('btn-servicios','n_clicks')],
    prevent_initial_call=True
)
def update_elementos(n_clicks_ecosistemas, n_clicks_servicios):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = None
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    updated_content = []
    
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
                                    html.H3(className="elemento-titulo", children=row['ecosistema'], id='titulo-elemento'),
                                    html.Button(html.Img(src="../assets/imagenes/information.png", alt="i"), className="btn-info"),
                                    html.Button(html.Img(src="../assets/imagenes/add.png", alt="+"),className="btn-add",id={"type": "btn-add-ecosistema", "index":int(row['id'])}),
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

    return updated_content
