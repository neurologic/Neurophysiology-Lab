# Lab Manual

Today you will be recording the activity of individual neurons in the motor system of yourself and/or each other. Yes. Individual neurons in your own human nervous system. Specifically, you will be using differential electrodes on the surface of the skin to pick up the extracellular voltage signal associated with muscle cell action potentials. Every time a pre-synaptic motor neuron fires an action potential, the muscle cells that it innervates fire an action potential. This one-to-one relationship enables the muscle action potential to serve as a proxy for the motor neuron action potential. 

The foundational configuration that you should start with to familiarize yourself with the technique is to measure EMG signals from the first dorsal interossei muscle. Contraction of the first dorsal interosseous muscle causes lateral movement of the index finger toward the thumb. As you move this finger note the bulge beneath the skin where the main meuscle contraction is ocurring. This bulge is the *belly* of the muscle. 

## Software Setup
The bonsai script for today has only one datastream pathway. 

The Analog Input node contains one channel receiving input from the output of an extracellular amplifier. The extracellular amplifier takes input from a differential electrode, amplifies it, bandpasses the signal frequency, and transforms it to a monopolar signal (relative to ground). The [amplifier](https://backyardbrains.com/products/files/EMGSpikerShield.SMD.V2.61.pdf) has a gain of approximately 2k and cutoff frequencies of 50-2500Hz. These amplifiers also have a built-in circuit that converts the raw EMG into an amplitude envelope of the signal. You will use this setting on the amplifier todya. 

The Matrix Writer node contains specifications for the file name and location where the file will be stored. Make sure the filename ends in ```.bin```.


The amplitude of each function generator is controlled by the amplitude of each analog input channel. 

## Core Experiment


## Copy data to your Google Drive for analysis
Use the [Human Motor Neuron Coding](../week-10/Human-Motor-Neuron-Coding.ipynb) notebook to analyse your data and answer the questions in the [Responses](../week-10/Human-Motor-Neuron-Coding_Responses.ipynb) notebook.

