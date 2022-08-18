
import argparse

from pathlib import Path
import dash
from dash import html, dcc
from dash.dependencies import Output, Input
from dash import no_update

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime,timezone,timedelta


# Create the parser
my_parser = argparse.ArgumentParser(prog='DataExplorer.py',
    description='Create an interactive graph of raw data collected in Bonsai-rx')

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


def main(args):
    chan_on_plot = [list(map(int, c)) for c in args.channels_per_subplot] #convert list of strings to list of int to index data

    # filepath = '/Users/kperks/Downloads/eod-50k-stim2022-08-17T14_50_39.bin'
    filepath = Path(args.filepath)

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

    # initialize app
    app = dash.Dash(__name__)

    # Create a Dash layout
    app.layout = html.Div([
                    # a header and a paragraph
                    html.Div([
                        html.H3("Raw Data Explorer"),
                        html.P("You can: Use the range slider below the plot to navigate through the recording. \
                        Zoom in and out on detail in the signal. Hover over the signal to annotate data points. \
                        Move the graph around if you are zoomed in. Save a png."),
                        html.P("The figure width will scale with your browser window. \
                            Use the 'graph height' slider at the bottom to change its height.")
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
                            ]),
                    html.P([
                        html.Label("Graph height"), 
                        dcc.Slider(id='figheight_slider', min=200, max=1000, step=100, value=500)])
                          ])


    # Step 5. Add callback functions
    @app.callback(Output('plot', 'figure'),
                 [Input('slider', 'value'),
                 Input('figheight_slider', 'value')])
    def update_figure(input1,height):
        # filtering the data
        starti = int(input1[0]*args.fs)
        stopi = int(input1[1]*args.fs)

        # create the plot
        fig = make_subplots(rows = args.number_subplots, cols = 1, shared_xaxes=True)
            
        # updating the data in the plot    
        for i_, nplot_ in enumerate(chan_on_plot):
            for chan in nplot_:
                fig.add_trace(go.Scatter(x = time[starti:stopi], y = data[starti:stopi,chan], 
                    name='channel ' + str(chan),opacity=1),
                    row = i_+1,col=1)

        # resize figure (reactive to input)
        fig.update_layout(height=int(height))

        return fig

      
    # Step 6. Add the server clause
    if __name__ == "__main__":
        app.run_server(debug=False)

    # app.run_server(mode='inline', port=8030)
    

if __name__ == "__main__":
   main(args)
