# Lab Manual

Today you will be using weakly electric fish and recording voltage in their tank using two sets of differential electrodes. 

## Software Setup
The bonsai script for today has only one datastream pathway. 

The Analog Input node contains a collection of two channels receiving input from the two sets of perpindicularly-oriented differential tank electrodes. The input is first digitized by the Nidaq ADC before being streamed by Bonsai. By clicking on this node, you can set the parameters of the ADC (sampling rate, type of electrode configuration, etc) and parameters of the display in Bonsai (buffer). The sampling rate controls the ADC conversion and the buffer controls the size of chunks from the datastream that you can visualize at once in Bonsai. 

The Matrix Writer node contains specifications for the file name and location where the file will be stored. Make sure the filename ends in ```.bin```.

```{note}
Whenever you want to visualize the electrode measurements without accumulating stored data on the PC harddrive, just <font color = 'red'>DISABLE</font> the recording node.
```

## Core Experiment

1. Hook up the tank electrodes from a weakly electric fish tank to your ADC input (channels 0 and 1).
2. Run the bonsai protocol (with the  **Analog Input** node <font color = 'green'>ENABLED</font> but the **Matrix Writer** node <font color = 'red'>DISABLED</font>. Double click the Analog Input node to visualize the measurement if it does not pop up upon start.

	:::{tip}
	You can set the y axis range explicitly by clicking on it so that the visualization does not jump around the screen and so that you can get a clear sense of the voltage picked up by each electrode.
	:::

	:::{tip}
	How could you determine which signal corresponded to each channel in the Bonsai visualization?
	:::
3. Make sure that you can see EOD events in the signal (aka. make sure there is *signal above the noise*).
4. Stop the bonsai protocol and <font color = 'green'>ENABLE</font> the write node. 
5. When you are ready to collect data, start the bonsai protocol and time the recording for about 1 minute using a sampling rate of 100kHz.
6. Repeat with different sample rates (10kHz and 50kHz)
7. Repeat for different species of fish (with 100kHz sample rate)

## Housekeeping

Clean up your area.  

Copy data to an external drive or your Google Drive for later.  

Use the [DataExplorer.py application](../../howto/Dash-Data-Explorer.md) to explore your raw data in detail. Use the [Data Explorer](../eod/Data-Explorer_eod.ipynb) notebook to process and analyse your raw data. Answer the questions in the [Responses](../eod/Responses_eod.ipynb) notebook.  

