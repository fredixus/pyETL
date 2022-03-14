import dash
import dash_core_components as dcc
import dash_html_components as html

import datetime

import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from dash import callback_context

from app import app
#import pandas as pd

layout = html.Div(className="container", children=[
      html.Div(className="header_bar", children =[
            dcc.Link('Home', className='home_button', href='/'),
            dcc.Link('CV', className='home_button', href='/'),
      ]),        
      html.Div(className="content", children=[
            html.Div(className="flex_data_section", children=[
                  html.Div(className="data_section flex-inline", children=[
                        html.Div(
                              html.Img(src='../assets/logo-amp.svg', height=400, className="logo"),
                        ),
                        html.Div([
                              html.H2('Arcelor Mittal', className='name'),
                              #html.H3('Software Engineer', className='position'),
                              html.H3("We are living in an age of remarkable progress, where invention and human ingenuity are driving unprecedented advances in global development. Steel is as relevant as ever to the future success of our world. As one of the only materials to be completely reusable and recyclable, it will play a critical role in building the circular economy of the future. Steel will continue to evolve, becoming smarter, and increasingly sustainable. At ArcelorMittal, our goal is to help build a better world with smarter steels. Steels made using innovative processes which are more efficient, use less energy, and emit significantly less carbon. Steels that are cleaner, stronger and reusable. Steels for electric vehicles and renewable energy infrastructure that will support societies as they transform through this century.", className='details'),
                              html.H3(dcc.Link('arcelormittal.com/about', href='https://corporate.arcelormittal.com/about'), className='details'),
                                
                        ])                     
                  ]),
                  html.Div(className="data_section", children=[
                        html.H1('Work history:', className="header"),
                        html.Div(id="active", className = "exp", children=[
                              
                                    
                                    html.Div(className = "text", children=[
                                          html.Span("ArcelorMittal Poland"),
                                          html.Span("Data Engineer / Data Analyst"),
                                          html.Span(["""The main goal of this project was to create a bunch of ETL scripts. Instead of the main goal client want to implement a cloud environment for internal and external partners.""",
                                                      html.H4("My responsibilities:"),
                                                      html.Ul([
                                                            html.Li("Create reports/dashboards ['Python','Power Bi']"),
                                                            html.Li("Analyze data and build ML models ['Python','Pandas','NumPy','SQL','Scikit-learn']"),
                                                            html.Li("Build Data Warehouse and ETL solutions ['SSIS','SQL','Python','Pandas']"),
                                                            html.Li("Desgn and implement vizualizations ['Plotly','Power BI','HTML']"),
                                                            html.Li("Implement Windows Application ['C#']"),
                                                            html.Li("Lead and track the projects ['Azure DevOpps']"),
                                                            html.Li("Preparing documentation "),
                                                            html.Li("Designing and creating the DW database structure ['DRAW.io', 'SQL']"),
                                                      ])
                                          ]),
                                    ]) 
                        ]),
                  ]),  
                  
            ]),
      html.Div(className="dataStorage", id='queryDataStorage_dis', style={'display':'none'}),

      ]) 
]) 