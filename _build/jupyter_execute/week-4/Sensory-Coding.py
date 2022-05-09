#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-3/Sensory-Coding.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Sensory Coding: Cockroach mechanoreceptors
# 
# Cockroach mechanoreceptor response properties. 
# 
# Cluster-based rate analysis of potential multi-unit activity.
# 
# Trial-averaged spiking responses. 
# 
# <!-- <figure align="center">
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/example-eods_Kramer.jpeg?raw=True' width="300" alt='eod e-field' align="center"/>
# <figcaption align = "center"><b>Electric organ discharge waveform</b> and sex, in three snoutfish species of southern Africa. All electric organ discharges represented as voltage over time, recorded in the field immediately after capture. Same time bar for all. (a) Sexual dimorphism in Marcusenius altisambesi with two distinct waveforms. (b) Sex difference of only a statistical nature in Petrocephalus catostoma (Upper Zambezi form) with, in most males, a stronger second positive phase than in females, such as shown here. (c) Petrocephalus wesselsi (Sabie River, South Africa) with no difference between the sexes. P. wesselsi was recognized as distinct from P. catostoma only recently.
# </figcaption>
# </figure> -->
# 
# 

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Load Data](#one)
# - [Part II. Event Detection](#two)
# - [Part III. Event Clustering](#three)
# - [Part IV. Clustered events and instantaneous rate](#four)
# - [Part V. Trial-Averaged Analysis](#five)

# <a id="setup"></a>
# # Setup

# Import and define functions

# In[ ]:


#@title {display-mode: "form" }

#@markdown Run this code cell to import packages and define functions 
import numpy as np
import pandas as pd
from scipy import ndimage
from scipy.signal import find_peaks
from copy import deepcopy
import math
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from pathlib import Path
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import csv
from scipy.signal import hilbert,medfilt,resample
from sklearn.decomposition import PCA
import scipy
import seaborn as sns
from ipywidgets import interactive, HBox, VBox, widgets, interact

from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Mount Google Drive

# In[ ]:


#@title {display-mode: "form" }

#@markdown Run this cell to mount your Google Drive. 

from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# Import data digitized with *Nidaq USB6211* and recorded using *Bonsai-rx* as a *.bin* file

# <a id="one"></a>
# # Part I. Load Data

# In[ ]:


#@title {display-mode: "form" }

#@markdown Specify the file path 
#@markdown to your recorded data on Drive (find the filepath in the colab file manager:

filepath = "full filepath goes here"  #@param 
filepath = "/Users/kperks/mnt/OneDrive - wesleyan.edu/Teaching/Neurophysiology_FA21/Data/CockroachSensoryPhysiology/20211020_30k/allfeaturesonce_diffspikes_KP2021-10-20T15_18_21.bin"

#@markdown Specify the sampling rate and number of channels recorded.

# sampling_rate = NaN #@param
# number_channels = NaN #@param
sampling_rate = 30000 #@param
number_channels = 1 #@param

downsample = False #@param
newfs = 10000 #@param

#@markdown After you have filled out all form fields, 
#@markdown run this code cell to load the data. 

filepath = Path(filepath)

# No need to edit below this line
#################################
data = np.fromfile(Path(filepath), dtype = np.float64)
if number_channels>1:
    data = data.reshape(-1,number_channels)
data = data-np.median(data)
dur = np.shape(data)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %dur)

fs = sampling_rate
if downsample:
    newfs = 2500 #downsample emg data
    chunksize = int(sampling_rate/newfs)
    if number_channels>1:
        data = data[0::chunksize,:]
    if number_channels==1:
        data = data[0::chunksidze]
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


# <a id="two"></a>
# # Part II. Event Detection

# In[ ]:


#@title { display-mode: "form" }

#@markdown <b>TASK: </b> Type in the start and stop time (in seconds) 
#@markdown that you want to focus on in the recording.
# start_time =   None#@param {type: "number"}
# stop_time = None  #@param {type: "number"}
# #@markdown <b>TASK: </b> Type in an appropriate event threshold amplitude for detection.
# threshold = None  #@param {type: "number"}
# #@markdown <b>TASK: </b> Then from the dropdown, select a polarity (whether peaks are up or down)
# peaks = "up"  #@param ['select peak direction','up', 'down']
# #@markdown <b>TASK: </b> Finally, RUN this cell to set these values.

start_time =   42 #@param {type: "number"}
stop_time = 52  #@param {type: "number"}
#@markdown <b>TASK: </b> Type in an appropriate event threshold amplitude for detection.
threshold = 0.016  #@param {type: "number"}
#@markdown <b>TASK: </b> Then from the dropdown, select a polarity (whether peaks are up or down)
peaks = "down"  #@param ['select peak direction','up', 'down']
#@markdown <b>TASK: </b> Finally, RUN this cell to set these values.

spike_detection_threshold = threshold

if peaks=='up': polarity = 1
if peaks=='down': polarity=-1

#@markdown After the values are set, the emg signal will be processed to detect events (peaks).
#@markdown "PCA" (principle component analysis) will be applied to determine  
#@markdown the fundamental waveform shapes across all events.
#@markdown <br> You will see a histogram of event peak amplitudes 
#@markdown as well as a plot of waveform PCs (principle components).
min_isi = 0.001 #seconds

# samples_inwin = samples[int(start_time/sample_rate):int(stop_time/sample_rate)]
peaks,props = find_peaks(polarity * data,height=spike_detection_threshold, 
                         prominence = spike_detection_threshold,
                         distance=int(min_isi*fs))
peaks_t = peaks/fs
inwin_inds = ((peaks_t>start_time) & (peaks_t<stop_time))
df_props = pd.DataFrame({
        'height': props['peak_heights'][inwin_inds],
        'prominences': props['prominences'][inwin_inds],
        'spikeT' : peaks_t[inwin_inds],
        'spikeInd' : peaks[inwin_inds]
        # 'widths' : props['widths']/fs
            })
n,bins = np.histogram(df_props['height'],bins = 100) # calculate the histogram
bins = bins[1:]
hfig,ax = plt.subplots(1)
ax.step(bins,n)
ax.set_ylabel('count')
ax.set_xlabel('amplitude')

windur = 0.001
winsamp = int(windur*fs)
spkarray = []
for i in df_props['spikeInd'].values:
    spkarray.append(data[i-winsamp : i+winsamp+1])

df = pd.DataFrame(np.asarray(spkarray).T)
df_norm =(df - df.mean()) / df.std() # normalize for pca


# also use PCA to get waveform information
n_components=3 #df.shape[0] 
pca = PCA(n_components=n_components)
pca.fit(df_norm)
df_pca = pd.DataFrame(pca.transform(df), columns=['PC%i' % i for i in range(n_components)], index=df.index)
print('You detected %i events above threshold.' %len(df.columns))
#print(You have transformed this dataset into %i principle components.' %(len(df.columns),n_components))

loadings = pd.DataFrame(pca.components_.T, columns=df_pca.columns, index=df.columns)
df_data = loadings.join(df_props[['height','prominences']])
# df_data = df_props['height'] # try clustering only on spike height

# hfig,ax = plt.subplots(1)
# ax.set_xlabel('seconds')
# ax.set_ylabel('amplitude (a.u.)')
# # ax.set_yticklabels([])
# for c in df_pca.columns[0:5]:
#     ax.plot(df_pca[c],label = c,alpha = 0.75)
# plt.legend(bbox_to_anchor=(1, 1));

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id="three"></a>
# # Part III. Event Clustering

# In[ ]:


#@title { display-mode: "form" }

#@markdown Let's start by clustering the events into putative motor units. { display-mode: "form" }
#@markdown Choose the number of clusters you want to split the data into and type that number below. <br>
#@markdown >Note: It can sometimes help to "over-split" the events into more clusters 
#@markdown than you think will be necessary. You can try both strategies and assess the results.
number_of_clusters = None #@param {type: "number"}
#@markdown RUN this cell to cluster events categorically based on waveform shape (in PC space) and amplitude. 
#@markdown <br>As a result, you will see a plot of the mean waveform from each cluster (with standard deviation shaded)

number_of_clusters = 3 #@param {type: "number"}

# No need to edit below this line
#################################

kmeans = KMeans(n_clusters=number_of_clusters).fit(df_data)
# df_props['peaks_t'] = peaks_t
df_props['cluster'] = kmeans.labels_

winsamps = int(windur * fs)
x = np.linspace(-windur,windur,winsamps*2)*1000
hfig,ax = plt.subplots(1,figsize=(10,8))
ax.set_ylabel('Volts recorded')
ax.set_xlabel('milliseconds')

# fig = go.Figure()

for k in np.unique(df_props['cluster']):
    spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values #['peaks_t'].values
    spkt = spkt[(spkt>windur) & (spkt<(len((data)/fs)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([data[(int(t*fs)-winsamps):(int(t*fs)+winsamps)] for t in spkt])
    wav_u = np.mean(spkwav,0)
    wav_std = np.std(spkwav,0)
    # fig.add_trace(go.Scatter(x = x, y = wav_u,line_color=pal[k],name='cluster ' + str(k)),
    #          row=1,col=1)
    ax.plot(x,wav_u,linewidth = 3,label='cluster '+ str(k),color=pal[k])
    ax.fill_between(x, wav_u-wav_std, wav_u+wav_std, alpha = 0.25,color=pal[k])
# fig.update_layout(xaxis_title="time(seconds)", yaxis_title='amplitude',width=500, height=500)
plt.legend(bbox_to_anchor=[1.25,1]);

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# If there are multiple spike clusters you want to merge into a single cell class, *edit and run* the cell below.
# 
# > **merge_cluster_list** = a list of the clusters (identified by numbers associated with the colors specified in the legend above).
#   - **For example**, the folowing list would merge clusters 0 and 2 together and 1, 4, and 3 together: <br>
#      **merge_cluster_list = [[0,2],[1,4,3]]**
#   - For each merge group, the first cluster number listed will be the re-asigned cluster number for that group (for example, in this case you would end up with a cluster number 0 and a cluster number 1). 
#   

# In[ ]:


#@title { display-mode: "form" }

#@markdown ONLY DO THIS TASK IF YOU WANT TO MERGE CLUSTERS. { display-mode: "form" }
#@markdown OTHERWISE, MOVE ON. 
#@markdown <br> Below, create your list (of sublists) of clusters to merge.
#@markdown >Just leave out from the list any clusters that you want unmerged.
merge_cluster_list = [[0,1,2],[4,3]] #@param
#@markdown Then, RUN the cell to merge clusters as specified.

for k_group in merge_cluster_list:
    for k in k_group:
        df_props.loc[df_props['cluster']==k,'cluster'] = k_group[0]
print('you now have the following clusters: ' + str(np.unique(df_props['cluster'])))

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# In[ ]:


#@title { display-mode: "form" }

#@markdown Now, RUN this cell to plot the average waveform for your new clusters. { display-mode: "form" }
##@markdown And to plot a color-coded scatter of each detected and categorized emg event.
winsamps = int(windur * fs)
x = np.linspace(-windur,windur,winsamps*2)*1000
hfig,ax = plt.subplots(1,figsize=(8,6))
ax.set_ylabel('amplitude')
ax.set_xlabel('milliseconds')

# fig = go.Figure()

for k in np.unique(df_props['cluster']):
    spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
    spkt = spkt[(spkt>windur) & (spkt<(len((data)/fs)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([data[(int(t*fs)-winsamps):(int(t*fs)+winsamps)] for t in spkt])
    wav_u = np.mean(spkwav,0)
    wav_std = np.std(spkwav,0)
    # fig.add_trace(go.Scatter(x = x, y = wav_u,line_color=pal[k],name='cluster ' + str(k)),
    #          row=1,col=1)
    ax.plot(x,wav_u,linewidth = 3,label='cluster '+ str(k),color=pal[k])
    ax.fill_between(x, wav_u-wav_std, wav_u+wav_std, alpha = 0.25,color=pal[k])
# fig.update_layout(xaxis_title="time(seconds)", yaxis_title='amplitude',width=500, height=500)
plt.legend(bbox_to_anchor=[1.25,1]);

# fig = go.Figure()
# fig.add_trace(go.Scatter(x = xtime, y = samples,line_color='black',name='emg0'))
# for i,k in enumerate(np.unique(df_props['cluster'])):
#     df_ = df_props[df_props['cluster']==k]
#     fig.add_trace(go.Scatter(x = df_['peaks_t'], y = polarity*df_['height'],line_color=pal[k],name=str(k),mode='markers'))
# fig.update_layout(xaxis_title="time(seconds)", yaxis_title='amplitude',width=800, height=400)

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id="four"></a>
# # Part IV. Clusters and instantaneous rate

# In[ ]:


#@title { display-mode: "form" }

#@markdown <b>TASK: </b> If you are satisfied with your clustering, { display-mode: "form" }
#@markdown RUN this cell to plot: 

#@markdown 1) a scatter of event times overlaid on the raw emg signal 

#@markdown 2) a line plot of instantaneous spike rate for each cluster. 

fig = make_subplots(rows=2, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.02)

fig.add_trace(go.Scatter(x = time[int(start_time*fs):int(stop_time*fs)],
                         y = data[int(start_time*fs):int(stop_time*fs)],
                         line_color='black',name='raw emg'),
             row=1,col=1)
for k in np.unique(df_props['cluster']):
    df_ = df_props[df_props['cluster']==k]
    
    fig.add_trace(go.Scatter(x = df_['spikeT'], y = polarity*df_['height'],
                             line_color=pal[k],name=str(k) + ' times',mode='markers'),row=1,col=1)
    # fig.add_trace(go.Scatter(x = df_['peaks_t'], y = polarity*df_['height'],
    #                          line_color=pal[k],name=str(k),mode='markers'),row=1,col=1)


for k in np.unique(df_props['cluster']):
    df_ = df_props[df_props['cluster']==k]
    fig.add_trace(go.Scatter(x = df_['spikeT'][1:], y = 1/np.diff(df_['spikeT']),
                             line_color=pal[k],name='cluster ' + str(k) + ' rate',mode='markers'),
                 row=2,col=1)
    # fig.add_trace(go.Scatter(x = df_['peaks_t'][1:], y = 1/np.diff(df_['peaks_t']),
    #                          line_color=pal[k],name='cluster ' + str(k) + ' rate',mode='markers'),
    #              row=2,col=1)

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))
print('Now wait a moment while the plots render.')

fig.update_layout(xaxis2_title="time(seconds)", 
                  yaxis_title='amplitude (volts)', yaxis2_title='instantaneous spike rate',
                  width=800, height=500)




# In[ ]:


#@title {display-mode:"form"}

#@markdown Select a section of your recording to analyze.
#@markdown For example, you can focus on a baseline period, a stimulus period, or a combination.

start_time = 42 #@param

stop_time = 44 #@param

#@markdown Then run this code cell to assign that segment of data to the variable $$y$$

y = data[int(start_time*fs):int(stop_time*fs)]


# What is the standard deviation of your signal? What is the mean?
# Use the numpy "std" and "mean" methods to calculate them. 
# 
# Assign the standard deviation to the variable "SD"
# Assign the mean to the variable "M"
# 
# Note: the signal is stored in a variable called "y"

# In[ ]:


SD = np.std(y)

M = np.mean(y)


# In[ ]:


#@title {display-mode:"form"}

#@markdown Run this cell to plot a voltage histogram for your section of signal
#@markdown You can zoom in along the y-axis to see the distribution for more "rare" voltages.

n,bins = np.histogram(y,"fd")


fig = go.Figure()
fig.add_trace(go.Scatter(x = bins[1:], y = n/sum(n)))
# plt.plot(,)
fig.add_vline(x=SD, line_width=3, line_dash="dash", line_color="green")
fig.add_vline(x=-SD, line_width=3, line_dash="dash", line_color="green")
fig.add_vline(x=M, line_width=3, line_dash="dash", line_color="purple")
# plt.vlines(SD,0,np.max(n/sum(n)),color = 'purple')
# plt.vlines(-SD,0,np.max(n/sum(n)),color = 'purple')
# plt.vlines(M,0,np.max(n/sum(n)),color = 'green')
# plt.ylim(0,0.001)
fig.update_layout(xaxis_title="voltage", 
                  yaxis_title='fraction samples',
                  width=600, height=400)


# <a id="five"></a>
# # Part V. Trial-Averaged Analysis

# In[ ]:


#@title {display-mode:"form"}

#@markdown Determine trial times and a trial duration from your recording
#@markdown > cluster_id is a list that can contain more than one cluster (the spikes from the clusters will be considered together)

trial_times = [44.32,46.45,49.14]
cluster_id = [0,1,2]
trial_dur = 2
baseline_dur = 1
bin_width = 0.15

trials = []
for t in trial_times:
    df_ = df_props[df_props['cluster'].isin(cluster_id)]
    trial_ = df_["spikeT"].values- trial_times[0]
    trials.append(trial_[(trial_> -baseline_dur) & (trial_<trial_dur)])

trials = np.concatenate(trials)

edges = np.concatenate([np.arange(-baseline_dur,0,bin_width),np.arange(0,trial_dur,bin_width)])
n,edges = np.histogram(trials,edges)

plt.scatter(edges[1:],n/bin_width)
plt.ylabel('spike rate')
plt.xlabel('time from trial onset')


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
