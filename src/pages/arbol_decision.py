import dash 
from dash import html, dcc

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
                        dcc.Dropdown(className="select-sectores", options=['NYC', 'MTL', 'SF'], value='NYC', id='demo-dropdown'),
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
                                html.Button(className="btn-ctg", children="Ecosistema"),
                                html.Button(className="btn-ctg", children="Servicios Eco"),
                                html.Button(className="btn-ctg", children="Especies"),
                            ],
                        ),
                        html.Div(
                            className="elementos-categoria",
                            children=[
                                html.Div(
                                    className="elemento",
                                    children=[
                                        html.H4(className="elemento-imagen", children="A"),
                                        html.Div(
                                            className="elemento-informacion",
                                            children=[
                                                html.Div(
                                                    className="titulo-botones",
                                                    children=[
                                                        html.H3(className="elemento-titulo", children="Materias primas"),
                                                        html.Button(html.Img(src="../assets/add.png", alt="+"), className="btn-add"),
                                                        html.Button(html.Img(src="../assets/information.png", alt="i"), className="btn-info"),
                                                    ],
                                                ),
                                                html.Div(
                                                    className="elemento-descripcion",
                                                    children="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin et lorem ut lorem tincidunt tempus. Aenean eleifend ultricies leo sit amet efficitur.",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
