import pandas as pd
import dash
from dash import html, callback, Input, State, Output, dcc
from dash.exceptions import PreventUpdate

preguntas = pd.read_csv("src/assets/recursos/preguntas.csv")
print(preguntas)

dash.register_page(__name__)

layout = html.Div(children=[
    html.Div(className="background", id='background', children=[
        html.Div(className="seccion-cuestionario", children=[
            html.Div(className='seccion-progreso',children=[
                dcc.Slider(id='avance-preguntas',min=1, max=14, step=1, value=1)
            ]),
            html.Div(className='seccion-preguntas',id='seccion-preguntas'),
            html.Div(className='seccion-botones', children=[
                html.Button("Atrás",id='btn-atras'),
                html.Button("Siguiente",id='btn-siguiente'),
            ]),
        ])
    ])
])

def obtener_pregunta(numero_pregunta):
    global preguntas
    pregunta = preguntas.iloc[numero_pregunta]
    tipo = pregunta['tipo']
    texto_pregunta = pregunta['pregunta']
    opciones = pregunta['opciones'].split('-')
    
    texto_pregunta_html = html.P(texto_pregunta, className="texto-pregunta")
    
    if tipo == 'FV':
        return html.Div([
            texto_pregunta_html,
            dcc.RadioItems(
                id='respuesta-fv',
                options=[{'label': 'Verdadero', 'value': 'Verdadero'}, {'label': 'Falso', 'value': 'Falso'}]
            )
        ])
    elif tipo == 'MC':
        return html.Div([
            texto_pregunta_html,
            dcc.RadioItems(
                id='respuesta-mc',
                options=[{'label': opcion, 'value': opcion} for opcion in opciones]
            )
        ])
    elif tipo == 'E':
        return html.Div([
            texto_pregunta_html,
            dcc.Dropdown(
                options=[{'label': opcion, 'value': opcion} for opcion in opciones],
                style={'width':'750px'}
            ),
        ])
    elif tipo == 'EM':
        return html.Div([
            texto_pregunta_html,
            dcc.Checklist(
                options=[{'label': opcion, 'value': opcion} for opcion in opciones]
            ),
        ])

              
        
@callback(
    [Output('seccion-preguntas','children'),
     Output('avance-preguntas','value')],
    Input('background','children'),
)
def obtener_primera_pregunta(children):
    return obtener_pregunta(0),1

@callback(
    Output('seccion-preguntas', 'children', allow_duplicate=True),
    Input('avance-preguntas', 'value'),
    prevent_initial_call=True
)
def actualizar_pregunta(numero_pregunta):
    return obtener_pregunta(numero_pregunta - 1)


@callback(
    [Output('seccion-preguntas','children',allow_duplicate=True),
     Output('avance-preguntas','value',allow_duplicate=True)],
    State('avance-preguntas','value'),
    Input('btn-siguiente','n_clicks'),
    prevent_initial_call=True
)
def siguiente_pregunta(num_pregunta,n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    return obtener_pregunta(num_pregunta),num_pregunta+1

@callback(
    [Output('seccion-preguntas','children',allow_duplicate=True),
     Output('avance-preguntas','value',allow_duplicate=True)],
    State('avance-preguntas','value'),
    Input('btn-atras','n_clicks'),
    prevent_initial_call=True
)
def anterior_pregunta(num_pregunta,n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    return obtener_pregunta(num_pregunta-2),num_pregunta-1