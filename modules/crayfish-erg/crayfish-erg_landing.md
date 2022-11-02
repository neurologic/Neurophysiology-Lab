# Week 9. ElectroRetinoGram

Phototransduction, the process by which light energy is absorbed and converted into an electrochemical signal, is an ancient trait common to nearly all present day animal phyla

## Photoreceptor cells

Receptor cells typically respond to stimuli with prolonged, graded potentials. Some receptor cells also have spike-generating mechanisms. Photoreceptor cells are a type of receptor that do not produce spikes.

Rhodopsin is a visual pigment found in photoreceptor cells that is responsible for initiating visual phototransduction. Rhodopsins in all animals are made up of an opsin protein, a member of the 7 transmembrane G protein-coupled receptor family, and an associated chromophore which is derived from retinal or a similar molecule. Opsin amino acid sequence and chromophore structure affect the absorbance of rhodopsin to different wavelengths of light (different rhodopsins are more likely to absorb photons at different wavelengths). 

Photoreceptors transform light energy into electrical energy via *second messengers*. When a photon is absorbed by the chromophore the rhodopsin becomes activated, initiating a G-protein cascade in the cell that ultimately leads to the opening of membrane-bound ion channels. Photoreceptor transduction has mostly been studied in *Drosophila* (another species in the Phylum *Arthropoda*)[^Hardie_2001]. Transient receptor protein (TRP) channels are the ultimate target of the molecular cascade initiated by rhodopsin-detected photons. There is a lag between the time in which the second messenger system is activated by rhodopsin and the opening of TRP channels. *You will be able to measure the time it takes for this metabotropic transformation!*

[^Hardie_2001]: [Hardie, R., Raghu, P. Visual transduction in Drosophila. Nature 413, 186–193 (2001)](https://doi.org/10.1038/35093002)

:::{figure-md} phototransduction-molecules
:class: figure

<img src="/images/phototransduction-molecules.png" alt="fishy" class="bg-primary mb-1" width="600px">

Cartoon of the proteins involved in the transduction of light energy into electrical energy. The Gq α-subunit acts as a diffusible shuttle between activated rhodopsin and the complex.[^Hardie_2001]
:::

Changing the brightness of the light will change the number of rhodopsin molecules that are activated, and thus the amount of second messenger that is produced. This is analogous to varying the amount of transmitter at a metabotropic synapse. Therefore, the graded potential changes that photoreceptor cells undergo can be measured as a relative change in response amplitude with changing light stimulus. 

Any photon that is absorbed by rhodopsin will induce the same kind of response. In practice, this means that a cell's raw response amplitude will increase due to either an increase in light intensity (more photons to absorb), or to a shift in wavelength toward its peak sensitivity (higher probability of rhodopsin absorbing that wavelength). 

## Vertebrate versus Invertebrate

The following video provides a brief overview of differences in phototransduction between drosophila and humans:
(You should be able to view this video signed in with your Wesleyan gmail, but please do not share this video with others, it was shared with me personally from Ilya, not publicly.)

**VIDEO**

Two main differences between vertebrate and invertebrate physiology is the sign of signal transmission. Invertebrate photoreceptors depolarize in response to light, and (at least in the fly) release an inhibitory neurotransmitter (histamine). Histamine opens chloride-permeable ionotropic Histamine receptors. Vertebrate photoreceptors hyperpolarize in response to light, and release an excitatory neurotransmitter (glutamate). 

The photoreceptor cells of invertebrate animals differ from those of vertebrates in morphology and physiology in many ways. These differences include: (From [B Rayer 1, M Naynert, H Stieve 1990 Phototransduction: different mechanisms in vertebrates and invertebrates.](https://doi.org/10.1016/1011-1344(90)85151-l)): 
1. In invertebrates, rhodopsin is converted by light into a meta-rhodopsin which is thermally stable and is usually re-isomerized by light. In contrast, photoisomerization in vertebrates leads to dissociation of the chromophore from opsin, and a metabolic process is necessary to regenerate rhodopsin. 
2. The electrical signals of visual excitation have opposite character in vertebrates and invertebrates: the vertebrate photoreceptor cell is hyperpolarized because of a decrease in conductance and invertebrate photoreceptors are depolarized owing to an increase in conductance. 
3. Single-photon-evoked excitatory events, which are believed to be a result of concerted action (the opening in invertebrates and the closing in vertebrates) of many light-modulated cation channels, are very different in terms of size and time course of photoreceptors for invertebrates and vertebrates. In invertebrates, the single-photon events (bumps) produced under identical conditions vary greatly in delay (latency), time course and size. The multiphoton response to brighter stimuli is several times as long as a response evoked by a single photon. The single-photon response of vertebrates has a standard size, a standard latency and a standard time course, all three parameters showing relatively small variations. Responses to flashes containing several photons have a shape and time scale that are similar to the single-photon-evoked events, varying only by an amplitude scaling factor, but not in latency and time course. 
4. In both vertebrate and invertebrate photoreceptors the single-photon-evoked events become smaller (in size) and faster owing to light adaptation. Calcium is mainly involved in these adaptation phenomena. All light adaptation in vertebrates is primarily, or perhaps exclusively, attributable to calcium feedback. In invertebrates, cyclic AMP (cAMP) is apparently another controller of sensitivity in dark adaptation. 
5. The interaction of photoexcited rhodopsin with a G-protein is similar in both vertebrate and invertebrate photoreceptors. However, these G-proteins activate different photoreceptor enzymes (phosphodiesterases): phospholipase C in invertebrates and cGMP phosphodiesterase in vertebrates. 

For more, see [Sanes and Zipursky (2010) Design Principles of Insect and Vertebrate Visual Systems. Neuron](https://doi.org/10.1016/j.neuron.2010.01.018)

## Local Field Potential (LFP)

(From [Teleńczuk, B., Dehghani, N., Le Van Quyen, M. et al. Local field potentials primarily reflect inhibitory neuron activity in human and monkey cortex. Sci Rep 7, 40211 (2017).](https://doi.org/10.1038/srep40211))

A popular measure of neural population activity in the brain is the local field potential (LFP), which represents summed synaptic activity located in small volume around the recording site. Although LFP is easy to record, it has proven notoriously difficult to interpret and model. These difficulties partially originate from the complexity of neuronal coding, but they also result from the very nature of the LFP signal, which represents the neuronal activity only indirectly through the flow of the extracellular currents. This current flow depends on a number of parameters such as the neuronal morphology, synaptic receptors, membrane ion channels, electric properties of the tissue, brain area and cortical layer impeding the interpretation of the resulting LFP signal.

***The LFP of the retina (the Electroretinogram) is not as difficult to interpret*** as LFPs elsewhere in the brain. 

## Electroretinogram (ERG)

The *electroretinogram* (ERG) is a LFP measurement of the summed (net) membrane potential from the retina, which primarily reflects the activity of a population of photoreceptors, but can also include post-synaptic activity of the lamina cell population (in invertebrates) or bipolar cell population (in vertebrates). 

:::{figure} ../../images/electroretinography-humans.png
:width: 500

Electroretinography is used as a clinically diagnostic tool in humans.
:::

If you don't know whether a features of the ERG waveform is caused by photoreceptors or postsynaptic neruons, you can use pharmacology to dissect the signal. Any procedure that blocks synaptic transmission from the photoreceptors, will eliminate features of the ERG waveform that are not caused by photoreceptor polarization.

In crayfish, previous work has shown that the waveform of the ERG is a good representation of intracellular events in the photoreceptors, as demonstrated by *simultaneous* intra- and extra-cellular measurement of photoreceptor potentials[^Stieve_1978]. As in other extracellular recordings, depolarization of the cells appears as a negative potential to the electrode outside the cells.

[^Stieve_1978]: [Stieve H, Bruns M, Gaube H. Simultaneous recording by extra- and intracellular electrodes of light responses in the crayfish retina. Vision Res. 1978;18(6):621-8.](https://10.1016/0042-6989%2878%2990141-4)

:::{figure-md} Stieve_1978_intraVextra
:class: figure

<img src="/images/Stieve_1978_intraVextra.png" alt="fishy" class="bg-primary mb-1" width="600px">

*Simultaneous* intracellular (left) and extracellular (right; plotted *negative* potential upwards) record of photoreceptor potentials in *Astacus* retina in response to a brief 10msec pulse of light (time base 1s total).[^Stieve_1978]
:::


## Crayfish neuroanatomy

:::{figure} ../../images/Diagram-of-crayfish-brain_eyestalk.png
:width: 700

Dorsal view diagram of the brain within the head carapace and the neural structures within the optic cups. MT: terminal medulla (lateral protocerebrum: LP), MI: internal medulla, ME: external medulla, L: lamina, R: retina.  (From DeForest Mellon Jr[^crayfish-brain-mellon])
:::

[^crayfish-brain-mellon]: [DeForest Mellon Jr (2016) Electrophysiological Evidence for Intrinsic Pacemaker Currents in Crayfish Parasol Cells](https://doi.org/10.1371/journal.pone.0146091)

:::{figure} ../../images/Diagram-of-crayfish-brain_all.png
:width: 700

Dorsal view diagram of the brain and visual ganglia of the crayfish and the neural structures within the optic cups. Theprojections  of  the  olfactory  lobe  and  accessory  lobe  to  the  lateralprotocerebrum (LP)  are  indicated  in  green  and  red  tracks,  respectively.The bilobed hemiellipsoid body (HEB) is dorsal to the terminal me-dulla.  (From DeForest Mellon Jr[^crayfish-brain-mellon])
:::

## Crayfish retina anatomy

:::{figure} ../../images/compound-eye-drosophila.jpeg
:width: 500

Crayfish, like other invertebrates, have ***compound eyes***
:::

## Pages:
- [](../crayfish-erg/Lab-Manual_crayfish-erg.md)
- [](../crayfish-erg/Data-Explorer_crayfish-erg.ipynb)
- [](../crayfish-erg/Responses_crayfish-erg.ipynb)

## Additional Resources: 

- [Circadian clock function in isolated eyestalk tissue of crayfish.](https://doi.org/10.1098%2Frspb.1998.0507)
- [Gaus, Gabriele and Stieve, Hennig. "The Effect of Neuropeptides on the ERG of the Crayfish Orconectes limosus" Zeitschrift für Naturforschung C, vol. 47, no. 3-4, 1992, pp. 300-303.](https://doi.org/10.1515/znc-1992-3-421)
- [DeForest Mellon Jr (2016) Electrophysiological Evidence for Intrinsic Pacemaker Currents in Crayfish Parasol Cells](https://doi.org/10.1371/journal.pone.0146091)
- [Héctor Solís-Chagoyán, Leonor Mendoza-Vargas, Beatriz Fuentes-Pardo (2008) Melatonin modulates the ERG circadian rhythm in crayfish](https://doi.org/10.1016/j.cbpa.2008.01.040)
- [Vertebrate Retina](https://openbooks.lib.msu.edu/neuroscience/chapter/vision-the-retina/)
- [THE ELECTRORETINOGRAM: ERG BY IDO PERLMAN](https://webvision.med.utah.edu/book/electrophysiology/the-electroretinogram-erg/)