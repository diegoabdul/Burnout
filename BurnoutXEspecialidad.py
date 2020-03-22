import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import query

BurnoutXEspecialidad = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Burnout por Especialidad"),
                        html.P(
                            "En este apartado de datos categorizados, mostramos las subescalas del Burnout por Especialidad Clínica."),
                        html.P(
                            "Son datos detallados por lo que están pensados para personas expertas en el tema. Para que les sirva en posteriores estudios."),

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