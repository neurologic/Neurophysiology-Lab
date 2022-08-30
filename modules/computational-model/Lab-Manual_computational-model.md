# Lab Manual

A small set of electrical components can be used to describe many of the basic electrophysiological properties of neurons. Electric circuits are also well-described by basic algebraic and differential equations. Therefore, we often use electrical circuit models of neural membranes to formulate computational models of neural membranes. Today, you will build/formulate two computational models based on this technique: one of the resting membrane potential, and one of membrane potential changes in response to applied trans-membrane current.


## Circuit Diagrams

A circuit diagram is a graphical representation of an electrical circuit. You have already encountered symbols for three of the basic circuit components that you will be using for your computational models today: *resistors*, *capacitors*, and *voltage source*. 

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

Today, you will need to include one more circuit component in your diagrams: a *current source*. A current source applies a current to the circuit.
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
3. In the *resting membrane potential* model circuit, are the Voltage source ($V_1$) and resistor ($R_1$) in series or in parallel?.
:::

Finally, to interpret circuit diagrams it is important to remember the following two principles 
- voltage is equal at all points along continuous *wires* (lines uninterrupted by a circuit component such as a resistor, capacitor, or voltage source)
  > with a voltage meter, you can test this for yourself on the physical electrical circuit models at your table.
- current is equal at all points along individual wires between nodes of bifurcation or convergence


## Concepts and Equations of Electric Circuits

### Conservation of Energy[^kirchhoff]

[^kirchhoff]: [Kirchhoff's circuit laws](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws)

By the *law* of *conservation of energy*, it follows that the algebraic directed sum of the potential differences (voltages) around any closed loop is zero.

::::{admonition} Task
Calculate the voltage at each labeled node ***n*** (relative to the reference *REF* node) in the following circuit diagrams.
:::{image} ../../images/circuit-task_conservation-energy.png
:alt: circuit diagram
:width: 600px
:align: center
:::
::::

(conservation-charge)=
### Conservation of Charge[^kirchhoff]  

By the *law* of *conservation of charge*, it follows that the current entering any *junction* (point of bifurcation or convergencfe) is equal to the current leaving that junction.

::::{admonition} Task
Calculate the current at each labeled *n* node in the following circuit diagrams.
:::{image} ../../images/circuit-task_conservation-charge.png
:alt: circuit diagram
:width: 250px
:align: center
:::
::::

### Voltage and Current across Capacitors

As you now know, capacitors *store* charge. The charge across a capacitor sets up an *electrical potential* (energy) measured in volts. As charge builds up on a capacitor, current effectively flows across the capacitor. 

$$
  I = \partial{Q} / \partial{t}
$$ (capacitor-current)

$$
  Q = C * V
$$ (capacitor-charge)

:::{admonition} Task
Rearrange these equations for capacitor current and charge to get an equation for the change in voltage across time ($\partial{V} / \partial{t}$) in terms of the current ($I$) across a capacitor. Assume that capacitance is a constant (the value does not change across time).  
*Only resort to this hint[^hint_dqdt] after discussing your strategy and considering the equations and equation manipulations for at least 5 minutes.* 
:::

[^hint_dqdt]: You can arrange the equation for $Q$ in terms of $V$ so that it is an equation for $V$ in terms of $Q$The equation for current through a capacitor is in terms of $\partial{Q} / \partial{t}$ but the equation for $V$ would be in terms of $Q$ not $\partial{Q} / \partial{t}$. 

### Voltage and Current across Resistors

The voltage at one end of a resistor is different from the voltage at the other end of the resistor. This is because voltage *drops* (or changes) across a resistor. The magnitude of this voltage change is given by *Ohm's Law*: 

$$
  V = I * R
$$ (ohms-law)

:::{admonition} Task
Rearrange the given equation for the voltage across a resistor to get an equation for the current across a resistor in terms of the voltage across the resistor and its resistance.  
:::

### Resistor-Capacitor Interactions

$$
  \tau = R * C
$$ (rc-tau)

For an *RC circuit* in which a resistor and capacitor are arranged in parallel, the *time constant* ($\tau$) is the amount of time it takes for the voltage across the RC circuit to reach 63% of its maximum value in response to a current applied across the RC circuit. Remember that you measured this value for [the neuron membrane model you worked with in Part IV of the lab in Week 1](../passive-membrane-models/Lab-Manual_passive-membrane-models)

## Computational Models

With that introduction to drawing and analyzing circuit diagrams, you are ready to learn how to build computational models based on electric circuit models of neuron membranes. 

### Resting Membrane Potential

::::{admonition} Task: Create a computational model of resting membrane potential
Consider the following electric circuit model of resting membrane potential that you [worked with in Part I of the lab in Week 1](../passive-membrane-models/Lab-Manual_passive-membrane-models)
:::{image} ../../images/circuit-task_membrane-potential-current-flow.png
:alt: circuit diagram
:width: 400px
:align: center
:::
Remember that each voltage source in the circuit represents a specific ion's equilibrium potential and each resistor in the circuit represents the conductance of that specific ion.
1. For each voltage source ($E$) in the electrical circuit diagram, indicate which side of each voltage source is equal to $V_{ref}$. Label the voltage value on the other side of each voltage source as $V_1$ or $V_2$, respectively.
2. Write the equation for the voltage change across each resistor ($V_{R1}$ and $V_{R2}$) in terms of $V_{in}$, $V_1$, $V_2$, and/or $V_{ref}$.
3. Write the equation for current across a resistor in terms of voltage across the resistor and the value of its resistance. 
4. Combine \#3 with \#2 to write the equation for current across each resistor ($I_1$ and $I_2$) in terms of $V_{in}$, $V_1$, $V_2$, and/or $V_{ref}$.  
5. In the circuit diagram, use an arrow to indicate the current across $R_1$ as $I_1$ and an arrow to indicate the current across $R_2$ as $I_2$ (the direction of the current is not important yet).  
6. Given the assumption of [*conservation of charge*](conservation-charge), write an equation for the total (*net*) current in the circuit in terms of $I_1$ and $I_2$.
7. Rearrange \#6 to git an equation for $I_1$ in terms of $I_2$.
  	> Hint: the *resting* membrane potential is a *steady state* condition, meaning that there is no *net* current flow in the circuit. 
8. Substitute your equations from \#4 for $I_1$ and $I_2$ into the equation from \#7.
9. Rearrange your equation from \#8 to make describe $V_{in}$ (the voltage *inside* the model neuron membrane) in terms of all the other variables.  
::::

*You have just built a computational model for the membrane potential of a neuron. You built the model from first principles of an electric circuit model of neuron membranes. Your model describes the voltage across the membrane in terms of voltage sources (*equilibrium potentials*) and resistors (*ion channel conductance*). In the Data Explorer, we will implement your model to test how well it explains resting membrane potentials of neurons.*

:::{admonition} Task: Analyze your model
Consider a neuron with two types of ion conductances: sodium ($Na$) and potassium ($K$). In your model, set $E_1$ equal to the sodium equilibrium potential and $R_1$ equal to the resistance across sodium channels. $E_2$ and $R_2$ will equal the equilibrium potential and resistance of the potassium conductance. 
1. Use your model to calculate the predicted resting membrane potential ($V_{in}$) for a neuron where the equilibrium potential of sodium is +130mV, the resistance acrooss sodium channels is 5M$\Omega$, the equilibrium potential of potassium is -90mV, and the resistance acrooss potassium channels is 95M$\Omega$. 
2. Use your model to calculate the predicted resting membrane potential ($V_{in}$) of the same neuron as in \#1, but with the resistance across sodium channels = 50M$\Omega$ and the resistance across potassium channels = 50M$\Omega$. 
:::

### Neural Membrane Response to Applied Current

The goal of this second computational model is to simulate how the resting membrane potential of a neuron changes when current is applied across the membrane. Physiologically, current gets applied across the membrane when synaptic inputs are activated. Experimentally, current can be applied across the membrane when using intracellular electrode configurations. In the first week of lab, you applied a current across an electric circuit model of a neuron membrane. Now, use that circuit to formulate a computational model. 

You can use a simplified circuit in which all voltage sources (equilibrium potentials) are combined into one *steady state equilibrium potential* (the "resting" potential of the neuron; $V_{rest}$) and all resistors (ion channels) are combined into one net *membrane resistance* of the neuron ($R_{mem}).

## Use your work to implement computational models on the computer
We will use the [Data Explorer](../computational-model/Data-Explorer_computational-model.ipynb) notebook to work through the implementation together during class. Later, you will answer questions in the [Responses](../computational-model/Responses_computational-model.ipynb) notebook.