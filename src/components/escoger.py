from dataclasses import dataclass, field
from dash import html, dcc, callback, Output,Input

@dataclass
class Escoger:
    pregunta: str
    opciones: list[str] = field(default_factory=list)
    layout = None
    
    def get_layout():
        layout = html.Div(id='main-layout'
        
        )
    
