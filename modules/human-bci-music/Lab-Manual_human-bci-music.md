# Lab Manual

## Software Setup

The output of the differential amplifiers are being sampled and digitized by the Nidaq ADC. Bonsai is set up to observe the Nidaq ADC output so that you can visualize and record these signals. The sampling rate is 30000 and the number of channels will depend on which experiment you are doing. 

## Movement Coding

In this exploration, you will measure EMG signals from the first dorsal interossei muscle. Contraction of ***the first dorsal interosseous muscle*** causes lateral movement of the index finger toward the thumb. As you move this finger note the bulge beneath the skin where the main muscle contraction is ocurring. This bulge is the *belly* of the muscle. 

:::{image} /images/interossi.png
:width: 400
:align: center
:::

Place the ***reference electrode*** on your elbow (you can try other locations to optimize noise, just make sure it is not a region that will pick up signal from the muscle of interest). 

Place the two ***differential measurement electrodes*** on the belly of the muscle. You can use the manual electrodes to optimize electrode placement. 

Test the motor neuron activity under different movement force (weight lifting):
1. Rest the forearm comfortably in a "handshake" position at the edge of a table with your thumb up
2. Tie a string to an object and loop the string over the index finger
3. Lift the object with your index finger. Repeat for a total of 3 trials.
4. Try objects of different weights (for a total of \~3 different conditions)

Compare the EMG signal under these different object weight conditions. To compare across conditions, make sure to use the same electrode placement and the same time and voltage ranges when exploring the signal offline. 

What differences do you predict to observe across conditions?

What differences do you observe across conditions?


## Recruitment

To move your body, motor units join together in a systematic way to supply the force required to achieve strength. This teamwork among motor units is called "Orderly Recruitment". In general, motor units with the smallest number of muscle fibers begin contracting first during a movement, followed by the motor units with the largest number of fibers afterward, to allow for a smooth, strong muscle contraction.

1. Lay your palm and forearm on the table. 
2. Slowly lift your hand off the table. Try to lift slowly enough that you recruit different motor units across time. 
> What amplitude motor unit spikes do you expect to observe early in the lift versus late in the lift? Why?

Record your EMG during this task.

Now, repeat the same procedure but with a weight placed on the back of your hand. 

Observe the amplitude (height) and firing rate (number of impulses) in the EMG. What do you see over time? How does the motor unit recruitment differ between the two conditions?


## Fatigue

Hook up your EMG patch electrodes to your bicep. Stand with your back to a wall to control your posture and arm position. Hold a weight in your hand for as long as you can, with your elbow at a 90 degree angle (If your wrist gets fatigued before your bicept, you can hang the weight from your forearm). This is called an "isometric" contraction since your muscles are working, but your joints are not moving. 
> Choose a weight load that you are comfortable maintaining between 15-120 seconds before load fatigue is too high. Keep the muscle active for as long as you can, even as you feel yourselves getting "weaker."

Record your EMG during this task.

Observe the amplitude (height) and firing rate (number of impulses) in the EMG. What do you see over time? 

Now, calculate the rate of fatigue and compare it with your partner. To do this, you will be using Root Mean Square (RMS). 

RMS is a measure of general ***signal strength*** (as opposed *peak* signal strength). RMS is calculated by squaring the signal, taking an average of the sum of squares, and then taking the square root. Seems mathematically excessive and unnecessary, so why do this?

First, it's important to remember that our signal has positive and negative values (A). So if we were to try to take an average of this signal, we wouldn't end up with much (B). However, we can get rid of the negative values by squaring the signal (C). 

:::{image} /images/rms-justification.png
:width: 500
:align: center
:::

Then we take the "sum of the squares" of the signal and divide it by the number of samples we took to get our mean (or average) value. Then you take the square root of your mean value to come up with the RMS.

A ***moving average*** RMS does this calculation within small windows that shift across the signal. This provides a (local) RMS estimate at each point in the signal.

Estimate the ***linear*** fatigue function from your data (ie, the slope of a line fit to your data). 

$$
y = m*x + b
$$

What are the y-value units? What are the x-value units? What variable in the function would you use as your estimate for **rate of fatigue**?

***If you have time, compare the rate of fatigue for different muscles.***

