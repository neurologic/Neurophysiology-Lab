# Lab Manual

A small set of electrical components can be used to describe many fundamental electrophysiological properties of neurons. Electric circuits are also well-described by basic algebraic and differential equations. Therefore, we often use electrical circuit models of neural membranes to formulate computational models of neural membranes. Today, you will build/formulate two computational models based on this technique: one of steady-state resting membrane potential, and one of membrane potential responses to applied trans-membrane current.


## Circuit Diagrams

A circuit diagram is a graphical representation of an electrical circuit. You have already encountered symbols for three of the basic circuit components that you will be using for your computational models today: *resistors*, *capacitors*, and *voltage source*. As you now know, circuit components can either be arranged ***in series*** (attached end-to-end) or ***in parallel*** (side by side with each set of ends all attached together). 

:::{image} ../../images/Electrical_Components.png
:alt: circuit components
:class: bg-primary mb-1
:width: 300px
:align: center
:::


:::{admonition} Task 1
Draw a circuit diagram of the *resting membrane potential* (*$V_{rest}$*) model circuit that you used in [](/modules/passive-membrane-models/passive-membrane-models_landing). You have a hard copy of this circuit at your rig. Label one pair of components with subscript '1' and the other set with subscript '2'.
:::

:::{admonition} Task 2
Draw a circuit diagram of the *RC* model circuit that you used in [](/modules/passive-membrane-models/passive-membrane-models_landing). You have a hard copy of this circuit at your rig.
:::

Today, you will need to include one more circuit component in your diagrams: a *current source*. A current source applies a current to the circuit.
:::{image} ../../images/symbol_current-source.png
:alt: circuit components
:width: 100px
:align: center
:::



:::{admonition} Task 3
Answer the following questions:  
a. In the *$V_{rest}$* model circuit, are the Voltage sources in series or in parallel?.  
b. In the *$V_{rest}$* model circuit, are the resistors in series or in parallel?.  
c. In the *$V_{rest}$* model circuit, are the Voltage source ($E_1$) and resistor ($R_1$) in series or in parallel?.
:::

Finally, to interpret circuit diagrams it is important to remember the following two principles: 
1. voltage is equal at all points along continuous *wires* (lines uninterrupted by a circuit component such as a resistor, capacitor, or voltage source)
    > with a voltage meter, you can test this for yourself on the physical electrical circuit models at your table.
2. current is equal at all points along individual wires between nodes of bifurcation or convergence



### Voltage and Current across Capacitors

As you now know, capacitors *store* charge.


The charge that a capacitor holds at steady state is proportional to its capacitance (ability to store charge) and the voltage across it. 

$$
Q = C * V
$$

A change in voltage ($\partial{V}$) would lead to a change in charge ($\partial{Q}$). We can assume that capacitance is a constant (the value does not change).

Conversely, a charge across a capacitor sets up an *electrical potential* (energy) measured in volts. As charge builds up on a capacitor due to an applied voltage, current effectively flows across the capacitor. 

$$
I = \partial{Q} / \partial{t}
$$

Without a change in charge, there is no current. Similarly, if a current is applied accross a capacitor, then charge builds up on it ($\partial{Q}$)... and the voltage changes ($\partial{V}$).  

:::{admonition} Task 6
Rearrange these equations for capacitor current and capacitor charge to get an equation for the change in voltage across time ($\partial{V} / \partial{t}$) in terms of the capacitor current ($I$). 

*Only resort to this hint[^hint_dqdt] after discussing your strategy and considering the equations and equation manipulations for at least 5 minutes.* 
:::

[^hint_dqdt]: You can arrange the equation for $Q$ in terms of $V$ so that it is an equation for $V$ in terms of $Q$. The equation for current through a capacitor is in terms of $\partial{Q} / \partial{t}$ but the equation for $V$ would be in terms of $Q$ not $\partial{Q} / \partial{t}$. 

### Voltage and Current across Resistors

The voltage at one end of a resistor is different from the voltage at the other end of the resistor. This is because voltage *drops* (or changes) across a resistor. The magnitude of this voltage change is given by *Ohm's Law*: 

$$
  V = I * R
$$

:::{admonition} Task
Rearrange the given equation for the voltage across a resistor to get an equation for the current across a resistor in terms of the voltage across the resistor and its resistance.  
:::

## Concepts and Equations of Electric Circuits

### Conservation of Energy[^kirchhoff]

[^kirchhoff]: [Kirchhoff's circuit laws](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws)

By the *law* of [*conservation of energy*](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws#Kirchhoff's_voltage_law), it follows that the algebraic directed sum of the potential differences (voltages) around any closed loop is zero.

::::{admonition} Task 4
Calculate the voltage at each labeled node ***n*** (relative to the reference *REF* node) in the following circuit diagrams.
:::{image} ../../images/circuit-task_conservation-energy.png
:alt: circuit diagram
:width: 600px
:align: center
:::
::::

(conservation-charge)=
### Conservation of Charge[^kirchhoff]  

By the *law* of [*conservation of charge*](https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws#Kirchhoff's_current_law), it follows that the current entering any *junction* (point of bifurcation or convergence) is equal to the current leaving that junction.

::::{admonition} Task 5
Calculate the current at each labeled *n* node in the following circuit diagrams.
:::{image} ../../images/circuit-task_conservation-charge.png
:alt: circuit diagram
:width: 250px
:align: center
:::
::::

## Computational Models

With that introduction to drawing and analyzing circuit diagrams, you are ready to learn how to build computational models based on electric circuit models of neuron membranes. 

### Resting Membrane Potential

::::{admonition} Task 6: Create a computational model of resting membrane potential
:name: computational-model-vrest
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

:::{admonition} Task 7: Analyze your model by hand
Consider a neuron with two types of ion conductances: sodium ($Na$) and potassium ($K$). In your model, set $E_1$ equal to the sodium equilibrium potential and $R_1$ equal to the resistance across sodium channels. $E_2$ and $R_2$ will equal the equilibrium potential and resistance of the potassium conductance. 
1. Use your model to calculate the predicted resting membrane potential ($V_{in}$) for a neuron where the equilibrium potential of sodium is +130mV, the resistance acrooss sodium channels is 5M$\Omega$, the equilibrium potential of potassium is -90mV, and the resistance acrooss potassium channels is 95M$\Omega$. 
2. Use your model to calculate the predicted resting membrane potential ($V_{in}$) of the same neuron as in \#1, but with the resistance across sodium channels = 50M$\Omega$ and the resistance across potassium channels = 50M$\Omega$. 
:::

### Neural Membrane Response to Applied Current

Physiologically, current gets applied across the membrane when synaptic inputs are activated. Understanding how membrane voltage changes in response to applied current is essential to understanding neural processing. Experimentally, current can be applied across the membrane when using intracellular electrode configurations. We therefore often do this to get information about how a specific neuron would process its synaptic inputs. 

What would you expect to happen to the voltage across a neuron membrane in response to an applied current? 

Now that [you have a computational model of a neuron's resting membrane potential](computational-model-vrest), you will create a second computational model to simulate how the membrane potential of a neuron changes when current is applied across the membrane. 

To start, we can use a simplified version of [the $V_{rest}$ circuit](computational-model-vrest) in in which all voltage sources (equilibrium potentials) are combined into one *steady state equilibrium potential* (the "resting" potential of the neuron; $E_{rest}$) and all resistors (ion channels) are combined into one net *membrane resistance* of the neuron ($R_{mem}$). For this experiment, we need to add a current source to the circuit. The current source simulates the synaptic input (or input from an electrode, like you have done with the Getting Intracellular Amp).

:::{image} ../../images/circuit-task_Vrest-simple.png
:alt: circuit diagram
:width: 300px
:align: center
:::

Now, let's use that circuit to formulate a computational model and predict the voltage response to applied current. 

The effective behavior of Voltage and Current sources in a circuit can get conceptually tricky. Practically, you can think of the voltage source adjusting its resistance to match the current flowing through and the current source adjusting its resistance to match the voltage across it. In other words, instead of shunting $V_{in}$ and $V_{ref}$, the voltage across the current source is $V_{in}$ - $V_{ref}$. Ultimately, the current source controls the amount of current flowing in the circuit. 

:::{admonition} Task 8: 
1. Assuming [*conservation of charge*](conservation-charge), write the equation for $V_{in}$ in terms of $V_{in}$, $E_{rest}$, $V_{ref}$, and the voltage across the membrane resistance. 
2. Write the equation for the voltage aross the memebrane resistance in terms of $R_{mem}$ and the applied current (the current in the circuit).
3. Substitute your equation from \#2 into your equation from \#1.
:::

You now have a computational model for $V_{in}$ in terms of $V_{ref}$, $E_{rest}$, $R_{mem}$, and the applied current. 

:::{admonition} Task 9: Analyze the model
Let's use the following values:
$V_{ref}$ = 0
$E_{rest}$ = -70mV
$R_{mem}$ = 50M$\omega$

1. Calculate $V_{in}$ (relative to $V_{ref}$) when the applied current is 0
2. Consider that you apply a current of 100pA across the model membrane. Calculate $V_{in}$ (relative to $V_{ref}$) when the applied current is 0
:::


:::{image} ../../images/circuit-task_RC-simple.png
:alt: circuit diagram
:width: 400px
:align: center
:::

 

In [](../passive-membrane-models/Lab-Manual_passive-membrane-models), you applied a current across an electric circuit model of a neuron membrane. In this model, the neuron membrane was modeled by an *RC circuit* in which a resistor and capacitor are arranged in parallel. You found that voltage does not change according to either $I \times R$ or $\frac{I}{C}$. Instead, in response to a current applied across the RC circuit, the voltage changes according to an exponential function, where the *time constant* ($\tau$) is the amount of time it takes for the voltage across the RC circuit to reach 63% of its maximum value. You measured this value for the passive membrane model you worked with in [](../passive-membrane-models/Lab-Manual_passive-membrane-models).

## Use your work to implement computational models on the computer
We will use the [Data Explorer](../computational-model/Data-Explorer_computational-model.ipynb) notebook to work through the implementation together during class. Later, you will answer questions in the [Responses](../computational-model/Responses_computational-model.ipynb) notebook.