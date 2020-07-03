import dash 
import dash_bootstrap_components as dbc 
import numpy as np

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

server = app.server
app.config.suppress_callback_exceptions = True

# x = np.arange(100)*0.1
# print(x)
# y = x
# print(y)
# y = np.square(x)
# print(y)
