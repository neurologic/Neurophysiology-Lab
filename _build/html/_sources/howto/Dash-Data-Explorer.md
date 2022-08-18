# Dash Data Explorer

An application written in python that uses the dash modules from plotly to create a (relatively) fast, interactive graph of raw binary data (.Net.Mat) collected in Bonsai-rx. 

## Get the app

1. Download the application file. Click on [the link to the application file](https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/howto/Data-Explorer.py). Then *right mouse click* in the raw file window and select 'Save As...' to save the file to your computer (using the default file name '**Data-Explorer**' with file extension '**py**'). Save the file somewhere easy to access, like your documents folder.

##  Usage

1. Make sure you have installed [Anaconda Individual Edition](https://www.anaconda.com/products/distribution) by downloading and executing the appropriate installer for your operating system.
2. Launch the Anaconda Navigator
3. Open the PowerShell prompt application
	:::{dropdown} Creating an environment with dash
	If you have not already done so, you will need to create an environment to run the application in. The environment must have dash installed.  
	Execute the following commands at the command line.  
	```conda create --name neurolab --clone base```  
	```conda install -c conda-forge dash```
	:::
4. Activate your anaconda environment (created in step 1) using ```conda activate neurolab```. 
5. Navigate the command line to the folder that contains the application file that you downloaded/saved.

	:::{dropdown} Navigating the command line on MacOS
	commands to get to the folder on a mac
	:::

	:::{dropdown} Navigating the command line on WindowsOS
	commands to get to the folder on WindowsOS
	:::

6. Follow the command line syntax below to provide the application with all the necessary information about your file and how you want it plotted in the Data Explorer when it launches. 

	:::{admonition} filepath TIP
	copy the full filepath from the file browswer.
	- on a mac right mouse click the filename, then press the *option* key, then select "Copy as Pathname"
	- on a Windows hold down the *Shift* key while right-clicking the file name. then select "Copy Full Path"
	:::

	***command line syntax***: DataExplorer [-h] -filepath FILEPATH -fs FS -n NUMBER_CHANNELS -p NUMBER_SUBPLOTS -c
	                    CHANNELS_PER_SUBPLOT [CHANNELS_PER_SUBPLOT ...]

	***optional arguments***:
	- -h, --help            show this help message and exit
	- -filepath FILEPATH    full path to the file location on your local computer
	- -fs FS                sampling rate of the data in file
	- -n NUMBER_CHANNELS    number of channels data in file
	- -p NUMBER_SUBPLOTS    number of subplots
	- -c CHANNELS_PER_SUBPLOT [CHANNELS_PER_SUBPLOT ...]
	                        list of channels to plot on each subplot (listed in order of
	                        appearance)

7. Open a browser window (Chrome recommended) and go to your local server](http://127.0.0.1:8050/)
	  > Note that this link will only work if you have already run the Data Explorer application from the terminal
8. **Shut down the application appropriately** by holding down the *Control* key while you press the *C* key. 

	:::{dropdown} If you get an error next time you try to run the applicaiton
	If you can an error that the application is already running on the server, then it did not get shut down appropriately the last time. In the terminal, use the command ```sudo lsof -1:8050``` to shut down the server and free it up for the application again. 
	:::
