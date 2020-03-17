import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import query
color={
'background': '#111111',
    'text': '#ff947f'
}

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