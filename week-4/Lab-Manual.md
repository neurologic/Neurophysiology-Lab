# Lab Manual

For this lab, you will be removing a leg from the cockroach's mesothorax, the last and largest leg closest to the abdomen. The major benefits of this approach are that the leg will grow back, and the cockroach nervous system provides wonderfully large spikes to explore sensory response coding. 

The cockroach leg is covered with large spines along the tibia and femur. Each spine has a mechanosensory neuron innervating it, which sends spikes to the ventral nerve cord (VNC) and eventually the brain when the spine is moved. The pattern and frequency of spikes sent will convey information to the VNC about the mechanosensory stimulus. Which hair cells are being stimulated will determine where the cockroach perceives the stimulation is located.

## Software Setup
The bonsai script for today has one measurement node. <b>Channel 0</b> receives amplified and digitized input from the differential measurement electrodes (referenced to a "ground"). The parameters of the analog input node can be adjusted to specify the NiUSB sampling rate, voltage range, and buffering rate (for visualization). Use a sampling rate of 30kHz. Adjust the voltage range as needed to maximize the signal resolution if needed once you start measuring voltage signals from the leg (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering rate according to your visualization preferences. 

## Physiology Setup
You need to think carefully about where you place your electrodes when recording neural signals. Remember that you can never just measure the voltage at a single point. Any voltage value that you see will always be a relative value, or, a value at one point as defined with respect to the value at another point. As an example, a nine volt battery has a "nine volt" difference in voltage between the '+' and the '-' ends. Because voltage is a measure of the difference between two points, your electrode cable has more than one needles. We are measuring the voltage between the two measurement electrode pins and <i>grounding</i> the signal with a third. In an ideal world, your two measurement electrodes have distinct identities, a "recording" electrode that captures the signal of interest (spikes) and is hopefully near nerves, and a "ground" electrode that ideally is in a part of the organism that has little electrical signal present.

Note: for this experiment we refer to "ground," "reference," and "recording" electrodes but you can arbitrarily decide which of your measurement electrodes you will call a recording electrode and which one you will call a reference.

<img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/Cockroach-Leg_StockFreeImages.png?raw=True' width="300" alt='cockroach leg'/>

<a id="experiment"></a>
## Core Experiment
<ol>
<li>From an anaesthetized cockroach, obtain a mesothoracic leg by cutting within the coxa.</li>
<li>Place the leg in your dish.</li>
<li>Pin the leg down to the dish using the two measurement electrodes. Place the <i>recording</i> electrode in the tarsus and the <i>reference</i> electrode in the coxa.</li>
<li>Using a dropper, place a small drop of saline solution at the cut end of the coxa and stick the ground electrode through the saline drop into the dish.</li>
<li>Turn on your audio monitor. </li>
<li>Run the bonsai protocol (with the <b>write node</b> <font color = 'red'>disabled</font> and the <b>analog input node</b> <font color = 'green'>enabled</font>). Double click the analog input node to visualize the measurement if it does not pop up upon start.</li>
<li>Touch the barbs with a toothpick by hand to find the barbs that are most sensitive. You should be able to hear voltage spikes as "clicks" using your audio monitor and see the voltage spikes in the analog input monitor within Bonsai.</li>
<li>Make a careful drawing of the leg and position of the spines you will focus on for your experiment.</li>
<li>Stimulation Protocol:</li>
<ol>
<li>Align the micromanipulator (with rod and toothpick attached) so that the toothpick is just touching the surface of a spine (but not yet eliciting spikes).</li>
<li>Note the retracted position on the micromanipulator. Rotate the micromanipulator knob so that the toothpick protracts and depresses the spine. Look under the microscope to determine the maximum spine depression you want to use. Note the distance travelled on the micromanipulator to find the protracted position.</li>
<li>Restart the Bonsai protocol with the <b>write node</b> <font color = 'green'>enabled</font>. Change the filename as needed.</li>
<li>Rotate the knob to its protracted position and leave for 2 seconds before retracting.</li>
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

