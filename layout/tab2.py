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
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np


chartOptions = [{'label': "Linear", 'value': "Linear"},
                     {'label': "Quadratic", 'value': "Quadratic"}]

layout = html.Div(
    [
        dbc.Form(
            [
                dbc.Label("PlotType"),
                dcc.Dropdown(id = 'ChartType', options = chartOptions, value="Linear", style=dict(width = '70%')),
            ],
        ),
        dcc.Graph(id='feature-graph-1'),
   ],
    style = {'display': 'inline-block', 'width': '90%', 'padding-left':'3%'}
)

@app.callback(Output('feature-graph-1', "figure"),
              [Input('ChartType', 'value')])

def update_graph(chartType):
    x = np.arange(100)*0.1
    if chartType == 'Linear':
        y = x
    else:
        y = np.square(x)
    fig = go.Figure(data=go.Scatter(x=x, y=y))
    return fig