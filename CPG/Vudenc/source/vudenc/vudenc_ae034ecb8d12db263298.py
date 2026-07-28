"""
ProjectQ plugin
========================

**Module name:** :mod:`openqml.plugins.projectq`

.. currentmodule:: openqml.plugins.projectq

This plugin provides the interface between OpenQML and ProjecQ.
It enables OpenQML to optimize quantum circuits simulable with ProjectQ.

ProjecQ supports several different backends. Of those, the following are useful in the current context:

- projectq.backends.Simulator([gate_fusion, ...])	Simulator is a compiler engine which simulates a quantum computer using C++-based kernels.
- projectq.backends.ClassicalSimulator()	        A simple introspective simulator that only permits classical operations.
- projectq.backends.IBMBackend([use_hardware, ...])	The IBM Backend class, which stores the circuit, transforms it to JSON QASM, and sends the circuit through the IBM API.

See PluginAPI._capabilities['backend'] for a list of backend options.

Functions
---------

.. autosummary::
   init_plugin

Classes
-------

.. autosummary::
   Gate
   Observable
   PluginAPI

----
"""
import logging as log
import numpy as np
from numpy.random import randn
from openqml import Device, DeviceError
from openqml import Variable
import projectq as pq
import projectq.setups.ibm
from projectq.ops import HGate, XGate, YGate, ZGate, SGate, TGate, SqrtXGate, SwapGate, SqrtSwapGate, Rx, Ry, Rz, R
from .ops import CNOT, CZ, Toffoli, AllZGate, Rot, Hermitian
from ._version import __version__
operator_map = {'PauliX': XGate, 'PauliY': YGate, 'PauliZ': ZGate, 'CNOT':
    CNOT, 'CZ': CZ, 'SWAP': SwapGate, 'RX': Rx, 'RY': Ry, 'RZ': Rz, 'Rot': Rot}
"""ProjectQ device for OpenQML.

    Args:
       wires (int): The number of qubits of the device.

    Keyword Args for Simulator backend:
      gate_fusion (bool): If True, gates are cached and only executed once a certain gate-size has been reached (only has an effect for the c++ simulator).
      rnd_seed (int): Random seed (uses random.randint(0, 4294967295) by default).

    Keyword Args for IBMBackend backend:
      use_hardware (bool): If True, the code is run on the IBM quantum chip (instead of using the IBM simulator)
      num_runs (int): Number of runs to collect statistics. (default is 1024)
      verbose (bool): If True, statistics are printed, in addition to the measurement result being registered (at the end of the circuit).
      user (string): IBM Quantum Experience user name
      password (string): IBM Quantum Experience password
      device (string): Device to use (‘ibmqx4’, or ‘ibmqx5’) if use_hardware is set to True. Default is ibmqx4.
      retrieve_execution (int): Job ID to retrieve instead of re-running the circuit (e.g., if previous run timed out).
    """
name = 'ProjectQ OpenQML plugin'
short_name = 'projectq'
api_version = '0.1.0'
plugin_version = __version__
author = 'Christian Gogolin'
_capabilities = {'backend': list(['Simulator', 'ClassicalSimulator',
    'IBMBackend'])}
def __init__(self, wires, **kwargs):...
kwargs.setdefault('shots', 0)
super().__init__(self.short_name, kwargs['shots'])
for k, v in {'log': 'verbose'}.items():
if k in kwargs:
if 'num_runs' in kwargs:
kwargs.setdefault(v, kwargs[k])
if isinstance(kwargs['num_runs'], int) and kwargs['num_runs'] > 0:
self.wires = wires
self.n_eval = kwargs['num_runs']
self.n_eval = 0
self.backend = kwargs['backend']
self.kwargs = kwargs
self.eng = None
self.reg = None
def reset(self):...
self.reg = self.eng.allocate_qureg(self.wires)
def __repr__(self):...
return super().__repr__() + 'Backend: ' + self.backend + '\n'
