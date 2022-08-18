# Dash Data Explorer

An application written in python that uses the dash modules from plotly to create a (relatively) fast, interactive graph of raw binary data (.Net.Mat) collected in Bonsai-rx. 

***usage***: DataExplorer [-h] -filepath FILEPATH -fs FS -n NUMBER_CHANNELS -p NUMBER_SUBPLOTS -c
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
