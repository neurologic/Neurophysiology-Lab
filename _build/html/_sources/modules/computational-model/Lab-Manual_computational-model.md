# Lab Manual

A small set of electrical components can be used to describe many of the basic electrophysiological properties of neurons. Electric circuits are also well-described by basic algebraic and differential equations. Therefore, we often use electrical circuit models of neural membranes to formulate computational models of neural membranes. 


## Circuit Diagrams

A circuit diagram is a graphical representation of an electrical circuit. You have already encountered symbols for three of the basic circuit components that you will be using for your computational models are *resistors*, *capacitors*, and *voltage source*. 

:::{image} ../../images/Electrical_Components.png
:alt: circuit components
:class: bg-primary mb-1
:width: 300px
:align: center
:::


:::{admonition} Task
Draw a circuit diagram of the *resting membrane potential* model circuit that you used in Week 1. You have a hard copy of this circuit at your rig.
:::

:::{admonition} Task
Draw a circuit diagram of the *RC* model circuit that you used in Week 1. You have a hard copy of this circuit at your rig.
:::

Today, you will need to include one more circuit component in your diagrams: a *current source*. 
:::{image} ../../images/symbol_current-source.png
:alt: circuit components
:width: 100px
:align: center
:::

Circuit components can either be arranged ***in series*** (attached end-to-end) or ***in parallel*** (side by side with each set of ends all attached together). 

:::{admonition} Task
Answer the following questions
1. In the *resting membrane potential* model circuit, are the Voltage sources in series or in parallel?.
2. In the *resting membrane potential* model circuit, are the resistors in series or in parallel?.
3. In the *resting membrane potential* model circuit, are the Voltage source (V1) and resistor (R1) in series or in parallel?.
:::


## Concepts and Equations of Electric Circuits

### Conservation of Energy[^kirchhoff]

[^kirchhoff]: [Kirchhoff's circuit laws](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws)

The algebraic directed sum of the potential differences (voltages) around any closed loop is zero.

::::{admonition} Task
Calculate the voltage at each labeled *n* node (relative to the reference *REF* node) in the following circuit diagrams.
:::{image} ../../images/circuit-task_conservation-energy.png
:alt: circuit diagram
:width: 600px
:align: center
:::
::::

(conservation-charge)=
### Conservation of Charge[^kirchhoff]  

The current entering any junction is equal to the current leaving that junction.

::::{admonition} Task
Calculate the current at each labeled *n* node in the following circuit diagrams.
:::{image} ../../images/circuit-task_conservation-charge.png
:alt: circuit diagram
:width: 250px
:align: center
:::
::::

### Voltage and Current across Capacitors

$$I = \partial{Q} / \partial{t}$$

$$Q = C * V$$

:::{admonition} Task
Rearrange the given equations to get an equation for the change in voltage across time in terms of the current across a capacitor. Assume that capacitance is a constant (the value does not change across time).  
*Only resort to this hint[^hint_dqdt] after discussing your strategy and considering the equations and equation manipulations for at least 5 minutes.* 
:::

[^hint_dqdt]: You can arrange the equation for $Q$ in terms of $V$ so that it is an equation for $V$ in terms of $Q$The equation for current through a capacitor is in terms of $\partial{Q} / \partial{t}$ but the equation for $V$ would be in terms of $Q$ not $\partial{Q} / \partial{t}$. 

### Voltage and Current across Resistors

$$V = I * R$$

:::{admonition} Task
Rearrange the given equation to get an equation for the current across a resistor in terms of the voltage across the resistor and its resistance.  
:::

### Resistor-Capacitor Interactions

$$\tau = R * C$$

## Computational Models

### Resting Membrane Potential

:::{admonition} Task
1. Draw a square circuit with one voltage source and one resistor in series on one side of the square. Attach a **$V_{in}$** electrode to one side of the square perpendicular to the $V:R$ series. Attach a **$V_{ref}$** electrode to the other side of the square perpendicular to the $V:R$ series. 
2. Write the equation for the current across the resistor in terms of voltage and current. 
3. Indicate which side of the voltage source is equal to $V_ref$. Label the voltage value on the other side of the voltage source $V_1$
4. Write the equation for the voltage change across the resistor ($V_R$) in terms of $V_{in}$, $V_1$, and/or $V_{ref}$.
5. Write the equation for the current across the resistor in terms of voltage across the resistor ($V_R$) and current across the resistor ($I$), substituting your equation from \#4 for $V_R$.
:::

:::{admonition} Task
1. In the following circuit, use an arrow to indicate the current across $R_1$ as $I_1$ and an arrow to indicate the current across $R_2$ as $I_2$ (the direction of the current is not important yet).  
	:::{image} ../../images/circuit-task_membrane-potential-current-flow.png
	:alt: circuit diagram
	:width: 300px
	:align: center
	:::
2. Given the assumption of [*conservation of charge*](conservation-charge), write an equation for $I_1$ in terms of $I_2$.
3. Write the equation for the voltage change across each resistor ($V_R1$ and $V_R2$) in terms of $V_{in}$, $V_1$, $V_2$, and/or $V_{ref}$.
4. Write the equation for current across each resistor ($I_1$ and $I_2$) in terms of $V_{in}$, $V_1$, $V_2$, and/or $V_{ref}$.
5. Solve your equation from \#4 in terms of $V_{in}$ (the voltage *inside* the model neuron membrane).  
  > Hint: To combine fractions, the denominators have to be equal. You can multiply fractions by "one" (ie. x/x) to get a needed variable (ie. x) into a fraction (like when denominators of two fractions need to be equal to each other). 
:::

### Neural Membrane Response to Applied Current

## Use your work to implement computational models on the computer
We will use the [Data Explorer](../computational-model/Data-Explorer_computational-model.ipynb) notebook to work through the implementation together during class. Later, you will answer questions in the [Responses](../computational-model/Responses_computational-model.ipynb) notebook.