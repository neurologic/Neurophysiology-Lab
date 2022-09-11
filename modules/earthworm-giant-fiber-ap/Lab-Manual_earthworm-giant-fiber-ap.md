# Lab Manual

## Hardware and Software Setup
The bonsai script for today has two measurement nodes. **Channel 0**[^chan0-setup] receives amplified and digitized input from the measurement electrode (referenced to a "ground"). **Channel 1**[^chan1-setup] receives input from a floating voltage source (the "stimulator" electrodes). Use a sampling rate of 30kHz. Adjust the voltage range for each channel in the AnalogInput parameters to maximize the signal resolution if needed based on your nerve cord recordings (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering samples according to your visualization preferences. 

[^chan0-setup]: RSE, ±5 V; electrode inside suction tip goes to an analog input; electrode outside suction tip (in bath) goes to; hot amplifier output goes to an analog input; cold amplifier output (gnd) goes to the AIGND (analog input ground reference) (try having this go to AISN and NRSE). 

[^chan1-setup]:NRSE, ±5 V; hot stimulus output goes to an analog input; cold stimulus output ('gnd') goes to the AISN (analog input sensor reference) (possible to try having this go to RSE with AIGND, but may cause stimulus artifact in recording). 

## Surgery
Anesthesia : Place the earthworm in the 10% ethanol ringer solution[^anaesthesia-alts]. Leave it in the anaethesia until you can pick it up without it wriggling away. Hallmarks of anesthetic effectiveness are a lack of worm movement and a cessation of the escape withdrawal reflex. The escape withdrawal reflex can be observed by tapping the tail and head with a plastic probe. An alert worm will exhibit a shortening muscle contraction in response to this stimulus, but an anesthetized worm will not have this reflex. The typical time for sufficient anesthesia is ∼5 min. Leaving the worm in anaesthesia too long will lead to an unresponsive nervous system (and eventually death). Earthworm anesthesia is a problem: dilute alcohol acts very slowly, and often leaves a squiggling worm that is difficult to dissect, while concentrated alcohol "pickles" the outside of the worm, knocking out the responses of touch receptors and threatening the response of the giant fibers. Use the minimum anesthesia you can tolerate. The worm will not get to the point where it is 100% unresponsive to touch, but it should not struggle strongly when pinned out.

[^anaesthesia-alts]: The 10% ethanol solution can also be prepared by mixing 30 ml of tap water with 10 ml of 80 proof (40% ethanol) vodka. Carbonated water can also be used as an anesthetic if ethanol is not available. Carbonated water (60%) can be prepared by mixing 30 ml of sugar-free seltzer water (also called “club soda” or “sparkling water” at grocery stores) with 20 ml of tap water.

After suitable anesthesia, briefly rinse the alcohol off the worm with tap water and allow the excess water to drain off. Pin out the worm dorsal side up on a flat dissecting dish. Place one pin at the anterior end and one pin at the posterior end. Then place two pins in the region of the worm where you intend to open an incision. For suction electrodes, an incision about two-thirds of the distance from the head to the tail works well. An annelid worm's nerve cord is near the ventral surface of the worm. With forceps and scissors (not a scalpel), open an incision on the dorsal skin surface. Extend the incision about 1-2cm straight down the dorsal midline. Fillet the body wall open and pin it flat with a pin in each corner. Insert the pins at very shallow angles so that they do not get in the way of your dissecting tools or (later) the electrode. Flush out the body cavity from time to time with saline to clear blood and dirt.

Cut the nerve cord near the end of the incision farthest from the head, and free about a centimeter of the cord from its lateral and ventral connections to the body wall. Use a glass or plastic rod for probing or lifting the nerve cord. Do not pinch the cord with forceps. If you must use forceps, try to only touch the very tip of the already cut end and cut off the crushed tip after freeing the cord.

## Physiology Setup

Tilt the dissecting dish on clay so that saline pools at the incision and keeps the nerve cord wet, while keeping the head of the worm try.

### Grounding the worm

Slide a strip of foil under the worm about halfway between the anterior tip of the worm and your incision. Clip an earth ground to the foil.
:::{note}
Once you hook up your measurement electrode reference, you may find that connecting the foil to different grounding points has different effects on the noise. Try what works best.   
:::

### Place the measurement electrode 
Clamp a suction electrode firmly in a micromanipulator, attach its electrode connections to the amplifier's input block. Select a suction electrode tip (and/or make a fresh one) with a tip diameter approximately the diameter of the nerve cord. Getting a tight fit will drastically improve your measurement quality of neural activity. Lower the manipulator so that the tip of the electrode is in the saline near the nerve cord. Gently draw some saline into the electrode; you need to have a continuous column of saline (no bubbles!) that is long enough to reach the electrode's internal wire (a few cm). Remove any excess saline to keep the body of the worm as dry as possible. Wet the exposed nerve cord with saline periodically. The electrode's external wire needs to be attached to one of the pins holding the worm down (preferable on the posterior end or in the saline pool around the incision). 

:::{figure-md}
:class: figure

<img src="/images/earthworm-gf-suctiontrode.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Suction electrode on exposed and cut nerve cord. 
:::

### Place the stimulating electrode. 
Connect two straight-pin electrodes to the output (red-anode and black-cathode terminals) of a stimulator. At the anterior end, place the anode and cathode stimulation electrode pins through the worm and into the dish below. Place them close together, but not touching, and on either side of the nerve cord. The body surface and the dissecting dish must be dry near the stimulating electrodes, or the saline will "short out" the stimulus and reduce its effectiveness. Use an absorbant tissue to dry the dish and the worm around the stimulating electrodes. Use a roll of absorbant tissue placed under the worm to help keep the anterior end dry. 

:::{note}
You can also try placing two pin electrodes under the ventral surface of the body (like you did for the CAP experiments last week). This may require stronger stimulus amplitudes, but could lower the risk of damaging the nerve cord. 
:::

:::{figure-md}
:class: figure

<img src="/images/earthworm-gf-stimtrodes-placement.jpg" alt="fishy" class="bg-primary mb-1" width="300px">

Stimulation electrode placement. Dry as much moisture as possible from around the worm and between the electrodes and dish. 
:::

:::{figure-md}
:class: figure

<img src="/images/earthworm-gf-whole.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Absorbant wipes help keep the stimulation site dry. 
:::


<a id="experiment"></a>
## Core Experiment

### Visualize Analog Inputs
Run the bonsai protocol with the *write node* <font color = 'red'>disabled</font> and the *analog input* and *channel select* nodes <font color = 'green'>enabled</font>. Double click the channel select nodes to visualize the electrode and stimulus measurements if it does not pop up upon start.

### Record Analog Inputs
Run the bonsai protocol with the *write node* <font color = 'green'>enabled</font> (and the *analog input* and/or *channel select* nodes <font color = 'green'>enabled</font>). Change the filename as needed.


### Mechanical stimulation
Lightly touch the anterior end of the worm with a glass or plastic rod (no metal). It can help to ground yourself while doing this to avoid electrical artifacts in the measured signal.

### Electrical Stimulation

#### Single Pulse

Basic Stimulation Parameters[^SD9-stimulator-controls]
- Switch the *stimulus mode* to **regular**
- Low frequency (1-2 Hz)
- Low amplitude (start with 0.1 gain and the lowest voltage setting)
  > If changing output gain, first turn off the stimulus, then turn the voltage knob all the way back to 0, then switch the voltage output gain
- Brief duration (200 microseconds)

[^SD9-stimulator-controls]: The Grass Instruments **SD9** has four controls on the top section of the stimulator's front panel that control the *Frequency* of the stimuli (how often stimulus pulses are produced), the *Delay* between the trigger pulse and the stimulus pulse, the *Duration* (width) of the stimulus pulse, and the *Volts* (amplitude) of the pulse. Each control has a black knob and a metal multiplier switch under it. The setting depends on both of these knobs. The stimulus is controlled by the *Regular/Twin Pulses* slide switch and the *Repeat/Off/Single* switch. *Polarity* allows reversing which stimulating connection is positive (start with Normal, where red is positive). Use a *Mono* (monophasic) output pulse. The stimulus itself is produced at the red and black binding posts at the right.

Slowly increase the stimulus amplitude and monitor the signal from the neural recording electrode.  

:::{warning}
Do not exceed 2-5V on the stimulus output voltage. If you are still not generating action potentials with a 2V stimulus amplitude (or 6V with non-invasive stimulation electrode setup), adjust the stimulus electrodes, dry off the stimulated region of the body, and/or dissect a new preparation. 
:::

Measure (and record) the distance between the stimulating electrodes and the recording electrode.

#### Paired Pulse

On the SD9 stimulator, the delay is the time between the prepulse sync pulse (which occurs at the trigger point for the sweep) and the actual stimulus pulse (which appears later, as the stimulus artifact). In *paired pulse* mode, there is an additional pulse at the time of the prepulse sync.  

- Switch the *stimulus mode* to **paired pulse**
- Long delay (20ms)
- Amplitude just above spike threshold (the point at which an action potential is generated with each stimulus pulse)

:::{admonition} Caution
Do not have the values of *Delay* plus *Duration* exceed 50% of the time between pulses. The time between pulses is determined by the *Frequency* control. For example, at a frequency of 20 pulses per second, there are 50 msec between pulses. The pulse duration plus delay should not exceed 50% of this period, or 25 msec. If the duration were 1 msec, the delay should not be more than 24 msec.
:::

Turn the stimulus on *repeat*. There should be a spike following each stimulus pulse - if not, increase the stimulus amplitude slightly.  
Gradually decrease the delay between the two stimulus pulses, and observe the action potentials. 

## Experimental Exploration

0. What happens when you touch the worm (at the head? in the middle? just in front of the recording site?)
1. What is the stimulus threshold for the medial giant axon? 
2. What is the stimulus threshold for the lateral giant axon?
3. What is the refractory period of the action potential? Can you overcome the refractory period with a stronger stimulus (do not exceed 5V). 

## Housekeeping

Clean up your area.  

Copy data to an external drive or your Google Drive for later.  

Use the [DataExplorer.py application](../../howto/Dash-Data-Explorer.md) to explore your raw data in detail. Use the [Data Explorer](../earthworm-giant-fiber-ap/Data-Explorer_earthworm-giant-fiber-ap.ipynb)notebook to process and analyse your raw data. Answer the questions in the [Responses](../earthworm-giant-fiber-ap/Responses_earthworm-giant-fiber-ap.ipynb) notebook.  

