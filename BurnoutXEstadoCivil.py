import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import query

BurnoutXEstadoCivil = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Burnout por Estado Civil"),
html.P(
                            "En este apartado de datos categorizados, mostramos los datos filtrando por una de las variables importantes EstadoCivil"),
                        html.P(
                            "Son datos detallados por lo que están pensados para personas expertas en el tema. Para que les sirva en posteriores estudios."),

                        dash_table.DataTable(
                            id='datatable-interactivity15',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_EstadoCivil.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_EstadoCivil.to_dict('records'),
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
                        html.Div(id='datatable-interactivity-container15'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

BurnoutXContrato = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Burnout por Tipo de Contrato"),
html.P(
                            "En este apartado de datos categorizados, mostramos los datos filtrando por una de las variables importantes Tipo de Contrato"),
                        html.P(
                            "Son datos detallados por lo que están pensados para personas expertas en el tema. Para que les sirva en posteriores estudios."),

                        dash_table.DataTable(
                            id='datatable-interactivity16',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_Contrato.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_Contrato.to_dict('records'),
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
                        html.Div(id='datatable-interactivity-container16'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

BurnoutXHijos = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Burnout por Número de Hijos"),
html.P(
                            "En este apartado de datos categorizados, mostramos los datos filtrando por una de las variables importantes número de hijos"),
                        html.P(
                            "Son datos detallados por lo que están pensados para personas expertas en el tema. Para que les sirva en posteriores estudios."),

                        dash_table.DataTable(
                            id='datatable-interactivity17',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_Hijos.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_Hijos.to_dict('records'),
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
                        html.Div(id='datatable-interactivity-container17'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)

BurnoutXEdad = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Burnout por Edad"),
html.P(
                            "En este apartado de datos categorizados, mostramos los datos filtrando por una de las variables importantes Edad"),
                        html.P(
                            "Son datos detallados por lo que están pensados para personas expertas en el tema. Para que les sirva en posteriores estudios."),

                        dash_table.DataTable(
                            id='datatable-interactivity18',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_Edad.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_Edad.to_dict('records'),
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
                        html.Div(id='datatable-interactivity-container18'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)