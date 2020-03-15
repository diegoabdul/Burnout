import re

import dash
from dash.dependencies import Input, Output,State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import query
import pandas as pd
import Clasificacion

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Sistema de Detección", href="/deteccion")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Datos Categorizados",
            children=[
                dbc.DropdownMenuItem("Burnout & Datos Fisiológicos en Detalle", href="/fisiologicos"),
                dbc.DropdownMenuItem("Burnout & Datos Fisiológicos por Paciente", href="/paciente"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Subescalas", href="/subescalas"),
                dbc.DropdownMenuItem("Burnout por Subescalas Individuales", href="/subescalasindividual"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Especialidad", href="/especialidad"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Sexo", href="/sexo"),
            ],

        ),
        dbc.NavItem(dbc.NavLink("Descargar los Datos", href="https://storage.googleapis.com/burnout/Burnout_Data.csv"))
    ],
    brand="Burnout",
    #brand_external_link='https://storage.cloud.google.com/burnout/Burnout.png'
    #src='data:image/png;base64,{}'.format(encoded_image),
    brand_href="http://127.0.0.1:8050/",
    sticky="top",

)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
color={
'background': '#111111',
    'text': '#ff947f'
}
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
Fisiologicos = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Burnout & Datos Fisiológicos en Detalle"),
                        dash_table.DataTable(
                            id='datatable-interactivity',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_DatosFisiologicos.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_DatosFisiologicos.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            row_selectable='multi',
                            row_deletable=True,
                            selected_rows=[],
                            page_action='native',
                            page_current=0,
                            page_size=4,
                        ),
                        html.Div(id='datatable-interactivity-container'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

FisiologicosXPaciente = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Burnout & Datos Fisiológicos por Paciente"),
                        dash_table.DataTable(
                            id='datatable-interactivity6',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_DatosFisiologicosIndividuales.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_DatosFisiologicosIndividuales.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            row_selectable='multi',
                            row_deletable=True,
                            selected_rows=[],
                            page_action='native',
                            page_current=0,
                            page_size=4,
                        ),
                        html.Div(id='datatable-interactivity-container6'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

Subescalas = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Burnout por Subescalas"),
                        dash_table.DataTable(
                            id='datatable-interactivity2',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_SubescalasBurnout.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_SubescalasBurnout.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            row_selectable='multi',
                            row_deletable=True,
                            selected_rows=[],
                            page_action='native',
                            page_current=0,
                            page_size=4,
                        ),
                        html.Div(id='datatable-interactivity-container2'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

SubescalasIndividuales = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Burnout & Subescalas por Paciente"),
                        dash_table.DataTable(
                            id='datatable-interactivity3',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_SubescalasIndividual.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_SubescalasIndividual.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            row_selectable='multi',
                            row_deletable=True,
                            selected_rows=[],
                            page_action='native',
                            page_current=0,
                            page_size=4,
                        ),
                        html.Div(id='datatable-interactivity-container3'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

BurnoutXEspecialidad = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Burnout por Especialidad"),
                        dash_table.DataTable(
                            id='datatable-interactivity4',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_Especialidad.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_Especialidad.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            row_selectable='multi',
                            row_deletable=True,
                            selected_rows=[],
                            page_action='native',
                            page_current=0,
                            page_size=4,
                        ),
                        html.Div(id='datatable-interactivity-container4'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

BurnoutXSexo = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Burnout por Sexo"),
                        dash_table.DataTable(
                            id='datatable-interactivity5',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_Sexo.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_Sexo.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            row_selectable='multi',
                            row_deletable=True,
                            selected_rows=[],
                            page_action='native',
                            page_current=0,
                            page_size=4,
                        ),
                        html.Div(id='datatable-interactivity-container5'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

SistemaDeDeteccion = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Sistema de Detección"),
                        dbc.FormGroup(
                            [
                                dbc.Label("Nombre"),
                                dbc.Input(id="nombre", type="text", value=""),
                                dbc.Label("Email"),
                                dbc.Input(id="email-input", type="email", value=""),
                                dbc.FormFeedback(
                                    "That looks like a gmail address :-)", valid=True
                                ),
                                dbc.FormFeedback(
                                    "Sorry, we only accept gmail for some reason...",
                                    valid=False,
                                ),
                                dbc.Label("Sexo", html_for="example-radios-row", width=4),
                                dbc.Col(
                                    dbc.RadioItems(
                                        id="Sexo",
                                        options=[
                                            {"label": "Hombre", "value": "hombre"},
                                            {"label": "Mujer", "value": "mujer"},
                                        ],
                                    ),
                                    width=10,
                                ),
                                dbc.Label("Edad"),
                                dbc.Input(id="edad", type="int", value=""),
                                dbc.FormFeedback(
                                    "OK EDAD:-)", valid=True
                                ),
                                dbc.FormFeedback(
                                    "MAL",
                                    valid=False,
                                ),
                                dbc.Label("Peso"),
                                dbc.Input(id="peso", type="int", value=""),
                                dbc.FormFeedback(
                                    "OK Peso:-)", valid=True
                                ),
                                dbc.FormFeedback(
                                    "MAL Peso",
                                    valid=False,
                                ),
                                dbc.Label("Numero de Hijos"),
                                dbc.Input(id="hijos", type="int", value=""),

                                dbc.Label("Estado Civil", html_for="dropdown"), #EstadoCivil
                                dcc.Dropdown(id="EstadoCivil",options=[
                                        {"label": "Soltero", "value": "soltero"},
                                        {"label": "Casado", "value": "casado"},
                                        {"label": "Divorciado", "value": "divorciado"},
                                    ],
                                ),

                                dbc.Label("Contrato de Trabajo Actual", html_for="dropdown"), #Contrato_Adjunto
                                dcc.Dropdown(id="Contrato_Adjunto",options=[
                                        {"label": "fijo", "value": 1},
                                        {"label": "eventual", "value": 2},
                                        {"label": "interino", "value": 3},
                                        {"label": "N/A", "value": 4},
                                    ],
                                ),

                               dbc.Label("Frecuencia de Musica", html_for="dropdown"), #Musica
                                dcc.Dropdown(id="Musica",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),
                                dbc.Label("Frecuencia de Estudio", html_for="dropdown"), #Estudio
                                dcc.Dropdown(id="Estudio",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),

                                dbc.Label("Frecuencia de Salida Socialmente", html_for="dropdown"), #Sales_Social
                                dcc.Dropdown(id="Sales_Social",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),

                                dbc.Label("Frecuencia de Lectura", html_for="dropdown"), #Lectura
                                dcc.Dropdown(id="Lectura",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),

                                dbc.Label("Frecuencia Cardiaca por Minuto"),#Frecuencia_Cardiaca_Minuto
                                dbc.Input(id="Frecuencia_Cardiaca_Minuto", type="int", value=""),

                                dbc.Label("Frecuencia Cardiaca en Descanso por Minuto"),#Resting_HeartRate
                                dbc.Input(id="Resting_HeartRate", type="int", value=""),

                                dbc.Label("Calorias quemadas al día"),#Calorias
                                dbc.Input(id="Calorias", type="int", value=""),

                                dbc.Label("Tiempo en años en el Trabajo Actual"),#Tiempo_PlazaActual
                                dbc.Input(id="Tiempo_PlazaActual", type="int", value=""),

                                dbc.Label("Horas al Mes que se dedican a Salidas Sociales"),#Hora_Social
                                dbc.Input(id="Hora_Social", type="int", value=""),

                                dbc.Label("Horas al Mes que se dedican a Cuidados Personales"),#Horas_Cuidados
                                dbc.Input(id="Horas_Cuidados", type="int", value=""),

                                dbc.Label("Años de Vida Laboral"),#Tiempo_Vida_Laboral
                                dbc.Input(id="Tiempo_Vida_Laboral", type="int", value=""),

                                dbc.Label("Horas de Sueño al día"),#Minutos_Dormido
                                dbc.Input(id="Minutos_Dormido", type="int", value=""),

                                html.Button(id='submit-button', type='submit', children='Submit'),
                                html.Div(id='output_div')
                            ]
                        )
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])
app.title = 'Burnout Data Website'

bodyIndex = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("¿Qué es el Burnout?"),
                        html.P(
                            """El término burnout o síndrome de quemado por el trabajo se define como la respuesta inadecuada al estrés emocional 
                             crónico que resulta de una discrepancia entre los ideales individuales y la realidad de la vida ocupacional diaria,
                             requiriéndose al menos seis meses de período adaptativo."""
                        ),
                        dbc.Button(
                            "Ver dimensiones del Burnout",
                            id="collapse-button",
                            className="mb-3",
                            color="primary",
                        ),
                        dbc.Collapse(
                            dbc.Card([html.H5("Agotamiento Emocional:"),dbc.CardBody("Pérdida o desgaste de recursos emocionales. "),
                                                  html.H5("Deshumanización o Despersonalización:"),dbc.CardBody("Actitudes negativas, cínicas e insensibles hacia los pacientes, familiares o compañeros."),
                                                  html.H5("Falta de realización personal en el trabajo:"),dbc.CardBody("Tendencia a evaluar el propio trabajo de forma negativa, sentimientos de inadecuación o fracaso.")]),
                            id="collapse",
                        ),
                    ],
                    md=6,
                ),dbc.Col(
                    [
                        html.H2("Factores de Riesgo"),
                        html.P("""Características Personales: Auto criticismo, uso de estrategias de afrontamiento ineficaces, de privación del sueño, desbalance del trabajo & vida personal"""),
                        html.P("""La Organización: Carga de trabajo execiva, falta de control sobre el ambiente laboral, recompensas insuficientes"""),
                        html.P("""Calidad de las relaciones personales laborales: Conflicto y mal ambiente"""),
                        dbc.Button(
                            "Ver consecuencias del Burnout",
                            id="collapse-button2",
                            className="mb-3",
                            color="primary",
                        ),
                        dbc.Collapse(
                            dbc.Card([dbc.CardBody("Trastorno de Estrés Postraumático."),html.Br(),
                            dbc.CardBody("Abuso de Alchol e incluso ideación autolítica."),html.Br(),
                            dbc.CardBody("Aumento de errores en el entorno laboral.")]),
                            id="collapse2",
                        ),
                    ],
                    md=6,
                )
            ]
        ),
        dbc.Row(
                dbc.Col(
                    [
                        html.H2("Datos Recopilados"),
                        html.P("La población de este estudio esta compuesta por médicos de servicios de Urgencias y Psiquiatría de dos hospitales participantes, "
                               "Hospital Son Llàtzer de Palma de Mallorca y el Hospital Infanta Sofía de San Sebastian de los Reyes, Madrid."),html.Br(),
                        html.P("Gracias a ellos hemos podido presentar los datos contenidos en esta página web, concluir ciertas hipótesis y construir un sistema de detección del Síndrome de Burnout."),
                        dcc.Graph(figure={
                "data": [
                    {
                        "x": query.df_DatosFisiologicos["Burnout"],
                        "y": query.df_DatosFisiologicos["Calorias"],
                        "type": "bar",
                        "marker": {"color": color},
                        'name': 'Calorias',
                    },{
                        "x": query.df_DatosFisiologicos["Burnout"],
                        "y": query.df_DatosFisiologicos["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        'name': 'Frecuencia_Cardiaca_Minuto',
                    },{
                        "x": query.df_DatosFisiologicos["Burnout"],
                        "y": query.df_DatosFisiologicos["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        'name': 'Eficiencia_Sueno',
                    },{
                        "x": query.df_DatosFisiologicos["Burnout"],
                        "y": query.df_DatosFisiologicos["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        'name': 'Resting_HeartRate',
                    },{
                        "x": query.df_DatosFisiologicos["Burnout"],
                        "y": query.df_DatosFisiologicos["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        'name': 'Max_HeartRate',
                    },{
                        "x": query.df_DatosFisiologicos["Burnout"],
                        "y": query.df_DatosFisiologicos["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        'name': 'Min_HeartRate',
                    },

                ],
                "layout": {
                    "xaxis": {"automargin": False},
                    "yaxis": {
                        "automargin": False,
                        "title": {"text": "Calorias"}
                    },
                    "height": 250,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            }),
                    ]
                )
        )
    ],
    className="mt-4",
)

index_page = html.Div([navbar,bodyIndex])
page_1_layout = html.Div([navbar,Fisiologicos])
page_2_layout = html.Div([navbar,Subescalas])
page_3_layout = html.Div([navbar,SubescalasIndividuales])
page_4_layout = html.Div([navbar,BurnoutXEspecialidad])
page_5_layout = html.Div([navbar,BurnoutXSexo])
page_6_layout = html.Div([navbar,FisiologicosXPaciente])
page_7_layout = html.Div([navbar,SistemaDeDeteccion])
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/fisiologicos':
        return page_1_layout
    if pathname == '/subescalas':
        return page_2_layout
    if pathname == '/subescalasindividual':
        return page_3_layout
    if pathname == '/especialidad':
        return page_4_layout
    if pathname == '/sexo':
        return page_5_layout
    if pathname == '/paciente':
        return page_6_layout
    if pathname == '/deteccion':
        return page_7_layout
    else:
        return index_page

@app.callback(
    Output('datatable-interactivity-container', "children"),
    [Input('datatable-interactivity', "derived_virtual_data"),
     Input('datatable-interactivity', "derived_virtual_selected_rows")])
def update_graphs(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = query.df_DatosFisiologicos if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        dcc.Graph(
            id='basic-interactions',
            figure={
                'data': [
                    {
                        "x": dff["Burnout"],
                        "y": dff["Calorias"],
                        'text': 'Calorias',
                        'name': 'Calorias',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        'text': 'Frecuencia_Cardiaca_Minuto',
                        'name': 'Frecuencia Cardiaca Minuto',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Resting_HeartRate"],
                        'text': 'Resting_HeartRate',
                        'name': 'Resting_HeartRate',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Eficiencia_Sueno"],
                        'text': 'Eficiencia_Sueno',
                        'name': 'Eficiencia_Sueno',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Peso"],
                        'text': 'Peso',
                        'name': 'Peso',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Hijos"],
                        'text': 'Hijos',
                        'name': 'Hijos',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Tiempo_Plaza"],
                        'text': 'Tiempo_Plaza',
                        'name': 'Tiempo_Plaza',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        'text': 'Tiempo_Vida_Laboral',
                        'name': 'Tiempo_Vida_Laboral',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Max_HeartRate"],
                        'text': 'Max_HeartRate',
                        'name': 'Max_HeartRate',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Min_HeartRate"],
                        'text': 'Min_HeartRate',
                        'name': 'Min_HeartRate',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["Minutos_Rem"],
                        'text': 'Minutos_Rem',
                        'name': 'Minutos_Rem',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },{
                        "x": dff["Burnout"],
                        "y": dff["SuenoProfundo"],
                        'text': 'SuenoProfundo',
                        'name': 'SuenoProfundo',
                        'mode': 'markers',
                        'marker': {'size': 16}
                    },
                ],
                'layout': {
                    'clickmode': 'event+select'
                }
            }
        )
    ]


@app.callback(
    Output('datatable-interactivity-container2', "children"),
    [Input('datatable-interactivity2', "derived_virtual_data"),
     Input('datatable-interactivity2', "derived_virtual_selected_rows")])
def update_graphs2(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = query.df_SubescalasBurnout if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [html.Br(),
        html.H5("Primera Encuesta de Burnout"),
        dcc.Graph(
            id=12,
            figure={
                "data": [
                    {
                        "x": dff["Burnout_Antes"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Cansancio_Emocional",
                    },
                    {
                        "x": dff["Burnout_Antes"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Despersonalizacion",
                    },
                    {
                        "x": dff["Burnout_Antes"],
                        "y": dff["Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                    },
                    "height": 250,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            },
        ),
        html.Br(),
        html.H5("Segunda Encuesta de Burnout"),
        dcc.Graph(
            id=22,
            figure={
                "data": [
                    {
                        "x": dff["Burnout_Despues"],
                        "y": dff["Ultima_Encuesta_Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Realizacion_Personal",
                    },
                    {
                        "x": dff["Burnout_Despues"],
                        "y": dff["Ultima_Encuesta_Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    },
                    {
                        "x": dff["Burnout_Despues"],
                        "y": dff["Ultima_Encuesta_Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True,
                    },
                    "height": 250,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            },
        )
        # check if column exists - user may have deleted it
        #If `column.deletable=False`, then you don't
        # need to do this check.
       # for column in ["Cansancio_Emocional","Despersonalizacion","Realizacion_Personal"] if column in dff
    ]

@app.callback(
    Output('datatable-interactivity-container3', "children"),
    [Input('datatable-interactivity3', "derived_virtual_data"),
     Input('datatable-interactivity3', "derived_virtual_selected_rows")])
def update_graphs3(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = query.df_SubescalasIndividual if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("Primera Encuesta de Burnout"),
        dcc.Graph(
            id=3,
            figure={
                "data": [
                    {
                        "x": dff["Identificador"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Cansancio_Emocional",
                    },
                    {
                        "x": dff["Identificador"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Despersonalizacion",
                    },
                    {
                        "x": dff["Identificador"],
                        "y": dff["Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },
                    {
                        "x": dff["Identificador"],
                        "y": dff["Burnout_Antes"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Burnout_Antes",
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True
                    },
                    "height": 300,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            },
        ),
        html.Br(),
        html.H5("Segunda Encuesta de Burnout"),
        dcc.Graph(
            id=4,
            figure={
                "data": [
                    {
                        "x": dff["Identificador"],
                        "y": dff["Ultima_Encuesta_Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Realizacion_Personal",
                    },
                    {
                        "x": dff["Identificador"],
                        "y": dff["Ultima_Encuesta_Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    },
                    {
                        "x": dff["Identificador"],
                        "y": dff["Ultima_Encuesta_Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    },{
                        "x": dff["Identificador"],
                        "y": dff["Burnout_Despues"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Burnout_Despues",
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True
                    },
                    "height": 300,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            },
        )
        # check if column exists - user may have deleted it
        #If `column.deletable=False`, then you don't
        # need to do this check.
       # for column in ["Cansancio_Emocional","Despersonalizacion","Realizacion_Personal"] if column in dff
    ]


@app.callback(
    Output('datatable-interactivity-container4', "children"),
    [Input('datatable-interactivity4', "derived_virtual_data"),
     Input('datatable-interactivity4', "derived_virtual_selected_rows")])
def update_graphs3(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = query.df_Especialidad if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("Primera Encuesta de Burnout"),
        dcc.Graph(
            id=31,
            figure={
                "data": [
                    {
                        "x": dff["Especialidad"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["Especialidad"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["Especialidad"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },
                    {
                        "x": dff["Especialidad"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Hijos"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hijos",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["Especialidad"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["Especialidad"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["Especialidad"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["Especialidad"],
                        "y": dff["Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True
                    },
                    "height": 300,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            },
        ),
        # check if column exists - user may have deleted it
        #If `column.deletable=False`, then you don't
        # need to do this check.
       # for column in ["Cansancio_Emocional","Despersonalizacion","Realizacion_Personal"] if column in dff
    ]


@app.callback(
    Output('datatable-interactivity-container5', "children"),
    [Input('datatable-interactivity5', "derived_virtual_data"),
     Input('datatable-interactivity5', "derived_virtual_selected_rows")])
def update_graphs3(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = query.df_Sexo if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("Primera Encuesta de Burnout"),
        dcc.Graph(
            id=31,
            figure={
                "data": [
                    {
                        "x": dff["Sexo"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["Sexo"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["Sexo"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Hijos"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hijos",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["Sexo"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["Sexo"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["Sexo"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["Sexo"],
                        "y": dff["Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True
                    },
                    "height": 300,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            },
        ),
        # check if column exists - user may have deleted it
        #If `column.deletable=False`, then you don't
        # need to do this check.
       # for column in ["Cansancio_Emocional","Despersonalizacion","Realizacion_Personal"] if column in dff
    ]

@app.callback(
    Output('datatable-interactivity-container6', "children"),
    [Input('datatable-interactivity6', "derived_virtual_data"),
     Input('datatable-interactivity6', "derived_virtual_selected_rows")])
def update_graphs3(rows, derived_virtual_selected_rows):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncracy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []

    dff = query.df_DatosFisiologicosIndividuales if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("Primera Encuesta de Burnout"),
        dcc.Graph(
            id=31,
            figure={
                "data": [
                    {
                        "x": dff["Email"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["Email"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["Email"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },{
                        "x": dff["Email"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["Email"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["Email"],
                        "y": dff["Hijos"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hijos",
                    },{
                        "x": dff["Email"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["Email"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["Email"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["Email"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["Email"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["Email"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["Email"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["Email"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["Email"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["Email"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["Email"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["Email"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["Email"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["Email"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["Email"],
                        "y": dff["Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },{
                        "x": dff["Email"],
                        "y": dff["Altura"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Altura",
                    },{
                        "x": dff["Email"],
                        "y": dff["Tiempo_PlazaActual"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_PlazaActual",
                    },{
                        "x": dff["Email"],
                        "y": dff["Ultima_Encuesta_Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Ultima_Encuesta_Cansancio_Emocional",
                    },{
                        "x": dff["Email"],
                        "y": dff["Ultima_Encuesta_Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Ultima_Encuesta_Despersonalizacion",
                    },{
                        "x": dff["Email"],
                        "y": dff["Ultima_Encuesta_Realizacion_Personal"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Ultima_Encuesta_Realizacion_Personal",
                    },{
                        "x": dff["Email"],
                        "y": dff["Horas_Cuidados"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Horas_Cuidados",
                    },{
                        "x": dff["Email"],
                        "y": dff["Horas_Activ_Fisica"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Horas_Activ_Fisica",
                    },{
                        "x": dff["Email"],
                        "y": dff["Hora_Gratificante"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hora_Gratificante",
                    },{
                        "x": dff["Email"],
                        "y": dff["Hora_Social"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hora_Social",
                    }
                ],
                "layout": {
                    "xaxis": {"automargin": True},
                    "yaxis": {
                        "automargin": True
                    },
                    "height": 300,
                    "margin": {"t": 50, "l": 50, "r": 50},
                },
            },
        ),
        # check if column exists - user may have deleted it
        #If `column.deletable=False`, then you don't
        # need to do this check.
       # for column in ["Cansancio_Emocional","Despersonalizacion","Realizacion_Personal"] if column in dff
    ]

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse2", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("collapse2", "is_open")],
)

@app.callback(
    [Output("email-input", "valid"), Output("email-input", "invalid")],
    [Input("email-input", "value")],
)

def check_validity(text):
    if text:
        is_gmail = text.endswith("@gmail.com") or text.endswith("@hotmail.com") or text.endswith("@yahoo.com")
        return is_gmail, not is_gmail
    return False, False

@app.callback(
    [Output("edad", "valid"), Output("edad", "invalid")],
    [Input("edad", "value")],
)

def check_edad(edad):
    if edad:
        is_gmail = bool(re.match("^[0-9 \-]+$", edad))
        return is_gmail, not is_gmail
    return False, False

def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('output_div', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('nombre', 'value'),State('email-input', 'value'),State('Sexo', 'value'),State('edad', 'value'),State('peso', 'value'),
                   State('hijos', 'value'),State('EstadoCivil', 'value'),State('Contrato_Adjunto', 'value'),State('Musica', 'value'),
                   State('Estudio', 'value'),State('Sales_Social', 'value'),State('Lectura', 'value'),State('Frecuencia_Cardiaca_Minuto', 'value'),
                   State('Resting_HeartRate', 'value'),State('Calorias', 'value'),State('Tiempo_PlazaActual', 'value'),State('Hora_Social', 'value'),
                   State('Horas_Cuidados', 'value'),State('Tiempo_Vida_Laboral', 'value'),State('Minutos_Dormido', 'value')
                   ]

              )
def update_output(clicks,nombre,Email,Sexo,Edad,Peso,hijos,EstadoCivil,Contrato_Adjunto,Musica,Estudio,Sales_Social,Lectura,Frecuencia_Cardiaca_Minuto,Resting_HeartRate,Calorias,Tiempo_PlazaActual,Hora_Social,Horas_Cuidados,Tiempo_Vida_Laboral,Minutos_Dormido):
    if clicks is not None:
        print(nombre,Email,Sexo,Edad,Peso,hijos,EstadoCivil,Contrato_Adjunto,Musica,Estudio,Sales_Social,Lectura,Frecuencia_Cardiaca_Minuto,Resting_HeartRate,Calorias,Tiempo_PlazaActual,Hora_Social,Horas_Cuidados,Tiempo_Vida_Laboral,Minutos_Dormido)
        df = pd.DataFrame({'Sexo': [Sexo], 'Edad': [Edad], 'Peso': [float(Peso)], 'Hijos': [float(hijos)], 'EstadoCivil': [EstadoCivil], 'Contrato_Adjunto': [Contrato_Adjunto], 'Musica': [Musica], 'Estudias': [Estudio], 'Sales_Social': [Sales_Social], 'Lectura': [Lectura], 'Frecuencia_Cardiaca_Minuto': [float(Frecuencia_Cardiaca_Minuto)], 'Resting_HeartRate': [float(Resting_HeartRate)], 'Calorias': [float(Calorias)], 'Tiempo_PlazaActual': [float(Tiempo_PlazaActual)], 'Hora_Social': [float(Hora_Social)], 'Horas_Cuidados': [float(Horas_Cuidados)], 'Tiempo_Vida_Laboral': [float(Tiempo_Vida_Laboral)], 'Minutos_Dormido': [float(Minutos_Dormido)], 'Estado_Animo': [''], 'Cantidad_Sueno_Profundo': [2]})
        data=Clasificacion.DataPreparation(df)
        Clasificacion.LinearEvaluation(data)

if __name__ == "__main__":
    app.run_server()