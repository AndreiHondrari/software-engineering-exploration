# Fundamentals

## From voltages to words

### Part 1 - Wires and electrons

Inside a computer, at the most basic level there are wires, resistors, power supplies, capacitors, transistors, relays, inductors, pins, switches, chips (more complicated transistors) that are organised in specific patterns.

Through all these components there is a flow of electricity, electrons (negative charges) going from - to +, or alternatively lack of electrons (positive charges) going from + to -. The flow of electricity starts from the power socket
to which the computer is connected to, then this electricity is transformed and redirected so that a sinusoidal (alternatively periodically changing) electrical current becomes a direct current of a specific value. The sinusoidal current varies from 0 volts (min value) to 220 volts (peak value) and cycles at a frequency of around 50 Hz. This current after it passes through the converter and regulator parts of the power supply it will be returned by the power supply as a constant current of several values (usually 3.3 V, 5 V, 9 V and 12 V). These values each come on dedicated wires, and all of them are positive endpoints, all which have a single counterpart negative charge endpoint.

In between the positive endpoints and the sole negative endpoint there are a multitude of circuits and chips that all serve the functionality of the computer.

### Part 2 - Structure on top of chaos

While in nature all of this electricity and matter (metal, silicon, graphite, quartz and compounds) appears randomly, chaotically, matching them in specific patterns gives birth to patterns of simple behaviour that occurs repetitively under the same circumstances.

Examples:

* a current through graphite will slow down the flow of electrons effectively creating a difference of potential (a voltage) between the entry and the exit points of the graphite, whose value depends on the thickness and length of the graphite
* two sheets of thin metal compound separated by a thin electrical isolator will keep an electrostatic charge when applying a differently charged (+ and -) voltage on each of the foils, essentially memorising the previously applied voltage
* a wire that is cut will act as a barrier (on/off) for the electricity that flows through the wire, depending on the fact that the severed ends of the wire are touching or not
* considering that silicon can be forced to have mostly negative charges or positive charges inside its structure (think about the valence layer of the atom), when applying a voltage on each of the two differently charged silicon crystals that are touching, the structure will act as a unidirectional current barrier, working when applying in one way and blocking when applying in reverse (the diode).
* considering the previous example and considering that you have three layers inside the crystal, on in the middle of one charge and two in the ends of an opposite charge, based on the configuration the structure can act as an electrically controlled switch (a smart wire basically) allowing the flow of current to pass from left to right as a function of a current applied in the middle

### Part 3 - Functionality

Going further, combining these patterns in more complex patterns allows us to condition the flow of electricity through these complex circuits in a very specific manner that can have a desirable functionality.

Examples:

* a resistor passes more or less current based on the temperature it is exposed to, current whose value will act on a transistor that will switch on or off a light bulb, essentially telling is that a medium surpassed a specific temperature
* two transistors in series will pass the voltage at the exit of the last transistor if both of the inputs (middle layers of the transistors) are exposed to a current, essentially acting as a condition of both inputs (first input AND second input)
* pulling a wire from the entry point of a transistor will output a current if there is no current on the input of the transistor, or oppositely it will not output a current if there is a current on the input of the transistor, essentially acting as a negation of the single input (NOT input)
* two transistors in parallel (one constant charge on the left and same output wire on the right) will yield a current if any of the inputs of the transistor sees a current, basically acting as a condition of both of the inputs (first input OR second input)

All of these slightly complex examples, combined in even more complex patterns can give birth to some useful applications like:

* starting a pump of cold water if the temperature is too high in a boiler
* switching on a light bulb if there is no light outside
* sounding an alarm and opening a water valve if there is smoke in a room
* starting the radio if it is 8:00 AM (morning)

### Part 4 - Values and numbers

While in nature values, sizes and forces have a continuous, analogue value that can vary subtly, the absence and existence of a current flow through a wire also has a value, although more discrete, giving birth to the notion of existence and non-existence, or otherwise said to the values of "true" and "false", 1 and 0, 5 Volts and 0 Volts. This system of binary values can be used to represent other types of values like decimal numbers, given enough bits (adjacent values of 0 and 1). Example, number 5 in the binary system is 101, number 8 is 1000.

Pairing this system of values with the conditional flow of electricity through wires, by using transistors, diodes, etc. we can create systems of logic that give certain outputs based on certain inputs.

### Part 5 - Logic circuits

The most fundamental logic circuits are:

* AND gates: outputs true if both of the inputs are true
* OR gates: outputs true if any of the inputs are true
* NOT gates: output the opposite value of the input

Combining these will give birth to NAND (NOT AND), NOR (NOT OR), XOR (EXCLUSIVE OR), NXOR (NOT EXCLUSIVE OR) gates.

### Part 6 - Decoders, encoders, multiplexers, demultiplexers, latches, counters, adders, registers

Combining the fundamental logic gates one can create:

* decoders - outputs on a specific wire based on the binary combination of the set of the input wires, basically each output wire corresponds to a binary value. 0000 will enable first wire, 0001 will enable second wire and so on and so forth. The number of outputs of a decoder depends on the number of inputs, according to the numbering systems.
* encoders - outputs a binary combination based on which input wire is enabled, essentially performing the opposite functionality of a decoder
* multiplexers - reroute a specific wire from the set of inputs to the sole output based on a selection address specified on a secondary set of inputs that condition which of the input wires from the first set are to be forwarded
* demultiplexers - opposite functionality of the multiplexer
* latches - have an internal state of 0 or 1 which is changed based on one of the two inputs that act as a set (change to 1) or reset (change to 0). Latches can be extended to different functionalities such as toggles or delay
* timed latches - will change the value only if the clock input of the latch is 1

Latches can be combined an extended to form:
* counters - binary output can change with a specific increment for every clock
* registers - memorise a word/group of bits
* adders/subtractors/multipliers - will give arithmetic outputs based on the numerical inputs

### Part 7 - Programmable computer

Combining even further these logic circuits, one can create a computer that executes a stored sequence of instructions. Usually the stored program is kept on a read-only memory medium, such as a tape, a magnetic matrix, an instruction punched-card, an EEPROM chip, etc.

The instructions found in one of these mediums are linearly sequentially ordered and each position of the instruction represents its address.

Usually inside a computer there is a counter that keeps track of the current address of the instruction that needs to be executed and jumps to the next after execution.

Instructions are kept in a binary format of course and each binary combination represents a specific low-level operation that the computer has to perform. This translation from instruction binary combination to sub-circuit of the computer that has to perform is done through a decoder that is hardwired to all the various parts of the computer.

These kind of operations are "set in stone", hardwired, and they are of the following sort:
* memorise a value somewhere
* read a value from an input device
* write a value to an output device
* perform an arithmetic operation on two numbers
* change the current instruction address to a different address

Organising a computer like this will allow us to define in the read-only memory any functionality that we want, which at first is in a very basic form, represented by binary numbers (also called machine code).

### Part 8 - Compilers and programming languages

Taking the ability of programming a computer at such a low level enables one to write an operating system for the computer which recognises text input from a keyboard and allows to store text in text files on a permanent memory device like a hard-drive. One can also create a program that will parse and translate this text to something else, like for example machine code, empowering the user of the computer to write computer code in a more visible, elegant way.

We may notice at this point that the machine code, as well as the programming languages are conventional by nature, and they do whatever the creator of these codes intended for them to do.

### Part 9 - Values, expressions and flow control

In a similar manner to building complex circuits out of basic AND, OR, NOT logic gates, by making an analogy we can assume that we can also build complex software constructs out of simple, fundamental instructions as copy/move, evaluate, jump and arithmetic operations to basically create any level of abstraction we desire that is represented by specific language syntax allowing us the following:
* to chose one sequence of instructions or another
* to loop a sequence of instructions a number of times or indefinitely
* to create complex data structure representations (arrays, linked lists, graphs, trees, queues, stacks, complex numbers, matrices, hash tables, etc.)
* to enclose a sequence of instructions under a label and to call that label anywhere we want (functions)
* to put data and functionality in a single construct (classes/objects, modules)
* to allow distribution of data and computation between multiple threads, processors, programs or computers

### Part 10 - Applications
On top of those abstractions we can finally create desirable functionality such as:
* to define communication protocols that allow two computers to communicate to each other
* to define encryption schemes that scramble information in storage or in transit
* to program other computers
* to create other programming languages
* to compress data
* to perform complex calculations (like Fast-Fourier Transform)
* to define business rules that serve a greater purpose (a route planner, an e-commerce solution, a personnel administration dashboard, a factory scheduling platform, etc.)
