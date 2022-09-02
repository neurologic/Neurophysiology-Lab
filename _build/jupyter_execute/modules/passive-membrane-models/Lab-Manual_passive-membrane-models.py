#!/usr/bin/env python
# coding: utf-8

# # Lab Manual
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
# This module will help you work on:
# - Describing passive properties of neural membranes that critically affect neural processing. 
# - Using a voltage meter.
# - Relating basic electrical circuit components to fundamental physiological properties of neurons (Resistance, Capacitance, Serial, Parallel, Voltage, Current).
# - Storing, managing, and visualizing data on the computer.
# - Creating figures that summarize your data and analysis - enabling you to discuss your results.
# 
# ## Electrical Circuit Components
# 
# A small set of electrical components can be used to describe many of the basic electrophysiological properties of neurons.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/Electrical_Components.png?raw=True' width="300" alt='electrical components'/>
# 
# [**Resistors**](#resistor-decoder) are electrical components that resist the flow of current through a circuit. The amount of current flowing through a resistor can be expressed by Ohm’s Law: $I = V/R$, where I represents the current, V represents the voltage, and R represents the resistance. Similarly, $V = IR$ determines the voltage in response to a current across a resistor. 
# 
# In an electrical circuit, a **capacitor** possesses two conducting regions with a separation of non-conducting material in between. When one conducting region accumulates a charge (due to current flow from an external voltage source), an electric field is created, which pushes the charge off of the subsequent conducting region of the capacitor. This phenomenon only lasts a short amount of time, producing a brief current which is expressed as: $I = C * \partial{V}/\partial{t}$, where $I$ represents the current, $C$ represents the capacitance, and $\partial{V}/\partial{t}$ represents the rate of voltage change with time. Current flows across the membrane capacitance only when voltage across the membrane changes. 
# 
# Since the lipid bilayer is an electrical insulator between two conducting areas (extra- and intracellular fluids), it acts as a capacitor, while ion channels act as resistors. Membrane capacitance is parallel to membrane resistance (though a circuit in series can be equivalent for some purposes). 
# 
# ## Electrical Circuit Models
# 
# Some **active** properties of a neuron membrane can be modelled with the following circuit. 
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-active.png?raw=True' width="400" alt='model membrane'/>
# 
# For example, in this model, $R_K$ is the resistance through potassium channels, $R_{Na}$ is the resistance through sodium channels, and $C$ is the capacitance of the lipid bilayer (not necessary for understanding steady state properties). By convension, we measure the inside of a neuron's membrane with respect to the outside ("*ground*").
# 
# Some **passive** properties of a neuron membrane can be modelled with the following two circuits. 
# 
# 1. This is a great model of a long compartment of a neuron, such as an axon. 
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-passive-spread.png?raw=True' width="500" alt='model membrane'/>
# 
# In this lab, the circuit you will use for this model has the following $R$ values:
# - Rinside = 1 kOhm
# - Routside = 100 Ohm
# - Rmembrane = 10 kOhm
# 
# Note that resistances in parallel sum according to $R_{total} = {R*n}/n$ while resistances in series sum according to $R_{total} = R*n$.
# 
# 2. This is a great model for summarizing the entire membrane of the neuron in a single *compartment*. 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-passive-rc.png?raw=True' width="300" alt='model membrane'/>
# 
# In this lab, you will start with values of $R=10MOhm$ and $C=0.001uF$. 
# 
#  
# 

# <a id="setup"></a>
# # Setup

# ## Physical Rig Hardware Setup

# You will be using the [***Getting Intracellular Amplifier***](http://www.gettinginstruments.com/5A.html) to measure the 
# 'membrane potential" in your model circuits. *An analog to digital converter* (the [***NiUSB-6211***](https://www.ni.com/en-us/support/model.usb-6211.html) from *National Instruments*) will digitize the analog voltage and sends it to the computer for visualization and recording of the raw (digitized) data.  

# ## Physical Rig Software Setup
# 
# [Bonsai-rx](https://bonsai-rx.org/) is an open-source software for managing streems of data from devices on a computer. Open the bonsai workflow (passive-membrane-models.bonsai) from the Documents/BIOL247/data/ folder on the lab PC. Hitting the *start* button on the workflow will start the digitization of data from the NiUSB. Double-clicking on the *Select Channels* nodes will enable you to visualize a live stream of the raw data from the electrodes. Whenever you want to visualize the electrode measurements without accumulating stored data on the PC harddrive, just <font color = 'red'>**disable**</font> the recording node.
# 

# ## Python Notebook Setup

# In[ ]:


#@title {display-mode:"form"}

#@title Run this cell to initialize packages and functions 

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ipywidgets import interactive, HBox, VBox, widgets, interact


# <a id="one"></a>
# # Part I. Membrane Potential
# 
# [TOC](#toc)
# 
# You will create the following circuit (ignoring capacitance) on a *breadboard*.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-active.png?raw=True' width="400" alt='model membrane'/>
# 
# **Setup**:
# - Use one battery for $E_K$ and one battery for $E_{Na}$ (make sure to measure and record the voltage of each battery... you will also use this info in future labs)
# - Start with equal [resistors](#resistor-decoder) for $R_K$ and $R_{Na}$ (make sure to measure and record the value of each resistor... you will also use this info in future labs).
# - Place the recording/measureing electrode on the ‘inside’ of the membrane 
# - Place the *ground* electrode on the ‘outside’
# - Open the script in Desktop/BIOL247_FA22/passive-membrane-models/Data called "passive-membrane-models.bonsai"
# - Make sure that the sampling rate is set to 5000.
# - <font color="red"> Disable</font> the "Matrix Writer" node. 
# 
# **Experiment**:
# - Hit play in Bonsai. Double click on the "Membrane Potential" node if the window is not already present. Close the "Stimulus" window if it is open.
# - Right mouse click on the bottom of the membrane potential window to change the y axis range of the graph.
# - Hover over the signal trace with your mouse to see the voltage. Record the measured 'membrane' potential of the model cell.
# > Note that *membrane potential* is measured inside the cell relative to outside and the Getting amplifier *has a gain of 10*. 
# - Keeping $R_K$ constant, change $R_{Na}$ and record the measured 'membrane' potential. (make sure to measure and record the value of each resistor... you will also use this info in future labs)
# - Keeping $R_{Na}$ constant, change $R_K$ and record the measured 'membrane' potential. (make sure to measure and record the value of each resistor... you will also use this info in future labs)
# - Keeping $R_K$ and $R_{Na}$ constant, change the polarity of the batteries and record what happens to the measured 'membrane' potential with each change in polarity configuration. 
# - Stop the data acquisition by hitting the *stop* button in Bonsai.
# 

# <a id="two"></a>
# # Part II. Intracellular Recording of Applied Current
# 
# [TOC](#toc)
# 
# You will use the following passive axon model (pre-made) to complete this experiment.
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/circuit-model-passive-spread.png?raw=True' width="500" alt='model membrane'/>
# 
# **Setup**:
# - At the middle of the axon (node 5), place one electrode on the ‘inside’ of the membrane and one on the ‘outside’.
# > Note that *membrane potential* is measured inside the cell relative to outside. 
# - Open the script in Desktop/BIOL247_FA22/passive-membrane-models/Data called "passive-membrane-models.bonsai"
# - Make sure that the sampling rate is set to 5000.
# - <font color="red"> Disable</font> the "Matrix Writer" node. 
# 
# **Experiment:**
# - Attach a voltage source (9V battery) across the cell membrane at the end of the axon (node 0). 
# - Move the voltage source along the axon one node at a time until you reach node 10. 
#  - At each node, record the voltage in the dictionary below by replacing the ```...``` with the measured value.
#  > Note that the Getting amplifier *has a gain of 10*. 
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
# **Setup**:
# - At the middle of the axon, place *both* electrodes on the ‘outside’ of the membrane, with one empty node between them (one electrode at node 4 and one at node 6).
# - Open the script in Desktop/BIOL247_FA22/passive-membrane-models/Data called "passive-membrane-models.bonsai"
# - Make sure that the sampling rate is set to 5000.
# - <font color="red"> Disable</font> the "Matrix Writer" node. 
# 
# **Experiment:**
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
# You will be using the [***Getting Intracellular Amplifier***](http://www.gettinginstruments.com/5A.html) to both deliver current and measure voltage The Getting provides a *current stimulation*, feature that applies a "square wave" stimulus across the measurement electrodes. A square wave stimulus one that instantaneously increases in amplitude and maintains that amplitude some duration before instantaneously decreasing to 0.
# 
# **Setup**: 
# - Place the recording/measureing electrode on the ‘inside’ of the membrane 
# - Place the *ground* electrode on the ‘outside’
#   > If you are using a separate SIU and amplifier, set up the stimulus electrodes so that you can "apply" current into the model membrane (one stimulating electrode on the outside and one on the inside). You will need to use a model circuit in series rather than parallel so the recording does not short the stim. 
# - Open the script in Desktop/BIOL247_FA22/passive-membrane-models/Data called "passive-membrane-models.bonsai"
#   > Note that a copy of the stimulus (*current monitor*) is also being sent to the NiUSB ADC. The coversion factor is 100 mV per nA.
# - Make sure that the sampling rate is set to 5000.
# - <font color="red"> Disable</font> the "Matrix Writer" node. 
# - Hit play. Double click on the "Membrane Potential" and "Stimulus" nodes if the windows are not already present. Make sure that you see a signal. 
# - Set the current amplitude to about 5nA and switch it on for approximately 2 seconds to see that you get a response.  
# - Stop the data acquisition by hitting the *stop* button in Bonsai.
# 
# **Experiment**:
# 1. With only a resistor across the membrane
#     - <font color="green"> Enable</font> the "Matrix Writer" node. 
#     - Hit play to collect data. Double click on the "Membrane Potential" and "Stimulus" nodes if the windows are not already present. Make sure that you see a signal. 
#     - Apply a stimulus pulse of 2 seconds. 
#     - Stop the data acquisition by hitting the *stop* button in Bonsai.
# 2. With both the capacitor and resistor across the membrane
#     - Hit play to collect data. Double click on the "Membrane Potential" and "Stimulus" nodes if the windows are not already present. Make sure that you see a signal. 
#     - Apply a stimulus pulse of 2 seconds.
#     - Stop the data acquisition by hitting the *stop* button in Bonsai. 
# 
# 
# Upload your data files to an external drive **OR** to your Google Drive.  
# 
# **Use the [DataExplorer.py](https://raw.githubusercontent.com/neurologic/Neurophysiology-Lab/main/howto/Data-Explorer.py) application found in the [howto section](https://neurologic.github.io/Neurophysiology-Lab/howto/Dash-Data-Explorer.html) of the course website to explore and analyze your data.**
# 
# Stop here for a class discussion about what you notice from this final experiment and a tutorial on the **DataExplorer.py** application.
# 
# **Experiment extensions** (time permitting): 
# - What happens when you change the stimulus amplitude?
# - What happens when you change the stimulus duration?
# - What happens when you change the resistance of the model cell?
# - What happens when you change the capacitance of the model cell?
# 
# 

# # Additional Resources
# 
# <a id='resistor-decoder'></a>
# ## Resistor Decoder
# From [worrydream](http://worrydream.com/#!/ResistorDecoder)
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/resistors-decoder_bret-victor.png?raw=True' width="700" alt='model membrane'/>

# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University. Materials based off of William Kristan's graduate student bootcamp at UCSD and the Membrane Properties Lab in the Crawdad Lab Manual by Robert A. Wyttenbach, Bruce R. Johnson, and Ronald R. Hoy

# In[ ]:




