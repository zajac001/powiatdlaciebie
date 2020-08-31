import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd


salaries = pd.read_csv("salaries.csv", delimiter=";", engine="python", encoding="utf-8")

salaries.columns = ["ID", "Region", "2002", "2003", "2004", "2005", \
                    "2006", "2007", "2008", "2009", "2010", "2011", \
                    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "unnamed"]

salaries.drop("unnamed", axis=1, inplace=True)
salaries.iloc[:, 2:] = salaries.iloc[:, 2:].replace(',', '.', regex=True)
salaries.iloc[:, 2:] = salaries.iloc[:, 2:].astype(float)

years = salaries.columns[2:]

salaries_Poland = salaries.values[0][2:]
#_________________________________________________________________________________________________

unemployment_rate = pd.read_csv("unemployment_rate.csv", delimiter=";", engine="python", encoding="utf-8")

unemployment_rate.columns = ["ID", "Region", "2004", "2005", \
                    "2006", "2007", "2008", "2009", "2010", "2011", \
                    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "unnamed"]

unemployment_rate.drop("unnamed", axis=1, inplace=True)
unemployment_rate.iloc[:, 2:] = unemployment_rate.iloc[:, 2:].replace(',', '.', regex=True)
unemployment_rate.iloc[:, 2:] = unemployment_rate.iloc[:, 2:].astype(float)

years_2 = unemployment_rate.columns[2:]

unemployment_rate_Poland = unemployment_rate.values[0][2:]

#_________________________________________________________________________________________________

population_density = pd.read_csv("population_density.csv", delimiter=";", engine="python", encoding="utf-8")

population_density.columns = ["ID", "Region", "2002", "2003", "2004", "2005", \
                    "2006", "2007", "2008", "2009", "2010", "2011", \
                    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "unnamed"]

population_density.drop("unnamed", axis=1, inplace=True)
population_density.iloc[:, 2:] = population_density.iloc[:, 2:].replace(',', '.', regex=True)
population_density.iloc[:, 2:] = population_density.iloc[:, 2:].astype(float)

years_3 = population_density.columns[2:]

population_density_Poland = population_density.values[0][2:]

#_________________________________________________________________________________________________

birthrate = pd.read_csv("birthrate.csv", delimiter=";", engine="python", encoding="utf-8")

birthrate.columns = ["ID", "Region", "2013", "2014", "2015", "2016", "2017", "2018", "unnamed"]

birthrate.drop("unnamed", axis=1, inplace=True)
birthrate.iloc[:, 2:] = birthrate.iloc[:, 2:].replace(',', '.', regex=True)
birthrate.iloc[:, 2:] = birthrate.iloc[:, 2:].astype(float)

years_4 = birthrate.columns[2:]

birthrate_Poland = birthrate.values[0][2:]

#_________________________________________________________________________________________________

divorces = pd.read_csv("divorces.csv", delimiter=";", engine="python", encoding="utf-8")

divorces.columns = ["ID", "Region", "2002", "2003", "2004", "2005", \
                    "2006", "2007", "2008", "2009", "2010", "2011", \
                    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "unnamed"]

divorces.drop("unnamed", axis=1, inplace=True)
divorces.iloc[:, 2:] = divorces.iloc[:, 2:].replace(',', '.', regex=True)
divorces.iloc[:, 2:] = divorces.iloc[:, 2:].astype(float)

years_5 = divorces.columns[2:]

divorces_Poland = divorces.values[0][2:]

#_________________________________________________________________________________________________

mortality_before_sixty = pd.read_csv("mortality_before_sixty.csv", delimiter=";", engine="python", encoding="utf-8")

mortality_before_sixty.columns = ["ID", "Region", "2002", "2003", "2004", "2005", \
                    "2006", "2007", "2008", "2009", "2010", "2011", \
                    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "unnamed"]

mortality_before_sixty.drop("unnamed", axis=1, inplace=True)
mortality_before_sixty.drop(mortality_before_sixty.columns[2:10], axis=1, inplace=True)
mortality_before_sixty.iloc[:, 2:] = mortality_before_sixty.iloc[:, 2:].replace(',', '.', regex=True)
mortality_before_sixty.iloc[:, 2:] = mortality_before_sixty.iloc[:, 2:].astype(float)

years_6 = mortality_before_sixty.columns[2:]

mortality_before_sixty_Poland = mortality_before_sixty.values[0][2:]


#_________________________________________________________________________________________________
cancer_death = pd.read_csv("cancer_death.csv", delimiter=";", engine="python", encoding="utf-8")

cancer_death.columns = ["ID", "Region", "2003", "2004", "2005", \
                    "2006", "2007", "2008", "2009", "2010", "2011", \
                    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "unnamed"]

cancer_death.drop("unnamed", axis=1, inplace=True)
cancer_death.iloc[:, 2:] = cancer_death.iloc[:, 2:].replace(',', '.', regex=True)
cancer_death.iloc[:, 2:] = cancer_death.iloc[:, 2:].astype(float)

years_7 = cancer_death.columns[2:]

cancer_death_Poland = cancer_death.values[0][2:]

#_________________________________________________________________________________________________

environment_protection_rate = pd.read_csv("environment_protection_rate.csv", delimiter=";", engine="python", encoding="utf-8")

environment_protection_rate.columns = ["ID", "Region", "2002", "2003", "2004", "2005", \
                    "2006", "2007", "2008", "2009", "2010", "2011", \
                    "2012", "2013", "2014", "2015", "2016", "2017", "2018", "unnamed"]

environment_protection_rate.drop("unnamed", axis=1, inplace=True)
environment_protection_rate.iloc[:, 2:] = environment_protection_rate.iloc[:, 2:].replace(',', '.', regex=True)
environment_protection_rate.iloc[:, 2:] = environment_protection_rate.iloc[:, 2:].astype(float)

years_8 = environment_protection_rate.columns[2:]

environment_protection_rate_Poland = environment_protection_rate.values[0][2:]

#_________________________________________________________________________________________________

bicycle_path = pd.read_csv("bicycle_path.csv", delimiter=";", engine="python", encoding="utf-8")

bicycle_path.columns = ["ID", "Region", "2011","2012", "2013", \
                        "2014", "2015", "2016", "2017", "2018", "unnamed"]

bicycle_path.drop("unnamed", axis=1, inplace=True)
bicycle_path.iloc[:, 2:] = bicycle_path.iloc[:, 2:].replace(',', '.', regex=True)
bicycle_path.iloc[:, 2:] = bicycle_path.iloc[:, 2:].astype(float)

years_9 = bicycle_path.columns[2:]

bicycle_path_Poland = bicycle_path.values[0][2:]


#_________________________________________________________________________________________________
app = dash.Dash("daszbord")

dropdown = dcc.Dropdown(
    id='dropdown',
    options=[
        {'label': i, 'value': i} for i in salaries["Region"].unique()
    ]
)

wykres = dcc.Graph(id='wykres')
wykres_2 = dcc.Graph(id='wykres_2')
wykres_3 = dcc.Graph(id='wykres_3')
wykres_4 = dcc.Graph(id='wykres_4')
wykres_5 = dcc.Graph(id='wykres_5')
wykres_6 = dcc.Graph(id='wykres_6')
wykres_7 = dcc.Graph(id='wykres_7')
wykres_8 = dcc.Graph(id='wykres_8')
wykres_9 = dcc.Graph(id='wykres_9')

app.layout = html.Div([
    html.H1('Dashboard'),
    dropdown,
    wykres,
    wykres_2,
    wykres_3,
    wykres_4,
    wykres_5,
    wykres_6,
    wykres_7,
    wykres_8,
    wykres_9,


])

@app.callback(
    Output('wykres', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph_a(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region = salaries.iloc[:, 1]
        id_region = id_region.to_dict()

        for index, region in id_region.items():
            if region == county_name:
                salaries_wykres = salaries.values[index][2:]

        return {
            'data': [{'x': years, 'y': salaries_wykres, 'type': 'line', 'name': county_name},
                    {'x': years, 'y': salaries_Poland, 'type': 'line', 'name': "Polska"}
                ],
                'layout': {
                    'title': 'Salaries'
                }
            }
#_________________________________________________________________________________________________
@app.callback(
    Output('wykres_2', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_b(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_2 = unemployment_rate.iloc[:, 1]
        id_region_2 = id_region_2.to_dict()

        for index_2, region_2 in id_region_2.items():
            if region_2 == county_name:
                unemployment_rate_wykres = unemployment_rate.values[index_2][2:]

        return {
            'data': [{'x': years_2, 'y': unemployment_rate_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_2, 'y': unemployment_rate_Poland, 'type': 'line', 'name': "Polska"}
                ],
                'layout': {
                    'title': 'unemployment rate'
                }
            }
#_________________________________________________________________________________________________
@app.callback(
    Output('wykres_3', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_c(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_3 = population_density.iloc[:, 1]
        id_region_3 = id_region_3.to_dict()

        for index_3, region_3 in id_region_3.items():
            if region_3 == county_name:
                population_density_wykres = population_density.values[index_3][2:]

        return {
            'data': [{'x': years_3, 'y': population_density_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_3, 'y': population_density_Poland, 'type': 'line', 'name': "Polska"}
                ],
                'layout': {
                    'title': 'population density'
                }
            }
#_________________________________________________________________________________________________

@app.callback(
    Output('wykres_4', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_d(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_4 = birthrate.iloc[:, 1]
        id_region_4 = id_region_4.to_dict()

        for index_4, region_4 in id_region_4.items():
            if region_4 == county_name:
                birthrate_wykres = birthrate.values[index_4][2:]

        return {
            'data': [{'x': years_4, 'y': birthrate_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_4, 'y': birthrate_Poland, 'type': 'line', 'name': "Polska"}
                ],
                'layout': {
                    'title': 'birthrate'
                }
            }


#_________________________________________________________________________________________________

@app.callback(
    Output('wykres_5', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_e(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_5 = divorces.iloc[:, 1]
        id_region_5 = id_region_5.to_dict()

        for index_5, region_5 in id_region_5.items():
            if region_5 == county_name:
                divorces_wykres = divorces.values[index_5][2:]

        return {
            'data': [{'x': years_5, 'y': divorces_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_5, 'y': divorces_Poland, 'type': 'line', 'name': "Polska"}
                     ],
                'layout': {
                    'title': 'divorces'
                }
        }
#_________________________________________________________________________________________________

@app.callback(
    Output('wykres_6', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_f(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_6 = mortality_before_sixty.iloc[:, 1]
        id_region_6 = id_region_6.to_dict()

        for index_6, region_6 in id_region_6.items():
            if region_6 == county_name:
                mortality_before_sixty_wykres = mortality_before_sixty.values[index_6][2:]

        return {
            'data': [{'x': years_6, 'y': mortality_before_sixty_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_6, 'y': mortality_before_sixty_Poland, 'type': 'line', 'name': "Polska"}
                     ],
                'layout': {
                    'title': 'mortality_before_sixty'
                }
        }

#_________________________________________________________________________________________________

@app.callback(
    Output('wykres_7', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_g(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_7 = cancer_death.iloc[:, 1]
        id_region_7 = id_region_7.to_dict()

        for index_7, region_7 in id_region_7.items():
            if region_7 == county_name:
                cancer_death_wykres = cancer_death.values[index_7][2:]

        return {
            'data': [{'x': years_7, 'y': cancer_death_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_7, 'y': cancer_death_Poland, 'type': 'line', 'name': "Polska"}
                     ],
                'layout': {
                    'title': 'cancer_death'
                }
        }


#_________________________________________________________________________________________________

@app.callback(
    Output('wykres_8', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_g(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_8 = environment_protection_rate.iloc[:, 1]
        id_region_8 = id_region_8.to_dict()

        for index_8, region_8 in id_region_8.items():
            if region_8 == county_name:
                environment_protection_rate_wykres = environment_protection_rate.values[index_8][2:]

        return {
            'data': [{'x': years_8, 'y': environment_protection_rate_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_8, 'y': environment_protection_rate_Poland, 'type': 'line', 'name': "Polska"}
                     ],
                'layout': {
                    'title': 'environment_protection_rate'
                }
        }

#_________________________________________________________________________________________________

@app.callback(
    Output('wykres_9', 'figure'),
    [Input('dropdown', 'value')]
)

def update_graph_g(county_name):
    if county_name is None:
        raise dash.exceptions.PreventUpdate
    else:

        id_region_9 = bicycle_path.iloc[:, 1]
        id_region_9 = id_region_9.to_dict()

        for index_9, region_9 in id_region_9.items():
            if region_9 == county_name:
                bicycle_path_wykres = bicycle_path.values[index_9][2:]

        return {
            'data': [{'x': years_9, 'y': bicycle_path_wykres, 'type': 'line', 'name': county_name},
                    {'x': years_9, 'y': bicycle_path_Poland, 'type': 'line', 'name': "Polska"}
                     ],
                'layout': {
                    'title': 'bicycle_path'
                }
        }




app.run_server(debug=True)