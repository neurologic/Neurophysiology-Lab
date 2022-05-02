#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-2/Electric-Organ-Discharge.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Electric Organ Discharge
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/weakly-electric-fish-efield-current_Kramer.jpeg?raw=True' width="300" align="center" alt='eod e-field'/>
# 
# <figure align="center">
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/example-eods_Kramer.jpeg?raw=True' width="300" alt='eod e-field' align="center"/>
# <figcaption align = "center"><b>Electric organ discharge waveform</b> and sex, in three snoutfish species of southern Africa. All electric organ discharges represented as voltage over time, recorded in the field immediately after capture. Same time bar for all. (a) Sexual dimorphism in Marcusenius altisambesi with two distinct waveforms. (b) Sex difference of only a statistical nature in Petrocephalus catostoma (Upper Zambezi form) with, in most males, a stronger second positive phase than in females, such as shown here. (c) Petrocephalus wesselsi (Sabie River, South Africa) with no difference between the sexes. P. wesselsi was recognized as distinct from P. catostoma only recently.
# </figcaption>
# </figure>
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/weakly-electric-fish-Efields-locate-communicate.jpeg?raw=True' width="300" alt='eod e-field'/>

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Event detection](#one)
# - Time series analyses:
#     - [Part II. Rate](#two)
#     - [Part III. ISI](#three)
#     - [Part IV. Filtered](#four)
# - [Part V. Sampling Rate](#five)

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
# # Part I. Event Detection
# 
# Python has built-in algorithms for detecting "peaks" in a signal. However, it will detect *all* peaks. Therefore, the function takes in arguments that specify parameters for minimum height that can count as a peak and a minimum acceptible interval between independent peaks. 

# In[ ]:


...


# Once you know the times of each peak (each event), we can look at the waveforms of those events. To do this, we plot the peak of the signal at the event time and some duration before and after that peak.  

# In[ ]:


...


# There are a fundamental set of processing techniques we use to quantify event time series (such as spike from a neuron or EODs from a fish): rate, isi, filtered/smoothed.

# <a id="two"></a>
# # Part II. Rate

# ## Average rate
# 
# How would you calculate the average event rate?
# 
# <div class="alert-info">
# <b>Tip:</b>
#     <li> <b>len(variable)</b> : len() is a function used to get the number of elements in an array called *variable*</li>
#     <li> the time of the first and last event are simply the event times</li>
#     <li> <code class="lang-python">+ - * / </code> are the symbols for addition, subtraction, multiplication, and division</li>
#     <li><b>eod_times</b> is a variable that contains the list of EOD times</li>
# </div>
# 
# In the code cell below, write code that would calculate the average EOD rate in your recording

# In[ ]:


...


# ## Subsampling (*bootstrapping*) the average rate
# 
# In order to do statistics and compare EOD rates between different conditions or groups (for example, among different species of fish), we need more than just one estimate of the EOD rate. 
# 
# *bootstrapping* is an analytic technique used to *subsample* your data. In this case, we will calculate a set of EOD rate averages. Then we can get the mean and standard deviation of the average EOD rate. A *subsample* of the data is a smaller continuous section of the data. 
# 
# You can control the number of subsampled sets and the duration of each set. 
# The script (hidden) in the code cell below randomly selects samples of the specified duration from throughout the total recording. It repeats this random selection process ***n*** times. 
# 
# Once you specify the bootstrapping parameters in the form below, run the code cell. You will see a plot of the average rate of each subsample (each black point in the scatterplot), the average value across the set of subsamples (green star symbol), and the standard deviation (green bar).

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


...


# In[ ]:


#@markdown Run this code cell to calculate the average isi and plot the isi over time. { display-mode: "form" }

print(f'Average isi is {np.mean(isi):0.2f}.')

# plot the isi at each EOD time.
fig = go.Figure()
fig.add_trace(go.Scatter(x=eod_times[1:], y=isi, mode='markers',name='isi',marker_size=1,line_color='black'))

fig.update_layout(scene = dict(
        xaxis = dict(title = 'EOD times'),
        yaxis = dict(title = 'isi'),
    width=600, height = 600)
    
fig.show()


# <a id="four"></a>
# # Part IV. Filtered
# 
# By *convolving* a waveform with a time series, each event is transformed into a waveform. When all of these event waveforms are added together, you get a continuous signal instead of a discrete time series. This transformation is sometimes called "smoothing" and is required before some calculations can be made (such as correlation analysis). 

# In[ ]:


...


# <a id="five"></a>
# # Part V. Sampling Rate
# 
# In terms of electrophysiology data acquisition, sampling rate is the rate at which analog signals in the world are digitized and sent to the computer. The sampling rate that you choose impacts the size of data files as well as the resolution of the digitized signal. 

# In[ ]:


...


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:




