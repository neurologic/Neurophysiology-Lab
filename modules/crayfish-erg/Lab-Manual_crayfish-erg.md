# Lab Manual

[Smith Lab Manual](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L6erg.html)

## Software Setup
The bonsai script for today has one measurement node. <b>Channel 0</b> receives amplified and digitized input from the differential measurement electrodes (referenced to a "ground"). The parameters of the analog input node can be adjusted to specify the NiUSB sampling rate, voltage range, and buffering rate (for visualization). Use a sampling rate of 30kHz. Adjust the voltage range as needed to maximize the signal resolution if needed once you start measuring voltage signals from the leg (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering rate according to your visualization preferences. 

## Surgery
For this lab, you will be removing the eye from a crayfish after anaesthetizing it on ice. 

1. From an anaesthetized crayfish, cut the head carapace from eye to eye (the pointed rostrum that partially shields the eyes).
2. Cut off the eye at the base of the eye stalk.
3. Wedge the eye stalk, nerve-side down, into the saline well of the dish and fill with saline.


## Physiology Setup
Reference electrode is in the well on the optic nerve side of the eya. Advance the recording electrode toward the eye surface using a micromanipulator. Pierce the cornea with the electrode, but keep it close to the surface. Alternatively, we will be using *wick* electrodes to touch the surface of the eye.

Adjust the amplifier's high-frequency filter setting to filter out noise. Adjust the amplifier's low-frequency filter to eliminate baseline drift without unduly reducing the amplitude of the ERG (As low as possibly, which on the P15 amplifiers is 0.1Hz).


<a id="experiment"></a>
## Core Experiment

:::{admonition} Stimulation Control
You will be driving an LED precicely with a constant voltage stimulator (the Grass SD9 or the AM-systems). The LED is driven by a 9V battery and triggered by a 1V pulse from the stimulator. The 1V stimulator pulse is sent to the ADC AI channel 3 in NRSE mode to monitor the state of the light simultaneously with measurement of the ERG. 
:::

Record measured data in Bonsai for each of the following experiments. Wait 1 minute between each of the experiments.

1. 5 seconds baseline. 1 second pulse. 5 seconds post-pulse. 
	> If you do not obtain a clean recording of this first pulse, you will need to wait 10 min before trying again.
2. 10 msec pulse at 1 Hz. Repeat until a steady-state amplitude is reached.
	> Use the ***Detect Spikes*** node with a threshold just above baseline noise. Set the "History" to 10 traces. You will be able to tell when a steady-state amplitude is reached when the traces do not change much. 
3. 10 msec pulse at 10 Hz. Repeat until a steady-state amplitude is reached.
4. 10 msec pulse at 50 Hz. Repeat until a steady-state amplitude is reached.
5. 0.2 Hz pulses with 3 trials at each of the following pulse durations (in msec): 1000, 500, 100, ..., ..., ..., 1.
6. "Paired" 10 msec duration pulses at 0.2 Hz with 3 trials at each of the following IPIs (in msec): 100, ..., ..., ..., ..., 12.

## Housekeeping

Clean up your area.  

Copy data to an external drive or your Google Drive for later.  

Use the [Data Explorer](Data-Explorer_crayfish-erg.ipynb) notebook to process and analyse your raw data. Answer the questions in the [Responses](Responses_crayfish-erg.ipynb) notebook. The [Dash DataExplorer.py application](../../howto/Dash-Data-Explorer.md) is available to explore your raw data in detail. 

