#!/usr/bin/env python
# coding: utf-8

# <a id="intro"></a>
# # Executable Notebooks (Data Explorers)
# 
# Welcome to the executable IPython notebook environment! We will be using the IPython notebooks for our lab class in neurophysiology. The IPython notebook is a very convenient way to interact with data using python. 
# 
# *Executable* notebooks are ones that contain python scripts and functions that enable you to interact with and process the data you collect in lab. Some executable notebooks in this course (like this one) are tutorials that do not depend on collected data.
# 
# You will be interacting with these notebooks using Google's Colaboratory server. Use the **Open in Colab** buttons to open the notebook in Colab.
# 
# Click this <a href="https://colab.research.google.com/github/neurologic/Neurophysiology-Lab/blob/main/howto/Executable-Notebooks.ipynb" target="_blank"><img alt="Open In Colab" src="https://colab.research.google.com/assets/colab-badge.svg"/></a> button to open this notebook on Colab. 
#   

# <a id="toc"></a>
# # Table of Contents
# 
# - [Introduction](#intro)
# - [Setup](#setup)
# - [Form Fields](#one)
# - [Hidden Executable Scripts](#two)
# - [Code Cell Tasks](#three)
# - [Interactive Plots](#four)
# 

# <a id="setup"></a>
# # Setup
# [toc](#toc)
# 
# Throughout this course, most (probably all!) *executable* notebooks contain a section of ***setup*** cells. These cells will import the required Python packages (e.g., Pandas, NumPy); set global or environment variables, and load in helper functions for things like plotting. 
# 
# Be sure to run all of the cells in the setup section. Feel free to expand them and have a look at what you are loading in, but you should be able to fulfill the learning objectives of every tutorial without having to look at these cells.
# 
# If you start building your own projects on this code base, you should look at them in more detail.

# <a id="one"></a>
# # Form Fields
# [toc](#toc)
# 
# Some code cells contain forms with editable fields. <br>
# For example, the following code cell asks for your name. However, the form field will only be formatted correctly when you open it in Colab.<br>
# After filling in the form fields, running the code cell assigns each entries as a value to each variable (In this case, your name would be stored in the variable called *name*)

# In[ ]:


#@markdown This is a form field. 
name = "insert your name between the quotation marks" #@param


# Often, form fields will be hidden in the html version of the notebook on the course website. <br>
# For example, on the course website, you can only see the contents of the following form field if you click the "*click to show*" button.<br>

# In[ ]:


#@title { display-mode: "form" }

#@markdown This is a form field. 
name = "insert your name between the quotation marks" #@param


# <a id="two"></a>
# # Hidden Executable Scripts
# [toc](#toc)
# 
# You will gain some basic computer coding skills by completing the assignments in this course. You will be asked to learn the most basic coding tasks. However, this course is not designed to teach you full literacy in data science computer programming. Instead, I have done most of the computer programming for you so that you can focus more on the interpretation of data, visualization of data, and foundational concepts in neurophysiology. 
# 
# All of the executable notebooks you will work with contain extensive code to transform, process, and analyze your data. However, you will not see much of these scripts because they are contained in code cells formatted to "hide" its contents.
# 
# Instead, you will see instructions to "run this code cell" to perform specific tasks that I have coded for you.
# 
# For example, when you open this notebook in Colab, you would be able to run the following code cell, and it would print out the result of ```2 * 3```. In the html version of the notebook, you can see the contents of the following code cell by clicking the "*click to show*" button. 

# In[ ]:


#@title { display-mode: "form" }

#@markdown Run this code cell to calculate the result of 2 * 3. 

result = 2*3
print(result)


# <a id="three"></a>
# # Code Cell Tasks
# [toc](#toc)
# 
# As described in [Hidden Executable Scripts](#two), some code cells contain scripts that are used to process your data and make calculations for results. You don't need to look at the actual python scripts (but can if you want to by double clicking on the code cell). Instead, you are given tasks that say "run this code cell" or "enter information in this form field". Follow these instructions and run the code cells as required. 

# <a id="four"></a>
# # Interactive Plots
# [toc](#toc)
# 
# Visually examining your data is a critical step in interpreting it. The executable notebooks in this course use [plotly](https://plotly.com/python/) to produce plots with "zoom, pan, and save" buttons as well as pop-up information when the mouse hovers over the data. If you have this notebook open in Colab, you can execute the code cell below to try it out.

# In[ ]:


#@title { display-mode: "form" }

#@markdown Run this code cell to generate an example interactive plot.

import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()


# <hr> 
# Written by Dr. Krista Perks for courses taught at Wesleyan University.

# In[ ]:




