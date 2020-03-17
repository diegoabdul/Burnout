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
import PanelNavegacion
import Fisiologicos
import PCA
import FisiologicosXPaciente
import Subescalas
import SubescalasIndividuales
import BurnoutXEspecialidad
import BurnoutXSexo
import SistemaDeDeteccionHTML
import BodyIndexHTML
import BurnoutXTipoTrabajo

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


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])
app.title = 'Burnout Study'
index_page = html.Div([PanelNavegacion.navbar,BodyIndexHTML.bodyIndex])
page_2_layout = html.Div([PanelNavegacion.navbar,Subescalas.Subescalas])
page_3_layout = html.Div([PanelNavegacion.navbar,SubescalasIndividuales.SubescalasIndividuales])
page_4_layout = html.Div([PanelNavegacion.navbar,BurnoutXEspecialidad.BurnoutXEspecialidad])
page_5_layout = html.Div([PanelNavegacion.navbar,BurnoutXSexo.BurnoutXSexo])
page_6_layout = html.Div([PanelNavegacion.navbar,FisiologicosXPaciente.FisiologicosXPaciente])
page_7_layout = html.Div([PanelNavegacion.navbar,SistemaDeDeteccionHTML.SistemaDeDeteccion])
page_8_layout = html.Div([PanelNavegacion.navbar,PCA.PCA])
page_9_layout = html.Div([PanelNavegacion.navbar,BurnoutXTipoTrabajo.BurnoutXTipoTrabajo])
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
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
    if pathname == '/PCA':
        return page_8_layout
    if pathname == '/trabajo':
        return page_9_layout
    else:
        return index_page

@app.callback(
    Output('datatable-interactivity-container12', "children"),
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

    dff = query.df_PCA if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        dcc.Graph(
            id='basic-interactions',
                figure={
                   "data": [
                       {
                           "x": dff["Importancia"],
                           "y": dff["Caracteristicas"],
                           'mode': 'markers',
                           'marker': {'size': 10}
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
    Output('datatable-interactivity-container13', "children"),
    [Input('datatable-interactivity13', "derived_virtual_data"),
     Input('datatable-interactivity13', "derived_virtual_selected_rows")])
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

    dff = query.df_Tipo_Trabajo if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        dcc.Graph(
            id=32,
            figure={
                "data": [
                    {
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },
                    {
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Hijos"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hijos",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["Tipo_Trabajo"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["Tipo_Trabajo"],
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

def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

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
    [Output("edad", "valid")],
    [Input("edad", "value")],
)
def check_edad(edad):
    if edad:
        is_gmail = bool(re.match("^[0-9 \-]+$", str(edad)))
        return is_gmail, not is_gmail
    return False, False

@app.callback(Output('output_div', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('nombre', 'value'),State('email-input', 'value'),State('Sexo', 'value'),State('edad', 'value'),State('peso', 'value'),
                   State('hijos', 'value'),State('EstadoCivil', 'value'),State('Contrato_Adjunto', 'value'),State('Musica', 'value'),
                   State('Estudio', 'value'),State('Sales_Social', 'value'),State('Lectura', 'value'),State('Frecuencia_Cardiaca_Minuto', 'value'),
                   State('Resting_HeartRate', 'value'),State('Calorias', 'value'),State('Tiempo_PlazaActual', 'value'),State('Hora_Social', 'value'),
                   State('Horas_Cuidados', 'value'),State('Tiempo_Vida_Laboral', 'value'),State('Minutos_Dormido', 'value'),State('Estado_Animo', 'value'),State('Cantidad_Sueno_Profundo', 'value')
                   ]
              )

def update_output(clicks,nombre,Email,Sexo,Edad,Peso,hijos,EstadoCivil,Contrato_Adjunto,Musica,Estudio,Sales_Social,Lectura,Frecuencia_Cardiaca_Minuto,Resting_HeartRate,Calorias,Tiempo_PlazaActual,Hora_Social,Horas_Cuidados,Tiempo_Vida_Laboral,Minutos_Dormido,Estado_Animo,Cantidad_Sueno_Profundo):
    if clicks is not None:
        print(nombre,Email,Sexo,Edad,Peso,hijos,EstadoCivil,Contrato_Adjunto,Musica,Estudio,Sales_Social,Lectura,Frecuencia_Cardiaca_Minuto,Resting_HeartRate,Calorias,Tiempo_PlazaActual,Hora_Social,Horas_Cuidados,Tiempo_Vida_Laboral,Minutos_Dormido,Estado_Animo,Cantidad_Sueno_Profundo)
        df = pd.DataFrame({'Sexo': [Sexo], 'Edad': [Edad], 'Peso': [float(Peso)], 'Hijos': [float(hijos)], 'EstadoCivil': [EstadoCivil], 'Contrato_Adjunto': [Contrato_Adjunto], 'Musica': [Musica], 'Estudias': [Estudio], 'Sales_Social': [Sales_Social], 'Lectura': [Lectura], 'Frecuencia_Cardiaca_Minuto': [float(Frecuencia_Cardiaca_Minuto)], 'Resting_HeartRate': [float(Resting_HeartRate)], 'Calorias': [float(Calorias)], 'Tiempo_PlazaActual': [float(Tiempo_PlazaActual)], 'Hora_Social': [float(Hora_Social)], 'Horas_Cuidados': [float(Horas_Cuidados)], 'Tiempo_Vida_Laboral': [float(Tiempo_Vida_Laboral)], 'Minutos_Dormido': [float(Minutos_Dormido)], 'Estado_Animo': [Estado_Animo], 'Cantidad_Sueno_Profundo': [float(Cantidad_Sueno_Profundo)]})
        data=Clasificacion.DataPreparation(df)
        prediccion,probabilidad=Clasificacion.LinearEvaluation(data)
        prediccion2, probabilidad2 = Clasificacion.RandomForest(data)
        #prediccion3,probabilidad3 = Clasificacion.GradientTree(data)
    return '{} Tu evaluación es: {} y la probabilidad es: {} Para el algoritmo de Regresión Lineal'.format(nombre,prediccion,probabilidad),'\n Tu evaluación es: {} y la probabilidad es: {} Para el algoritmo de Random Forest '.format(prediccion2,probabilidad2)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=80)