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
                dbc.DropdownMenuItem("Burnout por Área de Trabajo", href="/trabajo"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Sexo", href="/sexo"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Estado Civil", href="/civil"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Tipo de Contrato", href="/contrato"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Tipo Numero de Hijos", href="/hijos"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Burnout por Edad", href="/edad"),
            ],

        ),
        dbc.NavItem(dbc.NavLink("Descargar Dataset", href="https://storage.googleapis.com/burnout/Burnout_Data.csv"))
    ],
    brand="Burnout Study",
    #brand_external_link='https://storage.cloud.google.com/burnout/Burnout.png'
    #src='data:image/png;base64,{}'.format(encoded_image),
    #brand_href="https://burnoutweb.ddns.net:80",
    brand_href="http://burnoutweb.ddns.net:80",
    #brand_href="http://localhost:80/",
    sticky="top",

)