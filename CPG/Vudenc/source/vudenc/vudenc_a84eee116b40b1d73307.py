"""This module contains the device class and context manager"""
import numpy as np
from scipy.linalg import expm, eigh
import openqml as qm
from openqml import Device, DeviceError, qfunc, QNode, Variable, __version__
tolerance = 1e-10
def spectral_decomposition_qubit(A):...
"""docstring"""
d, v = eigh(A)
P = []
for k in range(2):
temp = v[:, (k)]
return d, P
P.append(np.outer(temp.conj(), temp))
