# Week 3. Giant Fiber

Common earthworms (Lumbricus spp.) have a *giant fiber system* consisting of a single median giant fiber and two lateral giant fibers. Each giant axon is formed from many individual neurons whose axons fuse into a single functional unit, but whose cell bodies remain separate. The two lateral fibers have numerous reciprocal electrical synapses and therefore normally fire together. 

In mediating the *startle response*, the median giant receives sensory input from the anterior end of the worm, and the laterals from the posterior, so that normally the median and laterals conduct in opposite directions.

:::{figure-md}
:class: figure

<img src="/images/earthworm-EMsections.jpg" alt="fishy" class="bg-primary mb-1" width="500px">

Left: micrograph cross-section of Lumbriculus variegatus. The region in the red rectangle, the ventral nerve cord, is enlarged at the right. gf, giant fibers; np, neuropile. [^smith-college-image]
:::

[^smith-college-image]: Micrographs of Lumbriculus variegatus by Alanna Morris, from a project in Bio 337, Fine Structure, at Smith College. [Image from Bio 330 Website](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L4giants.html).

In this lab, we’ll determine the threshold, rheobase &amp; chronaxie, refractory period, and
conduction velocity for the earthworm giant fiber system. 
The threshold is defined as the minimum stimulus voltage that elicits an action potential 50% of
the time. We’ll determine this with short stimuli. Stimulus voltages that don’t elicit an action
potential are called subthreshold, stimulus voltages that do elicit an action potential are called
suprathreshold.
In some neurons, we can elicit an action potential with a lower stimulus voltage if the stimulus
length is longer. A longer stimulus length enables charge to build up that can ultimately elicit an
action potential. However, there is a minimum stimulus voltage needed, even at infinite stimulus
durations. The rheobase is defined as the minimum stimulus voltage that can elicit an action
potential with very long durations of the stimulus. The stimulus duration at 2x the rheobase is
called the chronaxie. Chronaxie is a useful measure of the excitability of a nerve — the most
excitable nerves have the smallest chronaxie. We can plot this data in a strength-duration curve:

(A) Sample strength-duration curve for an earthworm, with the rheobase (r) and chronaxie (c) marked
(B &amp; C) histograms showing the number of observations for rheobase &amp; chronaxie, respectively.
The absolute refractory period is the minimum amount of time needed for a neuron to fire a
second action potential. This is caused by the inactivation of sodium channels after an action
potential — it takes time for them to close, to then be reopened by a depolarizing stimulus.
Since we’re recording from many axons, your measured refractory period will be more variable
than for a single axon. We’ll define the absolute refractory period as the time when the
amplitude of the second CAP is 30% of the first.

Earthworm Experiments
BIPN 145

Page 4

After an action potential, the membrane of the axon is also hyperpolarized, due to the slowness
of K+ channels closing. So, there is a period of time where the neuron requires more voltage to
fire an action potential. This period is called the relative refractory period. In this lab, we’ll
identify it as the period where the amplitude of the second CAP is 30-90% of the first.

## Pages:
- [](../earthworm-giant-fiber/Lab-Manual_earthworm-giant-fiber.md)
- [](../earthworm-giant-fiber/Data-Explorer_earthworm-giant-fiber.ipynb)
- [](../earthworm-giant-fiber/Responses_earthworm-giant-fiber.ipynb)

## Additional Resources

- [Smith College, Bio 330 Lab Manual](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L4giants.html)
- [Theodore Holmes Bullock (1945) FUNCTIONAL ORGANIZATION OF THE GIANT FIBER SYSTEM OF LUMBRICUS. Journal of Neurophysiology; 8(1).](https://doi.org/10.1152/jn.1945.8.1.55)
- [B Mulloney (1970) Structure of the giant fibers of earthworms. Science; 168(3934).](https://doi-org.ezproxy.wesleyan.edu/10.1126/science.168.3934.994)
- [Kyle M. Shannon, Gregory J. Gage, Aleksandra Jankovic, W. Jeffrey Wilson, and Timothy C. Marzullo (2014) Portable conduction velocity experiments using earthworms for the college and high school neuroscience teaching laboratory. Advances in Physiology Education 38(1).](https://doi.org/10.1152/advan.00088.2013)
- [A fine structural analysis of the ventral nerve cord and associated sheath of Lumbricus terrestris L.](https://doi.org/10.1002/cne.901250308)