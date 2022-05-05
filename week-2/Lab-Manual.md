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
<ol>
<li>Hook up the tank electrodes from a weakly electric fish tank to your ADC input (channels 0 and 1). </li>
<li>Run the bonsai protocol (with the  <b>Analog Input </b> node <font color = 'green'>ENABLED</font> but the <b>Matrix Writer</b> node <font color = 'red'>DISABLED</font>. Double click the Analog Input node to visualize the measurement if it does not pop up upon start.</li>

```{note}
You can set the y axis range explicitly by clicking on it so that the visualization does not jump around the screen and so that you can get a clear sense of the voltage picked up by each electrode.
```

```{tip}
How could you determine which signal corresponded to each channel in the Bonsai visualization?
```
<li>Make sure that you can see EOD events in the signal (aka. make sure there is <i>signal above the noise</i>).</li>
<li>Stop the bonsai protocol and <font color = 'green'>ENABLE</font> the write node. </li>
<li>When you are ready to collect data, start the bonsai protocol and time the recording for about 1 minute. </li>
</ol>

## Copy data to your Google Drive for analysis
Use the [Experimental Design for Analysiis](../week-2/Electric-Organ-Discharge.ipynb) notebook to analyse your data and answer the questions in the [Responses](../week-2/Electric-Organ-Discharge_Responses.ipynb) notebook.

