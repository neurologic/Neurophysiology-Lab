# Lab Manual

[Smith Lab Manual](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L6erg.html)

## Software Setup
The bonsai script for today has one measurement node. **Channel 0** (AI0 RSE) receives amplified and digitized input from the differential measurement electrodes (referenced to a "ground"). **Channel 1** (AI3 NRSE) receives a copy of the square-wave stimulus command to the LED. The parameters of the analog input node can be adjusted to specify the NiUSB sampling rate, voltage range, and buffering rate (for visualization). Use a sampling rate of 30kHz. Adjust the voltage range as needed to maximize the signal resolution if needed once you start measuring voltage signals from the leg (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering rate according to your visualization preferences. 

## Surgery
Remove the eye from a crayfish after anaesthetizing it on ice. 

1. From an anaesthetized crayfish, cut the head carapace from eye to eye (the pointed rostrum that partially shields the eyes).
2. Cut off the eye at the base of the eye stalk. Avoid pulling the eye stalk nerve excessively while cutting it off.
3. Wedge the eye stalk, nerve-side down, into the saline well of the dish and fill with saline.


## Physiology Setup
Reference electrode is in the well on the optic nerve side of the eya. Advance the measurement electrode toward the eye surface using a micromanipulator. If using a penetrating measurement electrode, pierce the cornea with the electrode, but keep it close to the surface. If using a *wick* measurement electrodes, firmly touch the surface of the eye.

Adjust the amplifier's high-frequency filter setting to filter out noise (1-3 kHz should be good). Adjust the amplifier's low-frequency filter to eliminate baseline drift without unduly reducing the amplitude of the ERG (As low as possibly, which on the ***P15 amplifiers*** is 0.1 Hz).

The gain of the amplifier should be at 1000x.


<a id="experiment"></a>
## Core Experiment

:::{admonition} Stimulation Control
You will be driving an LED precicely with a constant voltage stimulator (the Grass SD9 or the AM-systems). The LED is driven by a 9V battery and released by a transistor voltage provided by the voltage stimulator. A maximum intensity is achieved with a 1-2 V pulse from the stimulator. The stimulator pulse is sent to the ADC AI channel 3 in NRSE mode to monitor the state of the light simultaneously with measurement of the ERG. 
:::

Record measured data in Bonsai for each of the following experiments. Wait 5 minutes between each of the experiments. At the beginning of the experiments, the eye should be light-adapted for \~10 min.

1. 5 seconds baseline - One 2 second pulse - 5 seconds post-pulse. 
	> If you do not obtain a clean recording of this first pulse, you will need to wait 10 min before trying again.
2. 10 msec pulse at 2 Hz. Repeat until \~100 pulses have occured (note that you can calculate how long that will take).
	> Use the ***Detect Spikes*** node with a threshold just above baseline noise. Set the "History" to 10 traces. You will be able to tell when a steady-state amplitude is reached when the traces do not change much. 
3. 10 msec pulse at 4 Hz. Repeat until \~100 pulses have occured.
4. 10 msec pulse at 6 Hz. Repeat until \~100 pulses have occured.
5. At 0.2 Hz: 5 pulses of 400 msec duration followed by 2 pulses at each of the following pulse durations (in msec): 400 (yes, do this one again), 200, 100, 75, 50, 25, 10, 5, 1.
6. At 0.2 Hz: 10 single pulses of 10 msec duration followed "Paired" 10 msec duration pulses with 2 trials at each of the following IPIs (in msec): 200, 100, 50, 30.

## Housekeeping

Clean up your area.  

Copy data to an external drive or your Google Drive for later.  

Use the [Data Explorer](Data-Explorer_crayfish-erg.ipynb) notebook to process and analyse your raw data. Answer the questions in the [Responses](Responses_crayfish-erg.ipynb) notebook. The [Dash DataExplorer.py application](../../howto/Dash-Data-Explorer.md) is available to explore your raw data in detail. 

