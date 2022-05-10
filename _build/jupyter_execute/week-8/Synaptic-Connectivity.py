#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/<'folder'/'notebookname'>.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Synaptic Connectivity
# 
# Arthropod muscle innervation is different from vertebrate muscle innervation in several interesting ways:
# <ul>
#     <li>Arthropod muscles are innervated by relatively few excitatory motor neurons (sometimes only one).</li>
#     <li>Arthropod motor neurons innervate each muscle fiber at multiple points (multiterminal innervation).</li>
#     <li>More than one motor neuron may innervate one muscle fiber (polyneuronal innervation).</li>
#     <li>Inhibitory motor neurons may innervate muscle fibers (and sometimes the terminals of the excitatory motor nerve endings).
#     <li>The tonic superficial flexor does not have “all-or-none” propagated action potentials, but instead has graded electrical responses dependent upon the level of the excitation and inhibition. The degree of depolarization determines the amount of Ca2+ that enters the cell through voltage-gated channels; the amount of Ca2+ entry in turn determines the strength of muscle contraction. Note: unlike the superficial flexor, fast phasic crayfish muscles may fire Ca2+-based action potentials.</li>
#     </ul>
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/fig.A.3-Comparison_with_Skeletal_Muscle.png?raw=True' width="600" alt='arthoropod versus vertebrate muscle innervation' align="center"/>
# 
# Therefore, arthropod skeletal muscle integration (innervation and summation) is actually more analagous to cortical dendritic integration in vertebrates. As in human brains, glutamate is an excitatory transmitter and GABA is an inhibitory transmitter. The multiterminal, polyneuronal, and inhibitory innervation of crustacean muscle, the use of glutamate and GABA as transmitters, and the extensive synaptic plasticity make the crayfish neuromuscular junction a good simplified model for the complex mix of synaptic interactions that occur in our own brains.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/fig.A.4-Comparison_with_Brain_Synapses.png?raw=True' width="600" alt='arthoropod versus vertebrate muscle innervation' align="center"/>
# 
# 
# <!-- <figure align="center">
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/fig.A.3-Comparison_with_Skeletal_Muscle.png?raw=True' width="300" alt='arthoropod versus vertebrate muscle innervation' align="center"/>
# <figcaption align = "center"><b>Electric organ discharge waveform</b> and sex, in three snoutfish species of southern Africa. All electric organ discharges represented as voltage over time, recorded in the field immediately after capture. Same time bar for all. (a) Sexual dimorphism in Marcusenius altisambesi with two distinct waveforms. (b) Sex difference of only a statistical nature in Petrocephalus catostoma (Upper Zambezi form) with, in most males, a stronger second positive phase than in females, such as shown here. (c) Petrocephalus wesselsi (Sabie River, South Africa) with no difference between the sexes. P. wesselsi was recognized as distinct from P. catostoma only recently.
# </figcaption>
# </figure> -->
# 
# <!-- <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/<'folder'/'notebookname'>.ipynb" target="_blank" rel="noopener noreferrer">Link to Other Notebooks (colab link)</a>    -->
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

# sampling_rate = NaN #@param
# number_channels = NaN #@param

sampling_rate = 30000
number_channels = 2
muscle_channel = 0
nerve_channel = 1

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
pre = data[:,nerve_channel]
post = data[:,muscle_channel]

print('Now be a bit patient while it plots.')

f = go.FigureWidget(make_subplots(rows=2, cols=1, shared_xaxes= True)) #,layout=go.Layout(height=500, width=800))
f.add_trace(go.Scatter(x = time[0:fs], y = pre[0:fs],
                             name='pre synaptic',opacity=1),row=1,col=1)
f.add_trace(go.Scatter(x = time[0:fs], y = post[0:fs],
                             name='post synaptic',opacity=1),row=2,col=1)
f.update_layout(height=600, width=800,
               xaxis2_title="time(seconds)", 
                  yaxis_title='amplitude (volts)', yaxis2_title='amplitude (volts)')

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
        f.data[1].x = time[starti:stopi]
        f.data[1].y = post[starti:stopi]

vb = VBox((f, interactive(response, x=slider)))
vb.layout.align_items = 'center'
vb

# print('Now be a bit patient while it plots.')
# fig = go.Figure()
# fig.add_trace(go.Scatter(x = time, y = data,line_color='black',name='channel 1'))
# fig.update_layout(xaxis_title="time(seconds)", yaxis_title='amplitude',width=800, height=500)
# fig.show()


# <a id="one"></a>
# # Part I. Process Data
# 
# [toc](#toc)

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

start_time =   0 #@param {type: "number"}
stop_time = 20  #@param {type: "number"}
#@markdown <b>TASK: </b> Type in an appropriate event threshold amplitude for detection.
threshold = 0.1  #@param {type: "number"}
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
peaks,props = find_peaks(polarity * pre,height=spike_detection_threshold, 
                         prominence = spike_detection_threshold, distance=int(min_isi*fs))
peaks_t = peaks/fs
inwin_inds = ((peaks_t>start_time) & (peaks_t<stop_time))
df_props = pd.DataFrame({
        'height': props['peak_heights'][inwin_inds],
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
    spkarray.append(pre[i-winsamp : i+winsamp+1])

df = pd.DataFrame(np.asarray(spkarray).T)
df_norm =(df - df.mean()) / df.std() # normalize for pca

n_components=5 #df.shape[0] 
pca = PCA(n_components=n_components)
pca.fit(df_norm)
df_pca = pd.DataFrame(pca.transform(df), columns=['PC%i' % i for i in range(n_components)], index=df.index)
print('You detected %i events above threshold.' %len(df.columns))
#print(You have transformed this dataset into %i principle components.' %(len(df.columns),n_components))

loadings = pd.DataFrame(pca.components_.T, columns=df_pca.columns, index=df.columns)
df_data = loadings.join(df_props['height'])

hfig,ax = plt.subplots(1)
ax.set_xlabel('seconds')
ax.set_ylabel('amplitude (a.u.)')
ax.set_yticklabels([])
for c in df_pca.columns[0:5]:
    ax.plot(df_pca[c],label = c,alpha = 0.75)
plt.legend(bbox_to_anchor=(1, 1));

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# In[ ]:


#@title Cluster Detected Events { display-mode: "form" }

#@markdown Let's start by clustering the events into putative motor units. { display-mode: "form" }
#@markdown Choose the number of clusters you want to split the data into and type that number below. <br>
#@markdown >Note: It can sometimes help to "over-split" the events into more clusters 
#@markdown than you think will be necessary. You can try both strategies and assess the results.
number_of_clusters = None #@param {type: "number"}
#@markdown RUN this cell to cluster events categorically based on waveform shape (in PC space) and amplitude. 
#@markdown <br>As a result, you will see a plot of the mean waveform from each cluster (with standard deviation shaded)

number_of_clusters = 7 #@param {type: "number"}

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
    spkt = spkt[(spkt>windur) & (spkt<(len((pre)/fs)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([pre[(int(t*fs)-winsamps):(int(t*fs)+winsamps)] for t in spkt])
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
merge_cluster_list = [[0,3,4],[1,2]] #@param
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
    spkt = spkt[(spkt>windur) & (spkt<(len((pre)/fs)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([pre[(int(t*fs)-winsamps):(int(t*fs)+winsamps)] for t in spkt])
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


# In[ ]:


#@title Overlay cluster identity on Raw signal {display-mode:"form"}


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


# <a id="two"></a>
# # Part II.
# 
# [toc](#toc)

# In[ ]:


#@title {display-mode:"form"}

windur = 0.1 #@param

# No need to edit below this line
#################################
winsamps = int(windur * fs)
x = np.linspace(0,windur,winsamps)*1000 #transform time to milliseconds
hfig,ax = plt.subplots(1)
ax.set_ylabel('amplitude (volts)')
ax.set_xlabel('milliseconds')
for k in np.unique(df_props['cluster']):
    spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
    spkt = spkt[(spkt<((len(post)/fs)-windur))]
    synwav = np.asarray([post[(int(t*sampling_rate)):(int(t*sampling_rate)+winsamps)] for t in spkt])
    wav_u = np.mean(synwav,0)
    wav_std = np.std(synwav,0)
    ax.plot(x,wav_u,linewidth = 3,color = pal[k])
    # ax.fill_between(x, wav_u-wav_std, wav_u+wav_std, alpha = 0.25, color = pal[k])


# In[ ]:


windur = 0.1 #@param

winoffset = 0.002 # in milliseconds
winsamps = int(windur * fs)
xtime = ((np.linspace(0,windur,winsamps))- winoffset)*1000 #subtract pre-spike offset

k = df_props['cluster'][0] #seed it to start

f = go.FigureWidget(make_subplots(rows=2,cols=1,shared_xaxes=True))

spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
spkt = spkt[(spkt>winoffset) & (spkt<(len(post)/fs)-windur)] - winoffset

spkt_ = spkt[random.sample(range(0,len(spkt)),np.min([10,len(spkt)]))]
    
spkwav = np.asarray([pre[(int(t*fs)):(int(t*fs)+winsamps)] - pre[int(t*fs)] for t in spkt_]).T
spk_u = np.mean(spkwav,1)
spk_std = np.std(spkwav,1)

for i in spkwav.T:
    f.add_trace(go.Scatter(x = xtime, y = i, opacity = 0.5,line_color = pal[k]),row=1,col=1);
f.add_trace(go.Scatter(x=xtime,y = spk_u,line_color = 'black'),row=1,col=1)

synwav = np.asarray([post[(int(t*fs)):(int(t*fs)+winsamps)] - post[int(t*fs)] for t in spkt_]).T
syn_u = np.mean(synwav,1)
syn_std = np.std(synwav,1)
for i in synwav.T:
    f.add_trace(go.Scatter(x = xtime, y = i, opacity = 0.5,line_color = pal[k]),row=2,col=1);
f.add_trace(go.Scatter(x=xtime,y = syn_u,line_color = 'black'),row=2,col=1)

    
f.update_layout(height=600, width=800,
               xaxis2_title="time(milliseconds)", 
                  yaxis_title='amplitude (volts)',yaxis2_title='amplitude (volts)')

cluster_select = widgets.Dropdown(b
    options=np.unique(df_props['cluster']),
    value=k,
    description='Cluster ID:',
    disabled=False,
    )


# our function that will modify the xaxis range
def response(k):
    with f.batch_update():
        spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
        spkt = spkt[(spkt>winoffset) & (spkt<(len(post)/fs)-windur)] - winoffset
        
        spkt_ = spkt[random.sample(range(0,len(spkt)),np.min([10,len(spkt)]))]
    
        spkwav = np.asarray([pre[(int(t*fs)):(int(t*fs)+winsamps)] - pre[int(t*fs)] for t in spkt_]).T
        spk_u = np.mean(spkwav,1)
        spk_std = np.std(spkwav,1)

        synwav = np.asarray([post[(int(t*fs)):(int(t*fs)+winsamps)] - post[int(t*fs)] for t in spkt_]).T
        syn_u = np.mean(synwav,1)
        syn_std = np.std(synwav,1)

        trace_ = 0

        for i in spkwav.T:
            f.data[trace_].y = i
            trace_+=1
        f.data[trace_].y = spk_u
        trace_+=1

        for i in synwav.T:
            f.data[trace_].y = i
            trace_+=1
        f.data[trace_].y = syn_u
        trace_+=1


vb = VBox((f, interactive(response, k=cluster_select)))
vb.layout.align_items = 'center'
vb


# plot individual events

# In[ ]:


windur = 0.1 #@param

winoffset = 2 # in milliseconds
winsamps = int(windur * fs)
xtime = ((np.linspace(0,windur,winsamps))*1000)- winoffset #subtract pre-spike offset

k = df_props['cluster'][0] #seed it to start

f = go.FigureWidget(make_subplots(rows=2,cols=1,shared_xaxes=True))

spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
spkt = spkt[(spkt>winoffset) & (spkt<(len(post)/fs)-windur)] - winoffset/1000

spkt_ = spkt[0]
    
spkwav = pre[(int(spkt_*fs)):(int(spkt_*fs)+winsamps)] - pre[int(spkt_*fs)]
f.add_trace(go.Scatter(x=xtime,y = spkwav,line_color = 'black'),row=1,col=1)

synwav = post[(int(spkt_*fs)):(int(spkt_*fs)+winsamps)] - post[int(spkt_*fs)]
f.add_trace(go.Scatter(x=xtime,y = synwav,line_color = 'black'),row=2,col=1)

f.update_layout(height=600, width=800,
                xaxis2_title="time(milliseconds)", 
                yaxis_title='amplitude (volts)',yaxis2_title='amplitude (volts)')

cluster_select = widgets.Dropdown(
    options=np.unique(df_props['cluster']),
    value=k,
    description='Cluster ID:',
    disabled=False,
)

event_select = widgets.IntSlider(
    value=0,
    min=0,
    max=len(spkt),
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)

# our function that will modify the xaxis range
def response(k,t):
    with f.batch_update():
        spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
        spkt = spkt[(spkt>winoffset) & (spkt<(len(post)/fs)-windur)] - winoffset/1000
        
        event_select.max=len(spkt)-1

        spkt_ = spkt[event_select.value] # shoulod be able to use "t"
        spkwav = pre[(int(spkt_*fs)):(int(spkt_*fs)+winsamps)] - pre[int(spkt_*fs)]
        synwav = post[(int(spkt_*fs)):(int(spkt_*fs)+winsamps)] - post[int(spkt_*fs)]
        
        f.data[0].y = spkwav
        f.data[1].y = synwav
        
        f.update_layout(yaxis1_range=[np.min(pre),np.max(pre)])


vb = VBox((f, interactive(response, k=cluster_select, t=event_select)))
vb.layout.align_items = 'center'
vb



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