"""This module contains the device class and context manager"""
import numpy as np
from openqml import Device, DeviceError
from openqml import Variable
import strawberryfields as sf
from strawberryfields.ops import Catstate, Coherent, DensityMatrix, DisplacedSqueezed, Fock, Ket, Squeezed, Thermal, Gaussian
from strawberryfields.ops import GaussianTransform, Interferometer
from strawberryfields.ops import BSgate, CKgate, CXgate, CZgate, Dgate, Fouriergate, Kgate, Pgate, Rgate, S2gate, Sgate, Vgate, Xgate, Zgate
from strawberryfields.ops import MeasureFock, MeasureHeterodyne, MeasureHomodyne
from ._version import __version__
operator_map = {'CoherentState': Coherent, 'DisplacedSqueezed':
    DisplacedSqueezed, 'SqueezedState': Squeezed, 'ThermalState': Thermal,
    'GaussianState': Gaussian, 'Beamsplitter': BSgate, 'ControlledAddition':
    CXgate, 'ControlledPhase': CZgate, 'Displacement': Dgate,
    'QuadraticPhase': Pgate, 'Rotation': Rgate, 'TwoModeSqueezing': S2gate,
    'Squeeze': Sgate}
"""StrawberryFields Gaussian device for OpenQML.

    wires (int): the number of modes to initialize the device in.
    hbar (float): the convention chosen in the canonical commutation
        relation [x, p] = i hbar. The default value is hbar=2.
    """
name = 'Strawberry Fields OpenQML plugin'
short_name = 'strawberryfields.fock'
api_version = '0.1.0'
version = __version__
author = 'Josh Izaac'
_gates = set(operator_map.keys())
_observables = {'Fock', 'X', 'P', 'Homodyne', 'Heterodyne'}
_circuits = {}
def __init__(self, wires, *, shots=0, hbar=2):...
self.wires = wires
self.hbar = hbar
self.eng = None
self.state = None
super().__init__(self.short_name, shots)
def execute(self):...
"""docstring"""
if self.eng:
self.eng.reset()
self.eng, q = sf.Engine(self.wires, hbar=self.hbar)
self.reset()
for operation in self._queue:
if operation.name not in operator_map:
self.state = self.eng.run('gaussian')
p = [(x.val if isinstance(x, Variable) else x) for x in operation.params]
reg = self._observe.wires
op = operator_map[operation.name](*p)
if self._observe.name == 'Fock':
if isinstance(operation.wires, int):
ex = self.state.mean_photon(reg)
if self._observe.name == 'X':
op | q[operation.wires]
op | [q[i] for i in operation.wires]
var = 0
ex, var = self.state.quad_expectation(reg, 0)
if self._observe.name == 'P':
if self.shots != 0:
ex, var = self.state.quad_expectation(reg, np.pi / 2)
if self._observe.name == 'Homodyne':
ex = np.random.normal(ex, np.sqrt(var / self.shots))
self._out = ex
ex, var = self.state.quad_expectation(reg, *self._observe.params)
if self._observe.name == 'Displacement':
def reset(self):...
ex = self.state.displacement(modes=reg)
"""docstring"""
if self.eng is not None:
self.eng = None
self.state = None
