#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/computational-model/Data-Explorer_computational-model.ipynb" target="_blank" rel="noopener noreferrer"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# # Data Explorer

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Computer implementation of computational models](#function)
# - [Steady State Model](#steady-state)
# - [Dynamic Model](#dynamic-model)
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
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime,timezone,timedelta
pal = sns.color_palette(n_colors=15)
pal = pal.as_hex()

from ipywidgets import interactive, HBox, VBox, widgets, interact
import ipywidgets as widgets # interactive display

import matplotlib.pyplot as plt
from datetime import datetime,timezone,timedelta
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
# use NMA plot style
plt.style.use("https://raw.githubusercontent.com/NeuromatchAcademy/course-content/master/nma.mplstyle")
my_layout = widgets.Layout()

print('Task completed at ' + str(datetime.now(timezone(-timedelta(hours=5)))))


# <a id="functions"></a>
# # Computer implementation of computational models
# 
# To implement this computational model in computer code, you need to *define a **function***. 
# 
# A ***function*** in computer programming is *executable* code (it will do things when you "run" it). Functions *take* information that they need to do what they need to do. 
# 
# As an analogy, your computational model is a function (an equation in this case). You *executed* that function when you were given values for ion equilibrium potential and resistance of a neuron and calculate the neuron's resting membrane potential. 
# 
# To define a function in python so that the computer can execute it, we need to write down instructions in a specific way:
# 
# ```
# def function_name( parameters ):
#    variable = equation
#    return [variable]
# ```
# 
# - **def** indicates that we are defining a function
# - **function_name** is the name we give the function
# - in parentheses after the function name, we list the information that will be provided to the function when it is executed (these are info that will be needed to do what we want the function to do... in this case calculate the resting membrane potential of a neuron)
# - **:** transitions the code into the instructions for the function to follow when it is executed
# - the instructions for the function to execute are on the rest of the written lines, with each line indented
# - **return** terminates the function and provides information that can be accessed after the function executes
# 
# Let's consider a basic function that calculates the square of a number (the number times itself).  
# Examine the contents of the following code cell and then *run* the code cell to execute the definition of the function (this step actually creates the function that is defined with the text)

# In[ ]:


def square(x):
    result = x*x
    return result


# Nothing obvious will happen when you run a code cell that defines a function (other than an indication that the code cell ran). But... you can now use the function that you defined.  
# In the code cell below, assign a number to the varable ```my_number```. Then, run the code cell to execute that variable assignment.

# In[ ]:


my_number = 2


# Now, in the next code cell, we will execute that function by typing the name of the function followed by parentheses containing the variable *my_number* (to provide the function with that information).  
# Examine the code cell below and then run it. 

# In[ ]:


square(my_number)


# The function executes and returns the result of the instructions that it followed. In this case, the result is printed below the code cell, but can be assigned to another variable name by typing ```result = square(my_number)```.

# <a id="steady-state"></a>
# # Steady State Model
# 
# [toc](#toc)

# You created a computational model of the steady state membrane potential that depends on the equilibrium potential and resistance of two ion conductances. To implement this computational model in computer code, you need to *define a function* that computes Vin based on your computational model equation. In the following code cell, replace ```...``` with the equation from your computational model that defines $V_{in}$. 

# In[ ]:


# define the function

def simulate_Vin_steady_state(E1,R1,E2,R2):
    
    Vin = ... #( (E1/R1) + (E2/R2) ) / ( (1/R1) + (1/R2) )
    
    return Vin


# In the code cell below, assign the values that you used in your circuit membrane model (<a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/passive-membrane-models/Lab-Manual_passive-membrane-models.ipynb" target="_blank" rel="noopener noreferrer">Part I</a>) to each variable needed by the function. Then, run the code cell to assign those values to the variables. 
# 

# In[ ]:


R1 = ...
R2 = ...
E1 = ...
E2 = ...


# Now, examine the contents of the code cell below and run it to simulate your computational model given the values you just provided. Note that the order of information provided to the function matters - it must match the order you defined when defining the function.

# In[ ]:


simulate_Vin_steady_state(E1,R1,E2,R2)


# Do your computational model results match your electric circuit model results?

# ## Interactive Simulation
# 
# Let's implement your computational model into a more interactive simulation that you can use to efficiently exlpore the predictions of your model. There is more to learn about computer programming in Python than we will cover here to be able to make a more interactive simulation, so I have done the coding for you. But you can click ```Show Code``` if you want to take a look if you want. 
# 
# Run the code cell below to run the interactive simulation. 

# In[ ]:


#@title {display-mode: 'form'}

#@markdown Run this code cell to genrate an interactive widget using the model you just created.


slider_E1 = widgets.FloatSlider(
    min=-100,
    max=100,
    value=0,
    step= 1,
    readout=True,
    continuous_update=False,
    description='E1 (mV)')
slider_E1.layout.width = '600px'

slider_R1 = widgets.FloatSlider(
    min=1,
    max=100,
    value=1,
    step= 1,
    readout=True,
    continuous_update=False,
    description='R1 (MOhm)')
slider_R1.layout.width = '600px'

slider_E2 = widgets.FloatSlider(
    min=-100,
    max=100,
    value=0,
    step= 1,
    readout=True,
    continuous_update=False,
    description='E2 (mV)')
slider_E2.layout.width = '600px'

slider_R2 = widgets.FloatSlider(
    min=1,
    max=100,
    value=1,
    step= 1,
    readout=True,
    continuous_update=False,
    description='R2 (MOhm)')
slider_R2.layout.width = '600px'

label_result = widgets.Label(
    value='The resting membrane potential of the neuron will be: '
)
label_result.layout.width = '600px'
display(label_result)


# a function that will modify the xaxis range
def update_result(E1,R1,E2,R2):
    Vin = simulate_Vin_steady_state(E1,R1,E2,R2)
    label_result.value= f'The resting membrane potential of the neuron will be: {Vin} mV'

w = interact(update_result, E1=slider_E1,R1 = slider_R1,E2=slider_E2,R2=slider_R2);


# <a id="dynamic-model"></a>
# # Dynamic Model
# 
# [toc](#toc)

# In[ ]:


def simulate_Vin_dynamic(E, R, C, Iapp, duration, dt):
    '''
    The simulation starts at time = 0 with the voltage given by the input to the function (V)
    E = the equilibrium potential of the net ionic conductance
    
    R = the resistance of the membrane in Ohm
    
    C = the capacitance of the membrane in Farads
    
    Iapp = the current (microAmps) applied to the system throughout the simulation
    
    duration = the total time (seconds) that the current is applied to the system (in this case also the duration of the simulation)
    
    dt = the time step (seconds) for analysing the simulation (how much time elapses between each analysis of dV)
    '''
    
    timesteps = int(duration/dt)
    
    V_record = [E]
    for i in range(timesteps): # for each time step, iterate through the simulation
        V = V_record[-1]
        dV = (Iapp - (1/R)*(V-E))*(dt/C) # how much does the voltage change by on this time step?
        V = (V+dV) # add the change in voltage to the current voltage
        V_record.append(V)
    
    return V_record


# In[ ]:


# define the initial conditions
E = -60*1e-3 # millivolts
R = 100*1e6 # MOhm
C = 100*1e-12 # pF

Iapp = 100*1e-12 #pA  0.0000000001 # Amps
duration = 0.1
dt = 0.1*1e-3 #msec

V_record = simulate_Vin_dynamic(E, R, C, Iapp, duration, dt)

plt.plot(np.linspace(0,duration,int(duration/dt)+1),V_record);
plt.xlabel('seconds');
plt.ylabel('Volts');

print(f'tau = {(R*C):0.4f} seconds')


# Note that $ 1mV = 100pA * 10MOhm $. Why would you want to think in terms of these units?

# In[ ]:


#@title {display-mode: "form"}

#@markdown Run this code cell to genrate an interactive widget using the model you just created.

# set up the applied current
delay = 0.5 #seconds
duration = 1 #seconds

# define the simulation conditions
total_duration = 2 #seconds
dt = 0.0001 #seconds

# Create sliders for the figure widget inputs
E_slider = widgets.FloatSlider(
    min=-100,
    max=100,
    value=0,
    step= 10,
    readout=True,
    description='Equilibrium Potential (mV)')
E_slider.layout.width = '600px'

R_slider = widgets.FloatSlider(
    min=0,
    max=1000,
    value=100,
    step= 10,
    readout=True,
    description='R (MOhm)')
R_slider.layout.width = '600px'

C_slider = widgets.FloatSlider(
    min=1,
    max=1000,
    value=100,
    step= 0.1,
    readout=True,
    description='C (pF)')
C_slider.layout.width = '600px'

amplitude_slider = widgets.FloatSlider(
    min=0,
    max=500,
    value=100,
    step= 1,
    readout=True,
    description='I (pA)')
amplitude_slider.layout.width = '600px'

label_tau = widgets.Label(
    value='tau = '
)
label_tau.layout.width = '600px'
display(label_tau)

def update_plot(E,R,C,amplitude):# set up the simulation items
    E = E*1e-3 # convert from millivolts to volts
    # V = E # start the simulation at equilibrium
    R = R*1e6 # convert from MegaOhm to Ohm
    # tau = tau*1e-3 # convert from milliseconds to seconds
    amplitude = amplitude*1e-12 # Convert from picoAmps to Amps
    C = C*1e-12 # convert from microfarad to farad
    
    # print(R,tau,C,amplitude)   
    
    time = np.linspace(0,total_duration,int(total_duration/dt)+1)-delay
    stimulus = np.zeros((int(total_duration/dt)))
    stimulus[int(delay/dt):int((delay+duration)/dt)]=amplitude
    V_record = np.empty((int(total_duration/dt)+1))

    # write the "for" loop
    # simulate_V(E, R, C, Iapp, duration, dt)
#     for i,current in enumerate(stimulus):
#         dV = dt*((current - (V-E)/R)/C)
#         V = (V+dV) 
#         V_record[i]=V
        
    V_record[0]=E
    for i,Iapp in enumerate(stimulus): # for each time step, iterate through the simulation
        V = V_record[i]
        dV = (Iapp - (1/R)*(V-E))*(dt/C) # how much does the voltage change by on this time step?
        V = (V+dV) # add the change in voltage to the current voltage
        V_record[i+1]=V
    
#     V_record = [V_initial]
# for i in range(timesteps): # for each time step, iterate through the simulation
#     V = V_record[-1]
#     dV = (Iapp - (1/R)*(V-0))*(dt/C) # how much does the voltage change by on this time step?
#     V = (V+dV) # add the change in voltage to the current voltage
#     V_record.append(V)
  
    # return V_record

    hfig,ax = plt.subplots(figsize=(10,5))
    # add simulation vectors to the figure widget
    ax.plot(time,V_record*1e3) # convert from Volts to milliVolts
    
    label_tau.value=f'tau = {(R*C):0.4f} seconds'


w = interact(update_plot,
             E=E_slider,
             R=R_slider, 
             C=C_slider,
             amplitude=amplitude_slider);


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
    hfig,ax = plt.subplots(figsize=(10,5),num=1)
    V_th = pars['V_th']
    dt, range_t = pars['dt'], pars['range_t']
    if sp.size:
        sp_num = (sp / dt).astype(int) - 1
        v[sp_num] += 40  # draw nicer spikes
    ax.plot(pars['range_t'], v, 'b')
    ax.axhline(V_th, 0, 1, color='k', ls='--')
    ax.set_xlabel('Time (ms)',fontsize=14)
    ax.set_ylabel('V (mV)',fontsize=14)
    # ax.set_xticks(fontsize=14)
    # ax.set_yticks(fontsize=14)
    ax.legend(['Membrane\npotential', r'Threshold V$_{\mathrm{th}}$'],
             loc=[1.05, 0.75])
    ax.set_ylim([-90, -20])

    
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
