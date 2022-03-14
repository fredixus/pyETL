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
                              html.Img(src='../assets/epam.png', height=400, className="logo"),
                        ),
                        html.Div([
                              html.H2('Epam', className='name'),
                              #html.H3('Software Engineer', className='position'),
                              html.H3("We can help you reimagine your business through a digital lens. Our software engineering heritage combined with our strategic business and innovation consulting, design thinking, and physical-digital capabilities provide real business value to our customers through human-centric innovation.", className='details'),
                              html.H3(dcc.Link('www.epam.com/about', href='https://www.epam.com/about'), className='details'),
                                
                        ])                     
                  ]),
                  html.Div(className="data_section", children=[
                        html.H1('Work history:', className="header"),
                        html.Div(id="active", className = "exp", children=[
                              
                                    html.Div(className = "dates", children=[
                                          html.Span("current"),
                                          html.Span("2021/08"),
                                    ]),
                                    html.Div(className = "text", children=[
                                          html.Span("Wood Key Developer"),
                                          html.Span("Data Engineer"),
                                          html.Span(["""The main goal of this project was to create a bunch of ETL scripts. Instead of the main goal client want to implement a cloud environment for internal and external partners.""",
                                                      html.H4("My responsibilities:"),
                                                      html.Ul([
                                                            html.Li("prepare the environment and implement ETL scripts (Azure Functions, AWS SES),"),
                                                            html.Li("design and implement tables for new data layer (Azure SQL, Azure Blob),"),
                                                            html.Li("create and maintain a cloud environment (Azure ML)"),
                                                            html.Li("deploy web API (Azure ML)"),
                                                            html.Li("design and create web apps (Power Apps)"),
                                                            html.Li("managing repositories of projects (MLOps/DevOps)"),
                                                            html.Li("helping other developers to use Cloud solutions."),
                                                      ])
                                          ]),
                                    ]) 
                        ]),
                  ]),  
                  html.Div(className="data_section small_1", children=[
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
                  ]), 
                  
            ]),
      html.Div(className="dataStorage", id='queryDataStorage_dis', style={'display':'none'}),

      ]) 
]) 