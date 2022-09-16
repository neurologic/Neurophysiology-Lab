# Lab Manual

## Hardware and Software Setup

### Input

There are three inputs to the ADC available today. 

**Channel 0**[^chan0-setup] (AI0) and **Channel 1** (AI1) each receive input from a separate differential amplifier. For some experiments, you will only need one of these channels, for others you will need both. For any experiments in which you only need one differential measurement, make sure that you are only digitizing the channel that you need (using the 'collections' parameter of the AnalogInput node in the bonsai workflow). 

**Channel 2**[^chan1-setup] (AI3) receives input from a floating voltage source (a copy of the voltage sent to the "stimulation" electrodes). The stimulation electrodes will be used to evoke action potentials in the Giant Fiber(s). 

[^chan0-setup]: RSE, ±1 V (could get away with ±0.2 V for some preps); The differential amplifiers transform the signal into a single-ended output. The hot amplifier output goes to an analog input; cold amplifier output (gnd) goes to the AIGND (analog input ground reference). 

[^chan1-setup]:NRSE, ±10 V; hot stimulus output goes to an analog input; cold stimulus output ('gnd') goes to the AISN (analog input sensor reference). 


### Input Range

Adjust the voltage range for each channel in the **AnalogInput** node parameters if needed to maximize the signal resolution based on your nerve cord recordings (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). I would recommend starting with ±1 V for the input from each differential amplifier and ±10 V for the stimulus monitor. 

### Sampling Rate

Today you should use a sampling rate of 30kHz. Adjust the buffer samples according to your visualization preferences (I personally like a refresh interval of about 500msec). 

## Recording Chamber setup

You should have a recording chamber that consists of a channel lined with metal pins running perpendicularly to its length. This is the channel where your experimental preps will be placed (wet fibers or earthworms). The pin heads stick out on the outside of the chamber so that you can clip measurement and stimulation electrodes to them. You should have a sturdy strip of aluminum foil. You should have a clear piece of plastic to place over the channel and two strips of foam to place in the ends of the channel to constrain the earthworm's movement.   

## Part I. Fiber Arts Nervous System

For these experiments, you will only need one differential amplifier. 

### Setup

1. Moisten a long (15cm) towel/string/yarn/fabric/etc with tap water 
2. Lay the wet (but not dripping) fiber in the recording chamber channel (across the "bed of pins")
3. Clip the two leads of the stimulation electrode to two pins 1 cm apart from each other near one end of the wet fiber (does not matter which lead goes on which pin yet)
4. Clip the two measurement electrodes from one differential amplifier to two pins 1 cm apart from each other near the other end of the wet fiber (but leave room for the ground).
5. Grounding the preparation: Clip the ground (black) aligator clip lead from the differential amplifier to one of the pins between the measurement electrodes and the end of the fiber. 

### Experiment 1:

1. Set the [*stimulus isolation unit*](../howto/stimulus-isolation-unit) to deliver 0.2 msec, 0.5V pulses at 2Hz.
2. <font color="green"> Enable </font> the Matrix writer node and specify a filename for the experiment. 
3. Start the bonsai workflow and visualize both the stimulation and measurement windows.
4. Turn the stimulus on repeat for about 5 pulses.
5. Stop the bonsai workflow. 

Even with this relatively low stimulus amplitude, you should see a brief, biphasic deflection in the differential measurement near the time of the stimulation pulse. This is the ***stimulus artifact***, which results from virtually instantaneous, passive current spread from stimulating electrodes to measurement electrodes.

### Experiment 2: 
1. Take the fiber off of the bed of pins
2. Place a strip of foil across the canal between the stimulation pins and measurement pins.
3. Connect the foil to *earth ground* with a wire clip. 
    :::{note}
    You may now need to unclip the ground (black) lead from the differential amplifier. It sometimes sets up a ground loop(?) and causes more noise when both grounds are plugged in. If there was no noise increase - no problem - leave them both plugged in. You can also try using the ground lead of the differential amplifier to ground the foil instead of the earth ground from the table.
    :::
4. Place the wet fiber back in the recording chamber and make sure that it is firmly seated and touching all pins and the foil strip. 
5. <font color="green"> Enable </font> the Matrix writer node and specify a filename for the experiment (with a ```.bin``` extension). 
6. Start the bonsai workflow and visualize both the stimulation and measurement windows.
7. Turn the stimulus on repeat for about 5 pulses.
8. Stop the bonsai workflow.

The stimulus artifact should be significantly diminished by the grounded foil (If it is not, let's troubleshoot before moving on). Why do you think this is?

Set aside the wet fiber to make way for the earthworms...

## Part II. Earthworm Giant Fiber System

### General Physiology Setup

Read through each experiment in this section before actually getting and setting up the worm for the experiment. You will likely need a separate worm for each experiment. You may need to go through more than one worm for each experiment. Once the worm is under anesthesia, the time window to perform the experiment is limited and can be finicky. 

Anaesthetize the worm by placing it in 10% alcohol solution[^anaesthesia-alts]. Leave it in the anaethesia until you can pick it up without it wriggling away. The typical time for sufficient anesthesia is ∼5 min. Leaving the worm in anaesthesia too long will lead to an unresponsive nervous system (and eventually death). Hallmarks of anesthetic effectiveness are a lack of worm movement and a cessation of the escape withdrawal reflex. The escape withdrawal reflex can be observed by tapping the tail and head with a plastic probe. An alert worm will exhibit a shortening muscle contraction in response to this stimulus, but an anesthetized worm will not have this reflex. Earthworm anesthesia is a problem: dilute alcohol acts very slowly, and often leaves a squiggling worm that is difficult to keep in the recording apparatus (and later, to dissect), while concentrated alcohol "pickles" the outside of the worm, knocking out the responses of touch receptors and threatening the response of the giant fibers. Use the minimum anesthesia you can tolerate. After suitable anesthesia, briefly rinse the alcohol off the worm by dunking it in tap water and allow the excess water to drain off. 

[^anaesthesia-alts]: The 10% ethanol solution can also be prepared by mixing 30 ml of tap water with 10 ml of 80 proof (40% ethanol) vodka. Carbonated water can also be used as an anesthetic if ethanol is not available. Carbonated water (60%) can be prepared by mixing 30 ml of sugar-free seltzer water (also called “club soda” or “sparkling water” at grocery stores) with 20 ml of tap water.

Place a strip of foil across the channel of the recording chamber. 

An annelid worm's nerve cord is near the ventral surface of the worm. Lay out the worm dorsal side up on the bed of pins in the recording chamber. Aim for the foil to lay just behind the clitellum of the worm. Place the channel plugs at either end of the worm and the cover on top of the worm, constraining it in the channel. 

The worm should not be too wet, but if it gets too dry during the experiments, lift the cover to moisten it with a dropper (of either anaesthesia or water depending on current anaesthetic depth and desired depth). Note that the anaesthetic will tend to dry out the skin. 

### Experiment 1: Presenting... the CAP itself

In this experiment, you will examine the CAP as well as the effect of electrode separation on the CAP. With this data you can infer a variety of information about the anatomical and physiological features of the giant fiber system. 

For this experiment, you will only need one differential amplifier. 

#### Stimulation Preparation
1. Clip the stimulation electrodes to two pins 1 cm apart near the anterior end of the worm.
    :::{Think about it}
    The stimulation electrodes will be used to evoke an action potential in the Giant Fibers at the anterior end of the worm, which will be measured at the posterior half of the worm. Which of the two stimulation leads (+ or -) do you think should be closer to the differential measurement electrodes? Why?
    :::
2. Clip the measurement electrodes of one differential amplifier to two pins 1 cm apart from each other at around the middle of the worm (does not matter which of the two is closest to the stimulation). 
3. Set the *stimulus isolation unit* to deliver 0.2 msec pulses at 0.1V and 0.5 Hz
4. <font color="red"> Disable </font> the Matrix Writer node. 
5. Start the bonsai workflow and visualize both the stimulation and measurement windows.  
6. Turn the *stimulus isolation unit* on repeat. With a low initial stimulus amplitude, likely no CAP will be visible. If it is, decrease the stimulus amplitude until you do not see it anymore. 
7. Slowly increase the stimulus amplitude until you see a CAP at around the time of the stimulus. Hover around the lowest stimulus amplitude that evokes a reliable CAP.
    :::{warning}
    Do not exceed 6V on the stimulus output voltage. If you are still not generating a CAP with a 6V stimulus amplitude, adjust the stimulus electrodes, roll the worm so its ventral side is down, dry off the stimulated region of the body, and/or get a new worm. 
    :::
8. Turn off the stimulus and stop the bonsai workflow
9. Measure the distance between the stimulus electrodes and the measurement electrodes. 

#### Experiment Protocol
1. <font color="green"> Enable </font> the Matrix writer node and specify a filename for the experiment. 
2. Start the bonsai workflow. 
3. Turn the stimulus on repeat for just 5 pulses (at the amplitude you determined during stimulus preparation for reliably evoking a CAP). 
4. Move the measurement electrode furthest away from the stimuluation away one pin (1 cm)
5. Turn the stimulus on repeat for just 5 pulses.
6. Repeat \#4 and \#5, moving the second measurement electrode further away by one pin on each bout. 
7. When the second measurement electrode has gotten near the end of the worm (make sure you are still measuring a CAP), move the first measurement electrode down one pin away from it and repeat the stimulus for 5 pulses.
8. Then, finally, move both measurement electrodes to their original location and repeat the stimulus for 5 pulses. 
8. Stop the bonsai workflow. 

Clean up your worm by dipping it in tap water and return it to the soil.  
Set up for Experiment 2 before getting another worm. 

### Experiment 2: CAP conduction velocity

For this experiment, you will only need one differential amplifier (though two could be used: if using two amplifiers, one will remain in the same location on each bout, while the other will move). 

#### Preparation 

:::{Attention}
This needs to be repeated for a different worm, or if the first worm was re-positioned.
:::

1. Clip the stimulation electrodes to two pins 1cm apart near the anterior end of the worm. (Use the same logic as in Experiment 1 to decide on the orientation of the cathode and anode relative to the measurement electrodes)
2. Clip the measurement electrodes of one differential amplifier to two pins 1 cm apart from each other at around the middle of the worm (does not matter which of the two is closest to the stimulation). 
3. <font color="red"> Disable </font> the Matrix Writer node. 
4. Start the bonsai workflow and visualize both the stimulation and measurement windows. 
5. Set the stimulus isolation unit to deliver 0.2 msec pulses at 0.1V and 0.5 Hz
6. Turn the stimulus isolation unit on repeat. With a low initial stimulus amplitude, likely no CAP will be visible. If it is, decrease the stimulus amplitude until you do not see it anymore. 
7. Slowly increase the stimulus amplitude until you see a CAP at around the time of the stimulus. Hover around the lowest stimulus amplitude that evokes a reliable CAP
8. Turn off the stimulus and stop the bonsai workflow
9. Measure the distance between the stimulus electrodes and the measurement electrodes. 

#### Experiment Protocol
1. <font color="green"> Enable </font> the Matrix writer node and specify a filename for the experiment. 
2. Start the bonsai workflow. 
3. Turn the stimulus on repeat for just 5 pulses (at the amplitude you determined during stimulus preparation for reliably evoking a CAP). 
4. Move both measurement electrodes caudally by 2-4cm (depending on the length of the worm)... try to fit 4 different evenly spaced electrode placements along the worm).
5. Turn the stimulus on repeat for just 5 pulses 
6. Repeat \#4 and \#5 until you get to the end of the worm. 
7. Move the measurement electrodes to their original pins and turn the stimulus on repeat for just 5 pulses.
8. Stop the bonsai workflow. 

Clean up your worm by dipping it in tap water and return it to the soil.  
Set up for Experiment 3 (time permitting) before getting another worm. 


## Additional Exploration (time permitting)

### Experiment 3: Mechanical stimulation 

This experiment requires ***TWO*** differential amplifiers. 

This is one of the most complicated experiments, as it requires a defined level of anesthetization. While the worm should not be moving anymore, the giant fibers
have to be responding to mechanical stimuli. You may need to test several worms with varying exposure to the anesthetics (3-7 min) before you get a suitable worm. As soon as the
responses of the giant fibers can be seen in a worm, the experiment should be conducted quickly to minimize the chance of the worm changing its depth of anaesthesia. 

1. Setup two differential measurement electrode pairs 3-5cm apart from each other (depending on the length of the worm) on the second half of the worm. 
2. anaesthetize your worm and lay it out in the bed of pins so that is positioned well relative to the measurement electrodes that you set up
3. Intermittently (pausing 10-30 sec between), lightly touch the worm with a glass or plastic rod (no metal) on the anterior tip. Explore the stimulus strength to see if you can evoke more than one action potential without evoking muscle action potentials
    :::{tip}
    It can help to 'ground' yourself by touching the metal table with a moist hand
    :::
4. Intermittently (pausing at least 5sec between), lightly touch the worm with a glass or plastic rod (no metal) on the posterior tip. 
    :::{note}
    If using two single-ended electrodes (with common reference), you must rotate the worm 180 degrees before stimulating the posterior tip. Can you think of why?
    :::

Compare cap and conduction velocity for the anterior-stimulated and posterior-stimulated cap

If can distinguish multiple GF spikes, compare cv for each subsequent spike. 

### Experiment 4: conduction velocity potentiation

#### Preparation 

:::{note}
this needs to be repeated for a different worm or if the first worm was re-positioned
:::

1. Clip the two stimulation electrodes to two pins 1cm apart near the anterior end of the worm.
    :::{Note}
    Which of the two stimulation leads do you think should be closer to the differential measurement electrodes? Why?
    :::
2. Clip one differential measurement electrode pair to two pins closest to the stimulation electrodes (does not matter which of the two is the closest). 
2. Clip a second differential measurement electrode pair to two pins 3-5cm from the first. 
3. <font color="red"> Disable </font> the Matrix Writer node. 
4. Start the bonsai workflow and visualize both the stimulation and measurement windows. Visualize the **Detect Spikes** node directly from the Analog Input node (conveying two channels). 
5. Set the stimulus isolation unit to deliver 0.2 msec pulses at 0.1V and 0.5 Hz. Set the frequency so that pulses are 8-10msec apart from each other (or use the **paired pulse** mode to generate two pulses, 8-10 msec apart from each other.)
6. Turn the stimulus isolation unit on repeat. With a low initial stimulus amplitude, likely no CAP will be visible
7. Slowly increase the stimulus amplitude until you see a single biphasic spike at around the time of the stimulus. Hover around the lowest stimulus amplitude that evokes a reliable but single spike.
    :::{note}
    If the duration of the cap is longer than 4msec, you are evoking more than just a single spike. If you cannot evoke a single spike, either try a little more anaesthesia, another worm, or increase the delay between the paired pulses to 10-15 msec (depending on the duration of your cap).  
    You may also be able to get the data needed for this analysis from Experiment 4 below, so you could consider trying mechanical stimulation instead.
    :::
8. Turn off the stimulus and stop the bonsai workflow
9. Measure the distance between the stimulus electrodes and the measurement electrodes. 

#### Experiment Protocol
1. <font color="green"> Enable </font> the Matrix writer node and specify a filename for the experiment. 
2. Start the bonsai workflow. 
3. Turn the stimulus on repeat for 5-10 trains of 3-5 pulses or paired pulses (at the amplitude you determined during stimulus preparation for reliably evoking a single spike). 
7. Stop the bonsai workflow. 


## Housekeeping

Clean up your area.  

Copy data to an external drive or your Google Drive for later.  

Use the [DataExplorer.py application](../../howto/Dash-Data-Explorer.md) to explore your raw data in detail. Use the [Data Explorer](../earthworm-giant-fiber-cap/Data-Explorer_earthworm-giant-fiber-cap.ipynb)notebook to process and analyse your raw data. Answer the questions in the [Responses](../earthworm-giant-fiber-cap/Responses_earthworm-giant-fiber-cap.ipynb) notebook.  




