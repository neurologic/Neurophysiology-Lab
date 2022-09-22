# Week 3. Giant Fiber - CAP

## The great escape
Escape behaviors are stereotyped motor behaviors in response to threatening stimuli. They often need to be as rapid as possible. Many animals have escape behaviors that are mediated by some sort of **giant fiber** system.  

## Annelids' Giant Fiber system
Common earthworms (Lumbricus spp.), like other annelids, have a *giant fiber system* that mediates escape behaviors. 

:::{figure-md}
:class: figure

<img src="/images/earthworm-giant-fiber-sensory-circuit.jpg" alt="fishy" width="500px">

Components of the flight reflex, mediated by the MGF pathway. Mechanical stimulation of the worm front end leads to activity in skin sensory cells. This activates sensory interneurons that are connected to the median giant fiber. The MGF is connected to segmental giant motorneurons that elicit contraction of longitudinal muscles in the body wall. A positive feedback loop, via a single interneuron, can enhance the flight reflex by eliciting a second, or even several more, action potentials of the MGF.[^kladt-2010]
:::

[^kladt-2010]: [Kladt, N., Hanslik, U., & Heinzel, H. G. (2010). Teaching basic neurophysiology using intact earthworms. Journal of undergraduate neuroscience education : JUNE : a publication of FUN, Faculty for Undergraduate Neuroscience, 9(1)](http://www.ncbi.nlm.nih.gov/pmc/articles/pmc3597421/)

Near the dorsal surface of the ventral nerve cord, a single median giant fiber (MGF) and two lateral giant fibers (LGF) conduct commands for escape behaviors. Each giant axon is formed from many individual neurons whose axons fuse into a single functional unit, but whose cell bodies remain separate. The two lateral fibers have numerous reciprocal electrical synapses and therefore normally fire together. The median giant receives sensory input from the anterior end of the worm, and the laterals from the posterior, so that normally the median and laterals conduct in opposite directions. 

The skin of the earthworm is thin enough that action potentials from neurons in the escape circuit can be measured from the surface non-invasively.


:::{figure-md}
:class: figure

<img src="/images/Kladt_earthworm-cross-section.png" alt="fishy" width="500px">

Cross section of the earthworm, laying across a measurement electrode. Below, cartoon of the MFG and LGF axon locations within a cross-section of the nerve cord. 
:::

:::{figure-md}
:class: figure

<img src="/images/Eaton_earthworm_mgf-intra-extra.jpeg" alt="fishy" width="500px">

Comparison between intracellular (top) and extracellular (bottom) measurements of an MGF action potential elicited by a light touch to the anterior tip of the worm. Note the delay in action potential onset in each recording. Note the shape of the intracellularly-measured action potential. 
:::

## Experimental Setup

In this lab you will non-invasively measure the response of the giant fiber system to electrical (and potentially mechanical) stimulation using a ***differential*** amplifier. With this measurement technique, two pairs of metal electrodes that are both in contact with the nerve (from the skin surface of the earthworm), therefore the potential difference is compared between two points on the nerve. Electrical stimulation can be delivered as a differential voltage (or current) between two stimulation electrodes.  

:::{figure-md}
:class: figure

<img src="/images/Kladt_earthworm-bed-of-pins.png" alt="fishy" width="500px">

The setup for recording giant fiber activity in intact earthworms is illustrated. Basically, the intact earthworm is placed in a cage that maximally restricts locomotion. An array of electrodes comes into contact with the outer ventral side of the worm. These electrodes are plain stainless steel household pins and serve as recording, as well as stimulation electrodes. A transparent ruler, clamped above, completes the cage. This ruler can be shifted to allow mechanical stimulation of the worm. Cage modelled off of Kladt (2010)[^kladt-2010].
:::


## Complex Action Potentials

There are many aspects of the giant fiber system that can be studied using non-invasive extracellular recording techniques in an intact animal. With these techniques, you will often measure a ***complex action potential*** (CAP) rather than an individual action potential. This compound action potential (CAP) is the algebraic summation of all the action potentials produced by all the fibres that were fired by that stimulus. Additionally, the shape of the extracellularly-measured action potential from in individual fiber will depend on electrode geometry relative to each other and to the nerve.
  
Remember, from your work investigating the *electric circuit model of the passive membrane,* that both the classic intracellular action potential and the compound action potential are biphasic. In other words, they have both positive and negative deflections, but for different reasons. The negative phase of the intracellular action potential is attributed to the ionic conductance mechanism of after-hyperpolarization. The negative phase of the CAP is due to the manner in which it is recorded. In this lab you will be able to manipulate the configuration of the differential electrodes and test its effect on the shape of the measured CAP (and what you can infer about the nervous system anatomy based on the effects). Specifically, you can expect that the shape of the CAP will depend on the:

1. relationship between the inter-electrode distance
2. length of the axon segments depolarized by the action potentials
3. conduction velocities of the active axons  

Why do you think you would expect each of those dependencies? What are your predictions about how each will change the cap? Review your results and analysis from all week 1 passive membrane models to prepare. 


## Pages:
- [](../earthworm-giant-fiber-cap/Lab-Manual_earthworm-giant-fiber-cap.md)
- [](../earthworm-giant-fiber-cap/Data-Explorer_earthworm-giant-fiber-cap.ipynb)
- [](../earthworm-giant-fiber-cap/Responses_earthworm-giant-fiber-cap.ipynb)

## Additional Resources

- [The McGill Physiology Virtual Lab](http://www.medicine.mcgill.ca/physio/vlab/CAP/recording.htm)
- [McGill University Compound Action Potential (virtual lab website)](http://www.medicine.mcgill.ca/physio/vlab/CAP/vlabmenuCAP.htm)
- [Smith College, Bio 330 Lab Manual](https://www.science.smith.edu/departments/neurosci/courses/bio330/labs/L4giants.html)
- [Theodore Holmes Bullock (1945) FUNCTIONAL ORGANIZATION OF THE GIANT FIBER SYSTEM OF LUMBRICUS. Journal of Neurophysiology; 8(1).](https://doi.org/10.1152/jn.1945.8.1.55)
- [B Mulloney (1970) Structure of the giant fibers of earthworms. Science; 168(3934).](https://doi-org.ezproxy.wesleyan.edu/10.1126/science.168.3934.994)
- [Kyle M. Shannon, Gregory J. Gage, Aleksandra Jankovic, W. Jeffrey Wilson, and Timothy C. Marzullo (2014) Portable conduction velocity experiments using earthworms for the college and high school neuroscience teaching laboratory. Advances in Physiology Education 38(1).](https://doi.org/10.1152/advan.00088.2013)
- [A fine structural analysis of the ventral nerve cord and associated sheath of Lumbricus terrestris L.](https://doi.org/10.1002/cne.901250308)
- [Robert Bähring, and Christiane K. Bauer](https://doi.org/10.1152/advan.00137.2013)
- [Kladt, N., Hanslik, U., & Heinzel, H. G. (2010). Teaching basic neurophysiology using intact earthworms. Journal of undergraduate neuroscience education : JUNE : a publication of FUN, Faculty for Undergraduate Neuroscience, 9(1)](http://www.ncbi.nlm.nih.gov/pmc/articles/pmc3597421/)