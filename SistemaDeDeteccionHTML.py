import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

SistemaDeDeteccion = dbc.Container(
    [html.Div(
    [dbc.Modal(
            [
                dbc.ModalHeader("Tu Evaluación"),
                #html.Div(id='output_div'),
                dbc.ModalBody(html.Div(id='output_div')),
                dbc.ModalFooter('Click fuera de este recuadro para salir'),
            ],
            id="modal",
        ),
    ]
),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Sistema de Detección"),
                        html.P("Bienvenidos al Sistema de Detección de Burnout."),
                        html.P("Mediante este pequeño formulario, podrás saber si padeces del síndrome de Burnout instantáneamente."),
                        dbc.FormGroup(
                            [
                                dbc.Label("Nombre"),
                                dbc.Input(id="nombre", type="text", value=""),
                                dbc.Label("Correo Electrónico"),
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
                                dbc.Label("Peso en Kilos"),
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

                                html.P('¿Con qué frecuencia escuchas música?'),
                                dcc.Dropdown(id="Musica",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),

                                html.P('¿Con qué frecuencia estudias?'),
                                dcc.Dropdown(id="Estudio",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),

                                html.P('¿Con qué frecuencia tienes salidas sociales, con amigos, familaires, compañeros de trabajo?'),
                                dcc.Dropdown(id="Sales_Social",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),

                                html.P('¿Con qué frecuencia lees, al menos una lectura de 1 hora?'),
                                dcc.Dropdown(id="Lectura",options=[
                                        {"label": "Habitualmente", "value": "habitualmente"},
                                        {"label": "Ocasionalmente", "value": "ocasionalmente"},
                                        {"label": "Nunca", "value": "nunca"},
                                    ],
                                ),

                                html.P('¿Cuántas horas dedicas al mes en actividades que te hagan feliz como un pasatiempo?'),
                                dbc.Input(id="Hora_Gratificante", type="number", value=""),

                                html.P('¿Cuántas horas dedicas al mes haciendo ejercicio o algún deporte?'),
                                dbc.Input(id="Horas_Activ_Fisica", type="number", value=""),

                                html.P('¿Cuántas calorías quemas al día? -  La estimación es entre 400 - 600 Kcal en reposo'),
                                dbc.Input(id="Calorias", type="number", value=""),

                                html.P('¿Cuatos años llevas en la empresa que trabajas actualmente?'),
                                dbc.Input(id="Tiempo_PlazaActual", type="number", value=""),

                                html.P('¿Cuantas horas dedicas a salidas sociales en el mes?'),
                                dbc.Input(id="Hora_Social", type="number", value=""),

                                html.P('¿Cuantas horas dedicas a cuidarte?'),
                                dbc.Input(id="Horas_Cuidados", type="number", value=""),

                                html.P('¿Cuantos años llevas en general trabajando?'),
                                dbc.Input(id="Tiempo_Vida_Laboral", type="number", value=""),

                                html.P('¿Como dirías que es tu estado de ánimo?'),
                                dcc.Dropdown(id="Estado_Animo", options=[
                                    {"label": "Triste", "value": "triste"},
                                    {"label": "Contento", "value": "contento"},
                                    {"label": "Normal", "value": "normal"},
                                    {"label": "N/A", "value": "null"},
                                ],
                                ),
                                html.Br(),
                                dbc.Button("Ver Evaluación",id='submit-button', color="primary", className="mr-1"),
                                html.Br(),
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
