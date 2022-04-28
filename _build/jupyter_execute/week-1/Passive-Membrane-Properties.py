#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/week-1/Passive-Membrane-Properties.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# <a id="intro"></a>
# # Introduction
# 
# Today you will use electrical circuit models of a passive cell membrane to introduce yourself to some of the basic components of your essential electrophysiology toolkit. You will interrogate some of the passive properties of neural membranes and compare the difference between membrane potentials recorded intracellularly and membrane potentials recorded extracellularly. 
# 
# Upon completion of the materials assigned in this module, you will be able to:
# - Describe passive properties of neural membranes that critically affect neural processing. 
# - Use a voltage meter.
# - Understand how basic circuit components relate to fundamental physiological properties of neurons (Resistance, Capacitance, Serial, Parallel, Voltage, Current).
# - Store, manage, and visualize data on the computer.
# - Create figures that summarize your data and analysis - enabling you to discuss your results.
# 

# <a id="toc"></a>
# # Table of Contents
# 
# 

# <a id="initialize"></a>
# # Initialize Notebook

# In[10]:


import numpy as np
import matplotlib.pyplot as plt


# <a id="one"></a>
# # Part I. Intracellular Recording of Membrane Potential
# 
# Use the model cell axon and a voltmeter to complete the following:
# - At one end of the axon, place one electrode on the ‘inside’ of the membrane and one on the ‘outside’.
# - Set up a voltage across the membrane by attaching the voltage source across the cell membrane at one location along the axon. 
# > For each node placement, record the voltage measured with the recording electrodes and the distance of the voltage source from the recording electrodes (in number of nodes; - to the left, + to the right).
# - Move the voltage source to a different location along the axon. 
# > Record the voltage in the dictionary below by replacing the ```...``` with the value recorded at the corresponding node
# 

# In[1]:


voltage_intracellular = {
    '-5' : ...,
    '-4' : ...,
    '-3' : ...,
    '-2' : ...,
    '-1' : ...,
    '0' : ...,
    '1' : ...,
    '2' : ...,
    '3' : ...,
    '4' : ...,
    '5' : ...
}


# In[2]:


voltage_intracellular = {
    '-5' : 1,
    '-4' : 2,
    '-3' : 3,
    '-2' : 4,
    '-1' : 5,
    '0' : 6,
    '1' : 5,
    '2' : 4,
    '3' : 3,
    '4' : 2,
    '5' : 1
}


# Run the following code cell to plot your data

# In[9]:


nodes = list(map(int, list(voltage_intracellular.keys())))
voltage = list(voltage_intracellular.values())


# In[11]:


plt.figure()
plt.plot(nodes,voltage)

