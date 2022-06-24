# Lab Manual

[Smith Lab Manual](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L6erg.html)

## Software Setup
The bonsai script for today has one measurement node. <b>Channel 0</b> receives amplified and digitized input from the differential measurement electrodes (referenced to a "ground"). The parameters of the analog input node can be adjusted to specify the NiUSB sampling rate, voltage range, and buffering rate (for visualization). Use a sampling rate of 30kHz. Adjust the voltage range as needed to maximize the signal resolution if needed once you start measuring voltage signals from the leg (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering rate according to your visualization preferences. 

## Surgery
For this lab, you will be removing the tail from a crayfish. A major benefit of targetting the MRO for measurement is that crude surgical techniques work better than fine surgincal techniques. 

<ol>
	<li>From an anaesthetized crayfish, cut the head carapce from eye to eye.</li>
	<li>Cut off the eye at the base of the eye stalk.</li>
	<li>Place the eye stalk, nerve-side down, in the saline well of the dish and fill with saline.</li>
</ol>

## Physiology Setup



<a id="experiment"></a>
## Core Experiment

:::{note}
Try to drive a LED precicely with a constant voltage device - and/or - measure light with a photodiode or LED in reverse.
:::

1. Run the bonsai protocol (with the <b>write node</b> <font color = 'red'>disabled</font> and the <b>analog input node</b> <font color = 'green'>enabled</font>). Double click the analog input node to visualize the measurement if it does not pop up upon start.

Stimulation Protocol: 
1. Restart the Bonsai protocol with the <b>write node</b> <font color = 'green'>enabled</font>. Change the filename as needed.
2. Rotate the knob to its retracted position and leave for 5 seconds before protracting. Leave the knob protracted for 5 seconds before repeating.
3. Repeat the stimulation 5 times, with care to rotate the knob the same amount each time.

## Experimental Exploration
Effects of:
- Light duration
- Light frequency (time between)
- Onset ramp (rather than step)
- Wavelength of light

## Copy data to your Google Drive for analysis
Use the [Sensory Coding](../week-5/Sensory-Coding-MRO.ipynb) notebook to analyse your data and answer the questions in the [Responses](../week-5/Sensory-Coding-MRO_Responses.ipynb) notebook.

