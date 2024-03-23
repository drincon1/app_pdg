import dash
from dash import html

dash.register_page(__name__,path='/')

layout = html.Div(className="bg-[#FFFFFF] flex flex-row p-[278px_0_278px_0] w-[1512px] box-sizing-border",
    children=[
        html.Div(
            className="m-[354px_57.5px_81px_0] flex flex-col items-center box-sizing-border",
            children=[
                html.Div(
                    className="m-[0_9.3px_33px_0] inline-block break-words font-['Plus_Jakarta_Sans'] font-[var(--heading-h-6-font-weight,500)] text-[var(--heading-h-6-font-size,48px)] tracking-[var(--heading-h-6-letter-spacing,-1px)] leading-[var(--heading-h-6-line-height,1.25)] text-[#000000]",
                    children="Autodiagnóstico: Dependencias e impactos"
                ),
                html.Div(
                    className="m-[0_0_0_28.5px] flex flex-row w-[367px] box-sizing-border",
                    children=[
                        html.Div(
                            className="shadow-[var(--elevation-lightxs,0px_1px_2px_0px_rgba(16,24,40,0.05))] rounded-[4px] border-[1px_solid_var(--primary-500,#6449CC)] bg-[var(--primary-500,#6449CC)] m-[0_44px_0_0] flex flex-row justify-center p-[15px_0.1px_15px_0] w-[153px] box-sizing-border",
                            children=html.Span(
                                className="break-words font-['Plus_Jakarta_Sans'] font-[var(--button-medium-font-weight,500)] text-[var(--button-medium-font-size,20px)] tracking-[var(--button-medium-letter-spacing,-0.2px)] leading-[var(--button-medium-line-height,1.2)] text-[var(--neutrals-50,#FCFCFC)]",
                                children="Comenzar"
                            )
                        ),
                        html.Div(
                            className="rounded-[4px] border-[1px_solid_var(--neutrals-400,#C2C2C2)] bg-[var(--neutrals-50,#FCFCFC)] flex flex-row justify-center p-[15px_0.4px_15px_0] w-[170px] box-sizing-border",
                            children=html.Span(
                                className="break-words font-['Plus_Jakarta_Sans'] font-[var(--button-medium-font-weight,500)] text-[var(--button-medium-font-size,20px)] tracking-[var(--button-medium-letter-spacing,-0.2px)] leading-[var(--button-medium-line-height,1.2)] text-[var(--neutrals-800,#2E2E2E)]",
                                children="Información"
                            )
                        )
                    ]
                )
            ]
        ),
        html.Div(
            className="opacity-[0.07] relative m-[278px_0_0_0] w-[547px] h-[426px]",
            children=html.Img(
                className="absolute top-[0px] right-[-89.4px] w-[623.4px] h-[462.5px]"
            )
        )
    ]
)