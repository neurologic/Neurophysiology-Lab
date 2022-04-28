#!/usr/bin/env python
# coding: utf-8

# <a id="intro"></a>
# # Introduction to Colab Notebooks
# 
# This first notebook will introduce you to Colab Notebooks using Google's "Colaboratory" server. Colab notebooks are a handy coding environment for learning as well as sharing code with others.
# 
# At the end of this notebook, you'll be able to:
# * Recognize the main features of Colab Notebooks
# * Use Colab Notebooks to run Python3 Code
# * Identify and edit simple Markdown code
# * Practice interacting with data plots 
# 

# <hr>
# 
# <a id="toc"></a>
# # Table of Contents
# 1. [Part I. Getting Started](#one)
# 2. [Part II. About Python Code](#two)
# 2. [Part III. Using Markdown](#three)
# 3. [Part IV. Generate some plots](#four)
# 
# <hr>

# <a id="one"></a>
# # **Part I. Getting started**
# 
# At any point, you can click navigation hyperlinks to jump around between sections. For example, return to the Introduction by clicking: [Return to the Introduction](#intro)
# 
# ## About Colab Notebooks
# Colab notebooks allow you to combine **executable code**, **text**, and **code output** (such as images) in a single document. To save any work you do in a Colab notebook, it needs to be stored in your Google Drive account. You can then easily share your Colab notebooks with co-workers or friends, allowing them to comment on your notebooks or even edit them. To learn more, see Overview of Colab (/notebooks/basic_features_overview.ipynb). 
# 
# To save a Colab notebook to your drive, you can use the File menu above and select ```Save a copy in Drive```. Notebooks will automatically be saved in a "Colab Notebooks" folder in your Google Drive. You can reorganize from there if you like. To re-open a notebook to view your work and/or continue working, open it directly from your Google Drive (If necessary: ```Open With``` -> ```connected apps``` -> ```Google Colaboratory```) 
# 
# Colab notebooks are Jupyter notebooks that are hosted by Colab. To learn more about the Jupyter project, see [jupyter.org](https://www.jupyter.org). They can run on Google's 'Research Collaboratory' platform (as you are doing now) so that you do not need to download any programs locally. However, working with these notebooks on Colab does require an internet connection. 
# 
# ## Menu Options & Shortcuts
# There are also a large number of useful keyboard shortcuts. Click on the 'Tools' menu, and then 'Keyboard Shortcuts' to see a list.
# 
# ## "Running" Code
# In order for the text (code) written in these notebooks to **do** anything, the text needs to be **run**. Running code means *executing* it. The python <b>'kernel'</b> is the thing that executes your code. It is what connects the notebook (as you see it) with the DataHub computers at Google that run/execute code.
# 
# ## Types of Cells
# Colab Notebooks have two types of cells, a <b>Markdown</b> (like this one) and <b>Code</b>. You won't need to *run* the Markdown cells, just read through them. However, when we get to a code cell, you need to tell the kernel to run the lines of code that it contains. Then, the Python kernel will run whatever it recognizes as code within the cell.
# 
# *How do you recognize a code cell?* Each code cell has a ```play button``` at the top left corner (a circle with a right-pointing triangle in it).
# When you click on a code cell, it will be popped out (shadowed) and you will then be in *command mode* for that cell. You can then press the play button to execute that code cell (and run the code it contains). Alternatively, you can hit ```Control + Enter``` on your keyboard.
# 
# *Throughout the notebook, you will see instructions* starting with  **```TASK:```**. Often, the task includes running the code cell. Sometimes, the task will also includes making selection from a list or typing information into the code cell.  
# 
# Most of the code in these notebooks have been hidden for clarity so that you can focus on the data exploration and visualization tasks and save most of the "computer coding" learning for another time. You can ignore anywhere that it says ```Show Code```. If you accidentally get "inside" one of these code cells, simply double-click to the right where you see either black space normal-looking text.  
# 
# If you accidentally get "inside of" a Markdown cell, simply double click the version on the right-hand side of the cell to get back to normal-looking formatting. 

# <a id="two"></a>
# # **Part II. About Python Code**
# [Return to Table of Contents](#toc)
# 
# As you read in ["Part I. Getting Started"](#one), the document you are reading is not a static web page, but an interactive environment that lets you write and execute code.
# 
# For example, here is a **code cell** with a short Python script that computes a value, stores it in a variable, and prints the result:
# 

# In[ ]:


seconds_in_a_day = 24 * 60 * 60

print(seconds_in_a_day)


# To execute the code in the above cell, select it with a click and then either press the play button to the left of the code, or use the keyboard shortcut "Command/Ctrl+Enter". 
# 
# Variables that you define in one cell can later be used in other cells:

# In[ ]:


seconds_in_a_week = 7 * seconds_in_a_day

print(seconds_in_a_week)


# To edit the code, just click the cell and start editing. In the code cell below, type in a value for x after ```x = ``` (on the same line) and then run the code cell to print the value you assigned as an output of the code cell. 

# In[ ]:


x = 

print(x)


# In Python, anything with a "#" in front of it is code annotation, and is not read by the computer. For example, see the code cell below. Follow the instructions in the last line of the code cell. 

# In[ ]:


# In Python, anything with a "#" in front of it is code annotation,
# and is not read by the computer.

# This print function allows us to generate messages.
print('Nice work!')

# Run this code cell to execute the code and generate the message.


# <a id="three"></a>
# # **Part III. Using Markdown**
# [Return to Table of Contents](#toc)
# 
# Markdown is useful because it can be formatted using simple symbols.
# * You can create bulleted lists using asterisks.
# * Similarly, you can create numbered lists using numbers.
# * You can **bold** with two asterisks or underscores on either side (`**bold**`) or *italicize* with one asterisk or underscore (`*italicize*`)
# * Pound signs (#) create headers. More pound signs means a smaller header.
# 
# <b>Task:</b> Edit the markdown cell below with a quick biography of yourself. To edit, double click the cell. You should have your name as a big header, a short quippy subtitle for yourself as a smaller header, and a three bullet points that use both <b>bold</b> and <i>italic</i>. As you type, you will see a preview to the right of what you are typing. After you finish editing it, double-click on the preview to the right to finalize the Markdown (or hit Shift+Enter). You can re-edit as much as needed by double-clicking again on the Markdown cell. 

# Edit this markdown cell!

# <a id="four"></a>
# # **Part IV: Generate some plots**
# [Return to Table of Contents](#toc)
# 
# ## Step 1. Import packages 
# We can take advantage of pre-packaged code for many common functions in Python. But first, we need to tell Python to import it. This is a really common step for most Python code.
# 
# We'll import a package called ["numpy"](https://numpy.org/doc/stable/user/index.html) and nickname it "np", ["plotly" graph objects](https://plotly.com/python/graph-objects/) and nickname it "go", and ['pandas'](https://pandas.pydata.org/docs/user_guide/index.html) and nickname it "pd". When you see "np" in our script, it's actually calling scripts from the numpy package. 
# 
# <b> TASK: </b> Run the code cell below to instruct Python to import the numpy and plotly packages so that we can use them. 
# 
# After you import it, Python will print a message. Having printed messages like these is a really nice way to check that your cell actually ran.

# In[ ]:


import numpy as np
import plotly.express as px
import pandas as pd
print('Imported packages')


# ### Step 2: Create some random data to plot
# We'll use a function "random.rand" to create a random list of numbers.<br>
#  
# **TASK:** You decide on how long this list of numbers should be (anything between 5 to 100 is fine) by adding a value next to "list_length".

# In[ ]:


# Add your numerical value next to list_length below.
list_length = 

random_list = np.random.rand(list_length,1)
print('Created a random list')


# Let's make sure Python did what we wanted it to do (save our random list as a variable).<br>
# 
# **TASK:** Check by typing the variable name into the next cell, and running it. If that worked, you should see an array of values.

# In[ ]:





# ### Step 3: Create a dataframe to store the random list.
# We'll use a function "DataFrame" from "pandas" (pd) to create a dataframe to store the data. DataFrames are kind of like spreadsheets. Each column can be a different set of data. Rows can be different entries of that data (in this case random numbers). 
# 
# **Task:** Run the code cell below to store the random list in a dataframe called "data" and display the first 5 rows of the dataframe as an output. 

# In[ ]:


data = pd.DataFrame(random_list,columns=['random_list'])
display(data.head())


# ### Step 4: Plot your data
# Let's pretend this is data from an awesome experiment we ran. We need to plot the data. We already imported a package "plotly.express" as "px" above to help us plot the data. We'll now use the "line" function to plot our random list as a line.
# 
# **TASK:** Run the code cell below to plot the data. 

# In[ ]:


# line() is plotly's basic plotting function
# below, we're asking it to plot the random_list we just created
# the resulting figure is assigned to a variable ("fig") as well. 
fig = px.line(data,y="random_list")

# fig.show() will show our plot below
fig.show()


# When you hover over the plot, you will see some action buttons in the top right corner. These allow you to zoom in, pan around, reset, and save the figure. 
# 
# <b>TASKS:</b>
#     
# 1. Hover over the data to see the x and y values. 
# 
# 2. Zoom in on a smaller section of the plot. Click on the ```Zoom``` icon that looks like a magnifying glass with a square in it. Then draw a box around a region of your data that you want to zoom in on.  
# 
# 3. Pan around the data in this zoomed in view. Click the ```Pan``` icon, which is two arrows perpendicular to each other (to the right of Zoom). Hold the right mouse click down on the plot and drag it around. Release and re-click to drag further
# 
# 4. Reset the view back to normal by clicking the ```Home``` icon (looks like a house).
# 
# 5. Download your plot as a *png* file by clicking the ```Download``` icon that looks like a camera (all the way to the left of the icon list). 
# 
# 6. Click on your downloaded png file by clicking on it in your computer's file system navigator. This is how you will be saving the figure you create in future notebooks. 

# # **Part V: Bonus celebration** 
# That's the Colab Notebook tutorial! You're ready to tackle Colab Notebooks in the course. 
# 
# Celebrate your new skills by running the code cell below.
# 

# In[ ]:


from IPython.display import HTML
HTML('<img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif">')


# [Return to Table of Contents](#toc)

# ## Additional Resources
# For additional Jupyter Notebook information and practice if you want it for your own data science needs in the future, see [this tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) from DataQuest. 
# 
# This notebook was modified from [Introduction to Jupyter Notebooks.ipynb](https://colab.research.google.com/github/ajuavinett/CellTypesLesson/blob/master/Introduction%20to%20Jupyter%20Notebooks.ipynb) created by [Ashley Juavinett](https://github.com/ajuavinett/)
# 
