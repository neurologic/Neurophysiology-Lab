# Materials

This course has been designed to utilize open source materials as much as possible. This includes software used to interface with acquisition hardware and analysis of digitized data.

One motivation was to reduce proprietary software costs. 
Another motivation is to make the data processing and analysis materials generalizable across various data acquisition platforms that have traditionally been used in Neurophysiology Labs. At the time of publishing, the executable notebooks used in this course are 

## Hardware
- NiUSB 6211 [^footnote1] [^footnote2]

[^footnote1]: I think that the [Teensy Development Boards](https://www.pjrc.com/teensy/) would enable adequate ADC functionality. For example, they have been used [to record weakly electric fish EODs in the field](https://github.com/muchaste/EOD-Logger). If anyone wants to help me develop this, please reach out!

[^footnote2]: Price at time of purchase in 2021 was approximately $700. This cost has doubled in the past year. Other models can be used from Nidaq that are cheaper. Cheaper models would likely have fewer channels or slower sampling rates.
A USB model was chosen so that a wider range of refurbished PCs could be used (instead of requiring a large form factor case to house PCI devices). Additionally, USB models seemed to be cheaper for similar features. I have found great results (low noise, good resolution, reliable drivers, etc) with USB acquisition from Nidaq. 


- PC computer running Windows OS

## Equipment
- suction electrodes [^footnote3]

[^footnote3]: The Wesleyan machine shop fabricated AWESOME suction electrodes that replace the use of *Axon Instrument* style pipette holders normally referenced in the literature [^footnote4] for labs requiring suction electrodes.

[^footnote4]: [Johnson BR, Hauptman SA, Bonow RH. Construction of a simple suction electrode for extracellular recording and stimulation. J Undergrad Neurosci Educ. 2007;6(1):A21-A26.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3592669/#)

- Electrode holders with manipulators
- Backyard Brains
- Differential 'extracellular' amplifier. We have Grass Instruments P-15s in the lab. I love them. However, I have achieved equivalently good results by implementing [Backyard Brains'](https://backyardbrains.com/) Neuron Spiker Box ([DIY](https://backyardbrains.com/products/diyspikerbox) and [Pro](https://backyardbrains.com/products/neuronspikerboxpro)). The DIY works great. The Pro is more expensive, but it does have a "volume" (aka amplification) control, which has been nice at times.  
- Intracellular amplifier. I used the ____ that the course at Wesleyan has had for years. I love them. Simple and effective. Bruce Land has published [circuit specs to make your own](https://people.ece.cornell.edu/land/PROJECTS/preamp2/index.html). I have tried to make them for myself following his instructions, but have not had success yet (because I have not acutally needed to troubleshoot it yet, so it is just on the back-burner... I have full confidence his outline would produce great results.)

## Software
- <a href="https://bonsai-rx.org/">Bonsai-rx</a> is a package that can simultaneously manage streams of data coming from unrelated sources (for example video input and ADC input). [^footnote5]  

[^footnote5]: Unfortunately(?), currently Bonsai-rx only works on Windows PC.  

- <a href="">Anaconda</a> is a Python package manager that contains packages for managing, creating, and editing jupyter (.ipynb) notebooks. 

- <a href="">Google Colaboratory</a> is a cloud-based server on which anyone can run jupyter notebooks (.ipynb) without needing to install anything on their computer. 

- Google Drive [^footnote6]

[^footnote6]: Google Drive was used for file storage and access when competing the executable notebooks. Wesleyan has GSuite with unlimited Drive storage. There are other ways to achieve this goal, but this has been a simple solution that was especially attractive because of Google Collaboratories "Mount Google Drive" module.  

## Animals
- Weakly electric fish (could be replaced with a function generator). I happen to study weakly electric fish anyway and love them so I have them around.
- Cockroaches
- Crayfish [^footnote7]

[^footnote7]: If you are in the United States, you can get them from LA crayfish company for pretty cheap (expect many from the shipment to not survive... plan to have a crawfish boil with the less healthy ones upon arrival). Or you can get them (at a higher cost) from Carolina Biological throughout the year. 

- Humans with muscles [^footnote8]

[^footnote8]: Please be sensitive to people from cultures or backgrounds that would not feel comfortable exposing skin during class to apply surface EMG electrodes. In the classroom session before you do any of the human EMG modules, explain the procedure to the students and ask them to email you in private to address any concerns and to explore alternate (equally engaging) alternatives to the procedure. For example, you could have them use the lab room independently to explore their muscle activity in private. Or they could decide ahead of time that they will refrain from volunteering as a human subject. Having partners in lab means that not every student needs to do every procedure if they do not feel comfortable. 
