#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/modules/passive-membrane-models/Lab-Manual_passive-membrane-models.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a>   

# # Responses
# 
# Markdown cells awaiting your responses to the following questions contain ```...```
# 
# Edit these cells by replacing ```...``` with your responses. 
# 
# ---

# What is the biological equivalent of the resistors in the active neuron membrane model?

# ...

# What is the biological equivalent of the resistors in the passive axon model?

# ...

# What is the biological equivalent of the battery in the passive axon model?

# ...

# When a set of ion channels (selective for Potassium, for example) opens, what happens to the *resistance* of the membrane?

# ...

# When a set of ion channels (selective for Potassium, for example) opens, what happens to the *conductance* of the membrane?

# ...

# How does the balance between potassium and sodium *conductance* effect the voltage across the cell membrane?

# ...

# What part of the action potential were you simulating in **Part II and III** of the lab (modeling intracellular versus extracellular recordings). And which active ion conductance did this most closely simulate?

# ...

# In **Part II and III**, what was the scaling factor for the measured peak amplitude between the intracellular and extracellular configuration (extracellular amplitude divided by intracellular amplitude)?

# ...

# The *space constant* is the distance it takes for voltage to decrease to 63% of its original value. Approximate the space constant of the model membrane using the intracellular measurements of trans-"membrane" voltage as the battery source travelled down the "axon".
# Calculate it first by starting at Node \#5 (the middle node) and then calculate it again by starting at Node \#7.

# ...

# The space constant can also be calculated using the following equation:
# 
# $$
# \lambda = \sqrt{\frac{ R_{m} }{ R_{i} + R_{o} }}
# $$
# 
# What value do you get from calculating this way? 
# > Note that $R_{o}$ is usually so small compared to the other resistances that it can be ignored. (Why do you think it is so much smaller? In other words, what makes $R_{i}$ larger? And $R_{m}$?)
# 

# ...

# What caused the change in polarity in your recording of the membrane potential in **Part III** (and why did the polarity not change in **Part II**)? If you did not observe a polarity change or if you observed a polarity change in both configurations, make note of that. 

# ...

# Think back to your other neuroscience courses. Draw a typical neuron's action potential and describe what physiological events across the cell membrane cause the following components of the waveform shape: 
# - baseline (resting) voltage
# - polarity
# - change in polarity
# - amplitude 
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
# In the template URL provided, replace *1WoAa-oMOkAj9r9lyls4nLSLyIeuTu4Ae* with the ID from the link you see in your google drive's "share link" screen for your image.
# 
# Then "run" the markdown cell (or double click it). Your image will replace the one provided.
# 
# ```

# ...
# 
# <img src='https://drive.google.com/uc?id=1WoAa-oMOkAj9r9lyls4nLSLyIeuTu4Ae' width="300" >

# Would you expect small neurons to have higher or lower membrane resistance than large neurons? Why?

# ...

# One of the most useful equations in neuroscience is $V=IR$, where $V$ is voltage, $R$ is resistance, and $I$ is current. How could you calculate the membrane resistance of a neurons with known sizes to test your prediction? What experiment would you need to do?

# ...

# Would you expect small neurons to have higher or lower capacitance than large neurons? Why?

# ...

# If you knew that $\tau=RC$, where $R$ is resistance and $C$ is capacitance, how could you calculate the membrane capacitance of a neurons with known sizes to test your prediction? What experiment would you need to do?

# ...

# In[ ]:




