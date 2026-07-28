"""Hybrid quantum-classical DNN from Applied Sciences 15, 4037 (2025)."""
from __future__ import annotations

import pennylane as qml
import torch
from torch import nn


class HQCDNN(nn.Module):
    """Dense reduction, angle embedding, BasicEntanglerLayers, and classifier."""

    def __init__(
        self,
        input_dim: int,
        qubits: int = 4,
        quantum_layers: int = 1,
        quantum_device: str = "default.qubit",
    ):
        super().__init__()
        if qubits not in (2, 4):
            raise ValueError("The source paper evaluates only 2- and 4-qubit variants")
        self.qubits = qubits
        self.quantum_layers = quantum_layers
        self.classical_in = nn.Sequential(nn.Linear(input_dim, qubits), nn.ReLU())
        self.quantum_weights = nn.Parameter(torch.empty(quantum_layers, qubits))
        nn.init.uniform_(self.quantum_weights, -0.01, 0.01)
        self.classifier = nn.Linear(qubits, 2)
        device = qml.device(quantum_device, wires=qubits)

        @qml.qnode(device, interface="torch", diff_method="backprop")
        def circuit(values: torch.Tensor, weights: torch.Tensor):
            qml.AngleEmbedding(values, wires=range(qubits), rotation="X")
            qml.BasicEntanglerLayers(weights, wires=range(qubits))
            return tuple(qml.expval(qml.PauliZ(wire)) for wire in range(qubits))

        self.circuit = circuit

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        angles = torch.tanh(self.classical_in(features)) * torch.pi
        values = torch.stack(
            tuple(self.circuit(angles.cpu(), self.quantum_weights.cpu())), dim=-1
        ).to(features)
        return self.classifier(values)
