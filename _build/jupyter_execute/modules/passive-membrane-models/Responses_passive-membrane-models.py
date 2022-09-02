#!/usr/bin/env python
# coding: utf-8

# # Responses
# 
# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/passive-membrane-models/Responses_passive-membrane-models.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   
# 
# Markdown cells awaiting your responses to the following questions contain ```...```
# 
# Edit these cells by replacing ```...``` with your responses. 
# 
# ---

# ***NAME***:

# ...

# ***Prompt 1:** What is the biological equivalent of the resistors in the neuron membrane model from **Part I**?*

# ...

# ***Prompt 2:** What is the biological equivalent of each set of resistors (Rinside, Routside, Rmembrane) in the neuron membrane model from **Part II and III**?*

# ...

# ***Prompt 3:** What is the biological equivalent of the battery (the voltage applied across the membrane) in the neuron membrane model from **Part II and III**?*

# ...

# ***Prompt 4:** When a set of ion channels (selective for Potassium, for example) opens, what happens to the resistance of the membrane?*

# ...

# ***Prompt 5:** In neurophysiology we often talk about ion channel conductance ($g$) rather than resistance ($R$), where $R = 1/g$. How did the balance between the two conductances in the neuron membrane model from **Part I** effect the voltage across the cell membrane?*

# ...

# ***Prompt 6:** What part of the action potential were you simulating in **Part II and III** of the lab (modeling intracellular versus extracellular recordings). And which active ion conductance did this most closely simulate?*

# ...

# ***Prompt 7:** In **Part II and III**, what was the scaling factor between the measured peak amplitude in intracellular versus extracellular recording configuration (extracellular amplitude divided by intracellular amplitude)?*

# ...

# ***Prompt 8:** The *space constant* is the distance it takes for voltage to change by 63% from its original value. Approximate the space constant (in arbitrary "node" units) of the model membrane using the intracellular measurements of membrane potential (**Part I**) as the battery source travelled down the "axon".  
# First, calculate the space constant first by starting at Node \#5 (the middle node).  
# Then, calculate it by starting at Node \#7.*

# ...

# ***Prompt 9:** The space constant can also be calculated using the following equation:*
# 
# $$
# \lambda = \sqrt{\frac{ R_{m} }{ R_{i} + R_{o} }}
# $$
# 
# *What value do you get from calculating this way?*

# ...

# ***Prompt 10:** Note that $R_{o}$ is usually so small compared to the other resistances that it can be ignored when estimating neuron space constants. Why do you think it is so much smaller? In other words, what makes $R_{i}$ large compared to $R_{o}$? And what makes $R_{m}$ large compared to $R_{o}$?)*

# ...

# ***Prompt 11:** Axons of different types of neurons have different diameters. Why, based on the space constant, would spikes travel faster along axons with a larger cross-section diameter?*

# ...

# ***Prompt 11:** What caused the change in polarity in your membrane potential measurement in **Part III** (and why did the polarity not change in **Part II**)? If you did not observe a polarity change or if you observed a polarity change in both configurations, make note of that.*

# ...

# ***Prompt 12:** Think back to your other neuroscience courses. Draw a typical neuron's action potential and describe what physiological events across the cell membrane cause the following components of the waveform shape:*
# - *baseline (resting) voltage*
# - *polarity*
# - *change in polarity*
# - *amplitude* 
#     
# ```{hint} 
# Insert an image from your google drive in a markdown cell by doing the following... 
# 
# Get the "Anyone can view" share link from google drive. 
# With a  share link in the following format: https://drive.google.com/file/d/ID-of-image-/view?usp=sharing,
# all you need is the *ID-of-image* from the URL share link. 
# 
# Enter editing mode on the Markdown cell below.
# 
# In the template URL provided, replace "1WoAa-oMOkAj9r9lyls4nLSLyIeuTu4Ae" with the ID from the link you see in your google drive's "share link" screen for your image.
# 
# Then "run" the markdown cell (or double click it). Your image will replace the one provided.
# 
# ```

# ...
# 
# <img src='https://drive.google.com/uc?id=1WoAa-oMOkAj9r9lyls4nLSLyIeuTu4Ae' width="300" >

# ***Prompt** Based on what you observed today, what effects each of the following two features of the action potential waveform shape in your measurement/recording of the neuron membrane?: 1. polarity and 2. amplitude*
# 

# ...

# ***Prompt 13:** What was different between the membrane potential response to (the same) applied current **with** verusus **without** a capacitor in the circuit? What was the same between the membrane potential response to (the same) applied current **with** verusus **without** a capacitor in the circuit?

# ...

# ***Prompt 14:** Would you expect small neurons to have higher or lower membrane resistance than large neurons? Why?*

# ...

# ***Prompt 15:** One of the most used equations in neurophysiology is $V=IR$, where $V$ is voltage, $R$ is resistance, and $I$ is current. Use your experiences from this lab to describe a key experiment that would enable you to test your prediction in Prompt 13 by calculating the membrane resistance of a neurons with known sizes.*

# ...

# ***Prompt 16:** Would you expect small neurons to have higher or lower capacitance than large neurons? Why?*

# ...

# ***Prompt 17:** Another well-loved neurophysiology equation is $\tau=RC$, where $R$ is resistance and $C$ is capacitance, and $\tau$ is the time constant of the membrane. Analagous to the *space constant*, the *time constant* is the time it takes for the membrane potential to change by 63% of its original value in response to an applied current across the membrane. Use the tools you learned in this lab to describe a key experiment that would enable you to test your prediction in Prompt 15 by calculating the membrane capacitance of neurons with known sizes.*

# ...

# In[ ]:




