#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/ERG/Sensory-Coding-ERG.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# # Data Explorer

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Import Data](#one)
# 

# <a id="intro"></a>
# # Computer Models
# 
# Modelling passive and active properties of neurons based on electric circuit models from Week 1.

# <a id="setup"></a>
# # Setup
# 
# [toc](#toc)

# Import and define functions

# In[1]:


#@title {display-mode: "form"}

#@markdown Run this code cell to import packages and define functions 
from pathlib import Path
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

from ipywidgets import interactive, HBox, VBox, widgets, interact

def monoExp(x, m, t, b):
    return m * np.exp(-x / t) + b

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# In[2]:


from brian2 import *


# In[ ]:


from neuron import h
from neuron.units import ms, mV, µm


# <a id="one"></a>
# # Steady State
# 
# [toc](#toc)

# In[ ]:


# define the function

def get_V(Rk,Rna,Ek,Ena):
    Gk = 1/Rk
    Gna = 1/Rna
    
    V = ((Rna*Ek)+(Rk*Ena))/(Rna+Rk) # Resistance-based
    
    V = ((Gk*Ek)+(Gna*Ena))/(Gk+Gna) # Conductance-based
    
    return V


# In[ ]:


V = get_V(100,100,-90,130)
print(V)


# In[ ]:


import ipywidgets as widgets


# <a id="two"></a>
# # Dynamics
# 
# [toc](#toc)

# In[ ]:


def simulate_V(V, R, C, Iapp, duration, dt):
    '''
    The simulation starts at time = 0 with the voltage given by the input to the function (V)
    
    R = the resistance of the membrane in Ohm
    
    C = the capacitance of the membrane in Farads
    
    Iapp = the current (microAmps) applied to the system throughout the simulation
    
    duration = the total time (seconds) that the current is applied to the system (in this case also the duration of the simulation)
    
    dt = the time step (seconds) for analysing the simulation (how much time elapses between each analysis of dV)
    '''
    
    timesteps = int(duration/dt)
    
    V_record = [0]
    for i in range(timesteps): # for each time step, iterate through the simulation
        dV = dt*((Iapp - V/R)/C) # how much does the voltage change by on this time step?
        V = (V+dV) # add the change in voltage to the current voltage
        V_record.append(V)
    
    return V_record


# In[ ]:


# define the initial conditions

V = 0 # Volts
R = 100000000 # MegaOhm
tau = 0.01 # seconds
C = tau/(R)# 0.01 # F

Iapp = 0.0000000001 # Amps
duration = 0.1
dt = 0.001

V_record = simulate_V(V, R, C, Iapp, duration, dt)

plt.plot(np.linspace(0,duration,int(duration/dt)+1),V_record);
plt.xlabel('seconds');
plt.ylabel('Volts');

print(f'Capacitance = {C} Farads')


# Note that $ 1mV = 100pA * 10MOhm $. Why would you want to think in terms of these units?

# In[ ]:


# define the simulation conditions

total_duration = 2 #seconds
dt = 0.01 #seconds

# set up the simulation items
time = np.linspace(0,total_duration,int(total_duration/dt))
stimulus = np.zeros((int(total_duration/dt)))
stimulus[int(delay/dt):int((delay+duration)/dt)]=amplitude
V_record = np.zeros((int(total_duration/dt)))


# use the simulation function to get V_record

V_record = simulate_V(V,R,C)

# write the "for" loop


plt.plot(time,V_record/1000);
plt.ylabel='millivolt'
plt.xlabel='seconds'


# In[ ]:


C


# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to genrate an interactive widget using the model you just created.

# Create a figure widget using plotly
f = go.FigureWidget(layout=go.Layout(height=500, width=700))

# define the initial conditions
R = 100*1e6 # Ohm (in terms of megaohms)
tau = 10*1e-3 # seconds (in terms of milliseconds)
C = tau/R # Farads 

# set up the applied current
delay = 0.5 #seconds
duration = 1 #seconds
# amplitude = 100*1e-12 #Amps (in terms of picoamps)

# print(R,tau,C,amplitude)

# define the simulation conditions
total_duration = 2 #seconds
dt = 0.001 #seconds

# set up the vectors for time and simulation results
time = np.linspace(0,total_duration,int(total_duration/dt))-delay
V_record = np.zeros((int(total_duration/dt))) # assumes voltage starts at zero

# add simulation vectors to the figure widget
f.add_trace(go.Scatter(x = time, y = V_record,
                             name='simulation',opacity=1))

# Create sliders for the figure widget inputs
E_slider = widgets.FloatSlider(
    min=-100,
    max=100,
    value=0,
    step= 10,
    readout=True,
    description='eq. Voltage (millivolts)')
E_slider.layout.width = '600px'

R_slider = widgets.FloatSlider(
    min=0,
    max=1000,
    value=100,
    step= 10,
    readout=True,
    description='R (MOhm)')
R_slider.layout.width = '600px'

tau_slider = widgets.FloatSlider(
    min=1,
    max=100,
    value=10,
    step= 1,
    readout=True,
    description='tau (msec)')
tau_slider.layout.width = '600px'

amplitude_slider = widgets.FloatSlider(
    min=0,
    max=500,
    value=100,
    step= 1,
    readout=True,
    description='I (pA)')
amplitude_slider.layout.width = '600px'

def apply_current(E,R,tau,amplitude):# set up the simulation items
    E = E*1e-3 # convert from millivolts to volts
    V = E # start the simulation at equilibrium
    R = R*1e6 # convert from MegaOhm to Ohm
    tau = tau*1e-3 # convert from milliseconds to seconds
    amplitude = amplitude*1e-12 # Convert from picoAmps to Amps
    C = tau/R
    
    # print(R,tau,C,amplitude)   
    
    time = np.linspace(0,total_duration,int(total_duration/dt))-delay
    stimulus = np.zeros((int(total_duration/dt)))
    stimulus[int(delay/dt):int((delay+duration)/dt)]=amplitude
    V_record = np.zeros((int(total_duration/dt)))

    # write the "for" loop

    for i,current in enumerate(stimulus):
        dV = dt*((current - (V-E)/R)/C)
        V = (V+dV) 
        V_record[i]=V

    f.data[0].x = time
    f.data[0].y = V_record*1e3 # convert from Volts to milliVolts

vb = VBox((f, interactive(apply_current,
                          E=E_slider,
                          R=R_slider, 
                          tau=tau_slider,
                          amplitude=amplitude_slider)))
vb.layout.align_items = 'center'
vb


# <a id="three"></a>
# # Spiking
# 
# [toc](#toc)

# In[ ]:


soma = h.Section(name="soma")


# In[ ]:


soma.psection()


# In[ ]:


soma.L = 20
soma.diam = 20


# In[ ]:


soma.insert('hh')


# In[ ]:


iclamp = h.IClamp(soma(0.5))


# In[ ]:


print([item for item in dir(iclamp) if not item.startswith("__")])


# In[ ]:


iclamp.delay = 2
iclamp.dur = 0.2
iclamp.amp = 0.9


# In[ ]:


soma.psection()


# In[ ]:


v = h.Vector().record(soma(0.5)._ref_v)  # Membrane potential vector
t = h.Vector().record(h._ref_t)  # Time stamp vector


# In[ ]:


h.load_file("stdrun.hoc")


# In[ ]:


h.finitialize(-65 * mV)


# In[ ]:


h.continuerun(40 * ms)


# In[ ]:


f = go.Figure()
f.add_trace(go.Scatter(x = t, y = v,
                             name='simulation results',opacity=1,line_color='black'))
f.update_layout(height=600, width=800,
               xaxis_title="time(seconds)", 
                  yaxis_title='amplitude (volts)')



# In[ ]:


class BallAndStick:
    def __init__(self, gid):
        self._gid = gid
        self._setup_morphology()
        self._setup_biophysics()

    def _setup_morphology(self):
        self.soma = h.Section(name="soma", cell=self)
        self.dend = h.Section(name="dend", cell=self)
        self.dend.connect(self.soma)
        self.all = self.soma.wholetree()
        self.soma.L = self.soma.diam = 12.6157 * µm
        self.dend.L = 200 * µm
        self.dend.diam = 1 * µm

    def _setup_biophysics(self):
        for sec in self.all:
            sec.Ra = 100  # Axial resistance in Ohm * cm
            sec.cm = 1  # Membrane capacitance in micro Farads / cm^2
        self.soma.insert("hh")
        for seg in self.soma:
            seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
            seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
            seg.hh.gl = 0.0003  # Leak conductance in S/cm2
            seg.hh.el = -54.3 * mV  # Reversal potential
        # Insert passive current in the dendrite                       # <-- NEW
        self.dend.insert("pas")  # <-- NEW
        for seg in self.dend:  # <-- NEW
            seg.pas.g = 0.001  # Passive conductance in S/cm2        # <-- NEW
            seg.pas.e = -65 * mV  # Leak reversal potential             # <-- NEW

    def __repr__(self):
        return "BallAndStick[{}]".format(self._gid)


# In[ ]:


my_cell = BallAndStick(0)


# In[ ]:


for sec in h.allsec():
    print("%s: %s" % (sec, ", ".join(sec.psection()["density_mechs"].keys())))


# In[ ]:


h.topology()


# In[ ]:


my_cell.soma.wholetree()


# In[ ]:


h.PlotShape(False).plot(plt)


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
