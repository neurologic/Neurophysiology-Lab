# Lab Manual

You will record extracellularly from nerve 2 while curling the tail to stimulate MRO proprioceptors. This recording will allow you to determine the stimulus-response tuning curve (sensory coding) of the MROs and various dynamic properties of the MRO neural code. 

If there is time, you can also use this preparation to better understand how common anaesthetics work (for example [MS222](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7438171/) or ice).

## Hardware Setup

:::{figure-md}
:class: figure

<img src="/images/servo-circuit.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Servo motor control and stimulus monitor circuit. The 6V battery pack (upper right) powers the servo motor. The battery ground (negative lead) must be tied to the Arduino ground (GND) and the NIdaq AISN. Arduino Pin9 (PWM digital output) provides the signal to the servo motor and is also sent to the NIdaq AI1.
:::

## Software Setup
The bonsai script for today has one measurement node. **Channel 0**[^chan0-setup] receives amplified and digitized input from the measurement electrode relative to the *ground* electrode. **Channel 1**[^chan1-setup] receives input from a floating voltage source (the "stimulator" electrodes). Use a sampling rate of 30kHz. Adjust the voltage range for each channel in the AnalogInput parameters if needed to maximize the signal resolution if needed based on your nerve cord recordings (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering samples according to your visualization preferences. Make sure that the Ardiuno COM port is correct in the **CreateArduino** and **ServoOutput** nodes.

[^chan0-setup]: RSE, ±1 V; hot amplifier output goes to an analog input; cold amplifier output (gnd) goes to the AIGND (analog input ground reference). 

[^chan1-setup]:NRSE, ±10 V; hot stimulus output goes to an analog input; cold stimulus output ('gnd') goes to the AISN (analog input sensor reference). 


## Surgery
For this lab, you will be removing the tail from a crayfish. A major benefit of targetting the MRO for measurement is that crude surgical techniques work better than fine surgincal techniques. 

1. From an anaesthetized crayfish, cut the tail from the abdomen (as close to the abdomen as possible).
2. Cut along the ventral edge of the carapace as close to the ventral side as possible.
3. Use your finger or the handle of a pair of blunt forcepts to push the fast flexor muscle away from the dorsal surface. Take care not to push down too hard against the tissue left on the dorsal surface. Use scissors if necessary to cut the nerves away instead of pulling at them.
4. Pin the anterior segment of the tail down on the dish (dorsal side down) using two pins. Take care not to crack the carapace apart.
	:::{figure-md}
	:class: figure

	<img src="/images/crayfish-tail-mro-prep.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

	Crayfish tail (cleared of overlying fast flexor muscle) pinned to the dish. 
	:::
5. Thread a thread through the middle telson fin. Tie it gently but firmly. Trim the thread so that it does not interfere with the electrode. Attach the free end of the thread to the servo motor horn.


:::{figure-md}
:class: figure

<img src="/images/crayfish-tail-servo.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Suction electrode placed near an N2 root. Thread attaching telson fan to the servo motor horn. 
:::

## Physiology Setup

Identify the nerve roots (N2) near the base of the tale. Select or make a suction electrode tip that has an inside diameter approxiamtely the diameter of the nerve. Connect the electrode to the amplifier input block: electrode inside suction tip goes to a differential input of the amplifier; electrode outside suction tip (in bath) goes to the other differential input (which is *tied to* amplifier reference/ground).

:::{figure-md}
:class: figure

<img src="/images/crayfish-mroN2-0.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Example N2 visualized through microscope. 
:::

:::{figure-md}
:class: figure

<img src="/images/crayfish-mroN2-1.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Example N2 visualized through microscope. 
:::

:::{figure-md}
:class: figure

<img src="/images/crayfish-mroN2-2.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Example N2 visualized through microscope. 
:::


(experiment)=
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