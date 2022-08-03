#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-11/Motor-Coordination-and-Big-Data.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Motor Coordination and Big Data
# 
# This notebook provides tools for interacting with multi-channel EMG data collected using differential electrodes, Backyard Brains amplifiers, Nidaq acquisition hardware, and Bonsai-rx recording software. 
# 
# Throughout the notebook, you will plot both raw and processed data.
# - You can interact with the plots by zooming in and panning. <br>
# - You can save the current plot view at any time by hitting the "download" icon - it will save to your Downloads folder. Make sure to re-name the auto-generated file and make notes about what you plotted right away. <br>
# 
# The plotting tools available in this notebook include:
# - raw EMG data with each channel plotted separately
# - emg amplitude envelopes with each channel plotted separately
# - selected subsets of emg amplitude envelopes overlaid on the same plot
# - 3D plotting of the first 3 principal components of muscle activity for a specific range of data selected
# 
# The data processing and analysis tools available in this notebook include:
# - amplitude envelope smoothing
# - data range selection within a file
# - correlation of activity (of the amplitude envelopes) across recording channels
# - Principle Component Analysis on all recorded channels (channels may be dropped from the analysis in the step when you load the data)
# 

# <a id="toc"></a>
# # Table of Contents
# 1. [Introduction](#intro)
# 2. [Setup](#setup)
# 3. [Part I. Raw EMG Signal](#one)
# 4. [Part II. Select Data](#two)
# 5. [Part III. EMG envelope](#three)
# 6. [Part IV. Muscle Coordination](#four)
# 

# # Setup
# [toc](#toc)
# 

# In[ ]:


#@markdown Run this code cell to load packages and { display-mode: "form" }
#@markdown initialize the notebook.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display
import csv
from scipy.signal import hilbert,medfilt,resample
from sklearn.decomposition import PCA
import scipy
import seaborn as sns
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()



# In[ ]:


#@markdown **TASK:** Run this code cell to mount your Google Drive. { display-mode: "form" }

from google.colab import drive
drive.mount('/content/drive')


# In[ ]:


#@markdown **TASK:** Run this code cell to load the EMG dataset you will explore and analyze. { display-mode: "form" }

emg_filepath = "file path in colab" #@param

sampling_rate = NaN #@param
number_channels = NaN #@param
drop_channels = [] #@param

filepath = Path(emg_filepath)

# No need to edit below this line
#################################
emg = np.fromfile(Path(filepath), dtype = np.float64)
emg = emg.reshape(-1,number_channels)
dur = np.shape(emg)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %dur)
newfs = 2500
chunksize = int(sampling_rate/newfs)
emg = emg[0::chunksize,:]
newfs = np.shape(emg)[0]/dur

# nerve = y_data[:,nerve_channel] - np.median(y_data[:,nerve_channel],0)
time = np.linspace(0,np.shape(emg)[0]/newfs,np.shape(emg)[0])
# muscle = y_data[:,muscle_channel]

column_names = [str(i) for i in np.arange(0,number_channels)]
df_emg = pd.DataFrame(data = emg, columns = column_names)
if len(drop_channels)>0:
  for chan in drop_channels:
    df_emg = df_emg.drop(columns = str(chan))
  number_channels = number_channels - len(drop_channels)

# Use rectfication and gaussian smoothing on EMG to get mean-centered rate
df_rate = pd.DataFrame({})
filter_dur = 0.01 #@param
filtert = int(filter_dur*sampling_rate)
for h in list(df_emg.columns): # rename headers as input channels
    y = df_emg[h] - np.mean(df_emg[h])
    y = np.abs(y) #takes the absolute value of 
    y = scipy.ndimage.gaussian_filter(y,filtert)
    df_rate[h] = y


# <a id="one"></a>
# # Part I. Plot the raw EMG signal from each muscle
# [toc](#toc)
# 
# The amplitude units of the EMG signal are in Volts, but the amplitude was amplified before being recorded. The amplification factor was approximately 1000, so 1V recorded was really 1mV measured at the electrode. 
# 
# 

# In[ ]:


#@markdown **TASK:** First, specify a time range to plot. { display-mode: "form" }
#@markdown This is just necessary because these data files are so large.
#@markdown If you tried to plot all of the data at once the Google Colab kernel will "die."
#@markdown If you need a plot of the whole time range of the recording, let me know 
#@markdown and I can make one for you using a program local to my computer. 
#@markdown >Note: You could look at the simulataneously recorded
#@markdown video for guidance on time ranges to peak at if needed.
#@markdown <br> If you try to plot more than 200 seconds total of data
#@markdown (so about 20-30 seconds for 9 channels or 40-60 seconds for 5 channels), 
#@markdown the plot will "time out" and not show up.

time_range = [20, 40] #@param

#@markdown Then, Run this cell to plot the raw EMG data.
#@markdown You can zoom in and scroll around to explore the data. 


plotmask = ((time>time_range[0]) & (time<time_range[1]))
fig = make_subplots(rows=number_channels, cols=1,
                    vertical_spacing=0,
                    shared_xaxes=True)
for i,chan in enumerate(list(df_emg.columns)):
  fig.add_trace(go.Scatter(x = time[plotmask], y = df_emg[plotmask][chan].values,
                         name=chan),
                row=i+1,col=1)
fig.update_layout(xaxis_title="time(seconds)", 
                  yaxis_title='amplitude',width=800, height=1000)
# fig.layout.yaxis.showticklabels=False
print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))

fig.show()


# <a id="two"></a>
# # Part II. Plot the rectified, smoothed "amplitude envelope"
# [toc](#toc)
# 
# This is a type of *signal processing* that transforms raw EMG activity (a bipolar signal - both positive and negative values) into what we refer to as the *amplitude envelope* of the EMG activity. The "smoothing" of the envelope results in a waveform that reflects both the amplitude and the rate of the raw EMG signal (accounts for both spatial and temporal summation). Therefore, absolute voltage information is lost, but you can still compare relative voltage across channels and across recordings that used the same electrode configurations. 

# In[ ]:


#@markdown **TASK:** First, specify a time range to plot. { display-mode: "form" }
#@markdown This is just necessary because these data files are so large.
#@markdown If you tried to plot all of the data at once the Google Colab kernel will "die."
#@markdown If you need a plot of the whole time range of the recording, let me know 
#@markdown and I can make one for you using a program local to my computer. 
#@markdown >Note: You could look at the simulataneously recorded
#@markdown video for guidance on time ranges to peak at if needed.
#@markdown <br> If you try to plot more than 200 seconds total of data
#@markdown (so about 20-30 seconds for 9 channels or 40-60 seconds for 5 channels), 
#@markdown the plot will "time out" and not show up.

time_range = [0, 60] #@param

#@markdown Then, Run this cell to plot the envelope of the EMG data.
#@markdown You can zoom in and scroll around to explore the data. 


plotmask = ((time>time_range[0]) & (time<time_range[1]))

fig = make_subplots(rows=number_channels, cols=1,
                    vertical_spacing=0,
                    shared_xaxes=True)
for i,chan in enumerate(list(df_rate.columns)):
  # if plot_raw:
  #   fig.add_trace(go.Scatter(x = time, y = (df_emg[chan].values)/5,
  #                        name=chan),
  #               row=i+1,col=1)
  fig.add_trace(go.Scatter(x = time[plotmask], y = df_rate[plotmask][chan].values,
                         name=chan),
                row=i+1,col=1)
fig.update_layout(xaxis_title="time(seconds)", 
                  yaxis_title='amplitude',width=800, height=1000)

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))
fig.show()


# In[ ]:


#@markdown Overlay channels on same axis { display-mode: "form" }

#@markdown **TASK:** First, specify a time range and set of channels to plot.
#@markdown Remember that the first channel is numbered 0.
#@markdown >Note: If you plot less channels, you can plot more time.
#@markdown If the plot does not show up after the cell finishes, pick less data.

time_range = [35, 60] #@param
channels_to_plot = [2,4] #@param

#@markdown Then, Run this cell to make an overlaid plot 
#@markdown of the envelope of the EMG data on the selected channels.
#@markdown You can zoom in and scroll around to explore the data. 

plotmask = ((time>time_range[0]) & (time<time_range[1]))

fig = go.Figure()
for i,chan in enumerate(channels_to_plot):
  chan = str(chan)
  fig.add_trace(go.Scatter(x = time[plotmask], y = df_rate[plotmask][chan].values,
                         name=chan,opacity=1))
fig.update_layout(xaxis_title="time(seconds)", 
                  yaxis_title='amplitude',width=800, height=500)

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))
fig.show()


# <a id="three"></a>
# # Part III. Analyze a selection of the data. 
# [toc](#toc)

# In[ ]:


#@markdown Pick a time window to analyze that has the section  { display-mode: "form" }
#@markdown of movement you want to analyze 
#@markdown and enter it in the code cell below.
#@markdown > Note: get the time by hovering over the data plot. 
#@markdown - **start** = the start time of the section you want to analyze (seconds).
#@markdown - **stop** = the stop time of the section you want to analyze (seconds).

start =  36.5#@param {type:"number"}
stop = 50 #@param {type:"number"}

#@markdown <b>Task:</b> After you have specified the start and stop times,
#@markdown run this cell to execute the variable assignment.
# df_vid_selection = df_vid[((df_vid['time']>(start)) & (df_vid['time']<(stop)))] # select start:stop section
# df_emg_select = df_emg[((time>start) & (time<stop))]
df_rate_select = df_rate[((time>start) & (time<stop))]
time_select = time[((time>start) & (time<stop))]

print('all set - analysis domain defined')
print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id="four"></a>
# # Part IV. Muscle coordination
# [toc](#toc)
# 
# Think about how you would qualitatively describe the relationship between the two muscle signals that you plotted. The correlation metric is often helpful to quantify the relationship between signals. Essentially, correlation is the measure of how two or more variables are related to one another. https://en.wikipedia.org/wiki/Correlation
# 
# 

# In[ ]:


#@markdown <b>Task:</b> Run this cell to calculate the { display-mode: "form" }
#@markdown mathematical correlation values between the two signals.
#@markdown The results will be shown in table and matrix format.

# No need to edit this code cell
################################
print('correlation matrix:')
p_corr = df_rate_select.corr()
display(p_corr)
hfig, ax = plt.subplots(1)
sns.heatmap(p_corr, annot=True);




# <a id="five"></a>
# # Part V. Dimensionality Reduction
# [toc](#toc)
# 
# Use principal component analysis to observe the activity of all muscles simultaneously in the context of the dominant signals from the population activity. 

# In[ ]:


#@markdown <b>Task:</b> Run this cell to do a Principal Component Analysis { display-mode: "form" }
#@markdown (PCA) on the selected data.
#@markdown You will get a plot of the explained variance for each PC.

df = df_rate_select
df =(df - df.mean()) / df.std()
n_components=df.shape[1] # if try to take more components than have channels, use amount of channels
pca = PCA(n_components=n_components)
pca.fit(df)
df_pca = pd.DataFrame(pca.transform(df), columns=['PC%i' % i for i in range(n_components)], index=df.index)
print('Your data has now been transformed into ' + str(n_components) + ' principle components.')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df_pca.columns, y=pca.explained_variance_ratio_, 
                                 mode='markers',marker_size=15,line_color='black'))
fig.update_layout(xaxis_title="Principal Components", 
                  yaxis_title='Explained Variance', width=400, height=350)

fig.show()


# In[ ]:


#@markdown <b>Task:</b> Run this cell to plot the data in the space defined by { display-mode: "form" }
#@markdown the first three principle components of the selected data.
#@markdown The start and stop locations of the trajectory are marked by green and purple dots (respectively).
#@markdown > Note: The plot sometimes starts zoomed far in. 
#@markdown Hit the "home" button and/or zoom out. You can then 
#@markdown zoom back in as needed.

fig = go.Figure()
fig.add_trace(go.Scatter3d(x=df_pca['PC0'], y=df_pca['PC1'], z=df_pca['PC2'],
                                   mode='markers',name='trajectory',marker_size=1,line_color='black'))
fig.add_trace(go.Scatter3d(x=[df_pca['PC0'].values[0]], y=[df_pca['PC1'].values[0]], z=[df_pca['PC2'].values[0]],
                                   mode='markers',name='start',marker_size=10,line_color='green'))
fig.add_trace(go.Scatter3d(x=[df_pca['PC0'].values[-1]], y=[df_pca['PC1'].values[-1]], z=[df_pca['PC2'].values[-1]],
                                   mode='markers',name='stop',marker_size=10,line_color='purple'))

fig.update_layout(scene = dict(
        xaxis = dict(title = 'PC0'),
        yaxis = dict(title = 'PC1'),
        zaxis = dict(title = 'PC2')),
    width=600, height = 600)
    
   

fig.show()

