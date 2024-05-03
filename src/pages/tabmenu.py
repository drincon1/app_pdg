import dash 
from dash import html, dcc, Input,Output, State, callback, ALL
from components import proceso

dash.register_page(__name__)

layout = html.Div([
    dcc.Tabs(id="tab-main", className="tab-main", value='tab-proceso', children=[
        dcc.Tab(label='Proceso', value='tab-proceso'),
        dcc.Tab(label='Cultura eco.', value='tab-cultura-eco'),
        dcc.Tab(label='Talento Humano', value='tab-talento-humano'),
        dcc.Tab(label='Acc/Decs', value='tab-acc-decs'),
        dcc.Tab(label='Acceso a datos/tecno', value='tab-acceso-datos-tecno'),
        dcc.Tab(label='Monitoreo', value='tab-monitoreo'),
    ]),
    html.Div(className="container", 
             children=[
                html.Div(id='main-display',className="main-display"),
                html.Div(className="button-display", children=[
                        html.Button('Continuar',id='btn-next-tab'),
                    ]),
        ]),
    
])

@callback(Output('main-display', 'children'),
            Input('tab-main', 'value'))
def render_content(tab):
    if tab == 'tab-proceso':
        return proceso.layout
    elif tab == 'tab-cultura-eco':
        return cultura_eco.layout
    elif tab == 'tab-talento-humano':
        return talento_humano.layout
    elif tab == 'tab-acc-decs':
        return acc_decs.layout
    elif tab == 'tab-acceso-datos-tecno':
        return acceso_datos.layout
    elif tab == 'tab-monitoreo':
        return monitoreo.layout
    else:
        return html.H1(f"NO TAB WAS FOUND UNDER THE NAME: {tab}")