# Lab Manual



Muscle receptor organs (MROs) contain sensory neurons that depolarize in response to muscle stretch. In crayfish, 
the superficial extensor muscle on each side of each abdominal segment (and in the two most posterior thoracic segments) are innervated by stretch-sensitive receptors. The superficial extensor muscles span adjacent segments, running from the middle of one tergite to the back edge of the next most anterior tergite. When these muscles contract, they pull the tergites together, causing the abdomen to straighten and extend (thus the name). Conversely, when the abdomen is curled ventrally, the tergites rotate around their joints and the extensor muscles are stretched, along with their associated MROs. MRO neurons receive inhibitory synaptic innervation from the central ganglion (this does not occur in vertebrate proprioceptors). These inhibitory inputs depress the receptor activity.

Importantly, there are only two MRO cell types innervating each segmental superficial extensor muscle in crustaceans. The axons of the two MROs travel together from their dorsal muscles, laterally around the large abdominal muscles, to the ventral nerve cord to enter the abdominal ganglia as part of the second ganglionic nerve (nerve 2).

You will record extracellularly from nerve 2 while curling the tail to stimulate these receptors. This recording will allow you to determine the stimulus-response tuning curve (sensory coding) of the MROs (including their adequate stimulus), and measure the adaptation rate of the MROs. 

You will also use this preparation to better understand how anaesthetics work.
- MS222 is a common anaesthetic used for aquatic animals <a href = "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7438171/">MS222 protocol</a>
- Ice is another common anaesthetic.


## Software Setup
The bonsai script for today has one measurement node. <b>Channel 0</b> receives amplified and digitized input from the differential measurement electrodes (referenced to a "ground"). The parameters of the analog input node can be adjusted to specify the NiUSB sampling rate, voltage range, and buffering rate (for visualization). Use a sampling rate of 30kHz. Adjust the voltage range as needed to maximize the signal resolution if needed once you start measuring voltage signals from the leg (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering rate according to your visualization preferences. 

## Surgery
For this lab, you will be removing the tail from a crayfish. A major benefit of targetting the MRO for measurement is that crude surgical techniques work better than fine surgincal techniques. 

<ol>
	<li>From an anaesthetized crayfish, cut the tail from the abdomen (as close to the abdomen as possible).</li>
	<li>Cut along the ventral edge of the carapace as close to the ventral side as possible.</li>
	<li>Use your finger or the handle of a pair of blunt forcepts to push the fast flexor muscle away from the dorsal surface. Take care not to push down too hard against the tissue left on the dorsal surface. Use scissors if necessary to cut the nerves away instead of pulling at them.</li>
	<li>Pin the anterior segment of the tail down on the dish (dorsal side down) using two pins. Take care not to crack the carapace apart.</li>
	<li>Thread a thread through the telson fins. Tie it gently but firmly. Trim the thread so that it )does not interfere with the electrode</li>
</ol>

## Physiology Setup

Attach the free end of the thread to the servo motor horn.

<a id="experiment"></a>
## Core Experiment

### Visualize Analog Inputs
Run the bonsai protocol with the *write node* <font color = 'red'>disabled</font> and the *analog input* and *channel select* nodes <font color = 'green'>enabled</font>. Double click the channel select nodes to visualize the electrode and stimulus measurements if it does not pop up upon start.

### Record Analog Inputs
Run the bonsai protocol with the *write node* <font color = 'green'>enabled</font> (and the *analog input* and/or *channel select* nodes <font color = 'green'>enabled</font>). Change the filename as needed.

### Stimulation
You will use a servo motor to pull the thread attached to the tip of the tail. The goal is to bend the tail to varying degrees and examine how the MRO encodes stretch. By controlling the position command to the servo motor with the movement of your computer mouse, you will be able to deliver a relatively quantifiable and controlled stimulus that can be synced with the recording of MRO neural activity. 

Practice the stimulation protocol before trying for the MRO nerve recording. 

1. <font color = 'green'>Enable</font>) the **ServoOutput** node. (Disable all MatrixWriter nodes and you can close any Analog Input visualization nodes). 

### MRO physiology

1. Find the MRO nerve. Aim for one in the anterior segments. Use the suction electrode to suction up the nerve.</li>
2. Make sure you are getting a response from the MRO nerve. Make sure that the nerve is not falling out of the suction electrode when the tail is curled.
	
	<li>Run the bonsai protocol (with the <b>write node</b> <font color = 'red'>disabled</font> and the <b>analog input node</b> <font color = 'green'>enabled</font>). Double click the analog input node to visualize the measurement if it does not pop up upon start.</li>
	<li></li>
	<li></li>
	<li>Stimulation Protocol:</li>
	<ol>
		<li></li>
		<li></li>
		<li>Restart the Bonsai protocol with the <b>write node</b> <font color = 'green'>enabled</font>. Change the filename as needed.</li>
		<li>Rotate the knob to its retracted position and leave for 5 seconds before protracting. Leave the knob protracted for 5 seconds before repeating.</li>
		<li>Repeat the stimulation 5 times, with care to rotate the knob the same amount each time.</li>
	</ol> 
</ol>

## Experimental Exploration
Effects of:
- slow versus fast stretch?
- different amounts of stretch?
- starting from different positions?
- peak during stretch or at end of stretch?
- analytic results as a function of duration stretch is held
- is the onset and offset adaptation dynamics the same? (Need to start from a stretch that drives a non-zero baseline spike rate)

## Anaesthetic effects
Compare resutls from the core experiment under different aneasthetic conditions (none, MS222, and ice).
Try to bring the response back to baseline after each manipulation.

## Copy data to an external drive or your Google Drive for later analysis
Use the [Data Explorer](../crayfish-mro/Data-Explorer_crayfish-mro.ipynb) notebook to analyse your data and answer the questions in the [Responses](../crayfish-mro/Responses_crayfish-mro.ipynb) notebook.

## Additional Resources
- [Receptor Potentials](https://michaeldmann.net/mann4.html)
- [Adaptation in stretch receptor. Shigehiro Nakajima (1964)](https://www-jstor-org.ezproxy.wesleyan.edu/stable/pdf/1713939.pdf?refreqid=excelsior%3A65cca9fbb3864632b6d88815a65ca9d0&ab_segments=&origin=&acceptTC=1)
- [On the ionic mechanisms of adaptation in an isolated mechanoreceptor --an electrophysiological study](https://pubmed.ncbi.nlm.nih.gov/6316733/)
- [Structure and Function Relationship in the Abdominal Stretch Receptor Organs of the Crayfish](https://onlinelibrary-wiley-com.ezproxy.wesleyan.edu/doi/pdfdirect/10.1002/cne.20590)