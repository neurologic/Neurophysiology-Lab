#!/usr/bin/env python
# coding: utf-8

# <a id=intro></a>
# # Human Motor Neuron Activity
# 
# In vertebrates, every voltage spike in a motor neuron generates a voltage spike in the muscle fibers it innervates. A single motor neuron and the muscle fibers it innervates are called a *motor unit*. In humans, the only single-unit neural activity that we can measure non-invasively is from motor neurons. We measure motor neuron activity via muscle voltage spikes. Muscle voltage spikes can be measured by electrodes placed on the surface of the skin overlying the muscle. 
# 
# You will acquire electromyograms using differential surface electrodes above the *belly* of several dorsal interossei muscles. These muscles (along with palmar interossei) move fingers side to side.  
# - first dorsal (medial to the index finger)
# - abductor digiti minimi (lateral to the pinky finger)
# - third dorsal (lateral to the middle finger) (you could also try second dorsal medial to the middle finger)
# 
# First, you will try to isolate the smallest motor units from each of the interossei muscles.
# Then, you will put the muscle under load and analyze concentric and eccentric contraction 

# <a id=toc></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Load data](#one)
# - [Part II. Process the data](#two)
# - [Part III. Sort detected events](#three)
# - [Part IV. Analyze motor unit activity](#four)

# <a id=setup></a>
# # Setup

# In[ ]:


#@markdown <b>TASK: </b> RUN this cell to set up the notebook (import packages, etc) { display-mode: "form" }
# In Python, anything with a "#" in front of it is code annotation,
# and is not read by the computer.
# You can run a cell (this box) by pressing ctrl-enter or shift-enter.
# You can also run a cell by clicking the play button in the menu bar 
# at the top of the page (single right arrow, not double).
# Click in this cell and then press shift and enter simultaneously.
# This print function below allows us to generate a message.
print('Nice work!')

# No need to edit anything in this code cell
#################################
from google.colab import files
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
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# In[ ]:


#@markdown <b>TASK: </b> RUN this cell to mount your Google Drive. { display-mode: "form" }
#@markdown > Follow all instructions as prompted by pop-ups.
from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id=one></a>
# # Part I. Load data

# In[ ]:


#@markdown Specify the file path { display-mode: "form" }
#@markdown to your recorded data on Drive:
#@markdown > Also specify the sampling rate and number of channels recorded.
filepath = "full filepath goes here"  #@param 

#@markdown After you have copied/typed in a filepath and specified the metadata, 
#@markdown run this code cell to load the EMG data. 

sampling_rate = NaN #@param
number_channels = NaN #@param

filepath = Path(filepath)

# No need to edit below this line
#################################
emg = np.fromfile(Path(filepath), dtype = np.float64)
emg = emg.reshape(-1,number_channels)
dur = np.shape(emg)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %dur)
newfs = 2500 #downsample emg data
chunksize = int(sampling_rate/newfs)
emg = emg[0::chunksize,:]
newfs = np.shape(emg)[0]/dur

time = np.linspace(0,np.shape(emg)[0]/newfs,np.shape(emg)[0])


print('Data upload completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))

print('Now be a bit patient while it plots.')
fig = go.Figure()
fig.add_trace(go.Scatter(x = time, y = emg,line_color='black',name='emg0'))
fig.update_layout(xaxis_title="time(seconds)", yaxis_title='amplitude',width=800, height=500)


# <a id=two></a>
# # Part II. Process the data
# 
# You need to set a detection threshold that will be used to detect electrical events produced by motor units in the interossei muscle.

# In[ ]:


#@markdown <b>TASK: </b> Type in the start and stop time (in seconds) { display-mode: "form" }
#@markdown that you want to focus on in the recording.
start_time =   None#@param {type: "number"}
stop_time = None  #@param {type: "number"}
#@markdown <b>TASK: </b> Type in an appropriate event threshold amplitude for detection.
threshold = None  #@param {type: "number"}
#@markdown <b>TASK: </b> Then from the dropdown, select a polarity (whether peaks are up or down)
peaks = "up"  #@param ['select peak direction','up', 'down']
#@markdown <b>TASK: </b> Finally, RUN this cell to set these values.
spike_detection_threshold = threshold
if peaks=='up': polarity = 1
if peaks=='down': polarity=-1

#@markdown After the values are set, the emg signal will be processed to detect events (peaks).
#@markdown "PCA" (principle component analysis) will be applied to determine  
#@markdown the fundamental waveform shapes across all events.
#@markdown <br> You will see a histogram of event peak amplitudes 
#@markdown as well as a plot of waveform PCs (principle components).
min_isi = 0.0035 #seconds

# samples_inwin = samples[int(start_time/sample_rate):int(stop_time/sample_rate)]
peaks,props = find_peaks(polarity * samples,height=spike_detection_threshold, 
                         prominence = spike_detection_threshold, distance=(min_isi*sample_rate))
peaks_t = peaks/sample_rate
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

windur = 0.005
winsamp = int(windur*sample_rate)
spkarray = []
for i in df_props['spikeInd'].values:
    spkarray.append(samples[i-winsamp : i+winsamp+1])

df = pd.DataFrame(np.asarray(spkarray).T)
df_norm =(df - df.mean()) / df.std() # normalize for pca

n_components=df.shape[1] 
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
for c in df_pca.columns:
    ax.plot(df_pca[c],label = c,alpha = 0.75)
plt.legend(bbox_to_anchor=(1, 1));

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id=three></a>
# # Part III. Sort detected events
# 
# Based on PC "loadings" and waveform height, we should be able to tell that there are distinct categories of events - each generated by a different motor unit. 
# "Kmeans" is an algorithm built to automatically assign events to "clusters" based on similarity to each other and dissimilarity from other clusters. 

# In[ ]:


#@markdown Let's start by clustering the events into putative motor units. { display-mode: "form" }
#@markdown Choose the number of clusters you want to split the data into and type that number below. <br>
#@markdown >Note: It can sometimes help to "over-split" the events into more clusters 
#@markdown than you think will be necessary. You can try both strategies and assess the results.
number_of_clusters = None #@param {type: "number"}
#@markdown RUN this cell to cluster events categorically based on waveform shape (in PC space) and amplitude. 
#@markdown <br>As a result, you will see a plot of the mean waveform from each cluster (with standard deviation shaded)

# No need to edit below this line
#################################

kmeans = KMeans(n_clusters=number_of_clusters).fit(df_data)
# df_props['peaks_t'] = peaks_t
df_props['cluster'] = kmeans.labels_

winsamps = int(windur * sample_rate)
x = np.linspace(-windur,windur,winsamps*2)*1000
hfig,ax = plt.subplots(1,figsize=(10,8))
ax.set_ylabel('Volts recorded')
ax.set_xlabel('milliseconds')

# fig = go.Figure()

for k in np.unique(df_props['cluster']):
    spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values #['peaks_t'].values
    spkt = spkt[(spkt>windur) & (spkt<(len((samples)/sample_rate)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([samples[(int(t*sample_rate)-winsamps):(int(t*sample_rate)+winsamps)] for t in spkt])
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


#@markdown ONLY DO THIS TASK IF YOU WANT TO MERGE CLUSTERS. { display-mode: "form" }
#@markdown OTHERWISE, MOVE ON. 
#@markdown <br> Below, create your list (of sublists) of clusters to merge.
#@markdown >Just leave out from the list any clusters that you want unmerged.
merge_cluster_list = [[0,4,5],[1,3]] #@param
#@markdown Then, RUN the cell to merge clusters as specified.

for k_group in merge_cluster_list:
    for k in k_group:
        df_props.loc[df_props['cluster']==k,'cluster'] = k_group[0]
print('you now have the following clusters: ' + str(np.unique(df_props['cluster'])))

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# In[ ]:


#@markdown Now, RUN this cell to plot the average waveform for your new clusters. { display-mode: "form" }
##@markdown And to plot a color-coded scatter of each detected and categorized emg event.
winsamps = int(windur * sample_rate)
x = np.linspace(-windur,windur,winsamps*2)*1000
hfig,ax = plt.subplots(1,figsize=(8,6))
ax.set_ylabel('amplitude')
ax.set_xlabel('milliseconds')

# fig = go.Figure()

for k in np.unique(df_props['cluster']):
    spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
    spkt = spkt[(spkt>windur) & (spkt<(len((samples)/sample_rate)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([samples[(int(t*sample_rate)-winsamps):(int(t*sample_rate)+winsamps)] for t in spkt])
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


# <a id=four></a>
# # Part IV. Analyze motor unit activity

# In[ ]:


#@markdown <b>TASK: </b> If you are satisfied with your clustering, { display-mode: "form" }
#@markdown RUN this cell to plot: 

#@markdown 1) a scatter of event times overlaid on the raw emg signal 

#@markdown 2) a scatter of instantaneous spike rate for each cluster. 

fig = make_subplots(rows=2, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.02)


fig.add_trace(go.Scatter(x = xtime, y = samples,line_color='black',name='raw emg'),
             row=1,col=1)
for k in np.unique(df_props['cluster']):
    df_ = df_props[df_props['cluster']==k]
    
    fig.add_trace(go.Scatter(x = df_['spikeT'], y = polarity*df_['height'],
                             line_color=pal[k],name=str(k),mode='markers'),row=1,col=1)
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





# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.
