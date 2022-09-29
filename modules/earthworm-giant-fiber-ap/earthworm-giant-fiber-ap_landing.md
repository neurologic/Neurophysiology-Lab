# Week 5. Giant Fiber - AP

In this lab, we’ll determine the rheobase, chronaxie and refractory period for earthworm giant fiber action potentials. Action potentials are evoked by a depolarization inside relative to outside on a patch of membrane. The relationship between action potential generation ("*excitability*") and axon/membrane anatomy is a fundamental feature of neurons. This is ultimately a feature of *recruitability* and it effects how neural circuits function.

Comprehensive knowledge of the basic principles of cellular excitability is also fundamental to the education of medical students, because the measurement of neuronal excitability and signal conduction represents an essential part of electrodiagnostic testing in clinical practice. In addition, it is important to understand the principles of electrical excitability in nerve and muscle cells for the appropriate use of stimulation devices like *deep brain electrodes*, *cardiac pace-makers*, and *defibrillators*.

## Strength-Duration Relationships

Stimulus voltages that don’t elicit an action potential are called *subthreshold*, stimulus voltages that do elicit an action potential are called *suprathreshold*. But **threshold** itself is not all-or-none. In some neurons, we can elicit an action potential with a lower stimulus amplitude if the stimulus duration is longer. A longer stimulus duration enables charge to build up that can ultimately elicit an action potential. However, there is a minimum stimulus voltage needed, even at infinite stimulus durations. 

The **rheobase** is defined as the minimum stimulus voltage that can elicit an action potential with very long durations of the stimulus. This metric is one of the foundational parameters recorded in [the Allen Institute's Cell Types database](https://celltypes.brain-map.org/data). You can explore [example data](https://celltypes.brain-map.org/experiment/electrophysiology/474626527) in this database to see how it relates to other anatomical and electrophysiological properties. 

The **chronaxie** is defined as the stimulus duration at 2x the rheobase amplitude. Chronaxie is a useful measure of the excitability of a nerve — the most excitable nerves have the smallest chronaxie. 

We can obtain both of these measurements of excitability (rheobase and chronaxie) by obtaining a strength-duration curve for action potential stimulation.

## Refractory Period

The **refractory period** is the amount of time needed before a neuron can fire a second action potential. This is caused in part by the inactivation of sodium channels after an action potential — it takes time for them to close, to then be reopened by a depolarizing stimulus. This period is called the *absolute* refractory period. After an action potential, the membrane of the axon is also hyperpolarized, due to the slowness of K+ channels closing. So, there is a period of time where the neuron requires more voltage to fire an action potential. This period is called the *relative* refractory period. 

We can obtain an estimate of the refractory periods of a neuron by delivering pairs of stimulus pulses ("*paired pulses*") with different inter-pulse intervals. In this dataset, the relative refractory period is defined by the range of inter-pulse-intervals for which the action potential amplitude is reduced by more than 10%. The absolute refractory period is defined by the range of inter-pulse-intervals for which the second pulse fails to elicit an action potential at all. 

## Experimental Requirements

In these experiments, we need to more precisely and reliably measure action potential events from the giant fibers. Therefore, we will use a more invasive measurement technique. The measurements will still be extracellular, but a *single-ended* rather than a *differential* amplifier can be used. See the lab manual for more detail on the electrode and stimulation configuration. 

## Pages:
- [](../earthworm-giant-fiber-ap/Lab-Manual_earthworm-giant-fiber-ap.md)
- [](../earthworm-giant-fiber-ap/Data-Explorer_earthworm-giant-fiber-ap.ipynb)
- [](../earthworm-giant-fiber-ap/Responses_earthworm-giant-fiber-ap.ipynb)

## Additional Resources

- [Allen Brain Institute: Cell Types Electrophysiology](https://celltypes.brain-map.org/data)
- [Irnich W. (2010). The terms "chronaxie" and "rheobase" are 100 years old. Pacing and clinical electrophysiology : PACE, 33(4), 491–496.](https://doi.org/10.1111/j.1540-8159.2009.02666.x)
- [Robert Bähring, and Christiane K. Bauer. (2014) Easy method to examine single nerve fiber excitability and conduction parameters using intact nonanesthetized earthworms. Advances in Physiology Education.](https://doi.org/10.1152/advan.00137.2013)
- [McGill University Compound Action Potential (virtual lab website)](http://www.medicine.mcgill.ca/physio/vlab/CAP/vlabmenuCAP.htm)
- [Smith College, Bio 330 Lab Manual](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L4giants.html)
- [Theodore Holmes Bullock (1945) FUNCTIONAL ORGANIZATION OF THE GIANT FIBER SYSTEM OF LUMBRICUS. Journal of Neurophysiology; 8(1).](https://doi.org/10.1152/jn.1945.8.1.55)
- [B Mulloney (1970) Structure of the giant fibers of earthworms. Science; 168(3934).](https://doi-org.ezproxy.wesleyan.edu/10.1126/science.168.3934.994)
- [Kyle M. Shannon, Gregory J. Gage, Aleksandra Jankovic, W. Jeffrey Wilson, and Timothy C. Marzullo (2014) Portable conduction velocity experiments using earthworms for the college and high school neuroscience teaching laboratory. Advances in Physiology Education 38(1).](https://doi.org/10.1152/advan.00088.2013)
- [A fine structural analysis of the ventral nerve cord and associated sheath of Lumbricus terrestris L.](https://doi.org/10.1002/cne.901250308)