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

# In[ ]:


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
import ipywidgets as widgets # interactive display

import matplotlib.pyplot as plt
from IPython.display import display
from datetime import datetime,timezone,timedelta
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
# use NMA plot style
plt.style.use("https://raw.githubusercontent.com/NeuromatchAcademy/course-content/master/nma.mplstyle")
my_layout = widgets.Layout()


def monoExp(x, m, t, b):
    return m * np.exp(-x / t) + b

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


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


# Plug in the values that you used in your circuit membrane model (<a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/passive-membrane-models/Lab-Manual_passive-membrane-models.ipynb" target="_blank" rel="noopener noreferrer">Part I</a>). Do your computational model results match your electric circuit model results?

# In[ ]:


Rk = 100
Rna = 100
Ek = -90
Ena = 130

V = get_V(Rk,Rna,Ek,Ena)
print(V)


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


#@title {display-mode: "form"}

#@markdown **TASK:** Run this cell to enable the interactive plot
#@markdown that helps you explore the effect of intrinsic physiology on neuron behavior. 

def default_pars(**kwargs):
    pars = {}

    # typical neuron parameters#
    pars['V_th'] = -55.     # spike threshold [mV]
    pars['V_reset'] = -75.  # reset potential [mV]
    pars['tau_m'] = 10.     # membrane time constant [ms]
    pars['g_L'] = 10.       # leak conductance [nS]
    pars['V_init'] = -75.   # initial potential [mV]
    pars['E_L'] = -75.      # leak reversal potential [mV]
    pars['tref'] = 2.       # refractory time (ms)

    # simulation parameters #
    pars['T'] = 400.  # Total duration of simulation [ms]
    pars['dt'] = .1   # Simulation time step [ms]

    # external parameters if any #
    for k in kwargs:
        pars[k] = kwargs[k]

    pars['range_t'] = np.arange(0, pars['T'], pars['dt'])  # Vector of discretized time points [ms]

    return pars

def plot_volt_trace(pars, v, sp):
    """
    Plot trajetory of membrane potential for a single neuron

    Expects:
    pars   : parameter dictionary
    v      : volt trajetory
    sp     : spike train

    Returns:
    figure of the membrane potential trajetory for a single neuron
    """

    V_th = pars['V_th']
    dt, range_t = pars['dt'], pars['range_t']
    if sp.size:
        sp_num = (sp / dt).astype(int) - 1
        v[sp_num] += 40  # draw nicer spikes
    plt.clf()
    plt.plot(pars['range_t'], v, 'b')
    plt.axhline(V_th, 0, 1, color='k', ls='--')
    plt.xlabel('Time (ms)',fontsize=14)
    plt.ylabel('V (mV)',fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(['Membrane\npotential', r'Threshold V$_{\mathrm{th}}$'],
             loc=[1.05, 0.75])
    plt.ylim([-90, -20])
    plt.show()
    
def run_LIF(pars, Iinj, stop=False, durstep=100):
    """
    Simulate the LIF dynamics with external input current
    Args:
    pars       : parameter dictionary
    Iinj       : input current [pA]. The injected current here can be a value
                 or an array
    stop       : boolean. If True, use a current pulse
    Returns:
    rec_v      : membrane potential
    rec_sp     : spike times
    """

    # Set parameters
    V_th, V_reset = pars['V_th'], pars['V_reset']
    tau_m, g_L = pars['tau_m'], pars['g_L']
    V_init, E_L = pars['V_init'], pars['E_L']
    dt, range_t = pars['dt'], pars['range_t']
    fs = 1/dt
    Lt = range_t.size
    tref = pars['tref']

    # Initialize voltage
    v = np.zeros(Lt)
    v[0] = V_init

    # Set current time course
    Iinj = Iinj * np.ones(Lt)
    durstep = int((durstep*fs)/2)
    # If current pulse, set beginning and end to 0
    if stop:
        # Iinj[:int(len(Iinj) / 2) - (int(durstep/pars['dt'])/2)] = 0
        # Iinj[int(len(Iinj) / 2) + (int(durstep/pars['dt'])/2):] = 0

        Iinj[:int(len(Iinj) / 2) - durstep] = 0
        Iinj[int(len(Iinj) / 2) + durstep:] = 0

    # Loop over time
    rec_spikes = []  # record spike times
    tr = 0.  # the count for refractory duration

    for it in range(Lt - 1):

        if tr > 0:  # check if in refractory period
            v[it] = V_reset  # set voltage to reset
            tr = tr - 1 # reduce running counter of refractory period

        elif v[it] >= V_th:  # if voltage over threshold
            rec_spikes.append(it)  # record spike event
            v[it] = V_reset  # reset voltage
            tr = tref / dt  # set refractory time

        # Calculate the increment of the membrane potential
        dv = (-(v[it] - E_L) + Iinj[it] / g_L) * (dt / tau_m)

        # Update the membrane potential
        v[it + 1] = v[it] + dv

    # Get spike times in ms
    rec_spikes = np.array(rec_spikes) * dt

    return v, rec_spikes




my_layout.width = '700px'
# my_layout.description_width = 'initial'
style = {'description_width': 'initial'}
@widgets.interact(
    current_injection=widgets.FloatSlider(50., min=0., max=1000., step=2.,
                               layout=my_layout,style=style),
    Simulation_Duration=widgets.FloatSlider(400., min=0., max=1000., step=10.,
                               layout=my_layout,style=style),
    Injection_Step=widgets.Checkbox(value=True,
                               description='current step (vs continuous)',
                               layout=my_layout,style=style),
    Current_Step_Duration=widgets.FloatSlider(100., min=10, max=200., step=2.,
                               layout=my_layout,style=style),
    Leak_Reversal=widgets.FloatSlider(-75., min=-90, max=-30., step=2.,
                               layout=my_layout,style=style),
    Leak_Conductance=widgets.FloatSlider(10., min=1, max=50., step=2.,
                               layout=my_layout,style=style),
    AHP_Voltage=widgets.FloatSlider(-80., min=-90., max=-30.,step=2.,
                               layout=my_layout,style=style),
    Spike_Threshold=widgets.FloatSlider(-55., min=-100., max=-30., step=2.,
                               layout=my_layout,style=style),
    Membrane_Tau=widgets.FloatSlider(5., min=1., max=15., step=1.,
                               layout=my_layout,style=style)
)


def diff_DC(current_injection,
            Simulation_Duration,
            Injection_Step,
            Current_Step_Duration,
            Leak_Reversal,
            Leak_Conductance,
            AHP_Voltage,
            Spike_Threshold,
            Membrane_Tau): #I_dc=200., tau_m=10.):
    # pars = default_pars(T=100.)
    # pars['tau_m'] = tau_m
    pars = default_pars(
      E_L = Leak_Reversal,
      g_L = Leak_Conductance,
      V_init = Leak_Reversal,
      V_reset = AHP_Voltage,
      V_th = Spike_Threshold,
      tau_m = Membrane_Tau,
      T=Simulation_Duration)
    # pars=default_pars()
    v, sp = run_LIF(pars, Iinj=current_injection,stop=Injection_Step,durstep=Current_Step_Duration)
    plot_volt_trace(pars, v, sp)

print('Interactive demo initiated at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:





# <a id="setup"></a>

# <a id="one"></a>

# <a id="two"></a>

# <a id="three"></a>

# <a id="four"></a>
