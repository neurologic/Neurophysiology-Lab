# Lab Manual

## TO DO

solder coated silver-chlorided wires to stimulating electrodes and tank recording electrodes.  
chloride tips  
liquid electrical tape up to tips

## Introduction

Today you will again be using weakly electric fish and recording voltage in their tank using two sets of differential electrodes. You will also be presenting an electrical stimulus to the fish via a pair of electrodes controlled by a "stimulus isolation unit" (SIU). The SIU controls the voltage across the two output leads (which in this experiment provides a dipole source). 

## Software Setup
The bonsai script for today has two measurement nodes. 
1. <b>Node 1</b> is for SIU setup only and contains no "write" node. Channel 0 receives a copy of the SIU voltage command sent to the dipole stimulus electrodes. 
2. <b>Node 2</b> is for data collection:
	- <b>Channel 0</b> receives a copy of the SIU voltage command sent to the dipole stimulus electrodes. 
	- <b>Channels 1 and 2</b> receive input from the two sets of perpindicularly-oriented differential tank electrodes.

## SIU setup
1. Turn the voltage down to 0.
2. Set the stimulus duration to <input type="text">.
3. Set the stimulus frequency to <input type="text">.
4. Run the bonsai protocol (with the Node 2 pathway <font color = 'red'>disabled</font>). Double click the Node 1 pathway input node to visualize the measurement if it does not pop up upon start.
5. Slowly turn the voltage nob up until you start to see the stimulus amplitude register. 
```{warning}
If the SIU voltage = 1 and you do not see anything in bonsai, <font color = 'red'>DO NOT</font> turn the voltage any higher. Return the voltage to 0 and ask for help. 
```
6. Note the dial position on the SIU that corresponds to a measured voltage of 1 Volt. 
```{warning}
Do not exceed this voltage (do not go past this position on the voltage nob) during the experiment. 
```

<a id="experiment"></a>
## Core Experiment
1. Turn the voltage down to 0.
2. Set the stimulus duration to <input type="text">.
3. Set the stimulus frequency to <input type="text">.
4. Run the bonsai protocol (with the Node <b>1</b> pathway <font color = 'red'>disabled</font> and the Node <b>2</b> pathway <font color = 'green'>enabled</font>). Make sure the "write" node in pathway 2 is enabled and that the filename is set correctly. Double click the Node 2 pathway input node to visualize the measurement if it does not pop up upon start.
5. Wait _____ seconds (should be 10 repetitions) of the stimulus at 0 volts.
6. Turn the voltage nob up a little bit (about 1/10th of the way to the final amplitude corresponding to 1V) and let it run for about 10 repetitions of the stimulus. 
```{warning}
Do not exceed 1V on the SIU output. 
```
6. Increase the voltage until the dial position on the SIU that corresponds to the pre-measured position corresponding to 1 Volt. 
```{warning}
Do not exceed this voltage (do not go past this position on the voltage nob) during the experiment. 
```

## Experiment Supplement
If you have time, repeat [the core experiment](#experiment) but vary the stimulus duration instead of the amplitude. What amplitude do you think you should use? 
```{note}
If you are doing this supplemental experiment, change the filename to a name that you can distinguish from the filenames from your other experiment. 
```

## Copy data to your Google Drive for analysis
Use the [Experimental Design for Analysiis](../week-3/Experimental-Design-for-Analysis.ipynb) notebook to analyse your data and answer the questions in the [Responses](../week-3/Experimental-Design-for-Analysis_Responses.ipynb) notebook.
