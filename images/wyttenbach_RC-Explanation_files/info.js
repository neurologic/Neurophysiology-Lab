/*
	These functions contain information that may need to be edited to fix the content of the manual.
	For example, there would be language-specific versions of the titles if we ever have this translated.
	Similarly, changing lab or figure numbers will require updating this
	Dreamweaver should update all links in the texts.
	Figure Names; Lab Names; Window Sizes
*/

function getFooterText() {
	return 'Crawdad: An Online Lab Manual for Neurophysiology.<br>&copy; 2020 Robert Wyttenbach, Bruce Johnson, Ronald Hoy.';
}

// maybe instead of abbrevURL I should take the full URL and pop off the last part after the /
// check how I use this. Does it always do that first?
function getTitles(abbrevURL) {
	switch(abbrevURL.toLowerCase()) {
		// 1. Membrane Properties
		case 'fig.1.1' : return ['Figure 1.1','Fig. 1.1','Model Membrane','Model Membrane'];
		case 'fig.1.2' : return ['Figure 1.2','Fig. 1.2','Real &amp; Model Membranes','Real &amp; Model Membranes'];
		case 'fig.1.3' : return ['Figure 1.3','Fig. 1.3','Intracellular Recording','Intracellular Recording'];
		case 'fig.1.4' : return ['Figure 1.4','Fig. 1.4','Extracellular Recording','Extracellular Recording'];
		case 'fig.1.5' : return ['Figure 1.5','Fig. 1.5','RC Explanation','RC Explanation'];
		case 'fig.1.6' : return ['Figure 1.6','Fig. 1.6','Resistor-Capacitor Circuit','RC Circuit'];
		case 'fig.1.7' : return ['Figure 1.7','Fig. 1.7','Electric Fish Recording','Electric Fish'];
		case 'vid.1.1' : return ['Video 1.1','Vid. 1.1','Current Flow','Current Flow'];
		case 'fig.1.1i' : return ['Figure 1.1i','Fig. 1.1i','Model Membrane Circuit','Model Membrane Circuit'];
		case 'fig.1.2i' : return ['Figure 1.2i','Fig. 1.2i','Intracellular Results','Intracellular Results'];
		case 'fig.1.3i' : return ['Figure 1.3i','Fig. 1.3i','Extracellular Results','Extracellular Results'];
		case 'fig.1.4i' : return ['Figure 1.4i','Fig. 1.4i','RC Circuit Results','RC Circuit Results'];
		case 'fig.1.5i' : return ['Figure 1.5i','Fig. 1.5i','Time Constant Summation','RC Summation'];
		case 'fig.1.6i' : return ['Figure 1.6i','Fig. 1.6i','Pulse Fish EOD','Pulse Fish EOD'];
		case 'vid.1.1i' : return ['Video 1.1i','Vid. 1.1i','Extracellular Current','Extracellular Current'];
		case 'vid.1.2i' : return ['Video 1.2i','Vid. 1.2i','Intracellular Current','Intracellular Current'];

		// 2. Motor Nerve Recording
		case 'fig.2.1' : return ['Figure 2.1','Fig. 2.1','Nerve Recording Setup','Nerve Recording Setup'];
		case 'vid.2.1' : return ['Video 2.1','Vid. 2.1','Nerve Dissection &amp; Recording','Nerve Dissection &amp; Recording'];
		case 'vid.2.2' : return ['Video 2.2','Vid. 2.2','Exposing Nerve 3','Exposing Nerve 3'];
		case 'vid.2.3' : return ['Video 2.3','Vid. 2.3','Nerve 3 Recording','Nerve 3 Recording'];
		case 'fig.2.1i' : return ['Figure 2.1i','Fig. 2.1i','Baseline Activity','Baseline Activity'];
		case 'fig.2.2i' : return ['Figure 2.2i','Fig. 2.2i','Telson Stimulation','Telson Stimulation'];
		case 'fig.2.3i' : return ['Figure 2.3i','Fig. 2.3i','Swimmeret Stimulation','Swimmeret Stimulation'];
		case 'fig.2.4i' : return ['Figure 2.4i','Fig. 2.4i','Activity Histograms','Activity Histograms'];
		case 'fig.2.5i' : return ['Figure 2.5i','Fig. 2.5i','Nerve 3 Section','Nerve 3 Section'];

		// 3. Motor Nerve Anatomy
		case 'fig.3.1' : return ['Figure 3.1','Fig. 3.1','Filling Chamber','Filling Chamber'];
		case 'fig.3.2' : return ['Figure 3.2','Fig. 3.2','Processing Flowchart','Processing Flowchart'];
		case 'vid.3.1' : return ['Video 3.1','Vid. 3.1','Entire Backfill Procedure','Entire Backfill Procedure'];
		case 'vid.3.2' : return ['Video 3.2','Vid. 3.2','Exposing Abdominal Ganglia','Exposing Abdominal Ganglia'];
		case 'vid.3.3' : return ['Video 3.3','Vid. 3.3','Removing Abdominal Ganglia','Removing Abdominal Ganglia'];
		case 'vid.3.4' : return ['Video 3.4','Vid. 3.4','Building Filling Chamber','Building Filling Chamber'];
		case 'vid.3.5' : return ['Video 3.5','Vid. 3.5','Preparing Ganglia to Fill','Preparing Ganglia to Fill'];
		case 'fig.3.1i' : return ['Figure 3.1i','Fig. 3.1i','Filled Motor Neurons','Filled Motor Neurons'];

		// 4. Muscle Resting Potential
		case 'fig.4.1' : return ['Figure 4.1','Fig. 4.1','Muscle Recording Setup','Muscle Recording Setup'];
		case 'vid.4.1' : return ['Video 4.1','Vid. 4.1','Muscle Dissection and Recording','Dissection &amp; Recording'];
		case 'vid.4.2' : return ['Video 4.2','Vid. 4.2','Exposing Superficial Flexor','Exposing Superficial Flexor'];
		case 'vid.4.3' : return ['Video 4.3','Vid. 4.3','Muscle Recording','Muscle Recording'];
		case 'table.4.1' : return ['Table 4.1','Tab. 4.1','Crayfish Ion Concentrations','Crayfish Ion Concentrations'];
		case 'fig.4.1i' : return ['Figure 4.1i','Fig. 4.1i','Damaged Muscle Fibers','Damaged Muscle Fibers'];
		case 'fig.4.2i' : return ['Figure 4.2i','Fig. 4.2i','Resting Potential Results','Resting Potential Results'];

		// 5. Synaptic Connectivity
		case 'fig.5.1' : return ['Figure 5.1','Fig. 5.1','PSP Recording Setup','PSP Recording Setup'];
		case 'vid.5.1' : return ['Video 5.1','Vid. 5.1','Nerve-Muscle Dissection &amp; Recording','Dissection &amp; Recording'];
		case 'vid.5.2' : return ['Video 5.2','Vid. 5.2','Nerve-Muscle Recording','Nerve-Muscle Recording'];
		case 'vid.5.3' : return ['Video 5.3','Vid. 5.3','PSP Matching','PSP Matching'];
		case 'fig.5.1i' : return ['Figure 5.1i','Fig. 5.1i','Matching APs &amp; PSPs','Matching APs and PSPs'];
		case 'fig.5.2i' : return ['Figure 5.2i','Fig. 5.2i','Innervation Patterns','Innervation Patterns'];
		case 'fig.5.3i' : return ['Figure 5.3i','Fig. 5.3i','Summation','Summation'];
		case 'fig.5.4i' : return ['Figure 5.4i','Fig. 5.4i','Inhibition','Inhibition'];

		// 6. Synaptic Plasticity
		case 'fig.6.1' : return ['Figure 6.1','Fig. 6.1','Recording &amp; Stimulation Setup','Recording &amp; Stimulation Setup'];
		case 'vid.6.1' : return ['Video 6.1','Vid. 6.1','Dissection, Recording, &amp; Stimulation','Dissection, Recording, &amp; Stimulation'];
		case 'vid.6.2' : return ['Video 6.2','Vid. 6.2','Cutting Nerve 3','Cutting Nerve 3'];
		case 'vid.6.3' : return ['Video 6.3','Vid. 6.3','Stimulating Nerve 3','Stimulating Nerve 3'];
		case 'vid.6.4' : return ['Video 6.4','Vid. 6.4','Eliciting Facilitation','Eliciting Facilitation'];
		case 'fig.6.1i' : return ['Figure 6.1i','Fig. 6.1i','Facilitation Results','Facilitation Results'];
		case 'fig.6.2i' : return ['Figure 6.2i','Fig. 6.2i','Posttetanic Potentiation','Posttetanic Potentiation'];
		case 'fig.6.3i' : return ['Figure 6.3i','Fig. 6.3i','Synaptic Depression','Synaptic Depression'];
		case 'fig.6.4i' : return ['Figure 6.4i','Fig. 6.4i','PTP Results','PTP Results'];

		// 7. Stretch Receptor
		case 'fig.7.1' : return ['Figure 7.1','Fig. 7.1','Stimulating MROs','Stimulating MROs'];
		case 'fig.7.2' : return ['Figure 7.2','Fig. 7.2','Dissection Outline','Dissection Outline'];
		case 'fig.7.3' : return ['Figure 7.3','Fig. 7.3','Stimulus Setup','Stimulus Setup'];
		case 'fig.7.4' : return ['Figure 7.4','Fig. 7.4','MRO Recording Setup','Recording Setup'];
		case 'vid.7.1' : return ['Video 7.1','Vid. 7.1','Dissect and Record','Dissect &amp; Record'];
		case 'vid.7.2' : return ['Video 7.2','Vid. 7.2','Anesthetizing','Anesthetizing'];
		case 'vid.7.3' : return ['Video 7.3','Vid. 7.3','Attach Thread','Attach Thread'];
		case 'vid.7.4' : return ['Video 7.4','Vid. 7.4','MRO Dissection','Dissection'];
		case 'vid.7.5' : return ['Video 7.5','Vid. 7.5','Alternate Dissection','Alternate Dissection'];
		case 'vid.7.6' : return ['Video 7.6','Vid. 7.6','Finding MRO Nerves','Finding Nerves'];
		case 'vid.7.7' : return ['Video 7.7','Vid. 7.7','Record and Stretch','Record &amp; Stretch'];
		case 'vid.7.8' : return ['Video 7.8','Vid. 7.8','Activating MRO<sub>2</sub>','Activating MRO<sub>2</sub>'];
		case 'fig.7.1i' : return ['Figure 7.1i','Fig. 7.1i','Stimulus-Response','Stimulus-Response'];
		case 'fig.7.2i' : return ['Figure 7.2i','Fig. 7.2i','Spike Rates','Spike Rates'];
		case 'fig.7.3i' : return ['Figure 7.3i','Fig. 7.3i','Adaptation Curves','Adaptation Curves'];

		// 8. Snail Brain&mdash;Excitability
		case 'fig.8.1' : return ['Figure 8.1','Fig. 8.1','Snail Brain Diagram','Snail Brain Diagram'];
		case 'fig.8.2' : return ['Figure 8.2','Fig. 8.2','Initial Snail Dissection','Initial Dissection'];
		case 'fig.8.3' : return ['Figure 8.3','Fig. 8.3','Brain Dissection Steps','Dissection Steps'];
		case 'fig.8.4' : return ['Figure 8.4','Fig. 8.4','Dissected Snail Brain','Dissected Snail Brain'];
		case 'fig.8.5' : return ['Figure 8.5','Fig. 8.5','Snail Recording Setup','Snail Recording Setup'];
		case 'fig.8.6' : return ['Figure 8.6','Fig. 8.6','Circumesophageal Ganglia','Circumesophageal Ganglia'];
		case 'fig.8.7' : return ['Figure 8.7','Fig. 8.7','Action Potential Measurements','AP Measurements'];
		case 'fig.8.8' : return ['Figure 8.8','Fig. 8.8','Burster Measurements','Burst Measurements'];
		case 'fig.8.9' : return ['Figure 8.9','Fig. 8.9','Postinhibitory Rebound','Postinhibitory Rebound'];
		case 'vid.8.1' : return ['Video 8.1','Vid. 8.1','Entire Snail Dissection','Entire Snail Dissection'];
		case 'vid.8.2' : return ['Video 8.2','Vid. 8.2','Removing the Shell','Removing the Shell'];
		case 'vid.8.3' : return ['Video 8.3','Vid. 8.3','Removing Ganglia','Removing Ganglia'];
		case 'vid.8.4' : return ['Video 8.4','Vid. 8.4','Pinning','Pinning'];
		case 'vid.8.5' : return ['Video 8.5','Vid. 8.5','Cutting the Aorta','Cutting the Aorta'];
		case 'vid.8.6' : return ['Video 8.6','Vid. 8.6','Desheathing','Desheathing'];
		case 'vid.8.7' : return ['Video 8.7','Vid. 8.7','Snail Brain Recording','Snail Brain Recording'];
		case 'vid.8.8' : return ['Video 8.8','Vid. 8.8','Na<sup>+</sup> Potentials','Na<sup>+</sup> Potentials'];
		case 'vid.8.9' : return ['Video 8.9','Vid. 8.9','Ca<sup>2+</sup> Potentials','Ca<sup>2+</sup> Potentials'];
		case 'vid.8.10' : return ['Video 8.10','Vid. 8.10','Bursting','Bursting'];
		case 'vid.8.11' : return ['Video 8.11','Vid. 8.11','Stimulation','Stimulation'];
		case 'vid.8.12' : return ['Video 8.12','Vid. 8.12','Synaptic Input','Synaptic Input'];
		case 'fig.8.1i' : return ['Figure 8.1i','Fig. 8.1i','Silent Cell Stimulation','Stimulation'];
		case 'fig.8.2i' : return ['Figure 8.2i','Fig. 8.2i','Broadening and Accommodation','Broadening and Accommodation'];
		case 'fig.8.3i' : return ['Figure 8.3i','Fig. 8.3i','Amplitude Decrease','Amplitude Decrease'];
		case 'fig.8.4i' : return ['Figure 8.4i','Fig. 8.4i','Tonic Firing','Tonic Firing'];
		case 'fig.8.5i' : return ['Figure 8.5i','Fig. 8.5i','Hyperpolarization','Hyperpolarization'];
		case 'fig.8.6i' : return ['Figure 8.6i','Fig. 8.6i','Burster Stimulation','Burster Stimulation'];

		// 9. Snail Brain&mdash;Ionic Basis
		case 'fig.9.1i' : return ['Figure 9.1i','Fig. 9.1i','Reduced Calcium','Reduced Calcium'];
		case 'fig.9.2i' : return ['Figure 9.2i','Fig. 9.2i','Effect of Barium','Effect of Barium'];
		case 'fig.9.3i' : return ['Figure 9.3i','Fig. 9.3i','Effect of TEA and Cs<sup>+</sup>','Effect of TEA and Cs<sup>+</sup>'];

		// 11. Snail Nerve&mdash;Motor Control of Feeding
		case 'fig.11.1' : return ['Figure 11.1','Fig. 11.1','Feeding Pattern','Feeding Pattern'];
		case 'fig.11.2' : return ['Figure 11.2','Fig. 11.2','Dissection Steps','Dissection Steps'];
		case 'fig.11.3' : return ['Figure 11.3','Fig. 11.3','Buccal Ganglia','Buccal Ganglia'];
		case 'fig.11.4' : return ['Figure 11.4','Fig. 11.4','Nerve Recording Setup','Nerve Recording'];
		case 'fig.11.5' : return ['Figure 11.5','Fig. 11.5','Buccal Ganglia','Buccal Ganglia'];
		//case 'vid.11.1' : return ['Video 11.1','Vid. 11.1','Dissect and Record','Dissect and Record'];
		case 'vid.11.1.he' : case 'vid.11.1.ly' : return ['Video 11.1','Vid. 11.1','Feeding Behavior','Feeding Behavior'];
		case 'vid.11.2.he' : case 'vid.11.2.ly' : return ['Video 11.2','Vid. 11.2','Removing the Shell','Removing the Shell'];
		case 'vid.11.3.he' : case 'vid.11.3.ly' : return ['Video 11.3','Vid. 11.3','Exposing the Ganglia','Exposing the Ganglia'];
		case 'vid.11.4.he' : case 'vid.11.4.ly' : return ['Video 11.4','Vid. 11.4','Nerve Recording','Nerve Recording'];
		case 'vid.11.1.ly' : return ['Video 11.1','Vid. 11.1','Feeding Behavior','Feeding Behavior'];
		case 'vid.11.2.ly' : return ['Video 11.2','Vid. 11.2','Removing the Shell','Removing the Shell'];
		case 'vid.11.3.ly' : return ['Video 11.3','Vid. 11.3','Exposing the Ganglia','Exposing the Ganglia'];
		case 'vid.11.4.ly' : return ['Video 11.4','Vid. 11.4','Nerve Recording','Nerve Recording'];
		// 12.
		case 'vid.12.1.he' : case 'vid.12.1.ly' : return ['Video 12.1','Vid. 12.1','Removing Ganglia','Removing Ganglia'];
		case 'vid.12.2.he' : case 'vid.12.2.ly' : return ['Video 12.2','Vid. 12.2','Ganglion Recording','Ganglion Recording'];
		case 'vid.12.3a' : return ['Video 12.3a','Vid. 12.3a','Endogenous Rhythm','Endogenous'];
		case 'vid.12.3b' : return ['Video 12.3b','Vid. 12.3b','Exogenous Rhythm','Exogenous'];
		case 'vid.12.3c' : return ['Video 12.3c','Vid. 12.3c','Shallow Rhythm','Shallow Rhythm'];
		case 'vid.12.3d' : return ['Video 12.3d','Vid. 12.3d','Rhythmic Input','Rhythmic Input'];
		case 'vid.12.3e' : return ['Video 12.3e','Vid. 12.3e','Deep Rhythm','Deep Rhythm'];
		case 'vid.12.3f' : return ['Video 12.3f','Vid. 12.3f','Endogenous Rhythm','Endogenous'];
		case 'vid.12.3g' : return ['Video 12.3g','Vid. 12.3g','Endogenous Rhythm','Endogenous'];
		case 'vid.12.3h' : return ['Video 12.3h','Vid. 12.3h','Variable Rhythm','Variable'];
		case 'vid.12.3i' : return ['Video 12.3i','Vid. 12.3i','Regular Rhythm','Regular'];
		case 'vid.12.3j' : return ['Video 12.3j','Vid. 12.3j','Variable Activity','Variable'];
		case 'vid.12.3k' : return ['Video 12.3k','Vid. 12.3k','Silent','Silent'];
		case 'vid.12.3l' : return ['Video 12.3l','Vid. 12.3l','Sparse Bursts','Sparse Bursts'];
		case 'vid.12.3m' : return ['Video 12.3m','Vid. 12.3m','Silent Stimulated','Silent Stimulated'];
		case 'vid.12.3n' : return ['Video 12.3n','Vid. 12.3n','Active Stimulated','Active Stimulated'];

		// 10. Plant Action Potential
		case 'fig.10.1' : return ['Figure 10.1','Fig. 10.1','<i>Chara</i> Cells','<i>Chara</i> Cells'];
		case 'fig.10.2' : return ['Figure 10.2','Fig. 10.2','<i>Chara</i> Cell Diagram','<i>Chara</i> Cell Diagram'];
		case 'fig.10.3' : return ['Figure 10.3','Fig. 10.3','<i>Chara</i> Recording Chamber','<i>Chara</i> Recording Chamber'];
		case 'fig.10.4' : return ['Figure 10.4','Fig. 10.4','<i>Chara</i> Recording Setup','<i>Chara</i> Recording Setup'];
		case 'vid.10.1' : return ['Video 10.1','Vid. 10.1','<i>Chara</i> Preparation','<i>Chara</i> Preparation'];
		case 'vid.10.2' : return ['Video 10.2','Vid. 10.2','<i>Chara</i> Recording','<i>Chara</i> Recording'];
		case 'table.10.1' : return ['Table 10.1','Tab. 10.1','<i>Chara</i> Ion Concentrations','<i>Chara</i> Concentrations'];
		case 'fig.10.1i' : return ['Figure 10.1i','Fig. 10.1i','<i>Chara</i> Chamber Design','<i>Chara</i> Chamber Design'];
		case 'fig.10.2i' : return ['Figure 10.2i','Fig. 10.2i','Repeated Stimulation','Repeated Stimulation'];

		// A. Crayfish Neuromuscular Preparation
		case 'fig.a.1' : return ['Figure A.1','Fig. A.1','Abdominal Muscles','Abdominal Muscles'];
		case 'fig.a.2' : return ['Figure A.2','Fig. A.2','Abdominal Segment','Abdominal Segment'];
		case 'fig.a.3' : return ['Figure A.3','Fig. A.3','Compared with Skeletal Muscle','Compared with Muscle'];
		case 'fig.a.4' : return ['Figure A.4','Fig. A.4','Compared with Brain Synapses','Compared with Dendrite'];
		case 'vid.a.1' : return ['Video A.1','Vid. A.1','Removing the Abdomen','Removing the Abdomen'];
		case 'vid.a.2' : return ['Video A.2','Vid. A.2','Removing Swimmerets','Removing Swimmerets'];

		// B. Dissection Tips
		case 'fig.b.1' : return ['Figure B.1','Fig. B.1','Dissection Posture','Dissection Posture'];
		case 'fig.b.2' : return ['Figure B.2','Fig. B.2','Cutting Tools','Cutting Tools'];
		case 'fig.b.3' : return ['Figure B.3','Fig. B.3','Grasping Tools','Grasping Tools'];

		// C. Recording Tips
		case 'fig.c.1' : return ['Figure C.1','Fig. C.1','Noise Reduction','Noise Reduction'];
		case 'fig.c.2' : return ['Figure C.2','Fig. C.2','Filter Distortion','Filter Distortion'];
		case 'fig.c.3' : return ['Figure C.3','Fig. C.3','Sampling Rates','Sampling Rates'];
		case 'fig.c.4' : return ['Figure C.4','Fig. C.4','Stimulator Settings','Stimulator Settings'];
		case 'fig.c.5' : return ['Figure C.5','Fig. C.5','Microelectrodes','Microelectrodes'];
		case 'vid.c.1' : return ['Video C.1','Vid. C.1','Filter Effects','Filter Effects'];
		case 'vid.c.2' : return ['Video C.2','Vid. C.2','Electrode Filling','Electrode Filling'];
		case 'vid.c.1i' : return ['Video C.1i','Vid. C.1i','Electrode Inking','Electrode Inking'];

		// Equations
		case 'eq.1-ohm' : return ['Equation 1','Eq. 1','Ohm&rsquo;s Law','Ohm&rsquo;s Law'];
		case 'eq.2-tau' : return ['Equation 2','Eq. 2','Time Constant','Time Constant'];
		case 'eq.3-space' : return ['Equation 3','Eq. 3','Space Constant','Space Constant'];
		case 'eq.4-spread' : return ['Equation 4','Eq. 4','Passive Spread','Passive Spread'];
		case 'eq.5-input' : return ['Equation 5','Eq. 5','Input Resistance','Input Resistance'];
		case 'eq.6-nernst' : return ['Equation 6','Eq. 6','Nernst Potential','Nernst Potential'];
		case 'eq.9-saline' : return ['','','Saline Calculator','Saline Calculator'];

		// Equations
//		case 'peaks' : return ['peaks','','Peak Analysis','Peak Analysis'];
//		case 'exponential' : return ['exponential','','Exponential Analysis','Exponential Analysis'];
		case 'peaks' : return false;
		case 'exponential' : return false;

		// lab format
		// case 'lab.url' : return ['Full_title', 'Short_title'];
		// labs
		case 'index' : return ['Crawdad Introduction','Introduction'];
		case '1.membrane' : return ['Membranes','Membrane Prop.'];
		case '2.nerverecording' : return ['Motor Nerve','Nerve Recording'];
		case '3.nerveanatomy' : return ['Nerve Tracing','Nerve Tracing'];
		case '4.restingpotential' : return ['Resting Potential','Resting Potential'];
		case '5.connectivity' : return ['Synapses','Synaptic Connect.'];
		case '6.plasticity' : return ['Plasticity','Synaptic Plasticity'];
		case '7.stretchreceptor' : return ['Stretch Receptor','Stretch Receptor'];
		case '8.snailbrainap' : return ['Snail Brain I','Snail Excitability'];
		case '9.ionicbasisap' : return ['Snail Brain II','Snail Ionic Basis'];
		case '10.plantap' : return ['Plant AP','Plant AP'];
		case '11.snailnerve' : return ['Snail Nerves','Snail Nerves'];
		case '12.snailganglia' : return ['Snail Ganglia','Snail Ganglia'];
		case 'a.nmjprep' : return ['Crayfish NMJ','Crayfish NMJ'];
		case 'b.dissection' : return ['Dissection Tips','Dissection Tips'];
		case 'c.recording' : return ['Recording Tips','Recording Tips'];
		case 'd.pharmacopeia' : return ['Pharmacopeia','Pharmacopeia'];
		case 'e.analysis' : return ['Analysis Tools','Analysis'];
		case 'i.f.animalcare' : return ['Animal Care','Animal Care'];
		case 'i.g.resources' : return ['Resources','Resources'];
/*
		case 'index' : return ['Crawdad Introduction','Introduction'];
		case '1.membrane' : return ['Membrane Properties','Membrane Prop.'];
		case '2.nerverecording' : return ['Motor Nerve Recording','Nerve Recording'];
		case '3.nerveanatomy' : return ['Motor Nerve Tracing','Nerve Tracing'];
		case '4.restingpotential' : return ['Muscle Resting Potential','Resting Potential'];
		case '5.connectivity' : return ['Synaptic Connectivity','Synaptic Connect.'];
		case '6.plasticity' : return ['Synaptic Plasticity','Synaptic Plasticity'];
		case '7.stretchreceptor' : return ['Stretch Receptor','Stretch Receptor'];
		case '8.snailbrainap' : return ['Snail Brain&mdash;Excitability','Snail Excitability'];
		case '9.ionicbasisap' : return ['Snail Brain&mdash;Ionic Basis','Snail Ionic Basis'];
		case '10.plantap' : return ['Plant Action Potential','Plant AP'];
		case '11.snailnerve' : return ['Snail Nerves','Snail Nerves'];
		case '12.snailganglia' : return ['Snail Ganglia','Snail Ganglia'];
		case 'a.nmjprep' : return ['Crayfish NMJ','Crayfish NMJ'];
		case 'b.dissection' : return ['Dissection Tips','Dissection Tips'];
		case 'c.recording' : return ['Recording Tips','Recording Tips'];
		case 'd.pharmacopeia' : return ['Pharmacopeia','Pharmacopeia'];
		case 'e.analysis' : return ['Analysis Tools','Analysis'];
		case 'i.f.animalcare' : return ['Animal Care','Animal Care'];
		case 'i.g.resources' : return ['Resources','Resources'];
*/
		// instructor's supplements
		case 'i.1.membrane' :
		case 'i.2.nerverecording' :
		case 'i.3.nerveanatomy' :
		case 'i.4.restingpotential' :
		case 'i.5.connectivity' :
		case 'i.6.plasticity' :
		case 'i.7.stretchreceptor' :
		case 'i.8.snailbrainap' :
		case 'i.9.ionicbasisap' :
		case 'i.10.plantap' :
		case 'i.11.snailnerve' :
		case 'i.12.snailganglia' :
		case 'i.b.dissection' :
		case 'i.c.recording' :
		case 'i.d.pharmacopeia' :
			return ['Notes','Notes'];
	}
	return [abbrevURL+' not found','missing'];
}


function getFigureWindowSize(abbrevURL) {
	// dimensions of the window content (image/video and caption)
	var a = []; // desired window width,height
	var wLine = 0; // 1 if Windows adds a line to the caption because of different text wrapping
//console.log(abbrevURL);
	switch(abbrevURL) {

		case 'index' : a = [656,616]; break;

		case 'fig.1.1' : a = [616,207]; break;
		case 'fig.1.2' : a = [666,608]; wLine = 1; break;
		case 'fig.1.3' : a = [616,283]; wLine = 1; break;
		case 'fig.1.4' : a = [616,267]; break;
		case 'fig.1.5' : a = [616,491]; break;
		case 'fig.1.6' : a = [578,235]; break;
		case 'fig.1.7' : a = [574,296]; break;
		case 'vid.1.1' : a = [656,228]; break;
		case 'fig.1.1i' : a = [616,224]; break;
		case 'fig.1.2i' : a = [436,378]; wLine = 1; break;
		case 'fig.1.3i' : a = [436,428]; break;
		case 'fig.1.4i' : a = [466,408]; break;
		case 'fig.1.5i' : a = [556,395]; wLine = 1; break;
		case 'fig.1.6i' : a = [416,450]; break;
		case 'vid.1.1i' : a = [656,488]; wLine = 1; break;
		case 'vid.1.2i' : a = [656,454]; break;
		//
		case 'fig.2.1' : a = [556,330]; break;
		case 'vid.2.1' : a = [656,578]; break;
		case 'vid.2.2' : a = [656,595]; wLine = 1; break;
		case 'vid.2.3' : a = [656,612]; break;
		case 'fig.2.1i' : a = [541,382]; break;
		case 'fig.2.2i' : a = [541,399]; break;
		case 'fig.2.3i' : a = [541,382]; break;
		case 'fig.2.4i' : a = [576,824]; break;
		case 'fig.2.5i' : a = [512,394]; wLine = 1; break;
		//
		case 'fig.3.1' : a = [466,500]; break;
		case 'fig.3.2' : a = [716,406]; break;
		case 'vid.3.1' : a = [656,577]; break;
		case 'vid.3.2' : a = [656,594]; break;
		case 'vid.3.3' : a = [656,611]; break;
		case 'vid.3.4' : a = [656,611]; break;
		case 'vid.3.5' : a = [656,611]; break;
		case 'fig.3.1i' : a = [576,587]; break;
		//
		case 'fig.4.1' : a = [556,331]; wLine = 1; break;
		case 'vid.4.1' : a = [656,577]; break;
		case 'vid.4.2' : a = [656,611]; break;
		case 'vid.4.3' : a = [656,611]; break;
		case 'table.4.1' : a = [520,218]; wLine = 1; break;
		case 'fig.4.1i' : a = [656,556]; break;
		case 'fig.4.2i' : a = [571,592]; wLine = 1; break;
		//
		case 'fig.5.1' : a = [556,291]; break;
		case 'vid.5.1' : a = [656,592]; break;
		case 'vid.5.2' : a = [656,611]; break;
		case 'vid.5.3' : a = [656,611]; break;
		case 'fig.5.1i' : a = [509,382]; break;
		case 'fig.5.2i' : a = [509,400]; break;
		case 'fig.5.3i' : a = [509,366]; break;
		case 'fig.5.4i' : a = [509,418]; break;
		//
		case 'fig.6.1' : a = [556,291]; break;
		case 'vid.6.1' : a = [656,592]; break;
		case 'vid.6.2' : a = [656,594]; break;
		case 'vid.6.3' : a = [656,594]; break;
		case 'vid.6.4' : a = [656,611]; break;
		case 'fig.6.1i' : a = [643,347]; break;
		case 'fig.6.2i' : a = [536,395]; break;
		case 'fig.6.3i' : a = [516,408]; break;
		case 'fig.6.4i' : a = [362,466]; break;
		//
		case 'fig.7.1' : a = [465,425]; break;
		case 'fig.7.2' : a = [664,537]; break;
		case 'fig.7.3' : a = [616,327]; break;
		case 'fig.7.4' : a = [556,331]; break;
		case 'vid.7.1' : a = [656,577]; break;
		case 'vid.7.2' : a = [656,594]; break;
		case 'vid.7.3' : a = [656,594]; break;
		case 'vid.7.4' : a = [656,611]; break;
		case 'vid.7.5' : a = [656,611]; break;
		case 'vid.7.6' : a = [656,594]; break;
		case 'vid.7.7' : a = [656,611]; break;
		case 'vid.7.8' : a = [656,594]; break;
		case 'fig.7.1i' : a = [416,372]; break;
		case 'fig.7.2i' : a = [633,308]; break;
		case 'fig.7.3i' : a = [616,558]; break;
		//
		case 'fig.8.1' : a = [616,506]; break;
		case 'fig.8.2' : a = [656,276]; break;
		case 'fig.8.3' : a = [596,531]; break;
		case 'fig.8.4' : a = [1016,536]; break;
		case 'fig.8.5' : a = [556,331]; break;
		case 'fig.8.6' : a = [656,478]; break;
		case 'fig.8.7' : a = [516,391]; break;
		case 'fig.8.8' : a = [516,408]; wLine = 1; break;
		case 'fig.8.9' : a = [516,394]; break;
		case 'vid.8.1' : a = [656,577]; break;
		case 'vid.8.2' : a = [656,611]; break;
		case 'vid.8.3' : a = [656,611]; wLine = 1; break;
		case 'vid.8.4' : a = [656,611]; break;
		case 'vid.8.5' : a = [656,611]; break;
		case 'vid.8.6' : a = [656,611]; break;
		case 'vid.8.7' : a = [656,611]; break;
		case 'vid.8.8' : a = [656,594]; break;
		case 'vid.8.9' : a = [656,594]; break;
		case 'vid.8.10' : a = [656,594]; break;
		case 'vid.8.11' : a = [656,611]; break;
		case 'vid.8.12' : a = [656,611]; break;
		case 'fig.8.1i' : a = [516,392]; wLine = 1; break;
		case 'fig.8.2i' : a = [516,462]; break;
		case 'fig.8.3i' : a = [516,462]; break;
		case 'fig.8.4i' : a = [516,411]; break;
		case 'fig.8.5i' : a = [516,428]; break;
		case 'fig.8.6i' : a = [516,411]; break;
		//
		case 'fig.9.1i' : a = [516,428]; break;
		case 'fig.9.2i' : a = [516,411]; wLine = 1; break;
		case 'fig.9.3i' : a = [516,411]; break;
		//
		case 'fig.11.2' : a = [724,690]; wLine = 1; break;
		case 'fig.11.3' : a = [616,812]; wLine = 1; break;
		case 'vid.11.1.he' : case 'vid.11.1.ly' : a = [976,858]; break;
		case 'vid.11.2.he' : case 'vid.11.2.ly' : a = [736,872]; break;
		case 'vid.11.3.he' : case 'vid.11.3.ly' : a = [736,888]; break;
		case 'vid.11.4.he' : case 'vid.11.4.ly' : a = [736,872]; break;
		case 'vid.11.5.he' : case 'vid.11.5.ly' : a = [736,872]; break;
		case 'vid.11.6.he' : case 'vid.11.6.ly' : a = [736,872]; break;
		//
		case 'vid.12.1.he' : case 'vid.12.1.ly' : a = [736,872]; break;
		//
		case 'fig.10.1' : a = [516,362]; break;
		case 'fig.10.2' : a = [536,237]; break;
		case 'fig.10.3' : a = [556,192]; break;
		case 'fig.10.4' : a = [556,312]; break;
		case 'table.10.1' : a = [375,174]; break;
		case 'vid.10.1' : a = [656,611]; break;
		case 'vid.10.2' : a = [656,611]; break;
		case 'fig.10.1i' : a = [541,583]; break;
		case 'fig.10.2i' : a = [516,376]; break;
		//
		case 'fig.a.1' : a = [616,506]; break;
		case 'fig.a.2' : a = [658,590]; break;
		case 'fig.a.3' : a = [586,442]; wLine = 1; break;
		case 'fig.a.4' : a = [616,442]; wLine = 1; break;
		case 'vid.a.1' : a = [656,611]; break;
		case 'vid.a.2' : a = [656,594]; break;
		//
		case 'fig.b.1' : a = [616,494]; break;
		case 'fig.b.2' : a = [436,445]; break;
		case 'fig.b.3' : a = [366,242]; break;
		//
		case 'fig.c.1' : a = [616,504]; break;
		case 'fig.c.2' : a = [516,372]; break;
		case 'fig.c.3' : a = [546,591]; break;
		case 'fig.c.4' : a = [516,341]; wLine = 1; break;
		case 'fig.c.5' : a = [496,312]; break;
		case 'vid.c.1' : a = [656,611]; break;
		case 'vid.c.2' : a = [656,594]; wLine = 1; break;
		case 'vid.c.1i' : a = [656,611]; break;
		//
		case 'eq.1-ohm' : a = [250,140]; break;
		case 'eq.2-tau' : a = [250,140]; break;
		case 'eq.3-space' : a = [255,208]; break;
		case 'eq.4-spread' : a = [250,166]; break;
		case 'eq.5-input' : a = [280,190]; break;
		case 'eq.6-nernst' : a = [280,240]; break;
		case 'eq.7-ghk' : a = [00,00]; break;
		case 'eq.8-pcm' : a = [00,00]; break;
		case 'eq.9-saline' : a = [282,256]; break;

		case 'peaks' : a = [1024,830]; break;
		case 'exponential' : a = [1024,620]; break;
	}
	if (a[0] <= 0) return [0,0];

	// PROBLEM is that window size may include whatever crap the browser puts under the title bar.
	// Thus we have to adjust height on a browser-by-browser basis (may have to also adjust width on Windows).
	// Safari (Mac) obeys the request to not show the address field etc. and is thus correct. That might change based on user preferences.
	// Firefox (Mac) shows the address field and makes the window 12 px too short
	// Firefox (Win) shows the address field BUT sets the window properly to the desired innerHeight!
	// Opera (Mac) includes address bar AND title bar in the window size.
	// Chrome (Mac) includes the address bar in the window size.
	// MSIE 10 (Win) sizes window 4px larger than requested in both dimensions

	// Does this mean that I'll have to go back to the FixHeight() hack after the window opens? Not with the adjustments below.

	// I probably DO have to fix the height later to make the innerHeight and innerWidth what they need to be
	// problem is that this stuff seems to change with every system or browser update

	var addH = 0, addW = 0;

	var isWindows = (navigator.platform.indexOf('Win') >= 0);
	var isMac = (navigator.platform.indexOf('Mac') >= 0);
	var browser = browserType();
//console.log('browser',browser);
	//var ua = navigator.userAgent.toLowerCase();
	if (browser == 'Firefox' && isMac) addH += 0; // OK 6/3/16, need to test Windows; 6/18/16 appears OK in Windows and wLine is needed
	if (browser == 'Opera' && isMac) addH += 0; // OK 6/7/16, need to test Windows
	if (browser == 'Chrome' && isMac ) addH += 0; // OK 5/5/20 (was +20)
	if (browser == 'Chrome' && isWindows ) { addH += 20; wLine = 0; } // OK 6/3/16, need to test Windows
	if (browser == 'Edge' ) { addH += 0; wLine = 0; } // OK 6/3/16
	if (browser == 'Safari' ) addH = 22; // OK 6/3/16
	if (browser == 'MSIE10' || browser == 'MSIE') { addW -= 4; addH -= 4; } // need to test Windows; test MSIE 11
	if (isWindows) addH += 16*wLine; // Windows may change line breaks and require an extra caption line
	//if (browser == 'MSIE10' && url.toLowerCase().indexOf('vid') >= 0 ) addH += 20;
//alert(url.toLowerCase()+' '+addH+' '+wLine+' '+isWindows+' '+browser);
	return [a[0]+addW,a[1]+addH];
}

