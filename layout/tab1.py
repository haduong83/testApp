# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:07:13 2020

@author: hoang.da
"""

import base64
import datetime
import io
import dash_table

import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app

import pandas as pd
import numpy as np

options = [{'label': 'Test1', 'value': 'Test1'},
            {'label': 'Test2', 'value': 'Test2'}]

controls = dbc.Form(
    [
        html.Br(),
        dbc.Row([
            dbc.Col([
                        dbc.Label('Raw material 1'),
                        dbc.Form(
                            [
                                dcc.Dropdown(id = 'RM1', options = options, style=dict(width = '70%')),
                                dbc.Input(id='RM1', value=0, style=dict(width = '30%')),
                            ],
                            inline=True,
                        ),
                    ]
                ),
            dbc.Col([
                        dbc.Label('Raw material 2'),
                        dbc.Form(
                            [
                                dcc.Dropdown(id = 'RM2', options = options, style=dict(width = '70%')),
                                dbc.Input(id='RM2', value=0, style=dict(width = '30%')),
                            ],
                            inline=True,
                        ),
                    ]
                ),
            ]
        ),
        html.Button('Submit data', id='submit-button-1', n_clicks=0),
    ],
)

uploadForm = html.Div(
    [
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '50%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Button('Submit file', id='submit-button-2', n_clicks=0),
        html.Div(id="Text-output"),
])

layout = html.Div(
    [
            controls,
            html.Br(),
            uploadForm
    ],
    style = {'display': 'inline-block', 'width': '90%', 'padding-left':'3%'}
)

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        
    except Exception as e:
        print(e)
        return html.Div([
            html.H7('There was an error processing this file.')
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.head().to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        # html.Hr(),  # horizontal line
        # # For debugging, display the raw contents provided by the web browser
        # html.Div('Raw Content'),
        # html.Pre(contents[0:200] + '...', style={
        #     'whiteSpace': 'pre-wrap',
        #     'wordBreak': 'break-all'
        # })
    ])

# @app.callback(Output('Text-output', 'children'),
#               [Input('upload-data', 'contents')],
#               [State('upload-data', 'filename'),
#                State('upload-data', 'last_modified')])
# def update_database(list_of_contents, list_of_names, list_of_dates):
#     if list_of_contents is not None:
#         children = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(list_of_contents, list_of_names, list_of_dates)]
#         return children

@app.callback(Output('Text-output', 'children'),
              [Input('submit-button-2', 'n_clicks')],
              [State('upload-data', 'contents'),
               State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_database(n_clicks, list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
