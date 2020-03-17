import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Sistema de Detección", href="/deteccion")),
        dbc.NavItem(dbc.NavLink("Componentes Principales", href="/PCA")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Datos Categorizados",
            children=[
                dbc.DropdownMenuItem("Burnout & Datos Fisiológicos por Paciente", href="/paciente"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Subescalas", href="/subescalas"),
                dbc.DropdownMenuItem("Burnout por Subescalas Individuales", href="/subescalasindividual"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Especialidad", href="/especialidad"),
                dbc.DropdownMenuItem("Burnout por Tipo de Trabajo", href="/trabajo"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Sexo", href="/sexo"),
            ],

        ),
        dbc.NavItem(dbc.NavLink("Descargar Dataset", href="https://storage.googleapis.com/burnout/Burnout_Data.csv"))
    ],
    brand="Burnout",
    #brand_external_link='https://storage.cloud.google.com/burnout/Burnout.png'
    #src='data:image/png;base64,{}'.format(encoded_image),
    brand_href="http://127.0.0.1:80/",
    sticky="top",

)