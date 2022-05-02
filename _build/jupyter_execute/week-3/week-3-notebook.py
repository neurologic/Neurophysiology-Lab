#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/<'folder'/'notebookname'>.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Week 3
# 
# <!-- <figure align="center">
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/example-eods_Kramer.jpeg?raw=True' width="300" alt='eod e-field' align="center"/>
# <figcaption align = "center"><b>Electric organ discharge waveform</b> and sex, in three snoutfish species of southern Africa. All electric organ discharges represented as voltage over time, recorded in the field immediately after capture. Same time bar for all. (a) Sexual dimorphism in Marcusenius altisambesi with two distinct waveforms. (b) Sex difference of only a statistical nature in Petrocephalus catostoma (Upper Zambezi form) with, in most males, a stronger second positive phase than in females, such as shown here. (c) Petrocephalus wesselsi (Sabie River, South Africa) with no difference between the sexes. P. wesselsi was recognized as distinct from P. catostoma only recently.
# </figcaption>
# </figure> -->
# 
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


#@markdown { display-mode: "form" }


# Import and define functions

# In[ ]:


#@markdown Run this code cell to import packages and define functions { display-mode: "form" }
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import ndimage
from scipy.signal import hilbert,medfilt,resample, find_peaks
import seaborn as sns
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Mount Google Drive

# In[ ]:


#@markdown Run this cell to mount your Google Drive. { display-mode: "form" }

from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Import data digitized with *Nidaq USB6211* and recorded using *Bonsai-rx* as a *.bin* file

# In[ ]:


#@markdown Specify the file path { display-mode: "form" }
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
data = data.reshape(-1,number_channels)
dur = np.shape(data)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %dur)

fs = 1/sampling_rate
if downsample:
    newfs = 2500 #downsample emg data
    chunksize = int(sampling_rate/newfs)
    data = data[0::chunksize,:]
    fs = np.shape(data)[0]/dur

time = np.linspace(0,np.shape(data)[0]/newfs,np.shape(data)[0])


print('Data upload completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))

print('Now be a bit patient while it plots.')
fig = go.Figure()
fig.add_trace(go.Scatter(x = time, y = data,line_color='black',name='emg0'))
fig.update_layout(xaxis_title="time(seconds)", yaxis_title='amplitude',width=800, height=500)


# <a id="one"></a>
# # Part I.

# <a id="two"></a>
# # Part II.

# <a id="three"></a>
# # Part III.

# <a id="four"></a>
# # Part IV.

# <a id="five"></a>
# # Part V.

# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
