#!/usr/bin/env python
# coding: utf-8

# # Lab Manual and Data Explorer
# 
# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/passive-membrane-models/Lab-Manual_passive-membrane-models.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction: Electrical Circuit Models of Membrane Properties](#intro)
# - [Setup](#setup)
# - [Part I. Membrane voltage](#one)
# - [Part II. Intracellular Recording of Applied Current](#two)
# - [Part III. Extracellular Recording of Applied Current](#three)
# - [Part IV. Membrane Potential Dynamics with Applied Current](#four)

# <a id="intro"></a>
# # Introduction: Electrical Circuit Models of Membrane Properties
# 
# [Table of Contents](#toc)
# 
# Today you will use electrical circuit models of a passive cell membrane to introduce yourself to some of the basic components of your essential electrophysiology toolkit. You will interrogate some of the passive properties of neural membranes and compare the difference between membrane potential "spikes" recorded intracellularly and membrane potentials recorded extracellularly. 
# 
# Upon completion of the materials assigned in this module, you will be able to:
# - Describe passive properties of neural membranes that critically affect neural processing. 
# - Use a voltage meter.
# - Understand how basic circuit components relate to fundamental physiological properties of neurons (Resistance, Capacitance, Serial, Parallel, Voltage, Current).
# - Store, manage, and visualize data on the computer.
# - Create figures that summarize your data and analysis - enabling you to discuss your results.
# 
# A small set of electrical components can be used to describe many of the basic electrophysiological properties of neurons.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/Electrical_Components.png?raw=True' width="300" alt='electrical components'/>
# 
# [**Resistors**](#resistor-decoder) are electrical components that resist the flow of current through a circuit. The amount of current flowing through a resistor can be expressed by Ohm’s Law: I = V/R, where I represents the current, V represents the voltage, and R represents the resistance. Similarly, V = IR determines the voltage in response to a current across a resistor. 
# 
# In an electrical circuit, a **capacitor** possesses two conducting regions with a separation of non-conducting material in between. When one conducting region accumulates a charge (due to current flow from an external voltage source), an electric field is created, which pushes the charge off of the subsequent conducting region of the capacitor. This phenomenon only lasts a short amount of time, producing a brief current which is expressed as: I = C dV/dt, where I represents the current, C represents the capacitance, and dV/dt represents the rate of voltage change with time.
# 
# Current flows across the membrane capacitance only when voltage across the membrane changes. When one side of a membrane becomes more positive (for example when an excitatory synaptic input is "activated"), positive ions are repelled from and negative ions are attracted to the other side of the membrane. This redistribution of charges takes time, after which the membrane reaches a steady state and no current flows. When the voltage across the membrane returns to its initial value (for example, when synaptic ion channels close), charges separated by the membrane flow again, discharging the membrane capacitance.
# 
# Since the lipid bilayer is an electrical insulator between two conducting areas (extra- and intracellular fluids), it acts as a capacitor, while ion channels act as resistors. Membrane capacitance is parallel to membrane resistance (though a circuit in series can be equivalent for some purposes). 
# 
# Some **active** properties of a neuron membrane can be modelled with the following circuit. 
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-active.png?raw=True' width="400" alt='model membrane'/>
# 
# For example, in this model, $R_K$ is the resistance through potassium channels, $R_Na$ is the resistance through sodium channels, and $C$ is the capacitance of the lipid bilayer (not necessary for understanding steady state properties). By convension, we measure the inside of a neuron's membrane with respect to the outside ("*ground*").
# 
# Some **passive** properties of a neuron membrane can be modelled with the following two circuits. 
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-passive-spread.png?raw=True' width="500" alt='model membrane'/>
# 
# This is a great model of a long compartment of a neuron, such as an axon. In this lab, the circuit you will use for this model has the following $R$ values:
# - Rinside = 1 kOhm
# - Routside = 100 Ohm
# - Rmembrane = 10 kOhm
# 
# Note that resistances in parallel sum according to $R_total = {R*n}/n$ while resistances in series sum according to $R_total = R*n$.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-passive-rc.png?raw=True' width="300" alt='model membrane'/>
# 
# This is a great model for summarizing the entire membrane of the neuron in a single *compartment*. In this lab, $R=10KOhm$ and $C=1uF$ in the circuit you will use for this model. 
# 
#  
# 

# <a id="setup"></a>
# # Setup

# In[ ]:


#@title {display-mode:"form"}

#@title Run this cell to initialize packages and functions 

import numpy as np
import matplotlib.pyplot as plt


# <a id="one"></a>
# # Part I. Membrane Potential
# 
# [TOC](#toc)
# 
# You will create the following circuit (ignoring capacitance) on a *breadboard* and use a voltmeter to measure membrane potential.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-active.png?raw=True' width="400" alt='model membrane'/>
# 
# **Setup**:
# - Use one battery for $E_K$ and one battery for $E_{Na}$  
# - Start with equal [resistors](#resistor-decoder) for $R_K$ and $R_{Na}$.
# 
# **Experiment**:
# - Record the measered 'membrane' potential of the model cell.
# > Note that *membrane potential* is measured inside the cell relative to outside. 
# - Keeping $R_K$ constant, change $R_{Na}$ and record the measered 'membrane' potential.
# - Keeping $R_{Na}$ constant, change $R_K$ and record the measered 'membrane' potential.
# - Keeping $R_K$ and $R_{Na}$ constant, change the polarity of the batteries and record what happens to the measered 'membrane' potential with each change in polarity configuration. 
# 

# <a id="two"></a>
# # Part II. Intracellular Recording of Applied Current
# 
# [TOC](#toc)
# 
# You will use the following passive axon model and a voltmeter to complete this experiment.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-passive-spread.png?raw=True' width="500" alt='model membrane'/>
# 
# **Experiment:**
# - At the middle of the axon (node 5), place one electrode on the ‘inside’ of the membrane and one on the ‘outside’.
# - Attach a voltage source (9V battery) across the cell membrane at the end of the axon (node 0). 
# - Move the voltage source along the axon one node at a time until you reach node 10. 
#   - At each node, record the voltage in the dictionary below by replacing the ```...``` with the measured value.
# 

# In[ ]:


voltage_intracellular = {
    '0' : ...,
    '1' : ...,
    '2' : ...,
    '3' : ...,
    '4' : ...,
    '5' : ...,
    '6' : ...,
    '7' : ...,
    '8' : ...,
    '9' : ...,
    '10' : ...
}


# Run the code cell in which you just defined your data dictionary.
# 
# Then, run the following code cell to plot your data.

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run to plot data.

nodes = list(map(int, list(voltage_intracellular.keys())))
voltage = list(voltage_intracellular.values())

plt.figure()
plt.plot(nodes,voltage)


# <a id="three"></a>
# # Part III. Extracellular Recording of Applied Current
# 
# [TOC](#toc)
# 
# Use the same passive axon model that you used in [Part II](#two) and a voltmeter to complete this experiment.
# 
# **Experiment:**
# - At the middle of the axon, place *both* electrodes on the ‘outside’ of the membrane, with one empty node between them (one electrode at node 4 and one at node 6).
# - Attach the voltage source (9V battery) across the cell membrane at the end of the axon (node 0). 
# - Move the voltage source along the axon one node at a time until you reach node 10. 
#   - At each node, record the voltage in the dictionary below by replacing the ```...``` with the measured value.
# 

# In[ ]:


voltage_extracellular = {
    '0' : ...,
    '1' : ...,
    '2' : ...,
    '3' : ...,
    '4' : ...,
    '5' : ...,
    '6' : ...,
    '7' : ...,
    '8' : ...,
    '9' : ...,
    '10' : ...
}


# Run the code cell in which you just defined your data dictionary.
# 
# Then, run the following code cell to plot your data.

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run to plot data.

nodes = list(map(int, list(voltage_extracellular.keys())))
voltage = list(voltage_extracellular.values())

plt.figure()
plt.plot(nodes,voltage)


# <a id="four"></a>
# # Part IV. Membrane Potential Dynamics with Applied Current
# 
# [TOC](#toc)
# 
# For this exercise, you will use the following passive resistor-capacitor circuit model membrane. 
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-passive-rc.png?raw=True' width="300" alt='model membrane'/>
# 
# You will be using the [***Ghetting Intracellular Amplifier***](http://www.gettinginstruments.com/5A.html) to both deliver current and measure voltage (yes... it is unassuming, but fancy).  
# You will also use an analog to digital converter (the [***NiUSB-6211***](https://www.ni.com/en-us/support/model.usb-6211.html) from *National Instruments*) to send the measurements to the computer for recording the raw (digitized) data.  
# You will also be using a ***Stimulus Isolating Unit*** to deliver square-wave pulses of voltage to the Ghetting, which will be converted to current and delivered to the model membrane circuit. A "square wave" stimulus is one that instantaneously increases in amplitude and maintains that amplitude some duration before instantaneously decreasing to 0.
# 
# **Setup**: 
# - Place the recording/measureing electrode on the ‘inside’ of the membrane 
# - Place the *ground* electrode on the ‘outside’
# > If you are using a separate SIU and amplifier, set up the stimulus electrodes so that you can "apply" current into the model membrane (one stimulating electrode on the outside and one on the inside). You will need to use a model circuit in series rather than parallel so the recording does not short the stim. 
# - Open the script in Desktop/BIOL247_FA22/passive-membrane-models/Data called "passive-membrane-models.bonsai"
# > Note that a copy of the stimulus command is also being sent to the NiUSB ADC
# - Make sure that the sampling rate is set to 10000.
# - <font color="red"> Disable</font> the "Matrix Writer" node. 
# - Hit play. Double click on the "Membrane Potential" and "Stimulus" nodes if the windows are not already present. Make sure that you see a signal. 
# - Apply a voltage across the model membrane with a small (<1.5V) battery to check that you are seeing what you think you should. 
# - Stop the data acquisition by hitting the *stop* button in Bonsai.
# 
# **Experiment**:
# - <font color="green"> Enable</font> the "Matrix Writer" node. 
# - Hit play to collect data. Double click on the "Membrane Potential" and "Stimulus" nodes if the windows are not already present. Make sure that you see a signal. 
# - Apply a stimulus pulse.
# - Stop the data acquisition by hitting the *stop* button in Bonsai.
# 
# Upload your data to your Google Drive to access it.

# In[ ]:


#@title {display-mode: "form" }

#@markdown Run this cell to mount your Google Drive.

from google.colab import drive
drive.mount('/content/drive')

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# In[ ]:


#@title {display-mode: "form"}

#@markdown Specify the file path 
#@markdown to your recorded data (copy the filepath from the colab file manager by clicking the :).

filepath = "full filepath goes here"  #@param 

#@markdown Specify the sampling rate recorded.

# sampling_rate = None #@param
sampling_rate = 10000 #@param

number_channels = 2 # one is the stimulus and one is the membrane potential
membrane_channel = 0 #@param 
stimulus_channal = 1 #@param
downsample = False 
newfs = 10000 

#@markdown After you have filled out all form fields, 
#@markdown run this code cell to load and plot the data. 
#@markdown Use the range slider under the plot to scroll through the data in time.

filepath = Path(filepath)
data = np.fromfile(Path(filepath), dtype = np.float64)
data = data.reshape(-1,number_channels)
data_dur = np.shape(data)[0]/sampling_rate
print('duration of recording was %0.2f seconds' %dur)

fs = sampling_rate
if downsample:
    chunksize = int(sampling_rate/newfs)
    data = data[0::chunksize,:]
    fs = int(np.shape(data)[0]/data_dur)

time = np.linspace(0,data_dur,np.shape(data)[0])

print('Data upload completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))

f = go.FigureWidget(make_subplots(rows=2,cols=1,
                                  shared_xaxes=True,
                                  layout=go.Layout(height=500, width=800)))
f.add_trace(go.Scatter(x = time[0:fs], y = data[0:fs,membrane_channel],
                         name=str(chan),opacity=1),
             row=1,col=1)
f.add_trace(go.Scatter(x = time[0:fs], y = data[0:fs,stimulus_channel],
                         name=str(chan),opacity=1),
             row=2,col=1)

slider = widgets.FloatRangeSlider(
    min=0,
    max=data_dur,
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
        f.data[0].y = data[starti:stopi,membrane_channel]
        
        f.data[1].x = time[starti:stopi]
        f.data[1].y = data[starti:stopi,stimulus_channel]

vb = VBox((f, interactive(response, x=slider)))
vb.layout.align_items = 'center'
vb


# 
# **Experiment extensions**: 
# - What happens when you change the stimulus amplitude?
# - What happens when you change the stimulus duration?
# - What happens when you change the resistance of the model cell?
# 
# Upload your data file to the Colab kernel by dragging it into the file manager panel. Then follow the rest of the steps below to measure and analyze your data more quantitatively.

# # Additional Resources
# 
# <a id='resistor-decoder'></a>
# ## Resistor Decoder
# From [worrydream](http://worrydream.com/#!/ResistorDecoder)
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/resistors-decoder_bret-victor.png?raw=True' width="700" alt='model membrane'/>

# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University. Materials based off of William Kristan's graduate student bootcamp at UCSD and the Membrane Properties Lab in the Crawdad Lab Manual by Robert A. Wyttenbach, Bruce R. Johnson, and Ronald R. Hoy

# In[ ]:




