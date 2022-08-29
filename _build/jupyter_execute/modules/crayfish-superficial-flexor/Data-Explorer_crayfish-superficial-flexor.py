#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/crayfish-superficial-flexor/Data-Explorer_crayfish-superficial-flexor.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# # Data Explorer

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Part I. Process Data](#one)
# - [Part II. Motor Neuron Activity](#two)
# 

# <a id="intro"></a>
# # Intracellular Recording
# 
# Resting membrane potential measurement.
# 

# <a id="setup"></a>
# # Setup
# 
# [toc](#toc)

# Import and define functions

# In[ ]:


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

import matplotlib.pyplot as plt
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
import csv
from scipy.signal import hilbert,medfilt,resample
from sklearn.decomposition import PCA
import scipy
import seaborn as sns
colors = ['cyan','gray','red','green','blue','purple','orange']
merge_cluster_list = [[]]
get_ipython().run_line_magic('matplotlib', 'widget')


# <a id="two"></a>
# ## Part II. Import raw data ('.bin' file)
# ### Edit the code cell below with the appropriate information, then play/execute the cell
# - **filepath** is the path to your ".bin" data file that has simultaneous recording of muscle and nerve. 
#   - filepath needs to be in quotation marks.
#   - ***if you are on a windows operating system computer, you need an "r" before the first quote of the filepath***
# - **number_channels** = the number of inputs to the analog to digital converter were recorded.
# - **nerve_channel** and **muscle_channel** which analog input channel was the nerve amplifier hooked up to? This is "nerve_channel" and the same logic applies to "muscle_channel"
# - **sampling_rate** is the sampling rate that you recorded data at
# 
# ### You will also get a plot of your raw data from both channels (nerve in blue and muscle in green).
# - You can interact with the plot by zooming in and panning. <br>
# - You can make the plot bigger or smaller by dragging its bottom right corner (gray triangle). Note that when it gets smaller the axis labels might disappear.
# - You can save the current plot view at any time by hitting the "save" icon - it will save to your Downloads folder. <br>
# 
# <div class="alert alert-success"><b>Task:</b> Run the cell below after editing the variables to match your data parameters.</div>

# In[ ]:


filepath = "/Users/kperks/OneDrive - wesleyan.edu/Teaching/Neurophysiology/Data/CrayfishNerve3/nerve_Muscle_TelsonStim2021-07-16T14_34_57.bin"
number_channels = 2
nerve_channel = 1
muscle_channel = 0
sampling_rate = 30000


# No need to edit below this line
#################################
filepath = Path(filepath)
y_data = np.fromfile(Path(filepath), dtype = np.float64)
y_data = y_data.reshape(-1,number_channels)
nerve = y_data[:,nerve_channel] - np.median(y_data[:,nerve_channel],0)
time = np.linspace(0,np.shape(y_data)[0]/sampling_rate,np.shape(y_data)[0])
muscle = y_data[:,muscle_channel]
hfig,ax = plt.subplots(1)
ax.plot(time, nerve, color = 'blue')
ax.plot(time, muscle, color = 'green')
ax.set_ylabel('Volts (recorded)')
ax.set_xlabel('seconds')


# <a id="three"></a>
# ## Part III. Detect spiking events in the raw signal from the motor nerve.
# > If you ever need to restore your "df" dataframe, start here again and re-run the next two cells below (for example if you merge clusters you did not mean to. 
# ### Edit the code cell below with the appropriate information, then play/execute the cell
# - **spike_detection_threshold** is the Voltage value that peaks need to cross to be counted/detected as spikes. </br> 
# - **polarity** controls whether you are detecting spikes based on the positive peaks (polarity = 1) or negative peaks (polarity = -1) </br> 
#     - what this does is multiply the nerve voltage trace by the value of polarity before detecting peaks based on spike threshold.
# 
# ### You will also get a plot of the histogram (distribution) of peak heights for all peaks (putative spikes) detected (peaks larger than the threshold you set).
# 
# <div class="alert alert-success"><b>Task:</b> Run the cell below after editing the variables as needed based on your raw data signal.</div>

# In[ ]:


spike_detection_threshold = 0.04
polarity = -1



# No need to edit below this line
#################################
peaks,props = find_peaks(polarity * nerve,height=spike_detection_threshold, 
                         prominence = spike_detection_threshold, distance=(0.001*sampling_rate))
peaks_t = peaks/sampling_rate
df = pd.DataFrame({
        'height': props['peak_heights'],
        'r_prom' : -nerve[peaks]+nerve[props['right_bases']],
        'l_prom' : -nerve[peaks]+nerve[props['left_bases']]
        # 'widths' : props['widths']/fs
            })
n,bins = np.histogram(df['height'],bins = 100) # calculate the histogram
bins = bins[1:]
hfig,ax = plt.subplots(1)
ax.step(bins,n)
ax.set_ylabel('count')
ax.set_xlabel('Volts')


# <a id="four"></a>
# ## Part IV. Cluster peaks by waveform shape into putative neuron classes.
# 
# ### Edit the code cell below with the appropriate information, then play/execute the cell
# - **number_of_clusters** is the number of clusters you want the algorithm to make. Look at both your raw data and the histogram to decide what number you think this should be. *You will be able to combine clusters later, so it is better to over-estimate here*. (k cannot be larger than 7)</br> 
# 
# <div class="alert alert-success"><b>Task:</b> Run the cell below after editing the variables as needed to control the clustering analyisis.</div>

# In[ ]:


number_of_clusters = 4


# No need to edit below this line
#################################
df_normalized=(df - df.mean()) / df.std() #normalize data in dataframe for PCA
pca = PCA(n_components=df.shape[1])
pca.fit(df_normalized)
X_pca=pca.transform(df_normalized)
kmeans = KMeans(n_clusters=number_of_clusters).fit(X_pca[:,0:2])
df['peaks_t'] = peaks_t
df['cluster'] = kmeans.labels_


# <a id="five"></a>
# ## Part V. Plot the results of clustering to determine how many neurons you recorded.
# 
# ### You will get a plot of the raw voltage trace recorded from the nerve. 
# - This plot incorporates your "polarity" to show you what happens when this value changes (with respect to the peak finding algorithm). 
# - The overlaid scatter plot shows the height of each peak at the time of the peak. 
#   - The scatter is colored according to which cluster the spike was assigned.
#   
# ### You will get a plot of the mean spike waveform associated with each cluster. 
# - you can change **windur** to change the amount of time before and after each spike to plot.
#   
# ### With these two plots, you can determine how many distinguishable (unique) neurons you think there actually are in your recording. 
# 
# <div class="alert alert-success"><b>Task:</b> Run the cell below to plot the clustering results.</div>

# In[ ]:


windur = 0.002


# No need to edit below this line
#################################
hfig,ax = plt.subplots(1)
ax.plot(time, polarity * nerve, color = 'blue')
ax.plot(time, muscle, color = 'green')
for i,k in enumerate(np.unique(df['cluster'])):
    df_ = df[df['cluster']==k]
    ax.scatter(df_['peaks_t'],df_['height'],color = colors[i],zorder = 3)
ax.set_ylabel('Voltage recorded (V)')
ax.set_xlabel('seconds')
winsamps = int(windur * sampling_rate)
x = np.linspace(-windur,windur,winsamps*2)*1000
hfig,ax = plt.subplots(1)
ax.set_ylabel('Volts recorded')
ax.set_xlabel('milliseconds')
for k in np.unique(df['cluster']):
    spkt = df.loc[df['cluster']==k]['peaks_t'].values
    spkt = spkt[(spkt>windur) & (spkt<(len((muscle)/sampling_rate)-windur))]
    print(str(len(spkt)) + " spikes in cluster number " + str(k))
    spkwav = np.asarray([nerve[(int(t*sampling_rate)-winsamps):(int(t*sampling_rate)+winsamps)] for t in spkt])
    wav_u = np.mean(spkwav,0)
    wav_std = np.std(spkwav,0)
    ax.plot(x,wav_u,linewidth = 3,color = colors[k])


# ## If there are multiple spike clusters you want to merge into a single cell class, *edit and run* the cell below.
# 
# - **merge_cluster_list** = a list of the clusters (identified by numbers associated with the following colors).
# > cyan = 0,
# > gray = 1,
# > red = 2,
# > green = 3,
# > blue = 4,
# > purple = 5,
# > orange = 6
#   - **For example**, the folowing list would merge clusters 0 and 2 together and 1 and 3 together: <br>
#      **merge_cluster_list = [[0,2],[1,3]]**
#   - For each merge group, the first cluster number listed will be the re-asigned cluster number for that group (for example, in this case you would end up with a cluster number 0 and a cluster number 1). 
#   
# ## After running the cell below, go back up and re-plot the mean waveform for your new clusters. 

# In[ ]:


merge_cluster_list = [[1,2]]



# No need to edit below this line
#################################
for k_group in merge_cluster_list:
    for k in k_group:
        df.loc[df['cluster']==k,'cluster'] = k_group[0]
print('you now have the following clusters: ' + str(np.unique(df['cluster'])))


# <a id="six"></a>
# ## Part VI. Analyze the post-synaptic activity associated with pre-synaptic spikes.
# ### With the following plots, you can determine which neurons have a synapse close enough to your electrode to detect the psp. 
# - The mean and standard deviation are also plotted in addition to every spike-triggered membrane potential overlaid.
# 
# <div class="alert alert-success"><b>Task:</b> Run the cell below to plot the mean post-synaptic potentials triggered by spikes from each cluster overlaid.</div> 
# You can edit the value of windur in the first line of the code cell to change the amount of time after the spike that is plotted. 
# 

# In[ ]:


windur = 0.1



# No need to edit below this line
#################################
winsamps = int(windur * sampling_rate)
x = np.linspace(0,windur,winsamps)*1000
hfig,ax = plt.subplots(1)
ax.set_ylabel('Volts recorded')
ax.set_xlabel('milliseconds')
for k in np.unique(df['cluster']):
    spkt = df.loc[df['cluster']==k]['peaks_t'].values
    spkt = spkt[(spkt<((len(muscle)/sampling_rate)-windur))]
    synwav = np.asarray([muscle[(int(t*sampling_rate)):(int(t*sampling_rate)+winsamps)] for t in spkt])
    wav_u = np.mean(synwav,0)
    wav_std = np.std(synwav,0)
    ax.plot(x,wav_u,linewidth = 3,color = colors[k])
#     ax.fill_between(x, wav_u-wav_std, wav_u+wav_std, alpha = 0.25, color = colors[k])


# ### Edit the code cell below with the appropriate information, then play/execute the cell.
# - **k** is the cluster number (according to the following colors list) </br> 
# > cyan = 0,
# > gray = 1,
# > red = 2,
# > green = 3,
# > blue = 4,
# > purple = 5,
# > orange = 6
# 
# 
# <div class="alert alert-success"><b>Task:</b> Run the cell below to plot the post-synaptic potentials triggered by spikes from cluster *k*.</div>

# In[ ]:


k = 0



# No need to edit below this line
#################################
windur = 0.1
winsamps = int(windur * sampling_rate)
x = np.linspace(0,windur,winsamps)*1000
# colors = ['brown','black','red','green','blue','purple','orange']
hfig,ax = plt.subplots(1)
ax.set_ylabel('Volts recorded')
ax.set_xlabel('milliseconds')

spkt = df.loc[df['cluster']==k]['peaks_t'].values
spkt = spkt[(spkt<((len(muscle)/sampling_rate)-windur))]
synwav = np.asarray([muscle[(int(t*sampling_rate)):(int(t*sampling_rate)+winsamps)] - muscle[int(t*sampling_rate)] for t in spkt])
wav_u = np.mean(synwav,0)
wav_std = np.std(synwav,0)
ax.plot(x,synwav.T,linewidth = 0.5, alpha = 0.5,color = colors[k]);
ax.plot(x,wav_u,linewidth = 3,color = 'black')
ax.fill_between(x, wav_u-wav_std, wav_u+wav_std, alpha = 0.25, color = 'black',zorder=3);


# ### Edit the code cell below with the appropriate information, depending on which spike cluster you want to use to plot the average spike waveform and the average spike-triggered post-synaptic potential. Then play/execute the cell.
# - **k** is the cluster number (according to the following colors list) </br> 
# > cyan = 0,
# > gray = 1,
# > red = 2,
# > green = 3,
# > blue = 4,
# > purple = 5,
# > orange = 6
# - **offset** is the amount of time plotted before the spike time.
# - **windur** is the amount of time plotted after the spike time. 
# 
# ### With this plot, you can determine the average delay between the spike and the post-synaptic resposne for each neuron. 
# 
# <div class="alert alert-success"><b>Task:</b> Run the cell below to plot the average pre- and post-synaptic potentials triggered by spikes from cluster *k*.</div>

# In[ ]:


k = 0

# Optional parameters to change: offset (time before spike to plot) and windur (time after spike to plot)
offset = 0.002
windur = 0.1



# No need to edit below this line
#################################
winsamps = int(windur * sampling_rate)
hfig,ax = plt.subplots(1)
ax.set_ylabel('Volts recorded')
ax.set_xlabel('milliseconds')
x = np.linspace(-offset,windur,(winsamps + int(offset*sampling_rate)))*1000
spkt = df.loc[df['cluster']==k]['peaks_t'].values
spkt = spkt[(spkt>offset)&(spkt<((len(muscle)/sampling_rate)-windur))]
spkwav = np.asarray([nerve[(int(t*sampling_rate)-int(offset*sampling_rate)):(int(t*sampling_rate)+winsamps)] for t in spkt if (int(t*sampling_rate)+winsamps < len(muscle))])
synwav = np.asarray([muscle[(int(t*sampling_rate)-int(offset*sampling_rate)):(int(t*sampling_rate)+winsamps)] for t in spkt if (int(t*sampling_rate)+winsamps < len(muscle))])
spk_u = np.mean(spkwav,0)
spk_std = np.std(spkwav,0)
syn_u = np.mean(synwav,0)
syn_std = np.std(synwav,0)
ax.plot(x,spk_u,linewidth = 1,color = colors[k])
ax.plot(x,syn_u,linewidth = 1,color = colors[k])


# <div class="alert alert-success"><b>Task:</b> Celebrate your new analysis skills by running the cell below.</div>

# In[ ]:


from IPython.display import HTML
HTML('<img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif">')


# <a id="six"></a>
# ## Take Home: Answer the following questions in a separate document to turn in.
# > *When asked to report amplitudes of events (spikes or PSPs), correct for the amplifier gain (1000x for the extracellular amplifier and 10x for the intracellular amplifier).*
# 
# ### Figure 1. *Synaptic connections between pre- and post-synaptic cells*
# Only compare intracellular recordings using the same motor nerve. 
# - How many motor neurons did you record spikes from?
# - Which of these neurons evoked synaptic potentials that you recorded intracellularly from the muscle cell?
#   - Make note of different intracellular recording locations as needed.
# - We know that all of the 6 motor neurons in Nerve 3 synapse on the superficial flexor muscle. Were your results for each intracellular recording location consistent with this? If not, how do you explain the inconsistency? Did you see responses to different motor neurons at different intracellular recording locations?
# 
# ### Figure 2. *Synaptic **dynamics** - the timecourse of synaptic connectivity*
# Only compare intracellular recordings using the same motor nerve. 
# - How many motor neurons did you record spikes from? *only do this if it is different than in Figure 1, otherwise refer to Figure 1)*
# - For each panel of the figure (each PSP), annotate the following:
#   - the delay between the pre-synaptic spike time and the psp
#   - the psp rise time (the time from the onset of the psp to the peak of the psp)
#   - the psp amplitude 
# - Make it clear which panels are from the same intracellular recording and which are from different.
# 
# ### Figure 3. *Stereotypy of Pre to Post synaptic transformations - Does synaptic summation effect post-synaptic potential amplitude?*
# Because you will *"normalize"* your data, you can combine data using different motor nerves. 
# - Use recordings with distinct PSPs associated with a distinct neuron (identified by waveform amplitude).
# - Quantitative procedure for each intracellular recording:<br>
#   - Measure the amplitude of 5 solitary PSPs associated with that pre-synaptic neuron. 
#   - Find examples of synaptic summation. Measure the amplitude of the second PSP (from PSP onset, not from resting membrane potential). Measure the latency between the onset of the first PSP and the onset of the second PSP. If there are more than two PSPs in a row, compare sequentially.
# - Analysis: 
#   - Within each intracellular recording, divide all amplitudes by the mean solitary PSP amplitude. This enables you to plot data from different recordings together.
# - Visualization: 
#   - Use a program such as google sheets or excell to make a plot of PSP amplitude versus latency (the solitary PSPs will have a latency of 100ms). 
# 
# ### Figure 4. *Pre to post-synaptic transformations* 
# In any of your recordings *from the same motor nerve recordings*, did you see PSPs in repsponse to different neurons? (If not, then you won't have a figure - instead you will just answer the second bullet point.
# - Did either psp onset slope correlate with spike amplitude?
#   - To answer this question (are they correlated) use a spreadsheet program to make a scatter plot of psp onset slope (rise time / amplitude) against spike amplitude. 
# - Use what you have learned in your neuroscience courses (and what we have learned this semester in lab) to name two reasons why:
#   - the PSP amplitude could be different in response to different pre-synaptic neurons
#   - the PSP amplitude could be different at different intracellular recording locations (different muscle cells or different locations along the same muscle cell)
# 
