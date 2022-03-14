import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import os
import flask
from whitenoise import WhiteNoise
from apps import main, epam, amp 
from app import app


server = app.server
#server.wsgi_app = WhiteNoise(server.wsgi_app, root='static/')

app.layout = html.Div(className="container", children=[
	dcc.Location(id='url', refresh=False)
	,
	html.Div(id='page-content'),
]) 

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return main.layout
    if pathname == '/epam':
        return epam.layout
    if pathname == '/amp':
        return amp.layout

if __name__ == '__main__':
    app.run_server(debug=True)