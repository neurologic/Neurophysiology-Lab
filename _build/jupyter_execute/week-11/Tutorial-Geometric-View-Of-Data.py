#!/usr/bin/env python
# coding: utf-8

# <a id="intro"></a>
# # Tutorial: Geometric view of data
# 
# In this notebook we'll explore how multivariate data can be represented in different orthonormal bases (dimensions). In other words, how to change the dimensions defining a set of data. As a start, the cartesian coordinates are an example of a two-dimensional orthogonal basis. This notebook will help you build intuition that will be helpful in understanding the use of PCA in research that you will be reading about. 
# 
# Overview:
#  - Explore correlated multivariate data.
#  - Define and visualize an arbitrary orthonormal basis. 
#  - Project data from one basis (cartesian) onto another basis (arbitrary).

# <a id="toc"></a>
# # Table of Contents
# 
# 1. [Setup](#setup)
# 2. [Part I. (Correlated) Multivariate Data](#one)
# 3. [Part II. Orthonormal Basis](#two)
# 4. [Part III. New Basis Perspective](#three)
# 5. [Summary](#summary)
# 6. [Notation](#notation)

# <a id="setup"></a>
# # Setup
# [toc](#toc)

# In[2]:


# @title Imports, Settings, Functions { display-mode: "form" }
# @markdown Execute this code cell to set up the notebook
import numpy as np
import matplotlib.pyplot as plt

import ipywidgets as widgets  # interactive display
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
plt.style.use("https://raw.githubusercontent.com/NeuromatchAcademy/course-content/master/nma.mplstyle")


def plot_data(X):
  """
  Plots bivariate data. Includes a plot of each random variable, and a scatter
  plot of their joint activity. The title indicates the sample correlation
  calculated from the data.

  Args:
    X (numpy array of floats) :   Data matrix each column corresponds to a
                                  different random variable

  Returns:
    Nothing.
  """

  fig = plt.figure(figsize=[10, 6])
  gs = fig.add_gridspec(2, 2)
  ax1 = fig.add_subplot(gs[0, 0])
  ax1.plot(X[:, 0], color='k')
  plt.ylabel('Neuron 1')
  plt.title('Sample var 1: {:.1f}'.format(np.var(X[:, 0])))
  ax1.set_xticklabels([])
  ax2 = fig.add_subplot(gs[1, 0])
  ax2.plot(X[:, 1], color='k')
  plt.xlabel('Sample Number')
  plt.ylabel('Neuron 2')
  plt.title('Sample var 2: {:.1f}'.format(np.var(X[:, 1])))
  ax3 = fig.add_subplot(gs[:, 1])
  ax3.plot(X[:, 0], X[:, 1], '.', markerfacecolor=[.5, .5, .5],
           markeredgewidth=0)
  ax3.axis('equal')
  plt.xlabel('Neuron 1 activity')
  plt.ylabel('Neuron 2 activity')
  plt.title('Sample corr: {:.1f}'.format(np.corrcoef(X[:, 0], X[:, 1])[0, 1]))
  plt.show()


def plot_basis_vectors(X, W):
  """
  Plots bivariate data as well as new basis vectors.

  Args:
    X (numpy array of floats) :   Data matrix each column corresponds to a
                                  different random variable
    W (numpy array of floats) :   Square matrix representing new orthonormal
                                  basis each column represents a basis vector

  Returns:
    Nothing.
  """

  plt.figure(figsize=[4, 4])
  plt.plot(X[:, 0], X[:, 1], '.', color=[.5, .5, .5], label='Data')
  plt.axis('equal')
  plt.xlabel('Neuron 1 activity')
  plt.ylabel('Neuron 2 activity')
  plt.plot([0, W[0, 0]], [0, W[1, 0]], color='r', linewidth=3,
           label='Basis vector 1')
  plt.plot([0, W[0, 1]], [0, W[1, 1]], color='b', linewidth=3,
           label='Basis vector 2')
  plt.legend()
  plt.show()


def plot_data_new_basis(Y):
  """
  Plots bivariate data after transformation to new bases.
  Similar to plot_data but with colors corresponding to projections onto
  basis 1 (red) and basis 2 (blue). The title indicates the sample correlation
  calculated from the data.

  Note that samples are re-sorted in ascending order for the first
  random variable.

  Args:
    Y (numpy array of floats):   Data matrix in new basis each column
                                 corresponds to a different random variable

  Returns:
    Nothing.
  """
  fig = plt.figure(figsize=[8, 4])
  gs = fig.add_gridspec(2, 2)
  ax1 = fig.add_subplot(gs[0, 0])
  ax1.plot(Y[:, 0], 'r')
  plt.xlabel
  plt.ylabel('Projection \n basis vector 1')
  plt.title('Sample var 1: {:.1f}'.format(np.var(Y[:, 0])))
  ax1.set_xticklabels([])
  ax2 = fig.add_subplot(gs[1, 0])
  ax2.plot(Y[:, 1], 'b')
  plt.xlabel('Sample number')
  plt.ylabel('Projection \n basis vector 2')
  plt.title('Sample var 2: {:.1f}'.format(np.var(Y[:, 1])))
  ax3 = fig.add_subplot(gs[:, 1])
  ax3.plot(Y[:, 0], Y[:, 1], '.', color=[.5, .5, .5])
  ax3.axis('equal')
  plt.xlabel('Projection basis vector 1')
  plt.ylabel('Projection basis vector 2')
  plt.title('Sample corr: {:.1f}'.format(np.corrcoef(Y[:, 0], Y[:, 1])[0, 1]))
  plt.show()

def get_data(cov_matrix):
  """
  Returns a matrix of 1000 samples from a bivariate, zero-mean Gaussian.

  Note that samples are sorted in ascending order for the first random variable

  Args:
    cov_matrix (numpy array of floats): desired covariance matrix

  Returns:
    (numpy array of floats) : samples from the bivariate Gaussian, with each
                              column corresponding to a different random
                              variable
  """

  mean = np.array([0, 0])
  X = np.random.multivariate_normal(mean, cov_matrix, size=1000)
  indices_for_sorting = np.argsort(X[:, 0])
  # X = X[indices_for_sorting, :]

  return X

def calculate_cov_matrix(var_1, var_2, corr_coef):
  """
  Calculates the covariance matrix based on the variances and correlation
  coefficient.
  Args:
    var_1 (scalar)          : variance of the first random variable
    var_2 (scalar)          : variance of the second random variable
    corr_coef (scalar)      : correlation coefficient
  Returns:
    (numpy array of floats) : covariance matrix
  """

  # Calculate the covariance from the variances and correlation
  cov = corr_coef * np.sqrt(var_1 * var_2)

  cov_matrix = np.array([[var_1, cov], [cov, var_2]])

  return cov_matrix

def define_orthonormal_basis(u):
  """
  Calculates an orthonormal basis given an arbitrary vector u.
  Args:
    u (numpy array of floats) : arbitrary 2-dimensional vector used for new
                                basis
  Returns:
    (numpy array of floats)   : new orthonormal basis
                                columns correspond to basis vectors
  """

  # Normalize vector u
  u = u / np.sqrt(u[0] ** 2 + u[1] ** 2)

  # Calculate vector w that is orthogonal to w
  w = np.array([-u[1], u[0]])

  # Put in matrix form
  W = np.column_stack([u, w])

  return W

def change_of_basis(X, W):
  """
  Projects data onto new basis W.
  Args:
    X (numpy array of floats) : Data matrix each column corresponding to a
                                different random variable
    W (numpy array of floats) : new orthonormal basis columns correspond to
                                basis vectors
  Returns:
    (numpy array of floats)    : Data matrix expressed in new basis
  """

  # Project data onto new basis described by W
  Y = X @ W

  return Y


# <a id="one"></a>
# # Part I. (Correlated) multivariate data
# [toc](#toc)
# 
# This notebook provides code to draw random samples from a zero-mean bivariate normal distribution with a specified covariance matrix. Throughout this tutorial, we'll imagine these samples represent the activity (firing rates) of two recorded neurons on different trials. 
# 
# <details>
# <summary> <font color='blue'>Click here if you are interested in detials about the math behind multivariate normal distributions </font></summary>
# 
# To gain intuition, we will first use a simple model to generate multivariate data. Specifically, we will draw random samples from a *bivariate normal distribution*. This is an extension of the one-dimensional normal distribution to two dimensions, in which each $x_i$ is marginally normal with mean $\mu_i$ and variance $\sigma_i^2$:
# 
# \begin{align}
# x_i \sim \mathcal{N}(\mu_i,\sigma_i^2).
# \end{align}
# 
# Additionally, the joint distribution for $x_1$ and $x_2$ has a specified correlation coefficient $\rho$. Recall that the correlation coefficient is a normalized version of the covariance, and ranges between -1 and +1:
# 
# \begin{align}
# \rho = \frac{\text{cov}(x_1,x_2)}{\sqrt{\sigma_1^2 \sigma_2^2}}.
# \end{align}
# 
# For simplicity, we will assume that the mean of each variable has already been subtracted, so that $\mu_i=0$ for both $i=1$ and $i=2$. The remaining parameters can be summarized in the covariance matrix, which for two dimensions has the following form:
# 
# \begin{align}
# {\bf \Sigma} = 
# \begin{pmatrix}
#  \text{var}(x_1) & \text{cov}(x_1,x_2) \\
#  \text{cov}(x_1,x_2) &\text{var}(x_2)
# \end{pmatrix}.
# \end{align}
# 
# In general, $\bf \Sigma$ is a symmetric matrix with the variances $\text{var}(x_i) = \sigma_i^2$ on the diagonal, and the covariances on the off-diagonal. Later, we will see that the covariance matrix plays a key role in PCA.
# 
# The covariance can be found by rearranging the equation above:
# 
# \begin{align}
# \text{cov}(x_1,x_2) = \rho \sqrt{\sigma_1^2 \sigma_2^2}.
# \end{align}
# 
# </details>
# 

# ## Interactive Demo: Effect of correlation on data in two dimensions
# 
# Executing the code cell below will enable you to can change the correlation coefficient between data in two dimensions via an interactive slider. You should get a feel for how changing the correlation coefficient affects the geometry of the simulated data.
# 
# 1.   What effect do negative correlation coefficient values have?
# 2.   What correlation coefficient results in a circular data cloud?

# In[ ]:


# @markdown Execute this cell to enable widget { display-mode: "form" }

def _calculate_cov_matrix(var_1, var_2, corr_coef):

  # Calculate the covariance from the variances and correlation
  cov = corr_coef * np.sqrt(var_1 * var_2)

  cov_matrix = np.array([[var_1, cov], [cov, var_2]])

  return cov_matrix


@widgets.interact(corr_coef = widgets.FloatSlider(value=.2, min=-1, max=1, step=0.1))
def visualize_correlated_data(corr_coef=0):
  variance_1 = 1
  variance_2 = 1

  # Compute covariance matrix
  cov_matrix = _calculate_cov_matrix(variance_1, variance_2, corr_coef)

  # Generate data with this covariance matrix
  X = get_data(cov_matrix)

  # Visualize
  plot_data(X)


# <a id="two"></a>
# # Part II. Define an orthonormal basis (a different set of dimensions)
# [toc](#toc)
# 
# Data can be represented in many ways using different bases. We will be using "orthonormal" bases (orthogonal with length 1).
# <details>
# <summary> <font color='blue'>Click here if you are interested in some detail about the math </font></summary>
# 
# We will define a new orthonormal basis of vectors ${\bf u} = [u_1,u_2]$ and ${\bf w} = [w_1,w_2]$. Two vectors are orthonormal if: 
# 
# 1.   They are orthogonal (i.e., their dot product is zero):
# \begin{align}
# {\bf u\cdot w} = u_1 w_1 + u_2 w_2 = 0
# \end{align}
# 2.   They have unit length:
# \begin{align}
# ||{\bf u} || = ||{\bf w} || = 1
# \end{align}
# 
# In two dimensions, it is easy to make an arbitrary orthonormal basis. All we need is a random vector ${\bf u}$, which we have normalized. If we now define the second basis vector to be ${\bf w} = [-u_2,u_1]$, we can check that both conditions are satisfied: 
# \begin{align}
# {\bf u\cdot w} = - u_1 u_2 + u_2 u_1 = 0
# \end{align}
# and 
# \begin{align}
# {|| {\bf w} ||} = \sqrt{(-u_2)^2 + u_1^2} = \sqrt{u_1^2 + u_2^2} = 1,
# \end{align}
# where we used the fact that ${\bf u}$ is normalized. So, with an arbitrary input vector, we can define an orthonormal basis, which we will write in matrix by stacking the basis vectors horizontally:
# 
# \begin{align}
# {{\bf W} } =
# \begin{pmatrix}
#  u_1 & w_1 \\
#  u_2 & w_2
# \end{pmatrix}.
# \end{align}
# 
# </details>
# 

# In[ ]:


# @markdown Execute this cell to plot two orthonormal bases,  { display-mode: "form" }
# @markdown with the first dimension based on a vector defined by `[x,y]`

# @widgets.interact(corr_coef = widgets.FloatSlider(value=.2, min=-1, max=1, step=0.1))
def visualize_orthonormal_bases(x=0,y=3):
  u = [x,y]

  # Get orthonomal basis
  W = define_orthonormal_basis(u)

  # Visualize
  with plt.xkcd():
    fig,ax  = plt.subplots(figsize=[6, 6])
    # ax = plt.subplot(1)
    # plt.figure(figsize=[6, 6])
    ax.axis('equal')
    ax.plot([0, u[0]], [0, u[1]], color='k', linewidth=6,
              label='Original vector')
    ax.plot([0, W[0, 0]], [0, W[1, 0]], color='r', linewidth=3,
              label='Basis vector 1')
    ax.plot([0, W[0, 1]], [0, W[1, 1]], color='b', linewidth=3,
              label='Basis vector 2')
    ax.legend()
    plt.show()

_ = widgets.interact(visualize_orthonormal_bases, x=(-3,3,0.2), y=(-3,3,0.2))


# <a id="three"></a>
# # Part III. Project data onto new basis
# [toc](#toc)
# 
# Finally, we will express bivariate (2-dimensional) data ($\bf X$) in a new 2-dimensional basis defined as in Section 2. We can project the data into our new basis using ***matrix multiplication*** :
# 
# \begin{align}
# {\bf Y = X W}.
# \end{align}
# 
# We will explore the geometry of the transformed data $\bf Y$ as we vary the choice of basis.

# ## Interactive Demo: Explore the basis vectors
# To see what happens to the correlation between dimensions as we change the basis vectors, run the cell below. 
# 
# The parameter corr_coeff controls the correlation between the two original dimensions.
# 
# The parameter $\theta$ controls the angle of the first basis vector (red, $\bf u$) in degrees. The second basis vector will be orthogonal to the first. Use the slider to rotate the basis vectors (the new dimensions). 
# 
# 1.   What happens to the projected data as you rotate the basis? 
# 2.   How does the correlation coefficient change? How does the variance of the projection onto each basis vector change?
# 3.   Are you able to find a basis in which the projected data is **uncorrelated**?

# In[ ]:


# @markdown Execute this cell to enable the widget  { display-mode: "form" }

def refresh(corr_coef=0.5,theta=0):
  # corr_coef=0.5
  variance_1 = 1
  variance_2 = 1

  # Compute covariance matrix
  cov_matrix = _calculate_cov_matrix(variance_1, variance_2, corr_coef)

  # Generate data with this covariance matrix
  X = get_data(cov_matrix)
  u = [1, np.tan(theta * np.pi / 180)]
  W = define_orthonormal_basis(u)
  Y = change_of_basis(X, W)
  # plot_basis_vectors(X, W)

  # plot_data_new_basis(Y)
  fig = plt.figure(figsize=[20, 10])
  gs = fig.add_gridspec(4, 4)
  
  ax1 = fig.add_subplot(gs[0, 0])
  ax1.plot(X[:, 0], color='k')
  plt.ylabel('Neuron 1')
  plt.title('Sample var 1: {:.1f}'.format(np.var(X[:, 0])))
  ax1.set_xticklabels([])
 
  ax2 = fig.add_subplot(gs[1, 0])
  ax2.plot(X[:, 1], color='k')
  plt.xlabel('Sample Number')
  plt.ylabel('Neuron 2')
  plt.title('Sample var 2: {:.1f}'.format(np.var(X[:, 1])))
  
  ax3 = fig.add_subplot(gs[0:2, 1])
  ax3.plot(X[:, 0], X[:, 1], '.', markerfacecolor=[.5, .5, .5],
           markeredgewidth=0)
  ax3.plot([0, W[0, 0]], [0, W[1, 0]], color='r', linewidth=3,
            label='Basis vector 1')
  ax3.plot([0, W[0, 1]], [0, W[1, 1]], color='b', linewidth=3,
            label='Basis vector 2')
  ax3.axis('equal')
  plt.xlabel('Neuron 1 activity')
  plt.ylabel('Neuron 2 activity')
  plt.title('Sample corr: {:.1f}'.format(np.corrcoef(X[:, 0], X[:, 1])[0, 1]))
  
  ax4 = fig.add_subplot(gs[2, 0])
  ax4.plot(Y[:, 0], 'r')
  plt.xlabel
  plt.ylabel('Projection \n basis vector 1')
  plt.title('Sample var 1: {:.1f}'.format(np.var(Y[:, 0])))
  ax4.set_xticklabels([])
  ax5 = fig.add_subplot(gs[3, 0])
  ax5.plot(Y[:, 1], 'b')
  plt.xlabel('Sample number')
  plt.ylabel('Projection \n basis vector 2')
  plt.title('Sample var 2: {:.1f}'.format(np.var(Y[:, 1])))
  ax6 = fig.add_subplot(gs[2:4, 1])
  ax6.plot(Y[:, 0], Y[:, 1], '.', color=[.5, .5, .5])
  ax6.axis('equal')
  plt.xlabel('Projection basis vector 1')
  plt.ylabel('Projection basis vector 2')
  plt.title('Sample corr: {:.1f}'.format(np.corrcoef(Y[:, 0], Y[:, 1])[0, 1]))
  plt.show()


_ = widgets.interact(refresh, corr_coef=(-1,1,0.1), theta=(-90, 90, 5))


# <a id = "summary"></a>
# # Summary
# [toc](#toc)
# 
# - In this tutorial, we learned that multivariate data can be visualized as a cloud of points in a high-dimensional vector space. The geometry of this cloud is shaped by the *covariance matrix*.
# 
# - Multivariate data can be represented in a new orthonormal basis using the dot product (matrix multiplication). These new basis vectors correspond to specific mixtures of the original variables - *for example, in neuroscience, they could represent different ratios of activation  across a population of neurons*.
# 
# - The projected data (after transforming into the new basis) will generally have a different geometry from the original data. In particular, taking basis vectors that are aligned with the spread of cloud of points decorrelates the data.
# 
# * These concepts - covariance, projections, and orthonormal bases - are key for understanding PCA, which is a foundational computational tool in a wide variety of neuroscience research.

# <a id="notation"></a>
# # Notation
# [toc](#toc)
# 
# \begin{align}
# x_i &\quad \text{data point for dimension } i\\
# \mu_i &\quad \text{mean along dimension } i\\
# \sigma_i^2 &\quad \text{variance along dimension } i \\
# \bf u, \bf w &\quad \text{orthonormal basis vectors}\\
# \rho &\quad \text{correlation coefficient}\\
# \bf \Sigma &\quad \text{covariance matrix}\\
# \bf X &\quad \text{original data matrix}\\
# \bf W &\quad \text{projection matrix}\\
# \bf Y &\quad \text{transformed data}\\
# \end{align}
# 

# ---
# This tutorial was written by Krista Perks for courses taught at Wesleyan University. Based on content from **Neuromatch Academy 2020: Week 1, Day 5: Dimensionality Reduction** by Alex Cayco Gajic, John Murray
# 
# 

# In[ ]:




