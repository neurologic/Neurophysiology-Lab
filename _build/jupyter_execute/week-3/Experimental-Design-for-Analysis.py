#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-2/Experimental-Design-for-Analysis.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Experimental Design for Analysis
# 
# As you found in week 2 (<a href='https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-2/Electric-Organ-Discharge.ipynb' target="_blank" rel="noopener noreferrer">Dynamic Electrical Signals</a>), weakly electric fish vary their EOD rate over time. Is this variation random or is there non-random structure in it? If there is non-random structure, do the fish change their EOD rate in response to something in the environment or just spontaneously? How can you determine if a stimulus evokes a response? This notebook provides a tutorial on ways to approach this kind of analysis. We will not inclusively cover all possible approaches, but rather focus on basic principles of trial-based experimental design and the estimation of results under <i>null</i> hypotheses. After you complete your work, think about other questions that you are interested in and what kinds of experimental design considerations you would need to implement to analyze the data. 

# # Setup
# [toc](#toc)
# 

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Random or Non-Random?](#one)
# - [Part II. What's in a trial?](#two)
# - [Part III. Is it *real*?](#three)
# - [Part IV. Can you hear me now?](#four)
# - [Part V. ](#five)

# <a id="setup"></a>
# # Setup

# Import and define functions

# In[ ]:


#@title { display-mode: "form" }

#@markdown Run this code cell to import packages and define functions 
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


#@title { display-mode: "form" }

#@markdown Run this cell to mount your Google Drive. 

from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Import data digitized with *Nidaq USB6211* and recorded using *Bonsai-rx* as a *.bin* file

# In[ ]:


#@title { display-mode: "form" }

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
# # Part I. Random or Non-Random?
# 
# [toc](#toc)
# 
# We know that the EOD rate is variable (you measured this variability in week 2 [Dynamic Electrical Signals](../week-2/Electric-Organ-Discharge.ipynb)). Variability can be random or non-random. Are events distributed randomly in time or is there some <i>structure</i> to how events are generated?

# In[ ]:


...


# <a id="two"></a>
# # Part II. What's in a trial?
# 
# [toc](#toc)
# 
# A trial is generally defined as a portion of data (or behavior... or whatever...) that is defined by occuring at or starting at a particular moment in time and having a defined duration. A set of trials is often referred to as a *bout* if they happen contiguously. 
# 
# Practically, how do we define a trial? We need some temporal marker of the thing that we are analyzing a response to. In this case, is the fish responding to the EOD pulse of other fish? In that case, trials would be defined by the EOD times of other fish. Is the fish responding to the lights in the room turning on? In that case, trials would be defined by a transition in light switch state. Is the fish responding to our voice? ... we would need a microphone ...etc.
# 
# Trials don't have to be externally-imposed or experimentally-controlled. If we could track the position of the fish over time, then we could ask if the fish responded to being in a specific location in the tank. 
# 
# In this experiment, you presented an experimentally controlled stimulus to the fish (the dipole electric field). You recorded a copy of that stimulus command on channel 0 of your ADC. Therefore, we can use that channel to define trial start times. 
# 
# First, we need to determine when the stimulus occurred
# 
# Then, we need to determine the amplitude of the stimulus each time it was presented. 
# 
# We will end up with a table of of times corresponding to trials (rows) across stimulus amplitude (columns).

# In[ ]:


...


# <a id="three"></a>
# # Part III. Is it <i>real</i>?
# 
# [toc](#toc)
# 
# How can you tell if the response to a stimulus is 'real' or if the fish's EOD pattern resembled a response just by chance? We need to compare the trial-averaged response (and distribution of trial-averaged responses) to a <i>null</i> response distribution (this is the <i>null hypothesis</i>). 
# 
# One way that we can do this is by randomly marking "trials" for each stimulus condition distributed randomly throughout the recording time period. 
# 
# For simplicity, let's average all trials together for this first analysis. 

# In[ ]:


...


# <a id="four"></a>
# # Part IV. Can you hear me now?
# 
# [toc](#toc)
# 
# How strong does a stimulus need to be for the fish to detect it and respond to it? When a stimulus can be varied along a single parameter, we can test the response/detection threshold of an animal to that stimulus. The response/detection threshold is defined as the value of the stimulus parameter (for example amplitude or frequency) that the animal can detect or that it responds to. 

# In[ ]:


...


# To determine if a difference in response across stimulus amplitude is "real" we can do a "trial shuffle." Shuffling trials means that we use the SIU-determined stimulus times to segment the data, but randomly shuffle the identity of the stimulus amplitude on each trial. 

# In[ ]:


...


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
