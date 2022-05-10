#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-6/Motor-Nerve.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Motor Neuron Types
# 
# The superficial flexor muscle of the crayfish is innervated by a small number of motor neurons. Because each motor neuron has a different axon diameter, you can tell them apart in your recording. 
# 

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Process Data](#one)
# - [Part II. Motor Neuron Activity](#two)
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
from scipy import ndimage
from scipy.signal import hilbert,medfilt,resample, find_peaks
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
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
filepath = '/Users/kperks/mnt/OneDrive - wesleyan.edu/Teaching/Neurophysiology_FA21/Data/CrayfishNerve3/nerve_Muscle_TelsonStim2021-07-16T14_34_57.bin'

#@markdown Specify the sampling rate and number of channels recorded.

sampling_rate = None #@param
number_channels = None #@param
muscle_channel = None #@param
nerve_channel = None #@param

downsample = False #@param
newfs = 2500 #@param

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
    # newfs = 2500 #downsample data
    chunksize = int(sampling_rate/newfs)
    if number_channels>1:
        data = data[0::chunksize,:]
    if number_channels==1:
        data = data[0::chunksize]
    fs = int(np.shape(data)[0]/dur)

time = np.linspace(0,dur,np.shape(data)[0])
pre = data[:,nerve_channel]
post = data[:,muscle_channel]

print('Now be a bit patient while it plots.')

f = go.FigureWidget(make_subplots(rows=2, cols=1, shared_xaxes= True)) #,layout=go.Layout(height=500, width=800))
f.add_trace(go.Scatter(x = time[0:fs], y = pre[0:fs],
                             name='pre synaptic',opacity=1),row=1,col=1)
f.add_trace(go.Scatter(x = time[0:fs], y = post[0:fs],
                             name='post synaptic',opacity=1),row=2,col=1)
f.update_layout(height=600, width=800,
                showlegend=False,
               xaxis2_title="time(seconds)", 
                  yaxis_title='pre-synaptic voltage', yaxis2_title='post-synaptic voltage')

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
        f.data[0].y = pre[starti:stopi]
        f.data[1].x = time[starti:stopi]
        f.data[1].y = post[starti:stopi]

vb = VBox((f, interactive(response, x=slider)))
vb.layout.align_items = 'center'
vb


# <a id="one"></a>
# # Part I. Process Data
# 
# [toc](#toc)

# In[ ]:


#@title { display-mode: "form" }

#@markdown Type in the start and stop time (in seconds) 
#@markdown that specifies the section of your recording you want to focus on for analysis.
start_time =   None #@param {type: "number"}
stop_time = None  #@param {type: "number"}
#@markdown Also type in an appropriate threshold amplitude for event detection.
threshold = None  #@param {type: "number"}
#@markdown Then from the dropdown, select a polarity (whether peaks are up or down)
peaks = "select peak direction"  #@param ['select peak direction','up', 'down']
#@markdown Finally, run this cell to set these values and plot a histogram of peak amplitudes.

spike_detection_threshold = threshold

if peaks=='up': polarity = 1
if peaks=='down': polarity=-1

min_isi = 0.001 #seconds

peaks,props = find_peaks(polarity * pre,height=spike_detection_threshold, 
                         prominence = spike_detection_threshold, distance=int(min_isi*fs))
peaks_t = peaks/fs
inwin_inds = ((peaks_t>start_time) & (peaks_t<stop_time))
df_props = pd.DataFrame({
        'height': props['peak_heights'][inwin_inds],
        'spikeT' : peaks_t[inwin_inds],
        'spikeInd' : peaks[inwin_inds]
            })

n,bins = np.histogram(df_props['height'],bins = 500) # calculate the histogram
bins = bins[1:]
hfig,ax = plt.subplots(1)
ax.step(bins,n,color='black')
ax.set_ylabel('count',fontsize=14)
ax.set_xlabel('amplitude',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

windur = 0.001
winsamp = int(windur*fs)
spkarray = []
for i in df_props['spikeInd'].values:
    spkarray.append(pre[i-winsamp : i+winsamp+1])

df = pd.DataFrame(np.asarray(spkarray).T)
df_norm =(df - df.mean()) / df.std() # normalize for pca

n_components=5 #df.shape[0] 
pca = PCA(n_components=n_components)
pca.fit(df_norm)
df_pca = pd.DataFrame(pca.transform(df), columns=['PC%i' % i for i in range(n_components)], index=df.index)
print('You detected %i events above threshold.' %len(df.columns))

loadings = pd.DataFrame(pca.components_.T, columns=df_pca.columns, index=df.columns)
df_data = loadings.join(df_props['height'])

# hfig,ax = plt.subplots(1)
# ax.set_xlabel('seconds')
# ax.set_ylabel('amplitude (a.u.)')
# ax.set_yticklabels([])
# for c in df_pca.columns[0:5]:
#     ax.plot(df_pca[c],label = c,alpha = 0.75)
# plt.legend(bbox_to_anchor=(1, 1));

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id = "cluster-events"></a>
# 
# The histogram plot can give you a sense for how many distinct motor neurons might be in your recording. 
# 
# We can cluster events based on peak height and waveform shape using ["Kmeans"](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) clustering. 
# This will provide us with "putative single units" for further analysis.

# In[ ]:


#@title Cluster Detected Events { display-mode: "form" }

#@markdown Choose the number of clusters you want to split the event-based data into and type that number below. <br>
#@markdown >Note: It can sometimes help to "over-split" the events into more clusters 
#@markdown than you think will be necessary. You can try both strategies and assess the results.
number_of_clusters = None #@param {type: "number"}
#@markdown Then run this cell to run the Kmeans algorithm. 

# No need to edit below this line
#################################

kmeans = KMeans(n_clusters=number_of_clusters).fit(df_data)
# df_props['peaks_t'] = peaks_t
df_props['cluster'] = kmeans.labels_


# <a id = "display-clusters"></a>
# 
# Now that the events are clustered, you can visualize the mean spike waveform associated with each cluster (putative motor neuron).

# In[ ]:


#@title {display-mode:'form'}

#@markdown Run this cell to display the mean (and std) waveform for each cluster.

windur = 0.001
winsamps = int(windur * fs)
x = np.linspace(-windur,windur,winsamps*2)*1000
hfig,ax = plt.subplots(1,figsize=(8,6))
ax.set_ylabel('Volts recorded',fontsize=14)
ax.set_xlabel('milliseconds',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

for k in np.unique(df_props['cluster']):
    spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values #['peaks_t'].values
    spkt = spkt[(spkt>windur) & (spkt<(len((pre)/fs)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([pre[(int(t*fs)-winsamps):(int(t*fs)+winsamps)] for t in spkt])
    wav_u = np.mean(spkwav,0)
    wav_std = np.std(spkwav,0)
    ax.plot(x,wav_u,linewidth = 3,label='cluster '+ str(k),color=pal[k])
    ax.fill_between(x, wav_u-wav_std, wav_u+wav_std, alpha = 0.25,color=pal[k])
plt.legend(bbox_to_anchor=[1.25,1],fontsize=14);

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id='merge-clusters'></a>
# If there are multiple spike clusters you want to merge into a single cell class, *edit and run* the cell below.
# 
# > **merge_cluster_list** = a list of the clusters (identified by numbers associated with the colors specified in the legend above).
#   - **For example**, the folowing list would merge clusters 0 and 2 together and 1, 4, and 3 together: <br>
#      **merge_cluster_list = [[0,2],[1,4,3]]**
#   - For each merge group, the first cluster number listed will be the re-asigned cluster number for that group (for example, in this case you would end up with a cluster number 0 and a cluster number 1). 
#   

# In[ ]:


#@title Merge Clusters { display-mode: "form" }

#@markdown ONLY USE THIS CODE CELL IF YOU WANT TO MERGE CLUSTERS. 
#@markdown OTHERWISE, MOVE ON. 
#@markdown <br> Below, create your list (of sublists) of clusters to merge.
#@markdown >Just leave out from the list any clusters that you want unmerged.
merge_cluster_list = [[0,3,4],[1,2]] #@param
#@markdown Then, run this cell to merge clusters as specified.

for k_group in merge_cluster_list:
    for k in k_group:
        df_props.loc[df_props['cluster']==k,'cluster'] = k_group[0]
print('you now have the following clusters: ' + str(np.unique(df_props['cluster'])))

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# After merging, return to the [display clusters](#display-clusters) code cell to plot the mean waveform of each new cluster (and determine if you need to [merge more](#merge-clusters)).

# <a id="raw-cluster-scatter"></a>
# 
# Once you are happy with the clustering results based on the waveform shapes, check back with the raw data. 

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run this cell to overlay spike times by cluster identity on the raw signal

f = go.FigureWidget()
f.add_trace(go.Scatter(x = time[0:fs], y = pre[0:fs],
                             name='pre synaptic',opacity=1,line_color='black'))
for k in np.unique(df_props['cluster']):
    start = 0 
    stop = 1
    inwin_inds = np.asarray([(df_props['spikeT'].values>start) & (df_props['spikeT'].values<stop)]).T
    df_ = df_props[inwin_inds]
    df_ = df_[df_['cluster']==k]
    
    f.add_trace(go.Scatter(x = df_['spikeT'], y = polarity*df_['height'],
                             line_color=pal[k],name=str(k) + ' times',mode='markers'))
    
f.update_layout(height=600, width=800,
               xaxis_title="time(seconds)", 
                  yaxis_title='amplitude (volts)')


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
        f.data[0].x = time[starti:stopi]
        f.data[0].y = pre[starti:stopi]
        for i,k in enumerate(np.unique(df_props['cluster'])):
            inwin_inds = np.asarray([(df_props['spikeT'].values>x[0]) & (df_props['spikeT'].values<x[1])]).T
            df_ = df_props[inwin_inds]
            df_ = df_[df_['cluster']==k]
            f.data[1+i].x = df_['spikeT']
            f.data[1+i].y = polarity*df_['height']

vb = VBox((f, interactive(response, x=slider)))
vb.layout.align_items = 'center'
vb


# If you think that two different spike waveforms are being lumped together, try going back to the [Kmeans clustering algorithm](#cluster-events) and increasing the cluster number constraint on the Kmeans algorithm - then [merge](#merge-clusters) as needed. 

# <a id="two"></a>
# # Part II. Motor Neuron activity
# 
# [toc](#toc)
# 
# How do different motor neuron types differ in their activity under different conditions?  

# In[ ]:





# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
