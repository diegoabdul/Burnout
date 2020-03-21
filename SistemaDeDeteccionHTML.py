import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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
                                dbc.Input(id="edad", type="number", value=""),
                                dbc.Label("Peso"),
                                dbc.Input(id="peso", type="number", value=""),
                                dbc.Label("Numero de Hijos"),
                                dbc.Input(id="hijos", type="number", value=""),

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

                                dbc.Label("Horas al mes Gratificantes"),#Frecuencia_Cardiaca_Minuto
                                dbc.Input(id="Hora_Gratificante", type="number", value=""),

                                dbc.Label("Horas al mes que dedica a Actividades Fisicas"),#Resting_HeartRate
                                dbc.Input(id="Horas_Activ_Fisica", type="number", value=""),

                                dbc.Label("Calorias quemadas al día"),#Calorias
                                dbc.Input(id="Calorias", type="number", value=""),

                                dbc.Label("Tiempo en años en el Trabajo Actual"),#Tiempo_PlazaActual
                                dbc.Input(id="Tiempo_PlazaActual", type="number", value=""),

                                dbc.Label("Horas al Mes que se dedican a Salidas Sociales"),#Hora_Social
                                dbc.Input(id="Hora_Social", type="number", value=""),

                                dbc.Label("Horas al Mes que se dedican a Cuidados Personales"),#Horas_Cuidados
                                dbc.Input(id="Horas_Cuidados", type="number", value=""),

                                dbc.Label("Años de Vida Laboral"),#Tiempo_Vida_Laboral
                                dbc.Input(id="Tiempo_Vida_Laboral", type="number", value=""),

                                dbc.Label("Estado de Ánimo", html_for="dropdown"),#Minutos_Dormido
                                dcc.Dropdown(id="Estado_Animo", options=[
                                    {"label": "Triste", "value": "triste"},
                                    {"label": "Contento", "value": "contento"},
                                    {"label": "Normal", "value": "normal"},
                                ],
                                ),
                                html.Br(),
                                dbc.Button("Ver Evaluación",id='submit-button', color="primary", className="mr-1"),
                                html.Br(),
                                html.Div(id='output_div'),
                            ]
                        )
                    ],
                    md=8,
                ),

            ]
        )
    ],
    className="mt-4",
)