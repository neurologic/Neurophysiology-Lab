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
# Many of these questions should be review from your previous neuroscience courses. Do the best you can with reasoning through any problems that we did not end up discussing during class. You can work with others in this course to review material and discuss the questions. 
# 
# ---

# ***NAME***:

# ...

# ***Prompt 1: What is the biological equivalent of the resistors in the neuron membrane model from Part I?***

# ...

# ***Prompt 2: What is the biological equivalent of each set of resistors (Rinside, Routside, Rmembrane) in the neuron membrane model from Part II and III?***

# ...

# ***Prompt 3: What is the biological equivalent of each battery (the voltage applied across the membrane) in the neuron membrane model from Part I?***

# ...

# ***Prompt 4: What is the biological equivalent of the battery (the voltage applied across the membrane) in the neuron membrane model from Part II and III?***

# ...

# ***Prompt 5: When a set of ion channels (selective for Potassium, for example) opens, what happens to the resistance of the membrane?***

# ...

# ***Prompt 6: In neurophysiology we often talk about ion channel conductance ($g$) rather than resistance ($R$), where $R = 1/g$. How did the balance between the two conductances ($g$) in the neuron membrane model from Part I effect the voltage across the cell membrane?***

# ...

# ***Prompt 7: What part of the action potential were you simulating in Part II and III (when you compared intracellular versus extracellular recordings)?***

# ...

# ***Prompt 8: In Part II and III, what was the scaling factor between the measured peak amplitude in intracellular versus extracellular recording configuration (extracellularly measured peak amplitude divided by intracellularly measured peak amplitude)?***

# ...

# ***Prompt 9: The space constant is the distance in space it takes for voltage to change by 63% from its original value. Approximate the space constant (in arbitrary "node" units) of the model membrane using the intracellular measurements of membrane potential (Part II) as the voltage peak travelled down its length.***  
# 1. ***calculate the space constant by starting at Node \#5 (the middle node).***
# 2. ***calculate the space constant by starting at Node \#7.***

# ...

# ***Prompt 10: The space constant can also be calculated using the following equation:***
#     $$
#     \lambda = \sqrt{\frac{ R_{membrane} }{ R_{inside} + R_{outside} }}
#     $$
# ***What value do you get from calculating this way?***

# ...

# ***Prompt 11: $R_{outside}$ is usually so small compared to the other resistances that it can be ignored when estimating the space constant. Why do you think it is so much smaller? In other words, what makes $R_{inside}$ large compared to $R_{outside}$? And what makes $R_{membrane}$ large compared to $R_{outside}$?)***

# ...

# ***Prompt 12: Axons of different types of neurons have different diameters. Why, based on the space constant, would action potentials travel faster along axons with a larger cross-section diameter?*** 

# ...

# ***Prompt 13: Think back to your other neuroscience courses. Draw a typical neuron's action potential and describe what physiological events across the cell membrane cause the following components of the waveform shape:***
# 1. ***depolarization***
# 2. ***change in polarity ("after-hypoerpolarization")***
#     
# ```{admonition} How To 
# Insert an image from your google drive in a markdown cell by doing the following... 
# 
# Get the "Anyone can view" share link from google drive. 
# With a  share link in the following format: https://drive.google.com/file/d/ID-of-image-/view?usp=sharing,
# all you need is the *ID-of-image* from the URL share link. 
# 
# Enter editing mode on the Markdown cell below.
# 
# In the template URL provided, replace "1WoAa-oMOkAj9r9lyls4nLSLyIeuTu4Ae" with the ID from the link you see in your google drive's "share link" for your image.
# 
# Then "run" the markdown cell (or double click it). Your image will replace the one provided.
# 
# ```

# ...
# 
# <img src='https://drive.google.com/uc?id=1WoAa-oMOkAj9r9lyls4nLSLyIeuTu4Ae' width="300" >

# ***Prompt 14: What caused the change in polarity in your membrane potential measurement for the extracellular recording in Part III (and why did the polarity not change for the intracellular recording in Part II)? If you did not observe a polarity change or if you observed a polarity change in both configurations, make note of that. Include a diagram if it helps you explain more concisely.***

# ...
# 
# <img src='https://drive.google.com/uc?id=1WoAa-oMOkAj9r9lyls4nLSLyIeuTu4Ae' width="300" >

# ***Prompt 15: Based on what you observed today, what modulates each of the following two features of the action potential waveform shape when measuring the membrane potential of a neuron?*** 
# 1. ***polarity*** 
# 2. ***amplitude***
# 

# ...

# ***Prompt 16: What was different between the membrane potential response to (the same) applied current with verusus without a capacitor in the circuit? What was the same between the membrane potential response to (the same) applied current with verusus without a capacitor in the circuit?***

# ...

# ***Prompt 17: Would you expect small neurons to have higher or lower membrane resistance than large neurons? Why?***

# ...

# ***Prompt 18: Would you expect small neurons to have higher or lower capacitance than large neurons? Why?***

# ...

# ***Prompt 19: Analagous to the space constant, the time constant of a neuron membrane is the time it takes for the membrane potential to change by 63% of its original value in response to an applied current across the membrane. Calculate the time constant of the model membrane in Part IV.*** 

# ...

# ***Prompt 20: One of the most used equations in neurophysiology is $V=IR$, where $V$ is voltage, $R$ is resistance, and $I$ is current. Another well-loved neurophysiology equation is $\tau=RC$, where $R$ is resistance and $C$ is capacitance, and $\tau$ is the time constant of the membrane. Refer to your results from Part IV to complete the following (show your work):***
# 1. ***Use the amplitude of the experimentally-applied stimulus current and the corresponding measured change in voltage to calculate the model membrane's Resistance (compare your result to the value of the resistor tha that you used). NOTE: make sure to account for the amplifier's amplification factor.***
# 2. ***Use the time constant that you measured and the resistance that you calculated from \#1 to calculate the capacitance of the model membrane (compare your result to the value of the capacitor that you used).*** 
# 
# 

# ...
