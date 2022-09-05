# Dash Data Explorer

An application written in python that uses the dash modules from plotly to create a (relatively) fast, interactive graph of raw binary data (.Net.Mat) collected in Bonsai-rx. 

## Get the app

1. Click on [this link to the application file](https://raw.githubusercontent.com/neurologic/Neurophysiology-Lab/main/howto/Data-Explorer.py). Then hit *CONTROL*+*S* and a "Save As" window will pop up (or *right mouse click* in the window over the text and and select 'Save As...'). Save the file to your computer (using the default file name '**Data-Explorer**' with file extension '**py**'). Save the file somewhere easy to access, like your documents folder.
2. ***If you are on WindowsOS***, the OS often automatically appends '**txt**' to the end when you *Save As*. This will prevent the application from running. Use [**Sublime Text Editor**](https://www.sublimetext.com/) to open the file. In the *Sublime* text editor, select ```File>SaveAs``` and select the ```Python``` file type option. Delete the *txt* file.

##  Usage

1. Make sure you have installed [Anaconda Individual Edition](https://www.anaconda.com/products/distribution) by downloading and executing the appropriate installer for your operating system.
2. Launch the Anaconda Navigator
3. Open the PowerShell Prompt application
	:::{dropdown} Create an environment with dash if you have not yet done so
	If you have not already done so, you will need to create an environment to run the application in. The environment must have dash installed.  
	Execute the following commands at the PowerShell Prompt command line and follow given instructions along the way.  
	1. ```conda create --name neurolab --clone base```  
	2. After the environment has been created, you must activate it before proceeding with:  
	```conda activate neurolab``` 
	3. ```conda install -c conda-forge dash``` 
	Type *Y* followed by the *Enter/Return* key when prompted.
	:::
4. Activate the *neurolab* anaconda environment (created in step 3: 'Creating an environment with dash') by typing the text ```conda activate neurolab``` into the PowerShell Prompt command line and then hitting the *Enter* key. 
5. Navigate the command line to the folder that contains the *Data-Explorer.py* application file that you downloaded/saved.

	:::{dropdown} Navigating the command line on MacOS
	```cd folderpath```  
	To get the folder path, right mouse click the folder in the "Finder", then press the *option* key, then select "Copy as Pathname". You can then *CONTROL*+*P* to paste it into the command line. Note that Mac does not include the quotation marks around the filepath when you paste it, so you must do so manually.
	:::

	:::{dropdown} Navigating the command line on WindowsOS
	```cd folderpath```  will work most of the time. If you are changing drives (C drive to E drive, for example) you may need to do ```cd /D folderpath(including prepended drive letter)``` 
	To get the folder path, hold down the *Shift* key while right-clicking the folder name. then select "Copy Full Path". You can then *CONTROL*+*P* to paste it into the command line.
	:::

6. Follow the command line syntax below to provide the application with all the necessary information about your file and how you want it plotted in the Data Explorer when it launches. 

	:::{admonition} filepath TIP
	copy the full filepath to your data from the file browswer so that you can paste it into the command line rather than typing it out.
	- on a Mac right mouse click the filename, then press the *option* key, then select "Copy as Pathname"
	- on a Windows hold down the *Shift* key while right-clicking the file name. then select "Copy Full Path"
	:::

	***command line syntax***: python Data-Explorer\.py [-h] -filepath FILEPATH -fs FS -n NUMBER_CHANNELS -p NUMBER_SUBPLOTS -c
	                    CHANNELS_PER_SUBPLOT [provide additional -c flags for additional subplots >1]

	***optional arguments***:
	- -h, --help            show this help message and exit
	***required arguments***:
	- -filepath FILEPATH    full path to the file location on your local computer
	- -fs FS                sampling rate of the data in file
	- -n NUMBER_CHANNELS    number of channels data in file
	- -p NUMBER_SUBPLOTS    number of subplots to create
	- -c CHANNELS_PER_SUBPLOT [CHANNELS_PER_SUBPLOT ...]
	                        list of channels to plot on each subplot (listed in order of
	                        appearance)

7. Open a browser window (Chrome recommended) and go to [your local server](http://127.0.0.1:8050/) (127.0.0.1:8050)
	  > Note that this link will only work if you have already run the Data Explorer application from the terminal
8. **Shut down the application appropriately** 
	- Mac: hold down the *Control* key while you press the *C* key. 
	- Windows: hold down the *Control* key while you press the *Pause/Break* key. 

	:::{dropdown} If you get an error next time you try to run the applicaiton
	If you can an error that the application is already running on the server, then it did not get shut down appropriately the last time. In the terminal, use the command ```sudo lsof -1:8050``` to shut down the server and free it up for the application again. 
	:::

## HELP: Screen Recordings

Sign in to your Wesleyan Gmail account to see the videos shared via *Microsoft Stream*.  
Links to the videos shared via Google Drive are below each header.  

### Downloading the Data-Explorer application

[Google Drive share link](https://drive.google.com/file/d/19TQhdG2ghHtebo5ydBwdubMtQs7N-fEB/view?usp=sharing)

<div style='max-width: 640px'><div style='position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;'><iframe width="640" height="360" src="https://web.microsoftstream.com/embed/video/a5a745ea-8532-4b5d-a2a4-51b7593abe9f?autoplay=false&showinfo=true" allowfullscreen style="border:none; position: absolute; top: 0; left: 0; right: 0; bottom: 0; height: 100%; max-width: 100%;"></iframe></div></div>

### Setting up Anaconda with Python Environment

[Google Drive share link](https://drive.google.com/file/d/1I1TQeN5JVk0kIw2RvcyqMLCiazTQoCIt/view?usp=sharing)

<div style='max-width: 640px'><div style='position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;'><iframe width="640" height="360" src="https://web.microsoftstream.com/embed/video/a11ed7de-e722-444e-8306-6e7cf440b2c2?autoplay=false&showinfo=true" allowfullscreen style="border:none; position: absolute; top: 0; left: 0; right: 0; bottom: 0; height: 100%; max-width: 100%;"></iframe></div></div>

### Running the Data-Explorer application

This screen recording of the process includes some troubleshooting as well. 

[Google Drive share link](https://drive.google.com/file/d/17FdCjo2DAc4HyP6eCvRD2-_BEh1ZihJq/view?usp=sharing)

<div style='max-width: 640px'><div style='position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;'><iframe width="640" height="360" src="https://web.microsoftstream.com/embed/video/1e19f822-6f38-4850-abf1-635a88390661?autoplay=false&showinfo=true" allowfullscreen style="border:none; position: absolute; top: 0; left: 0; right: 0; bottom: 0; height: 100%; max-width: 100%;"></iframe></div></div>
