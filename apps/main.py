import dash
import dash_core_components as dcc
import dash_html_components as html

import datetime

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
                              html.Img(src='../assets/md1.png', className="logo"),
                        ),
                        html.Div([
                              html.H2('Michał Dębosz', className='name'),
                              html.H3('Software Engineer', className='position'),
                              html.H3(dcc.Link('michadbsz@gmail.com', href='mailto:michadbsz@gmail.com'), className='details'),
                              html.H3(dcc.Link('linkedin.com/in/mdebosz93/', href='http://linkedin.com/in/mdebosz93/'), className='details'),
                              html.Ul(className="list-horizontal", children=[
                                    html.Li("Python"),
                                    html.Li("Power BI"),
                                    html.Li("SQL"),
                                    html.Li("Azure: Functions, Key Vault, MLOps, ML API"),
                                    html.Li("Power Apps."),
                              ])    
                        ])                     
                  ]),
                  html.Div(className="data_section", children=[
                        html.H1('Work experience:', className="header"),
                        html.Div(id="active", className = "exp", children=[
                              
                                    html.Div(className = "dates", children=[
                                          html.Span("current"),
                                          html.Span("2021/08"),
                                    ]),
                                    html.Div(className = "text", children=[
                                          dcc.Link(html.Span("Software Engineer"),href='/epam'),
                                          dcc.Link(html.Span("Epam"),href='/epam'),
                                    ]) 
                        ]),
                              
                        
                        html.Div(className = "exp", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2021/08"),
                                    html.Span("2019/05"),
                              ]),
                              html.Div(className = "text", children=[
                                    dcc.Link(html.Span("Data Engineer"),href='/amp'),
                                    dcc.Link(html.Span("Arcelor Mittal Poland"),href='/amp'),
                              ])
                        ]),
                        html.Div(className = "exp", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2019/05"),
                                    html.Span("2018/06"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Junior Data Analyst"),
                                    html.Span("OEC"),
                              ])
                        ]),
                  ]),  
                  html.Div(className="data_section small_1", children=[
                        html.H1('Education:', className="header"),
                        html.Div(className = "edu", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2020"),
                                    html.Span("2019"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Data Science"),
                                    html.Span("AGH University of Science and Technology in Cracow"),
                              ])
                        ]),
                        html.Div(className = "edu", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2018"),
                                    html.Span("2013"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Virtotechnology"),
                                    html.Span("AGH University of Science and Technology in Cracow"),
                              ])
                        ]),

                        html.H1('Courses:', className="header"),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2021"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Microsoft power bi desktop & on-line"),
                                    html.Span("LinkedIn Learning"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2021"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Microsoft Azure Synapse for Developers"),
                                    html.Span("LinkedIn Learning"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2021"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Data Engineering Foundations"),
                                    html.Span("LinkedIn Learning"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2021"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Apache PySpark by Example"),
                                    html.Span("LinkedIn Learning"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2021"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Azure Spark Databricks Essential Training"),
                                    html.Span("LinkedIn Learning"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2021"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Python Data Analysis"),
                                    html.Span("LinkedIn Learning"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2020"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Microsoft power bi desktop & on-line"),
                                    html.Span("Altkom"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2019"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Dashboard in a day"),
                                    html.Span("Elitmind"),
                              ])
                        ]),
                        html.Div(className = "cur", children=[
                              html.Div(className = "dates", children=[
                                    html.Span("2019"),
                              ]),
                              html.Div(className = "text", children=[
                                    html.Span("Python 101 for Data Science"),
                                    html.Span("Cognitive Class"),
                              ])
                        ]),
                  ]), 
                  
            ]),
      html.Div(className="dataStorage", id='queryDataStorage_dis', style={'display':'none'}),
      #html.Div(className="data_output", id="etl-flow", style={'display':'block','width':'1000px','height': '500px','background-color':'#222'}),
      ]) 
])

