# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:07:13 2020

@author: hoang.da
"""

import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layout import tab1, tab2

app.layout = html.Div(
    [
        html.H1("PGP Micro Model"),
        html.Hr(),
        html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Submit new data', value='tab-1'),
                    dcc.Tab(label='Model Training', value='tab-2'),
                ])
            , html.Div(id='tabs-content')
        ])
    ]
)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.layout
    elif tab == 'tab-2':
       return tab2.layout

if __name__ == "__main__":
    app.run_server()