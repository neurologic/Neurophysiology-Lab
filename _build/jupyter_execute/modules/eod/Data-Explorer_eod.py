#!/usr/bin/env python
# coding: utf-8

# # Data Explorer
# 
# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/eod/Data-Explorer_eod.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Event detection](#one)
# - Time series analyses:
#     - [Part II. Rate](#two)
#     - [Part III. ISI](#three)
#     - [Part IV. Convolution](#four)
# - [Part V. Sampling Rate](#five)

# <a id="intro"></a>
# # Electric Organ Discharge (EOD) Physiology
# 
# As you explore your data, process and analyze it, think about some of the following questions:
# - Why were there two sets of differential electrodes (what if there had only been one)?
# - Why do events in the signal look different from each other (when do they look similar)?
# - How does the sampling rate of the Analog-to-Digital conversion effect the "raw" signal and my ability to observe EODs?
# - How are EOD events distributed through time?

# <a id="setup"></a>
# # Setup

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


# Import data digitized with *Nidaq USB6211* and recorded using *Bonsai-rx* as a *.bin* file
# 
# If you would like sample this Data Explorer, but do not have data, you can download an example from [here](https://drive.google.com/file/d/10cxBdfnEwRv77-dwcReqHyjYv-uLODe4/view?usp=sharing) and then upload the file to Google Colab (or access the file through Drive after uploading it to your Drive). If you are using this example file, the samplerate was 50000 on two channels (each channel was a set of bipolar electrodes perpendicular to each other with a fisn in the middle). 

# In[ ]:


#@title {display-mode: "form" }

#@markdown Specify the file path 
#@markdown to your recorded data on Drive (find the filepath in the colab file manager:

filepath = "full filepath goes here"  #@param 
# filepath = '/Users/kperks/Downloads/eod-50k-stim2022-08-17T14_50_39.bin'

#@markdown Specify the sampling rate and number of channels recorded.

sampling_rate = 50000 #@param
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
#@markdown Be patient with the range refresh... the more data you are plotting the slower it will be. 

slider = widgets.FloatRangeSlider(
    min=0,
    max=data_dur,
    value=(0,1),
    step= 1,
    readout=True,
    continuous_update=False,
    description='Time Range (s)')
slider.layout.width = '600px'

# a function that will modify the xaxis range
def update_plot(x):
    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    starti = int(x[0]*fs)
    stopi = int(x[1]*fs)
    ax.plot(time[starti:stopi], data[starti:stopi,:])

w = interact(update_plot, x=slider);


# For a more extensive ***RAW*** Data Explorer than the one provided in the above figure, use the [DataExplorer.py](https://raw.githubusercontent.com/neurologic/Neurophysiology-Lab/main/howto/Data-Explorer.py) application found in the [howto section](https://neurologic.github.io/Neurophysiology-Lab/howto/Dash-Data-Explorer.html) of the course website.

# <a id="one"></a>
# # Part I. Event Detection
# 
# Python has built-in algorithms for detecting "peaks" in a signal. However, it will detect *all* peaks. Therefore, the function takes in arguments that specify parameters for minimum height that can count as a peak and a minimum acceptible interval between independent peaks. 
# 
# First, we will subtract the median of the signal, take the absolute value of the signal, and sum across all channels (if you recorded more than one). With this single combined signal, we will detect peaks. 

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to plot the combined signal for peak detection. 
#@markdown Use the plot to determine an appropriate detection threshold.

y = data - np.median(data)
y = np.sum(np.abs(y),1)

slider = widgets.FloatRangeSlider(
    min=0,
    max=data_dur,
    value=(0,1),
    step= 1,
    readout=False,
    continuous_update=False,
    description='Time Range (s)')
slider.layout.width = '600px'

# a function that will modify the xaxis range
def update_plot(x):
    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    starti = int(x[0]*fs)
    stopi = int(x[1]*fs)
    ax.plot(time[starti:stopi], y[starti:stopi])

w = interact(update_plot, x=slider);


# In[ ]:


#@title {display-mode: "form"}

#@markdown Fill in this form with the detection threshold. 

detection_threshold = None #@param
# detection_threshold = 0.02 #@param
#@markdown Then run the code cell to detect peaks (events)

y = data - np.median(data)
y = np.sum(np.abs(y),1)

d = 0.0003*fs #minimum time allowed between distinct events
r = find_peaks(y,height=detection_threshold,distance=d)

eod_times = r[0]/fs


# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to plot the signal on each trial 
#@markdown overlaid with a scatter of EOD times detected using your threshold. 
    
slider = widgets.FloatRangeSlider(
    min=0,
    max=data_dur,
    value=(0,1),
    step= 1,
    readout=False,
    continuous_update=False,
    description='Time Range (s)')
slider.layout.width = '600px'

# a function that will modify the xaxis range
def update_plot(x):
    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    starti = int(x[0]*fs)
    stopi = int(x[1]*fs)
    ax.plot(time[starti:stopi], data[starti:stopi,:])
    ax.scatter(eod_times[(eod_times>x[0]) & (eod_times<x[1])],
               [np.median(data)] * len(eod_times[(eod_times>x[0]) & (eod_times<x[1])]),
              zorder=3,color='black',s=50)

w = interact(update_plot, x=slider);


# Once you know the times of each peak (each event), we can look at the waveforms of those events. To do this, we plot the peak of the signal at the event time and some duration before and after that peak. 
# 
# > Note: If you do not think you are detecting enough of the events or if you think you are detecting too much noise, modify your detection threshold and go through the detection steps in Part I again.

# In[ ]:


#@title {display-mode: "form"}

# #@markdown Select a pre and post event duration (dur; in milliseconds) to plot for each EOD.
# eod_range = 0.3 #@param

# #@markdown Set the y-axis range based on your raw data.
# ymin = -0.05 #@param
# ymax = 0.1 #@param

#@markdown Then run this cell to create an interactive plot with a slider to scroll through EOD events and channels.


slider_xrange = widgets.FloatSlider(
    min=0.05,
    max=2,
    value=0.6,
    step=0.05,
    continuous_update=False,
    readout=True,
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

slider_eod = widgets.IntSlider(
    min=0,
    max=len(eod_times),
    value=0,
    step= 1,
    continuous_update=False,
    description='EOD number')
slider_eod.layout.width = '600px'

slider_chan = widgets.IntSlider(
    min=0,
    max=number_channels-1,
    value=0,
    step= 1,
    continuous_update=False,
    description='channel')
slider_chan.layout.width = '300px'

# a function that will modify the xaxis range
def update_plot(eodi,chan,xrange,yrange):
    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    
    eod_range = xrange/2
    win_ = int(eod_range/1000*fs)

    events = np.asarray([data[(int(fs*t)-win_):(int(fs*t)+win_),chan] for t in eod_times 
          if (((int(fs*t)-win_)>0) & ((int(fs*t)+win_)<np.shape(data)[0]))]).T
    etime = np.linspace(-eod_range,eod_range,win_*2)

    ax.plot(etime,events[:,eodi],color='black',linewidth=3)
    ax.set_ylim(yrange[0],yrange[1]);

w = interact(update_plot, eodi=slider_eod, chan=slider_chan, xrange=slider_xrange, yrange=slider_yrange);


# Take some time to explore and observe the variation in EOD waveforms. 
# 
# There are a fundamental set of processing techniques we use to quantify event time series (such as spikes from a neuron or EODs from a fish): 
# - rate
# - isi
# - filtered/smoothed amplitude
# 
# In **Part II - Part IV**, you will work with each of these analyses.

# <a id="two"></a>
# # Part II. Rate

# ## Average rate
# 
# How would you calculate the average event rate?
# 
# <div class="alert-info">
# <b>Tip:</b>
#     <li> <b>len(variable)</b> : len() is a function used to get the number of elements in an array called *variable*</li>
#     <li> <code class="lang-python">+ - * / </code> are the symbols for addition, subtraction, multiplication, and division</li>
#     <li><b>eod_times</b> is a variable that contains the list of EOD times</li>
# </div>
# 
# 
# <div>
# <!--     class="alert-info"> -->
#     <p> This is a good time to introduce "indexing" lists in python, because eod_times is a list (with the earliest eod time in the first position of the list and the latest eod time in the last position of the list).</p>
#     <p> The following table shows, by example, how you would get the value at each position in a list (<b>L</b>) by indexing the list. In this examples, the values in the list are <b>t0, t1, t2</b>.</p>
# </div>
# 
# Consider the list where ```L=[t0, t1, t2]```
# 
# <div>
# <table class="table table-bordered" style="text-align:center;">
# <tbody><tr>
# <th style="text-align:center;width:33%">If you type: </th>
# <th style="text-align:center;width:33%">Then you will get: </th>
# <th style="text-align:center;width:33%">Because... </th>
# </tr>
# <tr>
# <td>L[2]</td>
# <td>t2</td>
# <td>you are asking for an offset of 2 positions (start at zero)</td>
# </tr>
# <tr>
# <td class="ts">L[-2]</td>
# <td class="ts">t1</td>
# <td>negative offsets count from the right</td>
# </tr>
# <tr>
# <td>L[1:]</td>
# <td>[t1, t2]</td>
# <td>a colon "slices" a list, which means it returns a section of the list (in this case, from position 1 until the end)</td>
# </tr>
# </tbody></table>
#     </div>
#     
# Finally, if you want to print the entire contents of a list to the output of a code cell, use the command ```print(list)``` where "list" can be the name of any list (in this case *eod_times*)
# 
# In the code cell below, write code that would calculate the average EOD rate in your recording. Store the result as a variable called ```average_rate```. 

# In[ ]:


...


# In[ ]:


#@title {display-mode:"form"}

#@markdown Run this code cell to print the average rate calculated using your equation. 
print(f'The average EOD rate is {average_rate}')


# ## Subsampling (*bootstrapping*) the average rate
# 
# In order to do statistics and compare EOD rates between different conditions or groups (for example, among different species of fish), we need more than just one estimate of the EOD rate. 
# 
# *bootstrapping* is an analytic technique used to *subsample* your data. In this case, we will calculate a set of EOD rate averages. Then we can get the mean and standard deviation of the average EOD rate. A *subsample* of the data is a smaller continuous section of the data. 
# 
# You can control the number of subsampled sets and the duration of each set. 
# The script (hidden) in the code cell below randomly selects samples of the specified duration from throughout the total recording. It repeats this random selection process ***N*** times. 
# 
# Once you specify the bootstrapping parameters in the form below, run the code cell. You will see a plot of the average rate of each subsample (each black point in the scatterplot), and the distribution (quantiles) of the set of subsamples in [boxplot](https://en.wikipedia.org/wiki/Box_plot) format.

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to enable the interactive analysis.
#@markdown Specify a duration time (seconds) for each subsample of the data 
#@markdown and a number of times to subsample the data.  
#@markdown Explore what changing these parameters does to your result.

slider_duration = widgets.FloatSlider(
    min=0,
    max=np.min([15,data_dur/2]),
    value=1,
    step= 0.001,
    readout=True,
    continuous_update=False,
    description='sample duration')
slider_duration.layout.width = '600px'

slider_N = widgets.IntSlider(
    min=0,
    max=100,
    value=10,
    step= 1,
    readout=True,
    continuous_update=False,
    description='number of reps')
slider_N.layout.width = '600px'

# a function that will modify the xaxis range
def update_plot(duration,N):
    
    rate_ = []
    for i in range(N):
        t = random.uniform(np.min(eod_times)+duration,np.max(eod_times)-duration)
        rate_.append(sum((eod_times>t) & (eod_times<t+duration))/duration)

    fig,ax = plt.subplots(figsize=(3,5),num=1);
    sns.boxplot(y=rate_, color = 'grey',ax = ax);
    sns.stripplot(y = rate_, color = 'black',size=10,ax = ax);
    ax.set_ylabel('rate (eod/sec)')#,fontsize=14);

w = interact(update_plot, duration=slider_duration, N=slider_N);


# If you increase/decrease the ***duration*** of the subsampled data, does the *variance* of the estimated rate increase/decrease? Is there an '*asymptote*' to the change in variance? How does that asymptote influence your choice of the *duration* parameter in analyzing your data?
# 
# If you decrease/increase ***N***, does the distribution of the estimate change? How?

# <a id="three"></a>
# # Part III. ISI
# 
# The time between events is called the *inter-event interval". Since events in neurons are called *spikes* the metric is called an *inter-SPIKE interval* (***ISI***). In electric fish, the metric is also called the IPI (inter-*pulse* interval), which refers to each EOD event as a pulse. 
# 
# How would you calculate the ISI from your recording?
# 
# <div class="alert-info">
# <b>Tip:</b> 
#     <li> <b>np.diff(variable)</b> : *diff()* is <a href="https://numpy.org/doc/stable/reference/generated/numpy.diff.html">a numpy module</a> that calculates the numerical difference between each element in a list named <i>variable</i> and returns the result as a list</li>
#     <li><b>eod_times</b> is a variable that contains the list of EOD times</li>
# </div>
# 
# In the code cell below, write a script that performs this calculation. 
# Store the result as a variable called ```isi```
# 

# In[ ]:


isi = ...


# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to use your equation to calculate the average isi and plot the isi over time. 

print(f'Average isi is {np.mean(isi):0.2f}.')

# plot the isi at each EOD time.
fig = go.Figure(layout=go.Layout(height=500, width=800))
fig.add_trace(go.Scatter(x=eod_times[1:], y=isi, mode='markers',name='isi',marker_size=5,line_color='black'))

fig.show()


# What should the titles of the x and y axes be?
# 
# How does the isi relate to the rate? Think about how would you calculate *instantaneous* rate (as opposed to the average rate across some window of time)?
# 
# Would you consider the isi relatively *variable* or *constant*? Why?
# 
# We can quantify how variable/constant something is by looking at the **distribution** of its values.

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run this code cell to plot the isi distribution (in boxplot format)

plt.figure(figsize=(3,5));
sns.boxplot(y=isi, color = 'grey');
# sns.stripplot(y = isi, color = 'black',size=10);
plt.ylabel('isi',fontsize=14);
plt.yticks(fontsize=14);


# <a id="four"></a>
# # Part IV. Convolution
# 
# By *convolving* a waveform with a time series, each event is transformed into a waveform. When all of these event waveforms are added together, you get a continuous signal instead of a discrete time series. This transformation is sometimes called "smoothing" and is required before some calculations can be made (such as correlation analysis). 
# 
# In this instance, we are using a ***Gaussian filter***. Therefore, the smoothness of the signal is controlled by a parameter called ***sigma*** that you can interactively control with a slider after running the code cell below. 
# 
# Details of the function used to accomplish this processing step can be found [at scipy.ndimage.gaussian_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html). For more general information on what a Gaussian is, you can consult the [wikipedia page on the Gaussian distribution](https://en.wikipedia.org/wiki/Normal_distribution). In this case, the *sigma* parameter of the Gaussian filter is equivalent to the *standard deviation* of a Gaussian distribution.

# In[ ]:


#@title {display-mode: "form"}

#@markdown Choose a smoothing filter width ```sigma``` (the standard deviation of the *gaussian kernel* in seconds). <br>
#@markdown Then run this code cell to plot the smoothed signal from discrete EOD times. 

slider_sigma = widgets.FloatSlider(
    min=0,
    max=1,
    value=(0.1),
    step= 0.01,
    readout=True,
    continuous_update=False,
    description='sigma')
slider_sigma.layout.width = '600px'

slider = widgets.FloatRangeSlider(
    min=0,
    max=data_dur,
    value=(0,1),
    step= 1,
    readout=False,
    continuous_update=False,
    description='Time Range (s)')
slider.layout.width = '600px'

# a function that will modify the xaxis range
def update_plot(x,sigma):
    
    filtered_fs = 1000
    sigma = sigma*filtered_fs

    eod_samps = [int(t*filtered_fs) for t in eod_times]

    filtered_time = np.linspace(0,data_dur,int(data_dur*filtered_fs))
    filtered_y = unit_impulse(len(filtered_time),eod_samps)
    filtered_y = ndimage.gaussian_filter1d(filtered_y,sigma=sigma,mode='wrap')*filtered_fs

    fig, ax = plt.subplots(figsize=(10,5),num=1); #specify figure number so that it does not keep creating new ones
    starti = int(x[0]*filtered_fs)
    stopi = int(x[1]*filtered_fs)
    ax.plot(filtered_time[starti:stopi], filtered_y[starti:stopi])
    ax.set_xlabel('msec')
    ax.set_ylabel('a.u.')

w = interact(update_plot, x=slider, sigma=slider_sigma);


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:




