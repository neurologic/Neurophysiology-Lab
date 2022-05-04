#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-1/Passive-Membrane-Properties.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Passive Membrane Properties
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
# Resistors are electrical components that resist the flow of current through a circuit. The amount of current flowing through a resistor can be expressed by Ohm’s Law: I = V/R, where I represents the current, V represents the voltage, and R represents the resistance. Similarly, V = IR determines the voltage in response to a current across a resistor. 
# 
# In an electrical circuit, a capacitor possesses two conducting regions with a separation of non-conducting material in between. When one conducting region accumulates a charge (due to current flow from an external voltage source), an electric field is created, which pushes the charge off of the subsequent conducting region of the capacitor. This phenomenon only lasts a short amount of time, producing a brief current which is expressed as: I = C dV/dt, where I represents the current, C represents the capacitance, and dV/dt represents the rate of voltage change with time.
# 
# The first model membrane circuit you will be working with contains 3 different resistances for each patch of "membrane". These are arranged both in serial and parallel across the "membrane". 
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/Passive-Membrane-Resistance-Circuit.png?raw=True' width="500" alt='model membrane'/>
# 
# - Rinside = 1 kOhm
# - Routside = 100 Ohm
# - Rmembrane = 10 kOhm
# 
# The second model membrane circuit you will be working with is a complete model of one small patch of cell membrane. Since the lipid bilayer is an electrical insulator between two conducting areas (extra- and intracellular fluids), it acts as a capacitor, while ion channels act as resistors. Membrane capacitance is parallel to membrane resistance (though a circuit in series would be equivalent for this lab). 
# 
# <img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/Passive-Membrane-Resistance-Capacitance-Circuit.png?raw=True' width="400" alt='model membrane RC'/>
# 
# Current flows across the membrane capacitance only when voltage across the membrane changes. Wen one side of a membrane becomes more positive (for example when an excitatory synaptic input is "activated"), positive ions are repelled from and negative ions are attracted to the other side of the membrane. This redistribution of charges takes time, after which the membrane reaches a steady state and no current flows. When the voltage across the membrane returns to its initial value (for example, when synaptic ion channels close), charges separated by the membrane flow again, discharging the membrane capacitance. 
# 

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Part I. Intracellular Recording of Membrane Potential](#one)
# - [Part II. Extracellular Recording of Membrane Potential](#two)
# - [Part III. Intracellular Recording of Membrane Potential (with capacitance)](#three)

# <a id="initialize"></a>
# # Initialize Notebook

# In[ ]:


#@title {display-mode:"form"}

#@title Run this cell to initialize packages and functions 

import numpy as np
import matplotlib.pyplot as plt


# <a id="one"></a>
# # Part I. Intracellular Recording of Membrane Potential
# 
# [TOC](#toc)
# 
# Use the model cell resistance-based axon and a voltmeter to complete the following:
# - At the middle of the axon (node 5), place one electrode on the ‘inside’ of the membrane and one on the ‘outside’.
# - Set up a voltage across the membrane by attaching the voltage source across the cell membrane at the end of the axon (node 0). 
# - Move the voltage source along the axon one node at a time until you reach node 10. 
# > Record the voltage in the dictionary below by replacing the ```...``` with the value recorded at the corresponding node.
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


# Run the following code cell to plot your data

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run to plot data.

nodes = list(map(int, list(voltage_intracellular.keys())))
voltage = list(voltage_intracellular.values())

plt.figure()
plt.plot(nodes,voltage)


# <a id="two"></a>
# # Part II. Extracellular Recording of Membrane Potential
# 
# [TOC](#toc)
# 
# Use the model cell resistance-based axon and a voltmeter to complete the following:
# - At the middle of the axon, place *both* electrodes on the ‘outside’ of the membrane, with one empty node between them (one electrode at node 4 and one at node 6).
# - Set up a voltage across the membrane by attaching the voltage source across the cell membrane at the end of the axon (node 0). 
# - Move the voltage source along the axon one node at a time until you reach node 10. 
# > Record the voltage in the dictionary below by replacing the ```...``` with the value recorded at the corresponding node.
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


# Run the following code cell to plot your data

# In[ ]:


#@title {display-mode:"form"}

#@markdown Run to plot data.

nodes = list(map(int, list(voltage_extracellular.keys())))
voltage = list(voltage_extracellular.values())

plt.figure()
plt.plot(nodes,voltage)


# <a id="three"></a>
# # Part III. Intracellular Recording of Membrane Potential (with capacitance)
# 
# [TOC](#toc)
# 
# "Stimulus Isolating Units" are used to inject current into a circuit (for example, across a neuron's membrane). You can control the amplitude, duration, and frequency of the stimulus pulses. In this case, you will be using a "square wave" current (an instantaneous increase in current that is constant for some duration before instantaneously decreasing to 0). 
# 
# Use the model cell RC circuit and a voltmeter to complete the following:
# - Instead of recording measured voltages by hand, you will use the analog to digital converter to send the measurements to the computer for recording. 
# > The electrodes are connected to a device called a NiUSB-6211 (National Instruments) and it has "analog to digital" (ADC) conversion circuitry inside. 
# - Place one recording/measureing electrode on the ‘inside’ of the membrane and one recording/measureing electrode on the ‘outside’.
# - Set up the stimulus electrodes so that you can "inject" current into the model membrane (one stimulating electrode on the outside and one on the inside).
# > Note that a copy of the stimulus command is also being sent to the NiUSB ADC
# - Open the script in Desktop/BIOL247_FA22/Week1/Data called "Nidaq_2Channel.bonsai"
# - "Disable" the "Matrix Writer" node. 
# - Hit play and double click on the "Analog Input" and "Stimulus" nodes. Make sure that you see a signal. You can apply a voltage across the recording electrodes with the battery to check that you are seeing what you think you should. 
# - Turn on the stimulus and see what you notice. 
# - "Enable" the "Matrix Writer" node to collect the data. 
# - Upload the data file to the Colab session with the file manager and follow the rest of the steps below.

# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:




