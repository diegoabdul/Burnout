import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import query

PCA = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Análisis de los Componentes Principales"),
                        html.P("En este apartado podemos observar las características en orden de importancia para optimizar la clasificación del Burnout, siendo el valor mas alto mas importante."),
                        html.P("Podemos ver en el gráfico que las características mas importantes son las que tienen in índice mayor a 1. "),
                        html.P("Por lo que estas son las variables tomadas para la construcción del modelo de predicción, asi como también para sub-categorías."),
                        dash_table.DataTable(
                            id='datatable-interactivity',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_PCA.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_PCA.to_dict('records'),
                            filter_action="native",
                            sort_action="native",
                            selected_rows=[],
                            page_action='native',
                            page_current=0,
                            page_size=4,
                        ),
                        html.Br(),
                        html.Br(),
                        html.Div(id='datatable-interactivity-container12'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)