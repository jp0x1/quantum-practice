from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

#basic circuit
#initialize single qubit with name X\
X = QuantumRegister(1,"X")
circuit = QuantumCircuit(X)
#starts with a standard qubit named q -> 
#sequence of gates representing unitary opertations on the qubit

#hadamard operation: H(|0> = 1/sqrt(2)|0> + 1/sqrt(2)|1>
#S = ([1,0],[0,i])
#T = ([1,0],[0, (1+i)/(sqrt(2))])

#What the circuit does is return the product of the states 

#Hadamard Operation
circuit.h(0)
#S operation
circuit.s(0)
#Hadamard Operation
circuit.h(0)
#T operation
circuit.t(0)
print(circuit)

