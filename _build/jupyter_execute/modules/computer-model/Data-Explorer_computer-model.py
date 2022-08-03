#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/ERG/Sensory-Coding-ERG.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Giant Fiber
# 
# Action Potential

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Import Data](#one)
# 

# <a id="setup"></a>
# # Setup
# 
# [toc](#toc)

# Import and define functions

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to import packages and define functions 
from pathlib import Path
import random
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import ndimage, optimize, signal
from scipy.signal import hilbert,medfilt,resample, find_peaks,butter
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

from ipywidgets import interactive, HBox, VBox, widgets, interact

def monoExp(x, m, t, b):
    return m * np.exp(-x / t) + b

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Mount Google Drive

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this cell to mount your Google Drive.

from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id="one"></a>
# # Import Data
# 
# [toc](#toc)

# Import data digitized with *Nidaq USB6211* and recorded using *Bonsai-rx* as a *.bin* file

# In[ ]:


#@title {display-mode: "form"}

#@markdown Specify the file path 
#@markdown to your recorded data on Drive (find the filepath in the colab file manager:

filepath = "full filepath goes here"  #@param 
filepath = "/Users/kperks/mnt/OneDrive - wesleyan.edu/Teaching/Neurophysiology_FA22/data/20220617/gf-stim2022-06-17T15_57_48.bin"

#@markdown Specify the sampling rate and number of channels recorded.
sampling_rate = None #@param
number_channels = None #@param
vnc_channel = 0 #@param
stimulus_channel = 1 #@param

sampling_rate = 30000 #@param
number_channels = 2 #@param

downsample = True #@param
newfs = 10000 #@param

#@markdown After you have filled out all form fields, 
#@markdown run this code cell to load the data. 

filepath = Path(filepath)

# No need to edit below this line
#################################
data = np.fromfile(Path(filepath), dtype = np.float64)
data = data.reshape(-1,number_channels)
data = data-data[0,:] # only do this offset adjustment for motor nerve recordings

dur = np.shape(data)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %dur)

fs = sampling_rate
if downsample:
    # newfs = 2500 #downsample data
    chunksize = int(sampling_rate/newfs)
    if number_channels>1:
        data = data[0::chunksize,:]
    if number_channels==1:
        data = data[0::chunksize]
    fs = int(np.shape(data)[0]/dur)

time = np.linspace(0,dur,np.shape(data)[0])

sos = butter(4, 500, 'lp', fs=fs, output='sos')


if len(np.shape(data))>1:
    vnc_signal = data[:,vnc_channel]
    stimulus_signal = data[:,stimulus_channel]
if len(np.shape(data))==1:
    signal = data

print('Now be a bit patient while it plots.')

f = go.FigureWidget(make_subplots(rows=2, cols=1, row_width=[3, 1], 
                                  vertical_spacing=0, shared_xaxes= True)) #,layout=go.Layout(height=500, width=800))
f.add_trace(go.Scatter(x = time[0:fs], y = vnc_signal[0:fs],
                             opacity=1),row=2,col=1)
f.add_trace(go.Scatter(x = time[0:fs], y = stimulus_signal[0:fs],
                             opacity=1),row=1,col=1)

f.update_layout(height=600, width=1000,
                showlegend=False,
               xaxis2_title="time(seconds)", 
                  yaxis1_title='photoresistor voltage',
               yaxis2_title='retina voltage')

slider = widgets.FloatRangeSlider(
    min=0,
    max=dur,
    value=(0,1),
    step= 1,
    readout=False,
    description='Time')
slider.layout.width = '600px'

# our function that will modify the xaxis range
def response(x):
    with f.batch_update():
        starti = int(x[0]*fs)
        stopi = int(x[1]*fs)
        f.data[0].x = time[starti:stopi]
        f.data[0].y = vnc_signal[starti:stopi]
        f.data[1].x = time[starti:stopi]
        f.data[1].y = stimulus_signal[starti:stopi]

vb = VBox((f, interactive(response, x=slider)))
vb.layout.align_items = 'center'
vb


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
