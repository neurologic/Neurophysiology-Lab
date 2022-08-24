#!/usr/bin/env python
# coding: utf-8

# # Data Explorer
# 
# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/earthworm-giant-fiber/Data-Explorer_earthworm-giant-fiber.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Event Detection](#one)
# - [Trial-Based Analysis](#two)
# 

# <a id="intro"></a>
# # Giant Fiber Physiology
# 
# How do structure and function and physiology relate to each other? The earthworm giant fiber system is great for investigating these questions for many reasons including: large distinct action potentials, robust stimulus-response relationship, ease of dissection, and interesting anatomical properties that lead to some fun anatomical-physiological relationships.
# 
# You will use a trial-based exploration of your data to examine parameters of action potential generation and propogation. 

# <a id="setup"></a>
# # Setup
# 
# [toc](#toc)

# Import and define functions

# In[ ]:


#@title {display-mode: "form" }

#@markdown Run this code cell to import packages and define functions 
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import ndimage
from scipy.signal import hilbert,medfilt,resample, find_peaks, unit_impulse
import seaborn as sns
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()
import matplotlib.pyplot as plt
import random

from pathlib import Path

from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from ipywidgets import widgets, interact
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
plt.style.use("https://raw.githubusercontent.com/NeuromatchAcademy/course-content/master/nma.mplstyle")

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Mount Google Drive

# In[ ]:


#@title {display-mode: "form" }

#@markdown Run this cell to mount your Google Drive.

from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# ## Import data 
# 
# Import data digitized with *Nidaq USB6211* and recorded using *Bonsai-rx* as a *.bin* file
# 
# If you would like sample this Data Explorer, but do not have data, you can download an example from [here](https://drive.google.com/file/d/1xVtqfthDE6ilAcjiF7pJ_qrIkDPpwZbo/view?usp=sharing) and then upload the file to Google Colab (or access the file through Drive after uploading it to your Drive). If you are using this example file, the sample rate was 30000 on two channels (channel 0 was the nerve signal and channel 1 was the stimulus monitor). At the beginning and end of the recording, I delivered single stimulus pulses with a Grass SD9 stimulator. In the middle of the recording, I used a glass rod to touch the head and the body about 25% from the head. The recording was taken with the photographed preparation in the lab manual. 

# In[ ]:


#@title {display-mode: "form" }

#@markdown Specify the file path 
#@markdown to your recorded data on Drive (find the filepath in the colab file manager:

filepath = "full filepath goes here"  #@param 
filepath = '/Users/kperks/mnt/OneDrive - wesleyan.edu/Teaching/Neurophysiology_FA22/data/earthworm-giant-fiber/stim-threshold-second_touch_0.bin'  #@param 

#@markdown Specify the sampling rate and number of channels recorded.

sampling_rate = 30000 #@param
number_channels = 2 #@param

downsample = False #@param
newfs = 10000 #@param

#@markdown After you have filled out all form fields, 
#@markdown run this code cell to load the data. 

filepath = Path(filepath)

# No need to edit below this line
#################################
data = np.fromfile(Path(filepath), dtype = np.float64)
data = data.reshape(-1,number_channels)
data_dur = np.shape(data)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %data_dur)

fs = sampling_rate
if downsample:
    # newfs = 10000 #downsample emg data
    chunksize = int(sampling_rate/newfs)
    data = data[0::chunksize,:]
    fs = int(np.shape(data)[0]/data_dur)

time = np.linspace(0,data_dur,np.shape(data)[0])

print('Data upload completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to plot imported data. <br> 
#@markdown Use the range slider to scroll through the data in time.
#@markdown Use the channel slider to choose which channel to plot
#@markdown Be patient with the range refresh... the more data you are plotting the slower it will be. 

slider_xrange = widgets.FloatRangeSlider(
    min=0,
    max=data_dur,
    value=(0,1),
    step= 1,
    readout=True,
    continuous_update=False,
    description='Time Range (s)')
slider_xrange.layout.width = '600px'

slider_chan = widgets.IntSlider(
    min=0,
    max=number_channels-1,
    value=0,
    step= 1,
    continuous_update=False,
    description='channel')
slider_chan.layout.width = '300px'

# a function that will modify the xaxis range
def update_plot(x,chan):
    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    starti = int(x[0]*fs)
    stopi = int(x[1]*fs)
    ax.plot(time[starti:stopi], data[starti:stopi,chan])

w = interact(update_plot, x=slider_xrange, chan=slider_chan);


# For a more extensive ***RAW*** Data Explorer than the one provided in the above figure, use the [DataExplorer.py](https://raw.githubusercontent.com/neurologic/Neurophysiology-Lab/main/howto/Data-Explorer.py) application found in the [howto section](https://neurologic.github.io/Neurophysiology-Lab/howto/Dash-Data-Explorer.html) of the course website.

# <a id="one"></a>
# # Part I. Event Detection
# 
# Python has built-in algorithms for detecting "peaks" in a signal. However, it will detect *all* peaks. Therefore, the function takes in arguments that specify parameters for minimum height that can count as a peak and a minimum acceptible interval between independent peaks. 
# 
# First, we will detect all the peaks on the stimulus monitor channel. This will give the time of each *stimulus-triggered trial*. Later, you can come back and detect all peaks on the nerve recording channel if you want to explore a trial-based view of the data triggered off of peaks from that channel. 

# In[ ]:


#@title {display-mode: "form"}

#@markdown Fill in this form. Decide on the peak detection threshold. 
#@markdown Choose which channel you want to use for event detection

channel = None #@param
detection_threshold = None #@param

#@markdown Then, run the code cell to detect peaks (events) and plot the signal
#@markdown overlaid with a scatter of trial times detected using your threshold. 

d = 0.0003*fs #minimum time allowed between distinct events
r = find_peaks(data[:,channel],height=detection_threshold,distance=d)

trial_times = r[0]/fs
event_amp = r[1]['peak_heights']
    
slider = widgets.FloatRangeSlider(
    min=0,
    max=data_dur,
    value=(0,1),
    step= 0.5,
    readout=False,
    continuous_update=False,
    description='Time Range (s)')
slider.layout.width = '800px'

# a function that will modify the xaxis range
def update_plot(x):
    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    starti = int(x[0]*fs)
    stopi = int(x[1]*fs)
    ax.plot(time[starti:stopi], data[starti:stopi,channel])
    ax.scatter(trial_times[(trial_times>x[0]) & (trial_times<x[1])],
               [np.median(data[:,channel])] * len(trial_times[(trial_times>x[0]) & (trial_times<x[1])]),
              zorder=3,color='black',s=50)

w = interact(update_plot, x=slider);


# Once you know the times of each peak (each event), we can look at the signal triggered off of those events. To do this, we plot the signal at the event time and some duration before and after that peak. 
# 
# > Note: If you do not think you are detecting enough of the events or if you think you are detecting too much noise, modify your detection threshold and go through the detection steps in Part I again.

# <a id="two"></a>
# # Part II. Trial-Based Analysis

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this cell to create an interactive plot with a slider to scroll 
#@markdown through data on each channel for individual trials.
#@markdown The stimulus amplitude will be printed for each trial. 

slider_xrange = widgets.FloatSlider(
    min=2,
    max=40,
    value=10,
    step=0.5,
    continuous_update=False,
    readout=False,
    description='xrange (ms)'
)
slider_xrange.layout.width = '600px'

slider_yrange = widgets.FloatRangeSlider(
    min=np.min(np.min(data)),
    max=np.max(np.max(data)),
    value=[np.min(np.min(data)),np.max(np.max(data))],
    step=0.01,
    continuous_update=False,
    readout=False,
    description='yrange'
)
slider_yrange.layout.width = '600px'

slider_trial = widgets.IntSlider(
    min=0,
    max=len(trial_times)-1,
    value=0,
    step= 1,
    continuous_update=False,
    readout=False,
    description='trial')
slider_trial.layout.width = '600px'

slider_chan = widgets.IntSlider(
    min=0,
    max=number_channels-1,
    value=0,
    step= 1,
    continuous_update=False,
    readout=False,
    description='channel')
slider_chan.layout.width = '300px'

label_eventamp = widgets.Label(
    value='stimulus amplitude'
)
label_eventamp.layout.width = '300px'
display(label_eventamp)

# a function that will modify the xaxis range
def update_plot(trial_,chan,xrange,yrange):
    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    
    offset_ = 1
    win_0 = int(offset_/1000*fs)
    win_1 = int(xrange/1000*fs)

    events = np.asarray([data[(int(fs*t)-win_0):(int(fs*t)+win_1),chan] for t in trial_times 
          if (((int(fs*t)-win_0)>0) & ((int(fs*t)+win_1)<np.shape(data)[0]))]).T
    xtime = np.linspace(-offset_,xrange,(win_0 + win_1))

    ax.plot(xtime,events[:,trial_],color='black',linewidth=3)
    ax.set_ylim(yrange[0],yrange[1]);
    ax.set_xlabel('milliseconds')
    
    # Change major ticks to show every 20.
    ax.xaxis.set_major_locator(MultipleLocator(5))
    # ax.yaxis.set_major_locator(MultipleLocator(20))

    # Change minor ticks to show every 5. (20/4 = 5)
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))

    # Turn grid on for both major and minor ticks and style minor slightly
    # differently.
    ax.grid(which='major', color='gray', linestyle='-')
    ax.grid(which='minor', color='gray', linestyle=':')

    # print(f'stimulus monitor peak = {event_amp[trial_]}')
    label_eventamp.value = 'peak amplitude = ' + str(np.round(event_amp[trial_],4)) + ' Volts'

w = interact(update_plot, trial_=slider_trial, chan=slider_chan, xrange=slider_xrange, yrange=slider_yrange);


# In[ ]:





# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
