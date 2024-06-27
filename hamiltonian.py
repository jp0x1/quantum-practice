#basic copying of worksheet 1 to get the feel of programming for quantum
# reference: https://github.com/Ilumirnau/Open-Quantum-Systems

import numpy as np
#defining values
hw = 0.2
u = 1/np.sqrt(2) * np.array([[1,1,0]])

#pauli matrices and identities
X = np.matrix([[0,1],[1,0]])
Y = np.matrix([[0,-1j],[1j,0]])
Z = np.matrix([[1,0],[0,-1]])
I = np.matrix([[1,0], [0,1]])
#matrix u*sigma
usigma = sum([u[0][0] * X, u[0][1]*Y, u[0][2]*Z])

#hamiltonian
H = hw/2 * usigma
#hamiltonian squared
H_sq = H@H
print('H^2=\n', H_sq)

#value of hw/2 to the power of 2 up to 8 decimals
hw_half_sq = round(((hw/2)**2).real, 8) + 1j * round(((hw/2)**2).imag, 8)
print('(hbar * w/2)**2 =\n', hw_half_sq)
#is every matrix element of H*H equal to (hw/2) ** 2?
#matrix with booleans in every matrix element to the previous equality
elements_bool = (H_sq == (hw_half_sq * I))
print('Boolean Matrix=\n', elements_bool)

#condition if all items in previous matrix are 'True'
if elements_bool.all() == True:
    print("all elements coincide. equality is verified")



