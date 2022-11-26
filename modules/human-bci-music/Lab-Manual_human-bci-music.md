# Lab Manual

You will complete all of the Analysis and Responses for today with your partner during class as you work through the experiments. 

## Software Setup

The output of the differential amplifiers are being sampled and digitized by the Nidaq ADC. Bonsai is set up to observe the Nidaq ADC output so that you can visualize and record these signals. The sampling rate is 30000 and the number of channels will depend on which experiment you are doing. 

## I. Movement Coding

In this exploration, you will measure EMG signals from the first dorsal interossei muscle. Contraction of ***the first dorsal interosseous muscle*** causes lateral movement of the index finger toward the thumb. As you move this finger note the bulge beneath the skin where the main muscle contraction is ocurring. This bulge is the *belly* of the muscle. 

:::{image} /images/interossi.png
:width: 400
:align: center
:::

Place the ***reference electrode*** on the back of your hand.
> You can try other locations to optimize noise. Just make sure it is not a region that will pick up signal from the muscle of interest and that it is not a region that will also be activated by the task. 

Place the two ***differential measurement electrodes*** on the belly of the muscle. You can use the manual electrodes to optimize electrode placement. 

Test the motor neuron activity under different movement force (weight lifting):
1. Rest the forearm comfortably in a "handshake" position at the edge of a table with your thumb up
2. Tie a string to an object and loop the string over the index finger
3. Lift the object with your index finger. Repeat for a total of 3 trials.
4. Try objects of different weights (for a total of \~3 different conditions)

Think about what differences in motor unit rate and/or amplitude you predict across conditions and why.

To compare across conditions, make sure to use the same electrode placement and the same time and voltage ranges when exploring the signal offline. 

:::{admonition} Analysis and Results

Use the Colab Data Explorer (Part I. Motor Unit Coding and Recruitment) to analyze the rate and amplitude of motor unit spikes. Compare the EMG signal under these different object weight conditions. 

1. What differences in motor unit spike rate and/or amplitude did you predict to observe across conditions?

2. What differences in motor unit spike rate and/or amplitude did you observe across conditions?

3. Save a copy of the Figure showing the median (and 95% confidence intervals) of peak rate and amplitude within each bout. 

:::


## II. Recruitment

To move your body, motor units join together in a systematic way to supply the force required to achieve strength. This teamwork among motor units is called "Orderly Recruitment". In general, motor units with the smallest number of muscle fibers begin contracting first during a movement, followed by the motor units with the largest number of fibers afterward, to allow for a smooth, strong muscle contraction.

Use the same electrode placement as in the first experiment to try to isolate the action potential of a single motor unit.

1. Rest the forearm comfortably in a "handshake" position at the edge of a table with your thumb up
2. Slowly lift your finger to try to isolate consistent spiking activity of a single motor unit
	> You may need to think about moving the finger rather than actually moving it.

Record your EMG during this task.

:::{admonition} Analysis and Results

Find a recording with a bout of regular activity in the single motor unit. 

Use the Colab Data Explorer (Part I. Motor Unit Coding and Recruitment) to observe the amplitude (height) and firing rate (number of impulses) in the EMG across this bout. 

1. Was the amplitude (height) consistent throughout the bout?

2. What was the approximate spike rate? 

3. Use the Dash Data Explorer or the Colab Data Explorer to save a copy of a Figure showing reliable isolation of single motor unit activity. 

:::


## III. Fatigue

1. Hook up two EMG measurement electrodes to your bicep. Use the EMG reference electrode on the back of your palm from Parts I and II.
2. Stand with your back to a wall to control your posture and arm position. 
3. Place a weight in your hand and hold it for as long as you can, with your elbow at a 90 degree angle (If your wrist gets fatigued before your bicept, you can hang the weight from your forearm). 
	> This is called an "isometric" contraction since your muscles are working, but your joints are not moving.   
	> Choose a weight load that you are comfortable maintaining between 15-120 seconds before load fatigue is too high. Keep the muscle active for as long as you can, even as you feel yourselves getting "weaker."

Record your EMG during this task.

::::{admonition} Root Mean Square (RMS)
  RMS provides a measure of *general* ***signal strength*** (as opposed *peak* signal strength). RMS is calculated by squaring the signal, taking an average of the sum of squares, and then taking the square root. Seems mathematically excessive and unnecessary, so why do this?

  First, it's important to remember that our signal has positive and negative values (A). So if we were to try to take an average of this signal, we wouldn't end up with much (B). However, we can get rid of the negative values by squaring the signal (C). 

  :::{image} /images/rms-justification.png
  :width: 500
  :align: center
  :::

  Then we take the "sum of the squares" of the signal and divide it by the number of samples we took to get our mean (or average) value. Then you take the square root of your mean value to come up with the RMS.

  A ***moving average*** RMS does this calculation within small windows that shift across the signal. This provides a (local) RMS estimate at each point in the signal.
::::

:::{admonition} Analysis and Results

Use the ***moving RMS*** calculation in the Colab Data Explorer (Part II. Fatigue).

For each partner: 
1. Estimate and report the initial RMS value 
2. Estimate and report the asymptotic RMS value (or the minimum value if an asymptote was not reached).
3. Estimate and report the time between the initial RMS and the asymptotic (or minimum) RMS. 
4. Calculate and report the rate of fatigue (ie estimate the slope, $m$, of the equation $y = mx + b$ for the part of your moving RMS signal for which you observe increasing fatigue) 
	> Note how linear your data is (or is not) in the range of increasing fatigue.
5. Save a copy of an example processed data signal, with the markers highlighting the initial RMS value.

Report these results in the form of a table (a template for the table is provided in the Responses Notebook). 

| Person | Muscle    | initial RMS    | fatigued RMS   | time to fatigue | rate of fatigue  |
| :----: | :-------: | :------------: | :------------: | :-------------: | :--------------: |
| name 1 | muscle id | value (microV) | value (microV) | value (s)       | value (microV/s) |
| name 2 | muscle id | value (microV) | value (microV) | value (s)       | value (microV/s) |

***If you have time, compare the rate of fatigue for different muscles.***

:::

