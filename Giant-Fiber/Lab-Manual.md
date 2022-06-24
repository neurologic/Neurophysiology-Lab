# Lab Manual

[Smith Lab Manual](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L4giants.html)

## Software Setup
The bonsai script for today has two measurement nodes. **Channel 0** receives amplified and digitized input from the measurement electrode (referenced to a "ground"). **Channel 1** receives input from a voltage source (the "stimulator").The parameters of the analog input node can be adjusted to specify the NiUSB sampling rate, voltage range, and buffering rate (for visualization). Use a sampling rate of 30kHz. Adjust the voltage range as needed to maximize the signal resolution if needed once you start measuring voltage signals from the nerve chord (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering rate according to your visualization preferences. 

## Surgery
Anesthesia. Obtain an earthworm and place it in the 10% ethanol solution to anesthetize it. Earthworm anesthesia is a problem: dilute alcohol acts very slowly, and often leaves a squiggling worm that is difficult to dissect, while concentrated alcohol "pickles" the outside of the worm, knocking out the responses of touch receptors and threatening the response of the giant fibers. Use the minimum anesthesia you can tolerate; it is really for you, not for the worm (which is too simple to care).

After suitable anesthesia, rinse the alcohol off the worm with tap water and allow the excess water to drain off. Pin out the worm dorsal side up on a flat dissecting dish placed on the stage of your microscope (check that the worm is in the field of view). Place pins only in the region of the worm where you intend to open an incision; for suction electrodes, an incision about two-thirds of the distance from the head to the tail works well. Insert the pins at very shallow angles so that they do not get in the way of your dissecting tools or (later) the electrode.

With forceps and scissors (not a scalpel), open an incision and extend it an inch or two, as shown above. Use the pins to keep the incision open, and flush out the body cavity from time to time with saline. The drawings below will help you identify the nerve cord and other internal structures. Keep the exposed nerve cord moist by tilting the dissecting dish so that saline pools at the incision. Use small blocks of tackiwax to support the dish in a tilted position.

## Physiology Setup

Cut the nerve cord near the end of the incision farthest from the head, and free about a centimeter of the cord from its lateral and ventral connections until it is no longer attached to the body wall.

Place the recording electrode. Start by grounding the preparation: clip one end of an alligator clip lead to one of the dissecting pins (pick one that is out of the way). Clip the other alligator clip to the white (ground) binding post of the amplifier's input block. Then clamp a suction electrode in a micromanipulator (firmly!), attach its connections to the amplifier's input block, and lower the manipulator so that the tip of the electrode is in the saline near the nerve cord. Gently draw some saline into the electrode; you need to have a continuous column of saline (no bubbles!) that is long enough to reach the electrode's internal wire (a few cm). The electrode's external wire also needs to be in the saline pool. Position the tip of the electrode against the cut end of the nerve cord, and gently draw the nerve cord into the electrode. Turn on your preamp and audio monitor, and you should hear and see some spontaneous activity in (non-giant) axons.


<a id="experiment"></a>
## Core Experiment

1. Run the bonsai protocol (with the <b>write node</b> <font color = 'red'>disabled</font> and the <b>analog input node</b> <font color = 'green'>enabled</font>). Double click the analog input node to visualize the measurement if it does not pop up upon start.

Stimulation Protocol: 
1. Restart the Bonsai protocol with the <b>write node</b> <font color = 'green'>enabled</font>. Change the filename as needed.


## Experimental Exploration
Effects of:


## Copy data to your Google Drive for analysis
Use the [Sensory Coding](../week-5/Sensory-Coding-MRO.ipynb) notebook to analyse your data and answer the questions in the [Responses](../week-5/Sensory-Coding-MRO_Responses.ipynb) notebook.

