# Week 6. Computational Models

*Computational models* of neurons and neural circuits are an integral part of neurobiology research in general. For example, [the Allen Institute for Brain Science as a whole division dedicated to computational modeling](https://portal.brain-map.org/explore/models). Today, we will work on building and interrogating computational models that capture some basic electrophysiological properties of neuron membranes. These will build on the principles [you learned by utilizing electrical circuit models of neuron membranes](../passive-membrane-models/passive-membrane-models_landing.md).

What does the term *computational model* and/or the thought of building one make you think? Is it something that you think you can do or already know how to do? If you are someone that feels overwhelmed by the idea, you might want to [read this](https://medium.com/the-spike/there-is-no-such-thing-as-a-computational-person-cca658b5c8f9).

What is a *computational model*?  
Models represent a scientist’s best informed guess as to the identity and function of important variables and the ways these variables interact with each other.

Computational models of neuroscience specifically are mathematical algorithms and/or expressions that are able to simulate neural cell and circuit phenomena. Part of the power of models comes from their ability to formulate predictions of hypotheses and test our understanding of specific factors that effect neural computation. In neuroscience, the physiology of neurons and circuits can be described by few high-level basic electrical physics equations (such as $V=IR$) or by detailed biophysical equations of biochemical reactions such as the following for a voltage-gated ion channel:
$
\frac{dx}{dt}=f(x,V);  
f(x,V)=α(V)(1−x)−β(V)x;  
α(V)=A_{α} \times exp(B_{α}V); 
β(V)=A_{β} \times exp(B_{β}V)  
$

The large number of variables and factors affecting the structure and function of the nervous system makes it almost impossible for them all to be considered in a single model. Therefore, specific computational models mostly consider a smaller number of biological variables. Sometimes computational models can seem like absurd simplifications. Though somewhat constrained in their generalizability and applicability, even heavily abstracted and *reduced* computational models provide powerful tools for understanding neural systems.  

Computers are particularly useful for implementing simulations of computational models. We will create two computational models and implement them in Python programming language. 


## Pages:
- [](../computational-model/Lab-Manual_computational-model.md)
- [](../computational-model/Data-Explorer_computational-model.ipynb)
- [](../computational-model/Responses_computational-model.ipynb)

## Additional Resources

- [Allen Brain Atlas: Generalized LIF Models](http://alleninstitute.github.io/AllenSDK/glif_models.html)
- [Scientifica: Understanding the cell as an electrical circuit](https://www.scientifica.uk.com/learning-zone/understanding-the-cell-as-an-electrical-circuit)
- [Molecular Devices' Axon Guide](https://www.moleculardevices.com/en/assets/user-guide/dd/cns/axon-guide-to-electrophysiology-and-biophysics-laboratory-techniques#gref)


