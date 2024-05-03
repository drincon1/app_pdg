import dash_bootstrap_components as dbc
import dash 
from dash import html, Output, Input, State, callback, dcc, dash_table
from dash.exceptions import PreventUpdate
import pandas as pd

dash.register_page(__name__)

columns = ['Nombre','Unidad','Frecuencia','Fuente']
df = pd.DataFrame(columns=columns)

def build_upper_left_panel():
    return html.Div(
        id="upper-left",
        className="six columns",
        children=[
            html.P(
                className="section-title",
                children="Ingrese la información del indicador que desea agregar.",
            ),
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="state-select-outer",
                        children=[
                            html.Label("Nombre del indicador"),
                            dcc.Input(
                                #id="state-select",
                                id = "input-name",
                                placeholder="Ingrese el nombre...",
                                type='text',
                                value=''
                            ),
                        ],
                    ),
                    html.Div(
                        id="select-metric-outer",
                        children=[
                            html.Label("Unidades del indicador"),
                            dcc.Input(
                                #id="metric-select",
                                id = 'input-unidad',
                                placeholder="Ingrese las unidades...",
                                type='text',
                                value=''
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                id="region-select-outer",
                className="control-row-2",
                children=[
                    # html.Label("Características del indicador"),
                    html.Div(
                        id="descripcion-container",
                        children=[
                            html.Label("Descripcion"),
                            dcc.Textarea(
                                id = 'txt-descripcion',
                                placeholder='Ingrese la descripción del indicador',
                                style={'width': '100%'}
                            )
                        ]
                    ),
                ],
            ),
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="state-select-outer",
                        children=[
                            html.Label("Frecuencia de medición"),
                            dcc.Dropdown(
                                id="select-frecuencia",
                                options=["Diario", "Semanal", "Mensual", "Bimestral", "Trimestral", "Semestral", "Anual"],
                            ),
                        ],
                    ),
                    html.Div(
                        id="select-metric-outer",
                        children=[
                            html.Label("Fuente de información"),
                            dcc.Dropdown(
                                id="select-fuente",
                                options=["Propia","Otro"],
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                children=[
                    html.Div(
                        id="checklist-container",
                        children=[
                            html.Button("Agregar umbral", id ="btn-agregar-umbral",className="button-primary")
                        ]
                        #dcc.Checklist(
                        #     id="region-select-all",
                        #     options=[{"label": "Umbral", "value": True}],
                        # ),
                    ),
                    html.Div(
                        id="region-umbral",
                        className="control-row-1",
                    ),
                ],
            ),
            html.Div(
                id = "contenedor-botones",
                className="control-row-1",
                children=[
                    html.Button("Cancelar", id='btn-cancelar'),
                    html.Button("Agregar más", id='btn-agregar-mas'),
                    html.Button("Guardar todos",id="btn-guardar", className="button-primary"),
                ],
            ),
            html.Div(
                id = "contenedor-mensaje-guardados",
                className="control-row-1",
                children=html.P(id='mensaje-guarado',style={'font-style': 'italic','margin-top':'20px'})
            ),
        ],
    )

layout = html.Div(
    className="container scalable",
    children=[
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.H6("Indicadores"),
            ],
        ),
        html.Div(
            id="upper-container",
            className="row",
            children=[
                build_upper_left_panel(),
                html.Div(
                    id="geo-map-outer",
                    className="six columns",
                    children=[
                        html.P(
                            id="map-title",
                            children="Indicadores agregados"
                        ),
                        html.Div(
                            id="geo-map-loading-outer",
                        ),
                    ],
                ),
                
            ],
        ),
    ],
)

@callback(
    Output('mensaje-guarado','children'),
    Input('btn-guardar', 'n_clicks'),
    prevent_initial_call=True
)
def guardar_todos(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    elif df.empty:
        return ["No hay indicadores por guardar. Si desea guardar indicadores llene la información solicitada y luego presione el botón 'Agregar más'"]
    return ["Indicadores guardados exitosamente. Muchas gracias por su información."]

@callback(
    Output('geo-map-loading-outer','children'),
    [State('input-name','value'),
     State('input-unidad','value'),
     State('select-frecuencia','value'),
     State('select-fuente','value'),],
    Input('btn-agregar-mas', 'n_clicks'),
    prevent_initial_call=True
)
def agregar_mas(nombre,unidad,frecuencia,fuente,n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    
    new_entry =  pd.DataFrame({'Nombre': [nombre],'Unidad':[unidad],'Frecuencia': [frecuencia],'Fuente':[fuente]},)
    global df
    df = pd.concat([df, new_entry], ignore_index=True)
    
    return dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
    


@callback(
    [Output('input-name','value'),
     Output('input-unidad','value'),
     Output('txt-descripcion','value'),
     Output('select-frecuencia','value'),
     Output('select-fuente','value'),
     Output('region-umbral','children',allow_duplicate=True),
     Output('mensaje-guarado','children',allow_duplicate=True)],
    Input('btn-cancelar', 'n_clicks'),
    prevent_initial_call=True
)
def cancelar_indicador(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    return '','','',None,None, [],[]



@callback(
    Output('region-umbral','children'),
    Input('btn-agregar-umbral','n_clicks'),
    prevent_initial_call=True
)
def add_umbral(n_clicks):
    if n_clicks is None:
        return []
    return [
        html.Div([
                html.Label("Mínimo"),
                dcc.Input(
                    id="umbral-min",
                    placeholder="Min.",
                    type='text',
                    value=''
                ),
            ]
        ),
        html.Div([
                html.Label("Máximo"),
                dcc.Input(
                    id="umbral-max",
                    placeholder="Máx.",
                    type='text',
                    value=''
                ),
            ]
        ),     
    ]
    
    