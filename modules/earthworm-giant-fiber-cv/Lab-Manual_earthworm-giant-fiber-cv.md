# Lab Manual

## Hardware and Software Setup

### Input

There are three inputs to the ADC available today. 

**Channel 0**[^chan0-setup] (AI0) and **Channel 1** (AI1) each receive input from a separate differential amplifier. For all of the experiments today, you will use both amplifers. 

**Channel 2**[^chan1-setup] (AI3) receives input from a floating voltage source (a copy of the voltage sent to the "stimulation" electrodes). The stimulation electrodes will be used to evoke action potentials in the Giant Fiber(s). 

[^chan0-setup]: RSE, ±1 V (could get away with ±0.2 V for some preps); The differential amplifiers transform the signal into a single-ended output. The hot amplifier output goes to an analog input; cold amplifier output (gnd) goes to the AIGND (analog input ground reference). 

[^chan1-setup]:NRSE, ±10 V; hot stimulus output goes to an analog input; cold stimulus output ('gnd') goes to the AISN (analog input sensor reference). 


### Input Range

Adjust the voltage range for each channel in the **AnalogInput** node parameters if needed to maximize the signal resolution based on your nerve cord recordings (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). I would recommend starting with ±1 V for the input from each differential amplifier and ±10 V for the stimulus monitor. 

### Sampling Rate

Today you should use a sampling rate of 30kHz. Adjust the buffer samples according to your visualization preferences (I personally like a refresh interval of about 500msec, but 100msec might help you better visualize the CAP at stimulus threshold if you are not used to interpreting the signal yet). 

## Recording Chamber setup

You should have a recording chamber that consists of a channel lined with metal pins (spaced 1 cm apart) running perpendicularly to its length. This is the channel where your experimental preps will be placed (wet fibers or earthworms). The pin heads stick out on the outside of the chamber so that you can clip measurement and stimulation electrodes to them. You should have a sturdy strip of aluminum foil. You should have a clear piece of plastic or opaque ruler to place over the channel and constrain movement. You can optionally use two strips of foam to place in the ends of the channel to constrain the earthworm's movement laterally if needed.   

## Test your stimulation and grounding

1. Moisten a long (15cm) towel/string/yarn/fabric/etc with tap water 
2. Lay the wet (but not dripping) fiber in the recording chamber channel (across the "bed of pins"), making sure it is making contact with all pins
3. Clip the two leads of the stimulation electrode to two pins 1 cm apart from each other near one end of the wet fiber (does not matter which lead goes on which pin yet)
4. Clip the two measurement electrodes from each differential amplifier to two pins 1 cm apart from each other along the wet fiber (4-10cm from stimulation electrodes).
5. Grounding the preparation: Clip the ground (black) aligator clip lead from the differential amplifier to one of the pins between the stimulation electrodes and the end of the fiber (make sure the ground pin is touching the we fiber). Clip the earth ground to the same pin. 
    :::{note}
    You may actually need to unclip the ground (black) lead from the differential amplifier once you clip the earth ground to the preparation. It sometimes sets up a ground loop(?) and causes more noise when both grounds are plugged in. If there was no noise increase - no problem - leave them both plugged in. You will need earth ground on the prep either way, so that one must stay.
    :::
6. Set the [*stimulus isolation unit*](../../howto/stimulus-isolation-unit) to deliver 0.2 msec, 0.5V pulses at about 2Hz.
7. <font color="red"> Disable </font> the Matrix writer node. 
8. Start the bonsai workflow and visualize both the stimulation and measurement windows.
9. Turn the stimulus on repeat.
    :::{admonition} stimulus artifact
    Even with this relatively low stimulus amplitude, you should see a brief, biphasic deflection in the differential measurement near the time of the stimulation pulse. This is the ***stimulus artifact***, which results from virtually instantaneous, passive current spread from stimulating electrodes to measurement electrodes along the worm's body.
    :::
10. Electrically Isolate the Stimulus artifact by either: 
    - placing a grounded strip of foil across the canal between the stimulation pins and measurement pins
    - grounding one of the pins between the stimulation and measurement electrodes
11. The stimulus artifact should be significantly diminished by the grounded pin/foil (if it is not, let's troubleshoot before moving on). Why do you think this is?
12. Increase the stimulus amplitude to 3V to make sure that the stimulus artifact remains minor in the measurement signal.
13. Stop the bonsai workflow.

Set aside the wet fiber to make way for the earthworms...

## General Earthworm Physiology Setup

**Read through each experiment** in this section ***before*** **actually getting and setting up the worm** for the experiment. You will likely need a separate worm for each experiment. You may need to go through more than one worm for each experiment. Once the worm is under anesthesia, the time window to perform these experiments is limited and can be finicky. 

1. **Anaesthetize the worm** by placing it in 10% alcohol solution[^anaesthesia-alts]. Leave it in the anaethesia until you can pick it up without it wriggling away. The typical time for sufficient anesthesia is ∼5-10 min (check on it at 5 min and then every min thereafter until ready). Leaving the worm in anaesthesia too long will lead to an unresponsive nervous system (and eventually death). Hallmarks of anesthetic effectiveness are a lack of worm movement and a cessation of the escape withdrawal reflex. The escape withdrawal reflex can be observed by tapping the tail and head with a plastic probe (or lightly pinching with fingers). An alert worm will exhibit a shortening muscle contraction in response to this stimulus, but an anesthetized worm will not have this reflex. Earthworm anesthesia is a problem: dilute alcohol acts very slowly, and often leaves a squiggling worm that is difficult to keep in the recording apparatus (and later, to dissect), while concentrated alcohol "pickles" the outside of the worm, knocking out the responses of touch receptors and threatening the response of the giant fibers. Use the minimum anesthesia you can tolerate. After suitable anesthesia, briefly rinse the alcohol off the worm by dunking it in tap water and allow the excess water to drain off. 
2. If the recording chamber is not already grounded, clip earth ground to one of the pins between your stimulation and measurement electrodes. If this is not enough to remove the stimulus artifact from your measurement, try placing a strip of foil across the channel of the recording chamber. Clip earth ground to it (clipping both the foil and a pin at the same time can help stabilize)
3. Lay out the worm dorsal side up on the bed of pins in the recording chamber (an annelid worm's nerve cord is near the ventral surface of the worm). Aim for the earth ground to land just behind the clitellum of the worm and the stimulating electrodes to land just anterior to the clitellum. Place the cover on top of the worm, constraining it in the channel. (use channel plugs at either end of the worm if needed)
4. The worm should not be too wet, but if it gets too dry during the experiments, lift the cover to moisten it with a dropper (of either anaesthesia or water depending on current anaesthetic depth and desired depth). Note that the anaesthetic will tend to dry out the skin. 

[^anaesthesia-alts]: The 10% ethanol solution can also be prepared by mixing 30 ml of tap water with 10 ml of 80 proof (40% ethanol) vodka. Carbonated water can also be used as an anesthetic if ethanol is not available. Carbonated water (60%) can be prepared by mixing 30 ml of sugar-free seltzer water (also called “club soda” or “sparkling water” at grocery stores) with 20 ml of tap water.

## Conduction Velocity Experiments

### Experiment 1: Electrical Stimulation

For this experiment, you will use ***two*** differential amplifiers (though one could be used: if using one amplifier, you would just do multiple bouts, each with different distance between both measurement electrodes and the stimulating electrode). 

#### Preparation 

:::{Attention}
This needs to be repeated for a different worm, or if the first worm was re-positioned.
:::

1. Clip the stimulation electrodes to two pins 1 cm apart near the anterior end of the worm (anterior to the clitellum). 
    :::{note}
    Which anode/cathode orientation do you need to send action potentials along the worm from anterior to posterior?
    :::
2. Clip the measurement electrodes of one differential amplifier to two pins 1 cm apart from each other at around the middle of the worm (does not matter which of the two is closest to the stimulation). 
2. Clip the measurement electrodes of the second differential amplifier to two pins 1 cm apart from each other and 2-5cm from the first electrodes (depending on the length of your worm). Record the distance between all sets of electrodes (stim and measurement).
3. <font color="red"> Disable </font> the Matrix Writer node. 
4. Start the bonsai workflow and visualize both the stimulation and measurement windows. 
5. Set the stimulus isolation unit to deliver 0.2 msec pulses at 0.5V and 1 Hz
6. Turn the stimulus isolation unit on repeat (or manually if needed to keep the worm mroe calm). With a low initial stimulus amplitude, likely no CAP will be visible. If it is, decrease the stimulus amplitude until you do not see it anymore. 
7. Slowly increase the stimulus amplitude until you see a CAP at around the time of the stimulus. Hover around the lowest stimulus amplitude that reliably evokes a CAP. 
    :::{note}
    Once you find the threshold, you may need to trigger the stimulus manually in between bouts of muscle activity on the recording electrodes.
    :::
8. Turn off the stimulus and stop the bonsai workflow
9. Measure the distance between the stimulus electrodes and the measurement electrodes again if you needed to move them during setup. 

#### Experiment Protocol
1. <font color="green"> Enable </font> the Matrix writer node and specify a filename for the experiment. 
2. Start the bonsai workflow. 
3. Turn the stimulus on repeat for 20 pulses (at the amplitude you determined during stimulus preparation for reliably evoking a CAP). 
    :::{admonition} Note
    You may need to manually trigger each stimulus pulse instead of on automatic repeat. If the worm is too active or there is too much noise from muscle potentials, you will need to time your stimulus pulses for when the worm (signal) is calm.
    :::
4. Stop the bonsai workflow. 

**OPTIONAL EXTENSION**
If the worm is a good one and is more deeply anaesthetized (so that you are not getting much movement or muscle activation), try the same experiment with a higher stimulation voltage (above the threshold for evoking both a median and a lateral giant fiber action potential). 

Clean up your worm by rinsing it in tap water and return it to the soil.  

Set up for Experiment 2 before getting another worm. 

### Experiment 2: Mechanical Stimulation 

This experiment requires two differential amplifiers. 

This is one of the most complicated experiments, as it requires a touchy level of anesthetization. While the worm should not be moving anymore, the giant fibers have to be responding to mechanical stimuli. You may need to test several worms and varying exposure to the anesthetics before you get a suitable worm (you can also try the "alternative method" described at the end of this protocol). As soon as the responses of the giant fibers can be seen in a worm, the experiment should be conducted quickly to minimize the chance of the worm changing its depth of anaesthesia. 

1. Anaesthetize your worm and lay it out in the bed of pins
2. Setup two differential measurement electrode pairs around the middle of the worm, but 2-5cm apart from each other (depending on the length of the worm). 
3. Intermittently (pausing 5-30 sec between as needed... wait longer if you stop seeing responses to the same stimulation), lightly touch the worm with a glass or plastic rod (no metal) on the anterior tip. If you are getting a reliable CAP response, move on quickly to step 4 so that you can record the data. 
    :::{tip}
    It can help to 'ground' yourself by touching the metal table with a moist hand. This reduces electrical and mechanical artifacts from the physical motion of getting near and touching the worm. 
    :::
4. <font color="green"> Enable </font> the Matrix writer node and specify a filename for the experiment. 
5. Start the bonsai workflow
6. Stimulate the worm by touching the ***anterior*** tip (remember to wait between touches so that the escape sysetm is not habituated to your touch). Explore the stimulus strength to see if you can evoke more than one CAP in a row.
7. Stop the bonsai workflow either once you stop getting reliable clean responses or once you have enough data (try for 5-10 good stimulation events that evoke a train of CAPs).
8. Specify a new filename and start the bonsai workflow (It is better to record the anterior and posterior stimulation conditions in separate files because they can be difficult to distinguish from each other within the same file).
9. Repeat steps 3-6 but stimulating the ***posterior*** tip of the worm.  
    :::{note}
    If using two single-ended electrodes (with common reference), you must rotate the worm 180 degrees before stimulating the posterior tip. Can you think of why?
    :::

**ALTERNATIVE METHOD**
Instead of using the bed of pins, lay the worm on a piece of styrofoam, soft wood, or rubber and stick thinner pines directly through the body near the nerve cord. Clip your stimulation and measurement electrodes up to these pins. This can help to keep a more mobile worm still for the stimulation protocol. Worms do recover just fine from the injury once the pins are removed. 


## Intruduction to the Surgery for next week.

Learn and practice the surgery for next week's experiment. You can use the same worm that you used for either experiment today. If you tried the "alternative" method for experiment \#2, use that worm.


## Housekeeping

Clean up your area.  

Copy data to an external drive or your Google Drive for later.  

Use the [DataExplorer.py application](../../howto/Dash-Data-Explorer.md) to explore your raw data in detail. Use the [Data Explorer](../earthworm-giant-fiber-cv/Data-Explorer_earthworm-giant-fiber-cv.ipynb)notebook to process and analyse your raw data. Answer the questions in the [Responses](../earthworm-giant-fiber-cv/Responses_earthworm-giant-fiber-cv.ipynb) notebook.  




