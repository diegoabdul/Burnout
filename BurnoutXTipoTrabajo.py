import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import query

BurnoutXTipoTrabajo = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Burnout por Tipo Trabajo"),
                        dash_table.DataTable(
                            id='datatable-interactivity13',
                            columns=[
                                {"name": i, "id": i, "deletable": True, "selectable": True} for i in query.df_Tipo_Trabajo.columns
                            ],
                            style_table={'overflowX': 'scroll'},
                            style_cell={
                                # all three widths are needed
                                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                                'overflow': 'hidden',
                                'textOverflow': 'ellipsis',
                            },
                            data=query.df_Tipo_Trabajo.to_dict('records'),
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
                        html.Div(id='datatable-interactivity-container13'),
                    ],
                    md=12,
                ),

            ]
        )
    ],
    className="mt-4",
)