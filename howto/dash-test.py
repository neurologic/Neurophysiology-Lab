
import argparse

import os
import sys


from pathlib import Path
import dash
from dash import html, dcc
from dash.dependencies import Output, Input
from dash import no_update

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.signal import hilbert,medfilt,resample, find_peaks, unit_impulse
import seaborn as sns
from datetime import datetime,timezone,timedelta
import random


# Create the parser
my_parser = argparse.ArgumentParser(prog='DataExplorer',description='List the content of a folder')

# Add the arguments
my_parser.add_argument('-filepath',
    action='store',
    required=True,
    dest='filepath',
    help='full path to the file location on your local computer')
my_parser.add_argument('-fs',
    action = 'store',
    required=True,
    type=float,
    dest='fs',
    help='sampling rate of the data in file')
my_parser.add_argument('-n',
    action='store',
    required=True,
    type=int,
    dest='number_channels',
    help='number of channels data in file')
my_parser.add_argument('-p',
    action='store',
    required=True,
    type=int,
    dest='number_subplots',
    help='number of subplots')
my_parser.add_argument('-c',
    action='append',
    required=True,
    type=str,
    nargs='+',
    dest='channels_per_subplot',
    help='list of channels to plot on each subplot (listed in order of appearance)')

# Execute the parse_args() method
args = my_parser.parse_args()

print('Great! you have provided all the necessary information... let\'s explore your data!')
# print(vars(args))

chan_on_plot = [list(map(int, c)) for c in args.channels_per_subplot] #convert list of strings to list of int to index data


# def main(argv):
 

# if __name__ == "__main__":
#    main(sys.argv[1:])

# load data
# #create data
# fs = 10
# data_dur = 100
# time = np.linspace(0,data_dur,int(data_dur*fs))
# data = np.random.rand(int(data_dur*fs)).reshape(-1,1)
# number_channels=1

# filepath = '/Users/kperks/Downloads/eod-50k-stim2022-08-17T14_50_39.bin'

sampling_rate = 50000 #@param
number_channels = 2 #@param

downsample = False #@param
newfs = 10000 #@param


filepath = Path(args.filepath)

# No need to edit below this line
#################################
data = np.fromfile(Path(filepath), dtype = np.float64)
data = data.reshape(-1,args.number_channels)
data_dur = np.shape(data)[0]/args.fs
print('duration of recording was %0.2f seconds' %data_dur)

# if downsample:
#     # newfs = 10000 #downsample emg data
#     chunksize = int(sampling_rate/newfs)
#     data = data[0::chunksize,:]
#     fs = int(np.shape(data)[0]/data_dur)

time = np.linspace(0,data_dur,np.shape(data)[0])

print('Data upload completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))

# Step 1. Launch the application

# initialize app
app = dash.Dash(__name__)
# # app = JupyterDash()
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

# Step 2. Import data

# Step 3. Create a plotly figure

layout=go.Layout(height=500, width=800)

# fig = go.Figure(layout = layout)
# # f = go.FigureWidget(layout=go.Layout(height=500, width=800))
# for chan in np.arange(number_channels):
#     fig.add_trace(go.Scatter(x = time[0:fs], y = data[0:fs,chan],
#                          name=str(chan),opacity=1))

# Step 4. Create a Dash layout
app.layout = html.Div([
                # a header and a paragraph
                html.Div([
                    html.H3("Raw Data Explorer"),
                    html.P("You can: Use the range slider below the plot to navigate through the recording. \
                    Zoom in and out on detail in the signal. Hover over the signal to annotate data points. \
                    Move the graph around if you are zoomed in. Save a png. ")
                         ],
                     style = {'padding' : '5px' ,
                              'backgroundColor' : '#3aaab2'}),
                # adding a plot
                dcc.Graph(id = 'plot'),#, figure = fig),
                 # range slider
                html.P([
                    html.Label("Time Period (seconds)"),
                    dcc.RangeSlider(id = 'slider',
                                    min = 0,
                                    max = data_dur,
                                    value = [0, 1],
                                    updatemode="mouseup")
                        ], style = {'width' : '100%',
                                    'fontSize' : '15px',
                                    'display': 'inline-block'})
                      ])


# Step 5. Add callback functions
@app.callback(Output('plot', 'figure'),
             [Input('slider', 'value')])
def update_figure(input1):
    # filtering the data
    starti = int(input1[0]*args.fs)
    stopi = int(input1[1]*args.fs)
        
    # updating the plot
    chan = 0
    fig = go.Figure()#layout = layout)
    
    for chan in np.arange(number_channels):
        fig.add_trace(go.Scatter(x = time[starti:stopi], y = data[starti:stopi,chan],
                         name=str(chan),opacity=1))
    # trace_1 = go.Scatter(x = time[starti:stopi], y = data[starti:stopi,chan],
    #                     name = str(chan))

    return fig
  
# Step 6. Add the server clause
if __name__ == "__main__":
    app.run_server(debug=True)

# if __name__ == "__main__":
#     app.run_server(debug=True)

# app.run_server(mode='inline', port=8030)
