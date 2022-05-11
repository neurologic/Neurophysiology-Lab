# Lab Manual

Today, you will primarily be recording activity of Motor Neurons in N3 of the abdominal ganglia of the crayfish. 

<img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/fig.A.1-Abdomial_Musculature.png?raw=True' width="600" alt='crayfish muscles cartoon' align="center"/>

<img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/Crayfish-Isolated-Nervous-System.Fig1_Seichter2014_JOVE.png?raw=True' width="300" alt='crayfish nerve cord' align="center"/>

## Surgery
There are two different ways that you can gain access to the abdominal ganglia nerve roots: from the ventral or dorsal side. 

Access from the dorsal side involves cutting away a lot of bulky muscle and can feel like a bit of a mess. The result, if done well, can provide more visibility.

Access from the ventral side involves cutting away less tissue and is therefore less messy. The result, if done well, will be cleaner and the tissue will often be more healthy. However, the nerves and muscle fibers from this perspective can sometimes be harder to distinguish for beginners. In this preparation you are able to keep the swimmerets intact and stimulate them during the experiment. 

<ol>
	<li>Get a crayfish from the ice bucket.</li>
	<li>Cut off the tail as close to the abdomen as possible.</li>
</ol>

### Ventral access
<ol>
	<li>Pin the tail out in the silguard dish.</li>
	<li>Cut along the midline with fine scissors or scalpel blade. Make sure not to cut too deep or else you will slice apart the nervous system.</li>
	<li>Cut along the posterior sternite of the segment. Use the forcepts to lift the surface exterior tissue up off of the superficial muscle as you cut. Try not to cut the superficial muscle.</li>
	<li>Cut along the posterior side of the superficial muscle attachment point and remove the exterior tissue flap.</li>
</ol>

<img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/fig.A.2.b-Segment-Dissected-Labeled.png?raw=True' width="600" alt='crayfish segment dissected labeled' align="center"/>

<img src='https://github.com/neurologic/Neurophysiology-Lab/blob/main/images/fig.A.2.d-Segment-Methylene_Blue-Labeled.png?raw=True' width="600" alt='segment methylene blue stained' align="center"/>

### Dorsal access
<ol>
	<li>Cut the swimmerettes off with coarse scissors.</li>
	<li>Cut along the exterior edges of the carapace with coarse scissors. Keep the cuts shallow so you don't destroy underlying tissue.</li>
	<li>Pin the ventral side of the tail to the dish.</li>
	<li>Slowly lift the dorsal carapace away as you cut the deep flexor muscle from the ventral surface of the carapace at its attachment points. Be careful not to cut any of the nerves close to the ganglia or the ganglia connectives.</li>
</ol>


## Core Experiment
<ol>
	<li>Electrode setup
		<ol>
			<li>Make suction electrodes by breaking off the tip of a glass capilary tube pulled with a long taper: under a dissection microscope, break the tip off with a pair of #5 forceps. After breaking, the tip should be large enough to accommodate a loop of the third nerve within the pipette, BUT small enough that the nerve does not slip out when suction is released. A snug fit provides optimal signal to noise ratio for the recording of motor neuron action potentials. Start small and increase the size by breaking more as needed. Once you find a good electrode, you should be able to re-use it throughout the day if treated carefully (don't drop it or bang the tip and rinse tissue goop off or out of it). </li>
			<li>Place the suction electrodes in the holder with the "active" recording wire inside the glass capilary. The glass capilary is not actually an "electrode" until it has both the wire and saline inside of it - and the saline is touching the wire.</li>
			<li>Suck saline up into the electrode until it touches the electrode wire.
			:::{attention}
			Make sure that the suction electrode has good suction! If it is difficult to pull fluid up into the electrode, then there is a leak or a clog somewhere. It must be fixed or else you will note be able to get a recording from the motor nerve. 
			:::
			:::{attention}
			Do not pull up more fluid than needed into the electrode (there should not be any fluid up into the tubing). 
			:::
			</li>
			<li>Place the differential reference/ground electrode into the saline bath of the petri dish (off to the side). The reference needs to be touching the saline in the dish, but does not need to be near the crayfish tail. </li>
		</li>
	<li>Start the Bonsai protocol (make sure the write node is <font color='red'>disabled</font> and the data visualizer window is visible)</li>
	<li>Lower the electrode toward N3. Once it is close enough, use the dissection scope to guide your movement of the electrode.</li>
	<li>Once lightly touching N3, pull the plunger lightly to suck the nerve up. Apply more pressure if needed. If needing to pull excessively hard, consider that you might need to increase the tip size or that there might be a clog or leak in the electrode system.
	:::{tip}
	Monitor the voltage trace in Bonsai before, during, and after sucking up the nerve. You should immediately be able to see motor neuron action potentials if it gets sucked up correctly. 
	:::</li>
	<li>Stop the Bonsai protocol, <font color='green'>enable</font> the write node, and restart. Collect approximately 10s of <i>spontaneous</i> activity.</li>
	:::{attention}
	Monitor the amplitude of the signal peaks. The amplitudes should remain stable throughout the recording. If the amplitudes <i>drift</i>, that is likely a sign that the nerve is slipping out of the electrode. Stable recordings will be essential for analysis.
	:::
</ol>


## Experiment Extension
<ul>
	<li>Compare activity between N3v of different abdominal ganglia. Repeating with the contralateral N3 for each ganglia can help control for differences in recording access or health (for example, the order would be N3 of A4, A5, and A6 on the right side and then N3 of A4, A5, and A6 on the left side).</li>
	<li>Compare activity under different conditions: stroking or touching contralateral swimmeretts, stroking or touching ipsilateral swimmerettes, stroking or touching the telson.</li>
	<li>Compare activity with different nerves (N1 or N2) of the same ganglia segment.</li>
	</ul>
