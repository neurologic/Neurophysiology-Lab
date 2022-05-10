#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/<'folder'/'notebookname'>.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Template
# 
# <!-- <figure align="center">
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/example-eods_Kramer.jpeg?raw=True' width="300" alt='eod e-field' align="center"/>
# <figcaption align = "center"><b>Electric organ discharge waveform</b> and sex, in three snoutfish species of southern Africa. All electric organ discharges represented as voltage over time, recorded in the field immediately after capture. Same time bar for all. (a) Sexual dimorphism in Marcusenius altisambesi with two distinct waveforms. (b) Sex difference of only a statistical nature in Petrocephalus catostoma (Upper Zambezi form) with, in most males, a stronger second positive phase than in females, such as shown here. (c) Petrocephalus wesselsi (Sabie River, South Africa) with no difference between the sexes. P. wesselsi was recognized as distinct from P. catostoma only recently.
# </figcaption>
# </figure> -->
# 
# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/<'folder'/'notebookname'>.ipynb" target="_blank" rel="noopener noreferrer">Link to Other Notebooks (colab link)</a>   
# 

# # Setup
# [toc](#toc)
# 

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. ](#one)
# - Time series analyses:
#     - [Part II. ](#two)
#     - [Part III. ](#three)
#     - [Part IV. ](#four)
# - [Part V. ](#five)

# <a id="setup"></a>
# # Setup

# In[ ]:


#@title {display-mode: "form"}


# Import and define functions

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to import packages and define functions 
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import ndimage
from scipy.signal import hilbert,medfilt,resample, find_peaks
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

from ipywidgets import interactive, HBox, VBox, widgets, interact

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Mount Google Drive

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this cell to mount your Google Drive.

from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Import data digitized with *Nidaq USB6211* and recorded using *Bonsai-rx* as a *.bin* file

# In[ ]:


#@title {display-mode: "form"}

#@markdown Specify the file path 
#@markdown to your recorded data on Drive (find the filepath in the colab file manager:

filepath = "full filepath goes here"  #@param 

#@markdown Specify the sampling rate and number of channels recorded.

sampling_rate = NaN #@param
number_channels = NaN #@param

downsample = False #@param

#@markdown After you have filled out all form fields, 
#@markdown run this code cell to load the data. 

filepath = Path(filepath)

# No need to edit below this line
#################################
data = np.fromfile(Path(filepath), dtype = np.float64)
if number_channels>1:
    data = data.reshape(-1,number_channels)
dur = np.shape(data)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %dur)

fs = sampling_rate
if downsample:
    newfs = 2500 #downsample emg data
    chunksize = int(sampling_rate/newfs)
    if number_channels>1:
        data = data[0::chunksize,:]
    if number_channels==1:
        data = data[0::chunksize]
    fs = int(np.shape(data)[0]/dur)

time = np.linspace(0,dur,np.shape(data)[0])


print('Now be a bit patient while it plots.')

f = go.FigureWidget(layout=go.Layout(height=500, width=800))
if number_channels == 1:
    f.add_trace(go.Scatter(x = time[0:fs], y = data[0:fs],
                             name=str(chan),opacity=1))
if number_channels>1:
    for i,chan in enumerate(range(number_channels)):
        f.add_trace(go.Scatter(x = time[0:fs], y = data[0:fs,chan],
                             name=str(chan),opacity=1))

slider = widgets.FloatRangeSlider(
    min=0,
    max=dur,
    value=(0,1),
    step= 1,
    readout=False,
    description='Time')
slider.layout.width = '800px'

# our function that will modify the xaxis range
def response(x):
    with f.batch_update():
        starti = int(x[0]*fs)
        stopi = int(x[1]*fs)
        
        if number_channels == 1:
            f.data[0].x = time[starti:stopi]
            f.data[0].y = data[starti:stopi]
        if number_channels > 1:
            for i in range(number_channels):
                f.data[i].x = time[starti:stopi]
                f.data[i].y = data[starti:stopi,i]

vb = VBox((f, interactive(response, x=slider)))
vb.layout.align_items = 'center'
vb

# print('Now be a bit patient while it plots.')
# fig = go.Figure()
# fig.add_trace(go.Scatter(x = time, y = data,line_color='black',name='channel 1'))
# fig.update_layout(xaxis_title="time(seconds)", yaxis_title='amplitude',width=800, height=500)
# fig.show()


# <a id="one"></a>
# # Part I.
# 
# [toc](#toc)

# <a id="two"></a>
# # Part II.
# 
# [toc](#toc)

# <a id="three"></a>
# # Part III.
# 
# [toc](#toc)

# <a id="four"></a>
# # Part IV.
# 
# [toc](#toc)

# <a id="five"></a>
# # Part V.
# 
# [toc](#toc)

# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
