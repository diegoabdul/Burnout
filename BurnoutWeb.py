import re
import dash
import time
from dash.dependencies import Input, Output,State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
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
import BurnoutXEstadoCivil

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

BS = "https://bootswatch.com/4/flatly/bootstrap.min.css"
app = dash.Dash(external_stylesheets=[BS])
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
page_1_layout = html.Div([PanelNavegacion.navbar,BurnoutXEstadoCivil.BurnoutXEstadoCivil])
page_10_layout = html.Div([PanelNavegacion.navbar,BurnoutXEstadoCivil.BurnoutXContrato])
page_11_layout = html.Div([PanelNavegacion.navbar,BurnoutXEstadoCivil.BurnoutXHijos])
page_12_layout = html.Div([PanelNavegacion.navbar,BurnoutXEstadoCivil.BurnoutXEdad])
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
    if pathname == '/civil':
        return page_1_layout
    if pathname == '/contrato':
        return page_10_layout
    if pathname == '/hijos':
        return page_11_layout
    if pathname == '/edad':
        return page_12_layout
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
                           "x": dff["Caracteristicas"],
                           "y": dff["Importancia"],
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
            animate=True,
            animation_options={ 'frame': { 'redraw': 'false', }, 'transition': { 'duration': 750, 'ease': 'cubic-in-out', }, },
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
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
        html.Br(),
        html.H5("Primera Encuesta de Burnout"),
        html.P("En esta primera gráfica observamos los datos recogidos en la primera encuesta"),
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
        html.P("En esta primera gráfica observamos los datos recogidos en la segunda encuesta"),
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
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
        html.Br(),
        html.H5("Primera Encuesta de Burnout"),
        html.P("En esta primera gráfica observamos los datos recogidos en la primera encuesta por paciente"),
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
        html.P("En esta primera gráfica observamos los datos recogidos en la segunda encuesta por paciente"),
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
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
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
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
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
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
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
    Output('datatable-interactivity-container15', "children"),
    [Input('datatable-interactivity15', "derived_virtual_data"),
     Input('datatable-interactivity15', "derived_virtual_selected_rows")])
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

    dff = query.df_EstadoCivil if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
        dcc.Graph(
            id=31,
            figure={
                "data": [
                    {
                        "x": dff["EstadoCivil"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["EstadoCivil"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["EstadoCivil"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Hijos"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hijos",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["EstadoCivil"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["EstadoCivil"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["EstadoCivil"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["EstadoCivil"],
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
    Output('datatable-interactivity-container16', "children"),
    [Input('datatable-interactivity16', "derived_virtual_data"),
     Input('datatable-interactivity16', "derived_virtual_selected_rows")])
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

    dff = query.df_Contrato if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
        dcc.Graph(
            id=31,
            figure={
                "data": [
                    {
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Hijos"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hijos",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["Tipo_Contrato"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["Tipo_Contrato"],
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
    Output('datatable-interactivity-container17', "children"),
    [Input('datatable-interactivity17', "derived_virtual_data"),
     Input('datatable-interactivity17', "derived_virtual_selected_rows")])
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

    dff = query.df_Hijos if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
        dcc.Graph(
            id=31,
            figure={
                "data": [
                    {
                        "x": dff["Hijos"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["Hijos"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["Hijos"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Hijos"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Hijos",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["Hijos"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["Hijos"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["Hijos"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["Hijos"],
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
    Output('datatable-interactivity-container18', "children"),
    [Input('datatable-interactivity18', "derived_virtual_data"),
     Input('datatable-interactivity18', "derived_virtual_selected_rows")])
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

    dff = query.df_Edad if rows is None else pd.DataFrame(rows)

    colors = ['#7FDBFF' if i in derived_virtual_selected_rows else '#0074D9'
              for i in range(len(dff))]

    return [
        html.Br(),
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
        dcc.Graph(
            id=31,
            figure={
                "data": [
                    {
                        "x": dff["Edad"],
                        "y": dff["Calorias"],
                        "type": "bar",
                        "marker": {"color": colors},
                        "name": "Calorias",
                    },
                    {
                        "x": dff["Edad"],
                        "y": dff["Frecuencia_Cardiaca_Minuto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name":"Frecuencia_Cardiaca_Minuto",
                    },
                    {
                        "x": dff["Edad"],
                        "y": dff["Resting_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Realizacion_Personal",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Eficiencia_Sueno"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Eficiencia_Sueno",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Peso"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Peso",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Edad"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Edad",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Tiempo_Plaza"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Plaza",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Tiempo_Vida_Laboral"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_Vida_Laboral",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Max_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Max_HeartRate",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Min_HeartRate"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_HeartRate",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Minutos_Rem"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_Rem",
                    },{
                        "x": dff["Edad"],
                        "y": dff["SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "SuenoProfundo",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Min_SuenoProfundo"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoProfundo",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Min_SuenoLigero"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_SuenoLigero",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Minutos_SuenoDespierto"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Minutos_SuenoDespierto",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Min_Dormido"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Dormido",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Min_Despierto_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Min_Despierto_enCama",
                    },{
                        "x": dff["Edad"],
                        "y": dff["Tiempo_enCama"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Tiempo_enCama",
                    }
                    , {
                        "x": dff["Edad"],
                        "y": dff["Cansancio_Emocional"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Cansancio_Emocional",
                    }, {
                        "x": dff["Edad"],
                        "y": dff["Despersonalizacion"],
                        "type": "bar",
                        "marker": {"color": color},
                        "name": "Despersonalizacion",
                    }, {
                        "x": dff["Edad"],
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
        html.H5("¡Es un gráfico dinámico!"),
        html.P("Siéntete libre de hacer zoom, seleccionar variables, filtrar en la tabla superior."),
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

@app.callback(
    Output("loading-output", "children"), [Input("loading-button", "n_clicks")]
)
def load_output(n):
    if n:
        time.sleep(1)
        return f"Output loaded {n} times"
    return "Output not reloaded yet"

@app.callback([Output('output_div', 'children'),Output("modal", "is_open")],
                  [Input('submit-button', 'n_clicks')],
                  [State('nombre', 'value'),State('email-input', 'value'),State('Sexo', 'value'),State('edad', 'value'),State('peso', 'value'),
                   State('hijos', 'value'),State('EstadoCivil', 'value'),State('Contrato_Adjunto', 'value'),State('Musica', 'value'),
                   State('Estudio', 'value'),State('Sales_Social', 'value'),State('Lectura', 'value'),State('Hora_Gratificante', 'value'),
                   State('Horas_Activ_Fisica', 'value'),State('Calorias', 'value'),State('Tiempo_PlazaActual', 'value'),State('Hora_Social', 'value'),
                   State('Horas_Cuidados', 'value'),State('Tiempo_Vida_Laboral', 'value'),State('Estado_Animo', 'value'),
                   ]
              )

def update_output(clicks,nombre,Email,Sexo,Edad,Peso,hijos,EstadoCivil,Contrato_Adjunto,Musica,Estudio,Sales_Social,Lectura,Hora_Gratificante,Horas_Activ_Fisica,Calorias,Tiempo_PlazaActual,Hora_Social,Horas_Cuidados,Tiempo_Vida_Laboral,Estado_Animo):

    print(nombre,Email,Sexo,Edad,Peso,hijos,EstadoCivil,Contrato_Adjunto,Musica,Estudio,Sales_Social,Lectura,Hora_Gratificante,Horas_Activ_Fisica,Calorias,Tiempo_PlazaActual,Hora_Social,Horas_Cuidados,Tiempo_Vida_Laboral,Estado_Animo)

    df = pd.DataFrame({'Sexo': [Sexo], 'Edad': [Edad], 'Peso': [float(Peso)], 'Hijos': [float(hijos)], 'EstadoCivil': [EstadoCivil], 'Contrato_Adjunto': [Contrato_Adjunto], 'Musica': [Musica], 'Estudias': [Estudio], 'Sales_Social': [Sales_Social], 'Lectura': [Lectura], 'Hora_Gratificante': [float(Hora_Gratificante)], 'Horas_Activ_Fisica': [float(Horas_Activ_Fisica)], 'Calorias': [float(Calorias)], 'Tiempo_PlazaActual': [float(Tiempo_PlazaActual)], 'Hora_Social': [float(Hora_Social)], 'Horas_Cuidados': [float(Horas_Cuidados)], 'Tiempo_Vida_Laboral': [float(Tiempo_Vida_Laboral)], 'Estado_Animo': [Estado_Animo]})
    data=Clasificacion.DataPreparation(df)
    #prediccionLinear,probabilidadLinear=Clasificacion.LinearEvaluation(data)
    prediccionRandom, probabilidadRandom = Clasificacion.RandomForest(data)
    #prediccionDecisionTreet,probabilidadDecisionTree = Clasificacion.DecisionTree(data)
    #prediccionIsotonic,labelIsotonic  = Clasificacion.Isotonic(data)

    # print(prediccionLinear + ' ' + str(probabilidadLinear) + ' Logistic Regresion')
    # print(prediccionRandom + ' ' + str(probabilidadRandom) + ' Random Forest ')
    # print(prediccionDecisionTreet + ' ' + str(probabilidadDecisionTree) + ' DecisionTree ')
    # print(labelIsotonic + ' Isotonic ')
    #
    # if probabilidadRandom>probabilidadDecisionTree:
    #     respuesta=prediccionRandom
    # if probabilidadDecisionTree>probabilidadRandom:
    #      respuesta=prediccionDecisionTreet
    # if probabilidadDecisionTree>probabilidadRandom and probabilidadDecisionTree>probabilidadLinear:
    #     respuesta=prediccionDecisionTreet
    id=query.contar()
    val = id['contar'].values[0]
    print(val)
    val=val+1
    usuarios = pd.DataFrame(
        {'ID': [val],'Nombre': [nombre], 'Email': Email, 'Prediccion':[prediccionRandom], 'Sexo': [Sexo], 'Edad': [Edad], 'Peso': [float(Peso)],
         'Hijos': [float(hijos)],
         'EstadoCivil': [EstadoCivil], 'Contrato_Adjunto': [Contrato_Adjunto], 'Musica': [Musica],
         'Estudias': [Estudio], 'Sales_Social': [Sales_Social], 'Lectura': [Lectura],
         'Hora_Gratificante': [float(Hora_Gratificante)],
         'Horas_Activ_Fisica': [float(Horas_Activ_Fisica)], 'Calorias': [float(Calorias)],
         'Tiempo_PlazaActual': [float(Tiempo_PlazaActual)], 'Hora_Social': [float(Hora_Social)],
         'Horas_Cuidados': [float(Horas_Cuidados)],
         'Tiempo_Vida_Laboral': [float(Tiempo_Vida_Laboral)], 'Estado_Animo': [Estado_Animo]})
    #usuarios.to_csv('usuarios.csv')
    query.insert(usuarios)
    if prediccionRandom=='VERDADERO':
        salida='{} Tu evaluación es: {}  Te recomendamos que: '.format(nombre, prediccionRandom)
        salida2='1. Date un paseo cada día al menos de 30’ (mejor en contacto con la naturaleza)'
        salida3 = '2. Dedica al menos 10’ al día a practicar alguna técnica de meditación y/o relajación (como la observación de la respiración)'
        salida4='3. Llama a algún amigo con quien no hayas contactado desde hace tiempo.'
        salida5='4. Participa en algún grupo de “hobbies” externo al trabajo. '
        prueba=html.Div(html.P([salida, html.Br(),html.Br(), salida2,html.Br(),html.Br(),salida3,html.Br(),html.Br(),salida4,html.Br(),html.Br(),salida5]))
        return prueba, "is_open"
    if prediccionRandom=='FALSO':
        return 'Enhorabuena!! {} Tu evaluación es: {} !! Sigue así!!'.format(nombre, prediccionRandom), "is_open"

@app.callback(
    Output("alert-fade", "is_open"),
    [Input("submit-button", "n_clicks")],
    [State("alert-fade", "is_open")],
)
def toggle_alert(n, is_open):
    if n != 1:
        raise PreventUpdate
    else:
        return not is_open


if __name__ == '__main__':
    #app.run_server(host='0.0.0.0', port=80,ssl_context='adhoc')
    app.run_server(host='0.0.0.0', port=80)