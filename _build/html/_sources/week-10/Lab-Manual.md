# Lab Manual

Today you will be recording the activity of individual neurons in the motor system of yourself and/or each other. Yes. Individual neurons in your own human nervous system. Specifically, you will be using differential electrodes on the surface of the skin to pick up the extracellular voltage signal associated with muscle cell action potentials. Every time a pre-synaptic motor neuron fires an action potential, the muscle cells that it innervates fire an action potential. This one-to-one relationship enables the muscle action potential to serve as a proxy for the motor neuron action potential. 

You will pick one of several experimental questions to explore (and/or create your own).
The general strategy of this experiment is to selectively analyze the activity of individual motor neurons (by taking advantage of the diversity and specificity of motor unit action potential amplitude). 

The foundational configuration that you should start with to familiarize yourself with the technique is to measure EMG signals from the first dorsal interossei muscle. Contraction of the first dorsal interosseous muscle causes lateral movement of the index finger toward the thumb. As you move this finger note the bulge beneath the skin where the main meuscle contraction is ocurring. This bulge is the <i>belly</i> of the muscle. 

## Software Setup
The bonsai script for today has only one datastream pathway. 

The Analog Input node contains one channel receiving input from the output of an extracellular amplifier. The extracellular amplifier takes input from a differential electrode, amplifies it, bandpasses the signal frequency, and transforms it to a monopolar signal (relative to ground). The [amplifier](https://backyardbrains.com/products/files/EMGSpikerShield.SMD.V2.61.pdf) has a gain of approximately 2k and cutoff frequencies of 50-2500Hz. This amplified input is first digitized by the Nidaq ADC before being streamed by Bonsai. By clicking on this node, you can set the parameters of the ADC (sampling rate, type of electrode configuration, etc) and parameters of the display in Bonsai (buffer). The sampling rate controls the ADC conversion and the buffer controls the size of chunks from the datastream that you can visualize at once in Bonsai. 

The Matrix Writer node contains specifications for the file name and location where the file will be stored. Make sure the filename ends in ```.bin```.

:::{note}
Whenever you want to visualize the electrode measurements without accumulating stored data on the PC harddrive, just <font color = 'red'>DISABLE</font> the recording node.
:::

## Core Experiment
<ol>
<li>Find the <i>belly</i> of the muscle from which you want to measure motor neuron activity. </li>
<li>Put electrode gell on three surface electrodes and cut athletic tape to secure them</li>
<li>Place one surface electrode on the belly of the muscle</li>
<li>Place one surface electrode </li>
<li>Run the bonsai protocol (with the  <b>Analog Input </b> node <font color = 'green'>ENABLED</font> but the <b>Matrix Writer</b> node <font color = 'red'>DISABLED</font>. Double click the Analog Input node to visualize the measurement if it does not pop up upon start.</li>

:::{note}
You can set the y axis range explicitly by clicking on it so that the visualization does not jump around the screen and so that you can get a clear sense of the voltage picked up by the electrode.
:::

<li>Make sure that there is clear <i>signal</i> above the <i>noise</i>).</li>
<li>Stop the bonsai protocol and <font color = 'green'>ENABLE</font> the write node. </li>
<li>When you are ready to collect data, start the bonsai protocol as needed to execute your experiment.</li>

:::{tip}
If your experiment compares the same motor neuron pool across conditions, record all of your data in a single file. If your experiment involves recording from different motor neuron pools or with different electrode configurations, record each condition with a separate file. 
:::

</ol>

## Experiment Options
Choose one of the following options to complete a comparative analysis:
<ul>
<li>Eccentric, Concentric, and Isometric contractions.</li>
<li>The motor neuron activity under different movement force (weight lifting): Rest the forearm comfortably in a "handshake" position at the edge of a table with your thumb up; Tie a string to objects with different weight and loop the string over the index finger; Lift the object with your index finger.</li>
<li>The motor neuron activity of different interossei muscles: Perform lateral movements of the fingers in a palm-down hand configuration; Make sure to move each finger an equal distance.</li>
<li>The timecourse of motor neuron activity: Move the finger to a position away from rest; Hold the finger in the final position for different durations of time.  </li>
<li>Electrode placement (relative locations of differential electrode leads and ground): Try placing both differential leads on the belly of the muscle (make sure they are electrically isolated from each other on the surface); Switch the location of the two leads; Try the ground in the location of one of the differential leads; Try placing the differential lead off to the edge of the muscle belly rather than on the belly; etc....</li>
	</ul>

For each of the experiment options, consider what conditions need to be held constant.

## Copy data to your Google Drive for analysis
Use the [Human Motor Neuron Coding](../week-10/Human-Motor-Neuron-Coding.ipynb) notebook to analyse your data and answer the questions in the [Responses](../week-10/Human-Motor-Neuron-Coding_Responses.ipynb) notebook.

