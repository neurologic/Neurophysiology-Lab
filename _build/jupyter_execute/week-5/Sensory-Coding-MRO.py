#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-6/Motor-Nerve.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Sensory Coding - MROs
# 
# There are two MROs innervating the deep flexor muscles, which can be distinguished based on spike height and shape. 
# 
# What are the dynamic properties of sensory responses (tonic, phasic, tonic/phasic)?
# How are sensory responses effected by anaesthetics (why would this be useful)?
# 

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Process Data](#one)
# - [Part II. Sensory Neuron Activity](#two)
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
from scipy import ndimage, optimize
from scipy.signal import hilbert,medfilt,resample, find_peaks
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

from ipywidgets import interactive, HBox, VBox, widgets, interact

def monoExp(x, m, t, b):
    return m * np.exp(-x / t) + b

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
filepath = "/Users/kperks/mnt/OneDrive - wesleyan.edu/Teaching/Neurophysiology_FA22/data/20220609/MRO2022-06-09T12_59_19.bin"
#@markdown Specify the sampling rate and number of channels recorded.

sampling_rate = None #@param
number_channels = None #@param
channel_to_process = 0 #@param

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
data = data.reshape(-1,number_channels)
data = data-data[0,:] # only do this offset adjustment for motor nerve recordings

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

if len(np.shape(data))>1:
    channel = channel_to_process
    channel_signal = data[:,channel]
if len(np.shape(data))==1:
    channel_signal = data

print('Now be a bit patient while it plots.')

f = go.FigureWidget(make_subplots(rows=1, cols=1, shared_xaxes= True)) #,layout=go.Layout(height=500, width=800))
f.add_trace(go.Scatter(x = time[0:fs], y = channel_signal[0:fs],
                             opacity=1),row=1,col=1)

f.update_layout(height=600, width=800,
                showlegend=False,
               xaxis_title="time(seconds)", 
                  yaxis_title='voltage')

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
        f.data[0].y = channel_signal[starti:stopi]

vb = VBox((f, interactive(response, x=slider)))
vb.layout.align_items = 'center'
vb


# <a id="one"></a>
# # Part I. Process Data
# 
# [toc](#toc)
# 
# Decide what portion of the raw data you want to analyze (maybe your data file contains multiple conditions, maybe there was some bad noise during part of your recording, or the nerve was lost before the end of the recording, or you accidentally forgot to stop the recording, etc...). 
# 
# If you want to analyze spiking activity (calculating rate, for example), you could look through your raw data and write down each time you see a spike. 
# 
# There are lots of computational tools for automating this process. Computers can also help you extract patterns from large amounts of data (for example different "classes" of spike waveform). In neuroscience research, the process of clustering spiking events based on their amplitude and waveform is termed the "spike sorting."
# 
# For this dataset, you will proocess the data using the following sequence of steps:
# <ol>
#     <li><a href='#select-data'>Select Data</a></li>
#     <li><a href='#detect-spikes'>Detect Peaks</a></li>
#     <li><a href='#cluster-events'>Cluster Events</a></li>
#     <li><a href='#display-clusters'>Visualize</a> (and <a href='#merge-clusters'>Merge</a> clusters if needed)</li>
#     <li><a href='#raw-cluster-scatter'>Check event-category identity with raw data</a></li>
#     </ol>

# <a id='select-data'></a>
# 
# 1. Specify the timerange for the data you want to analyze.

# In[ ]:


#@title { display-mode: "form" }

#@markdown Type in the start and stop time (in seconds) 
#@markdown that specifies the section of your recording you want to focus on for analysis.
start_time =   None #@param {type: "number"}
stop_time = None  #@param {type: "number"}

start_time =   0 #@param {type: "number"}
stop_time = 153  #@param {type: "number"}


# <a id='detect-spikes'></a>
# 
# 2. Detect peaks in the signal
# 
# First, in the code cell below, write a simple script that:
# - calculates the standard deviation of voltage in the raw signal using the ```np.std()``` module to store the result as a variable called "<b>SD</b>". 
# - uses the ```print()``` function to print the value stored in the variable ```SD``` as an output of the code cell. 
# - calculates the value equal to 5 times the standard deviation and stores the result as a variable called "<b>threshold</b>". 
# - uses the ```print()``` function to print the value stored in the variable ```threshold``` as an output of the code cell. 

# In[ ]:


...


# Then use the result to determine a spike detection threshold used by the ```find peaks``` algorithm in the following code cell

# In[ ]:


#@title { display-mode: "form" }

#@markdown Type in the threshold amplitude for event detection determined by your SD calculations.
spike_detection_threshold = None  #@param {type: "number"}
spike_detection_threshold = 0.1  #@param {type: "number"}
#@markdown Then from the dropdown, select a polarity (whether peaks are up or down)
peaks = "select peak direction"  #@param ['select peak direction','up', 'down']
peaks = "up"  #@param ['select peak direction','up', 'down']
#@markdown Finally, run this cell to set these values and plot a histogram of peak amplitudes.


if peaks=='up': polarity = 1
if peaks=='down': polarity=-1

min_isi = 0.001 #seconds

peaks,props = find_peaks(polarity * channel_signal,height=spike_detection_threshold, 
                         prominence = spike_detection_threshold, distance=int(min_isi*fs))
peaks_t = peaks/fs
inwin_inds = ((peaks_t>start_time) & (peaks_t<stop_time))
df_props = pd.DataFrame({
        'height': props['peak_heights'][inwin_inds],
        'spikeT' : peaks_t[inwin_inds],
        'spikeInd' : peaks[inwin_inds]
            })

bins = np.linspace(0,np.abs(np.max(polarity*channel_signal)),200)
n,_ = np.histogram(df_props['height'],bins = bins) # calculate the histogram
hfig,ax = plt.subplots(1)
ax.step(bins[1:],n,color='black')
ax.set_ylabel('count',fontsize=14)
ax.set_xlabel('amplitude',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

windur = 0.003
winsamp = int(windur*fs)
spkarray = []
for i in df_props['spikeInd'].values:
    spkarray.append(channel_signal[i-winsamp : i+winsamp+1])

df = pd.DataFrame(np.asarray(spkarray).T)
df_norm =(df - df.mean()) / df.std() # normalize for pca

n_components=5 #df.shape[0] 
pca = PCA(n_components=n_components)
pca.fit(df_norm)
df_pca = pd.DataFrame(pca.transform(df), columns=['PC%i' % i for i in range(n_components)], index=df.index)
print('You detected %i events above threshold.' %len(df.columns))

loadings = pd.DataFrame(pca.components_.T, columns=df_pca.columns, index=df.columns)
df_data = loadings.join(df_props['height'])

hfig,ax = plt.subplots(1)
ax.set_xlabel('event time (sec)',fontsize=14)
ax.set_ylabel('amplitude (volts)',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax.set_ylim(0,np.abs(np.max(polarity*channel_signal)))
ax.scatter(df_props['spikeT'],df_props['height'],color='black')

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id = "cluster-events"></a>
# 
# 3. Cluster events
# 
# The histogram plot produced in the last step can give you a sense for how many distinct neurons might be in your recording. The scatter plot of peak amplitude across time can give you a sense for how stable the recording was. If you had good recording stability, you can cluster spike events categorically to analyze the activity of individual neurons independently. 
# 
# If your recording is not stable, or is too noisy, then you may not be able to distinguish cell types. In this case, your *number of clusters* should be one. 
# 
# We can cluster events based on peak height and waveform shape using ["Kmeans"](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) clustering. 
# This will provide us with "putative single units" for further analysis.

# In[ ]:


#@title Cluster Detected Events { display-mode: "form" }

#@markdown Choose the number of clusters you want to split the event-based data into and type that number below. <br>
#@markdown >Note: It can sometimes help to "over-split" the events into more clusters 
#@markdown than you think will be necessary. You can try both strategies and assess the results.
number_of_clusters = None #@param {type: "number"}
number_of_clusters = 1
#@markdown Then run this cell to run the Kmeans algorithm. 

# No need to edit below this line
#################################

kmeans = KMeans(n_clusters=number_of_clusters).fit(df_data)
# df_props['peaks_t'] = peaks_t
df_props['cluster'] = kmeans.labels_


# <a id = "display-clusters"></a>
# 
# 4. Visualize (and Merge Clusters if needed)
# 
# Now that the events are clustered, you can visualize the mean spike waveform associated with each cluster (putative motor neuron).

# In[ ]:


#@title {display-mode:'form'}

#@markdown Run this cell to display the mean (and std) waveform for each cluster.

windur = 0.003 #@param
winsamps = int(windur * fs)
x = np.linspace(-windur,windur,winsamps*2)*1000
hfig,ax = plt.subplots(1,figsize=(8,6))
ax.set_ylabel('Volts recorded',fontsize=14)
ax.set_xlabel('milliseconds',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

for k in np.unique(df_props['cluster']):
    spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values #['peaks_t'].values
    spkt = spkt[(spkt>windur) & (spkt<(len(channel_signal)/fs)-windur)]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([channel_signal[(int(t*fs)-winsamps):(int(t*fs)+winsamps)] for t in spkt])
    wav_u = np.mean(spkwav,0)
    wav_std = np.std(spkwav,0)
    ax.plot(x,wav_u,linewidth = 3,label='cluster '+ str(k),color=pal[k])
    ax.fill_between(x, wav_u-wav_std, wav_u+wav_std, alpha = 0.25,color=pal[k])
plt.legend(bbox_to_anchor=[1.25,1],fontsize=14);

print('Tasks completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id='merge-clusters'></a>
# 
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
# 5. Check event-category identity with raw data.
# 
# Once you are happy with the clustering results based on the waveform shapes, check back with the raw data. 

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run this cell to overlay spike times by cluster identity on the raw signal

f = go.FigureWidget()
f.add_trace(go.Scatter(x = time[0:fs], y = channel_signal[0:fs],
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
        f.data[0].y = channel_signal[starti:stopi]
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
# # Part II. Sensory Neuron activity
# 
# [toc](#toc)
# 
# How do MRO receptor neurons respond and encode muscle stretch? How do different MRO receptor neuron types differ in their activity? You can explore the answers to these questions using your data and simple analysis of spike rate and spike rate decay. 

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run this code cell to plot: 1) a histogram of inter-spike-interval (ISI; the time between spikes)
#@markdown and 2) a scatter of ISI across time for individual clusters.

#@markdown <br> Once you run this code cell a first time, you will be able to select different clusters from the dropdown menu to change the plot data accordingly.


k = df_props['cluster'][0] #seed it to start

f = go.FigureWidget(make_subplots(rows=1,cols=1))

# bins = np.arange(0,0.202,0.002)
spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
# n,_ = np.histogram(np.diff(spkt),bins)

# f.add_trace(go.Scatter(x = bins[1:], y = n/sum(n), line_color = 'black'),row=1,col=1)

isi = np.diff(spkt)
f.add_trace(go.Scatter(x = spkt[1:], y = isi, line_color = 'black', mode='markers'),row=1,col=1)

    
f.update_layout(height=600, width=800,
                showlegend=False,
                xaxis_title="isi (seconds)",
                  yaxis_title='isi (seconds)')

cluster_select = widgets.Dropdown(
    options=np.unique(df_props['cluster']),
    value=k,
    description='Cluster ID:',
    disabled=False,
    )


# our function that will modify the xaxis range
def response(k):
    with f.batch_update():
        spkt = df_props.loc[df_props['cluster']==k]['spikeT'].values
        # n,_ = np.histogram(np.diff(spkt),bins)
        isi = np.diff(spkt)

        # f.data[0].x = bins[1:]
        # f.data[0].y = n/sum(n)
        
        f.data[0].x = spkt[1:]
        f.data[0].y = isi


vb = VBox((f, interactive(response, k=cluster_select)))
vb.layout.align_items = 'center'
vb


# Determine peak response times for each *trial*. 
# 
# The next code cell will take those trial times and overlay a plot of isi for each trial. The amount of data plotted before and after the trial time are *hard-coded* (determined based on the lab protocol). 

# In[ ]:


trials = [6.345,13.836,21.63,32.635,40.319]
plt.figure()
win = 10
for t in trials:
    ti = np.argmin(np.abs(spkt-t))
    sweep = spkt[(spkt>spkt[ti]-10) & (spkt<spkt[ti]+10)]-spkt[ti]
    sweep_rate = 1/np.diff(sweep)
    
    plt.plot(sweep[1:],sweep_rate)
    


# In[ ]:





# In[ ]:


trials = [94.692,103.73,111.665,120.871,129.286]
plt.figure()
win = 10
for t in trials:
    ti = np.argmin(np.abs(spkt-t))
    sweep = spkt[(spkt>spkt[ti]-10) & (spkt<spkt[ti]+10)]-spkt[ti]
    sweep_rate = 1/np.diff(sweep)
    
    plt.plot(sweep[1:],sweep_rate)


# In[ ]:


trials = [99.832,110,118.327,126.86]
plt.figure()
win = 10
for t in trials:
    ti = np.argmin(np.abs(spkt-t))
    sweep = spkt[(spkt>spkt[ti]-10) & (spkt<spkt[ti]+10)]-spkt[ti]
    sweep_rate = 1/np.diff(sweep)
    
    plt.plot(sweep[1:],sweep_rate)


# Data fitting software will report something like y = a + bemx, where τ is −1/m.
# 
# Data are fit with exponential equations, Rt = R∞ + R0e−t/τ, where Rt is the firing rate at time t, R∞ is the calculated firing rate if this degree of stretch were maintained infinitely, R∞ + R0 is the calculated “initial” peak firing rate at time 0, and τ is the adaptation rate. Thus the inverse of the exponent is the adaptation rate.

# Choose a single trial. Specify trial onset (peak of response) and the duration of the trial (end of the smooth curve).

# In[ ]:


t = 99.832 #@param
trial_dur = 3 #@param
p0 = (1, 1, 10) #@param # start with values near those we expect


ti = np.argmin(np.abs(spkt-t))
xs = spkt[(spkt>=spkt[ti]) & (spkt<spkt[ti]+trial_dur)]-spkt[ti]
ys = 1/np.diff(xs)
xs = xs[1:]

# perform the fit
p0 = (1, 1, 10) # start with values near those we expect
params_, cv = optimize.curve_fit(monoExp, xs, ys, p0)
m, t, b = params_
tauSec = (1 / t) 

# determine quality of the fit
squaredDiffs = np.square(ys - monoExp(xs, m, t, b))
squaredDiffsFromMean = np.square(ys - np.mean(ys))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
print(f"R² = {rSquared}")

# plot the results
plt.plot(xs, ys, '.', label="data")
plt.plot(xs, monoExp(xs, m, t, b), '--', label="fitted")
plt.title("Fitted Exponential Curve")

# inspect the parameters
print(f"Y = {m} * e^(-t / {t}) + {b}")
print(f"Tau = {tauSec} s")


# Across multiple trials, get param distribution

# In[ ]:


# trials = [94.692,103.73,111.665,120.871,129.286]
trials = [6.345,13.836,21.63,32.635,40.319]
trial_dur = 3
    
# plt.figure()
params = []
for t in trials:
    ti = np.argmin(np.abs(spkt-t))
    xs = spkt[(spkt>=spkt[ti]) & (spkt<spkt[ti]+trial_dur)]-spkt[ti]
    ys = 1/np.diff(xs)
    xs = xs[1:]
    
    params_, cv = optimize.curve_fit(monoExp, xs, ys, p0)
    m, t, b = params_
    
    squaredDiffs = np.square(ys - monoExp(xs, m, t, b))
    squaredDiffsFromMean = np.square(ys - np.mean(ys))
    rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
    params_ = np.concatenate([params_, [rSquared]])
    
    params.extend(params_)

fit_parameters = np.asarray(params).reshape(-1,4)

u_fit = np.mean(fit_parameters,0)
std_fit = np.std(fit_parameters,0)

print('mean fit parameters: ')
print(u_fit)
print('')
print('standard deviation fit parameters: ')
print(std_fit)
print('')
# inspect the results
print('results based on mean across trials:')
print(f"R² = {u_fit[3]}")
print(f"Y = {u_fit[0]} * e^(-x / {u_fit[1]}) + {u_fit[2]}")
print(f"Tau = {1/u_fit[1]} s")


# Use the mean parameters to plot the model equations.
# For multiple conditions, list multiple values for each parameter.

# In[ ]:


m = [7.5,10] #@param
t = [0.54,0.6] #@param
b = [14,9.3] #@param
trial_dur = 15

x_ = np.linspace(0,trial_dur,trial_dur*100)

for m_,t_,b_ in zip(m,t,b):
    y_ = monoExp(x_, m_,t_,b_)
    plt.plot(x_,y_)


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
