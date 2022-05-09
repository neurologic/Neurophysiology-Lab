# Lab Manual

Muscle receptor organs (MROs) contain sensory neurons that depolarize in response to muscle stretch. In crayfish, 
the superficial extensor muscle on each side of each abdominal segment (and in the two most posterior thoracic segments) are innervated by stretch-sensitive receptors. The superficial extensor muscles span adjacent segments, running from the middle of one tergite to the back edge of the next most anterior tergite. When these muscles contract, they pull the tergites together, causing the abdomen to straighten and extend (thus the name). Conversely, when the abdomen is curled ventrally, the tergites rotate around their joints and the extensor muscles are stretched, along with their associated MROs. MRO neurons receive inhibitory synaptic innervation from the central ganglion (this does not occur in vertebrate proprioceptors). These inhibitory inputs depress the receptor activity.

Importantly, there are only two MRO cell types innervating each segmental superficial extensor muscle in crustaceans. The axons of the two MROs travel together from their dorsal muscles, laterally around the large abdominal muscles, to the ventral nerve cord to enter the abdominal ganglia as part of the second ganglionic nerve (nerve 2).

You will record extracellularly from nerve 2 while curling the tail to stimulate these receptors. This recording will allow you to determine the stimulus-response tuning curve (sensory coding) of the MROs (including their adequate stimulus), and measure the adaptation rate of the MROs. 


## Software Setup
The bonsai script for today has one measurement node. <b>Channel 0</b> receives amplified and digitized input from the differential measurement electrodes (referenced to a "ground"). The parameters of the analog input node can be adjusted to specify the NiUSB sampling rate, voltage range, and buffering rate (for visualization). Use a sampling rate of 30kHz. Adjust the voltage range as needed to maximize the signal resolution if needed once you start measuring voltage signals from the leg (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering rate according to your visualization preferences. 

## Surgery
For this lab, you will be removing the tail from a crayfish. A major benefit of targetting the MRO for measurement is that crude surgical techniques work better than fine surgincal techniques. 

## Physiology Setup



<a id="experiment"></a>
## Core Experiment
<ol>
<li>From an anaesthetized crayfish, cut off the tail.</li>
<li>Cut along the ventral edge of the carapace to remove the ventral surface.</li>
<li></li>
<li></li>
<li></li>
<li>Run the bonsai protocol (with the <b>write node</b> <font color = 'red'>disabled</font> and the <b>analog input node</b> <font color = 'green'>enabled</font>). Double click the analog input node to visualize the measurement if it does not pop up upon start.</li>
<li></li>
<li></li>
<li>Stimulation Protocol:</li>
<ol>
<li></li>
<li></li>
<li>Restart the Bonsai protocol with the <b>write node</b> <font color = 'green'>enabled</font>. Change the filename as needed.</li>
<li>Rotate the knob to its retracted position and leave for 2 seconds before protracting.</li>
<li>Repeat the stimulation 10 times, with care to rotate the knob the same amount each time.</li>
</ol> 
<li>Repeat the Stimulation Protocol with a second spine using the same stimulus protraction distance. Note which two spines you chose to compare and why you chose them.</li>
</ol>

## Extended Exploration
If there is time, repeat [the core experiment](#experiment) but select one of the following questions to explore:
<ul>
<li>Do different spines have different response properties</li>
<li>Does the spine response differ based on manual versus manipulator-controlled stimulation</li>
<li>The effect of relative electrode location on measured response to the same barb stimulus</li>
	</ul>
"Response properties" include: spike amplitude, spike shape, rate, regularity, etc.

## Copy data to your Google Drive for analysis
Use the [Sensory Coding](../week-4/Sensory-Coding.ipynb) notebook to analyse your data and answer the questions in the [Responses](../week-4/Sensory-Coding_Responses.ipynb) notebook.

