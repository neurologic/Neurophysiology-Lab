# Lab Manual

## Anatomy

:::{figure} /images/superficial-flexor-segment.png
:width: 600

Abdominal Segment (ventral view) after dissection and staining with methylene blue. Note the ventral nerve cord (vnc), ganglia of the 3rd and 4th segments (g3, g4), nerves (n1, n2, n3), and the superficial flexor muscle (sf) with its attachment point (ma). You will not have methelene blue staining in your preparations (it disrupts nerve activity), but this image with the staining should help orient you to the unstained tissue.
:::

## Hardware and Software Setup

The bonsai script for today has two measurement nodes. 
1. **Channel 0**[^chan0-setup] (AI0) receives amplified (***1000x***) input from the ***extracellular suction electrode*** (referenced to a "ground" in the saline bath). 
	> For the extracellular N3v recording, use a differential amplifier with 1000x gain and \~100Hz high pass filter and \~10kHz low pass filter. We will use either the Backyard Brains or the P-15 amplifiers for this.
2. **Channel 1**[^chan1-setup] (AI3) receives amplified (***10x***) input from the ***intracellular sharp electrode*** (referenced to a "ground" in the saline bath). 
	> For the intracellular superficial flexor muscle recording, use a single-ended DC amplifier with 10x gain and \~10kHz low pass filter. We will use the Getting Model 5/5A amplifiers for this.

Use a sampling rate of 40kHz. Adjust the voltage range for each channel in the AnalogInput parameters to maximize the signal resolution if needed based on your nerve cord recordings (options include: ±0.2 V, ±1 V, ±5 V, ±10 V). Adjust the buffering samples according to your visualization preferences. I recommend starting with ±5 V RSE for AI0 and ±2 V RSE for AI3.

[^chan0-setup]: RSE, ±5 V; electrode inside suction tip goes to an analog input; electrode outside suction tip (in bath) goes to AIGND (analog input ground reference). 

[^chan1-setup]: RSE, ±2 V; electrode inside suction tip goes to an analog input; electrode outside suction tip (in bath) goes to AIGND (analog input ground reference). 

## Physiology Setup

### Place the extracellular measurement electrode 

***I recommend getting a clean N3v signal from the suction electrode before trying for any intracellular recordings***. The extracellular access is more stable than the intracellular access will be. If you penetrate a superficial muscle cell before getting a nerve recording, you are more likely to lose the intracellular recording in the process (compared to getting the nerve recording first). 

1. Clamp a ***suction electrode*** firmly in a micromanipulator, attach its measurement and reference electrode connections to the amplifier's input. Reference ("tie") the differential amplifier reference electrode to amplifier ground. 
2. Select a suction electrode tip (and/or make a fresh one) with a tip diameter approximately twive the diameter of the nerve (because you will be sucking up a loop of the nerve rather than a cut end. Getting a tight fit will drastically improve your measurement quality of neural activity. 
3. Lower the manipulator so that the tip of the electrode is in the saline (not too close to the nerve or other tissue). Gently draw some saline into the electrode; you need to have a continuous column of saline (no bubbles!) that is long enough to reach the electrode's internal wire (a few cm). 
4. Place a reference electrode (connected to the ground input) in the saline bath. 
5. <font color = 'red'>Disable</font> the *Matrix Writer* node. Start the Bonsai protocol. Use the Bonsai protocol to monitor the success of your suction electrode. 
6. Move the tip of the suction electrode toward the nerve about half-way between the ventral nerve cord and the muscle. The nerve should have some *slack* in it (it should not be fully taught). 
7. Suction up a loop of the nerve. If successful, you should not see action potentials in your signal from the differential amplifier (ch 0).

Re-run the Bonsai protocol with the *Matrix Writer* node <font color = 'green'>Enabled</font> to ***record approximately 2-5 minutes of spontaneous activity***. Then, ***in a separate file, record spontaneous and evoked activity*** while gently tickling the tail fan or the swimmeretts (try to ***avoid artifacts*** in the recorded signal by grounding yourself and moving slowly. 

### Place the intracellular measurement electrode 

Throughout the handling and placement of the glass sharp electrodes, it is comically easy to break the sharp tip without noticing or realizing how. Avoid this. Be cautious not to touch the fine tip to anything. 

:::{admonition} ***Backfilling*** a sharp capillary electrode
Squirt a small amount of intracellular solution into the very tip of the blunt end of the electrode. Then rest the capillary on the tray (tip up so it is not touching anything) and wait for the sharp tip to fill by capillary action. You can then gently flick the capillary while holding it sharp-tip down to help bubbles rise out of the tip. Finally, use the electrode filling tip to fill backwards from the meniscus at the tip back to the blunt end (fill as much as you need to for the wire to reach the fluid, but not much more). 
:::

Clamp a pulled and filled glass capilary ***sharp electrode*** firmly in a grooved holder that is firmly clamped in a micromanipulator (sharp tip toward the prep). Thread the chlorided silver wire of the measurement electrode from the Getting Intracellular Amplifier into the blunt end of the capillary. Place a reference electrode (connected to the ground input) in the saline bath. 

#### Sharp electrode above the bath 

<font color = 'red'>Disable</font> the *Matrix Writer* node. Start the Bonsai protocol. Use the Bonsai protocol to monitor the actions of your sharp intracellular electrode. 

Use lower magnification to see the sharp electrode tip above the bath as you lower it. Gently lower the tip using the coarse manipulator controls. ***Keep the tip in focus as you lower it***.

Continue lowering ***until you see or monitor that the electrode is in the bath***. When the electrode penetrates the surface of the saline bath, the intracellular amplifier will show a measurement of around 0 Volts. 

#### Sharp electrode in the bath 

1. "***Zero***"" the amplifier offset using the "Position" knob. 
2. ***Check the electrode resistance*** using the "Electrode Check" button (red button). For every MegaOhm of electrode resistance, you will observe a 100 mV change in the raw measured voltage from the intracellular amplifier. 
	> Aim for electrode resistance of \~30-70 MOhm.  
	> If the electrode resistance is low (<5 MOhm), the tip likely got broken.  
	> If the electrode resistance is a little low or high, the electrode puller setting might need to be adjusted.  

#### Sharp electrode searching for a cell 



#### Sharp electrode in a cell 

Stop the Bonsai protocol and <font color = 'green'>Enable</font> the *Matrix Writer* node. Restart the Bonsai protocol to ***record simultaneous and extracellular (pre-synaptic) intracellular (post-synaptic) neural activity.  