"""RQENN circuit from Scientific Reports 14, 13642 (2024)."""
from __future__ import annotations

import math

import pennylane as qml
import torch
from torch import nn


class RQENN(nn.Module):
    """Seven-qubit recurrent quantum embedding neural network.

    The 106 trainable parameters comprise two binary-index angles, 56
    QEmbedding parameters, and 48 QWeight parameters.
    """

    def __init__(
        self,
        vocab_size: int = 128,
        max_len: int = 100,
        qembedding_layers: int = 4,
        qweight_layers: int = 4,
        quantum_device: str = "default.qubit",
    ):
        super().__init__()
        self.qubits = math.ceil(math.log2(vocab_size))
        if vocab_size != 128 or self.qubits != 7:
            raise ValueError("RQENN paper configuration requires vocab_size=128 and 7 qubits")
        self.max_len = max_len
        self.qembedding_layers = qembedding_layers
        self.qweight_layers = qweight_layers
        self.binary_angles = nn.Parameter(torch.tensor([-math.pi / 2, math.pi / 2]))
        self.qembedding = nn.Parameter(
            torch.empty(qembedding_layers, 2, self.qubits)
        )
        self.qweight = nn.Parameter(
            torch.empty(qweight_layers, self.qubits - 1, 2)
        )
        nn.init.uniform_(self.qembedding, -0.01, 0.01)
        nn.init.uniform_(self.qweight, -0.01, 0.01)

        device = qml.device(quantum_device, wires=self.qubits)

        @qml.qnode(device, interface="torch", diff_method="backprop")
        def circuit(
            input_angles: torch.Tensor,
            qembedding: torch.Tensor,
            qweight: torch.Tensor,
        ):
            for wire in range(self.qubits):
                qml.Hadamard(wires=wire)
            for step in range(self.max_len):
                for wire in range(self.qubits):
                    qml.RY(input_angles[:, step, wire], wires=wire)
                for layer in range(self.qembedding_layers):
                    for wire in range(self.qubits):
                        qml.RY(qembedding[layer, 0, wire], wires=wire)
                    for control in range(0, self.qubits - 1, 2):
                        qml.CNOT(wires=[control, control + 1])
                    for wire in range(self.qubits):
                        qml.RY(qembedding[layer, 1, wire], wires=wire)
                    for control in range(1, self.qubits - 1, 2):
                        qml.CNOT(wires=[control, control + 1])
                for layer in range(self.qweight_layers):
                    for control in range(self.qubits - 1):
                        qml.RY(qweight[layer, control, 0], wires=control)
                        qml.RY(qweight[layer, control, 1], wires=control + 1)
                        qml.CNOT(wires=[control, control + 1])
            return (
                qml.expval(qml.PauliZ(self.qubits - 2)),
                qml.expval(qml.PauliZ(self.qubits - 1)),
            )

        self.circuit = circuit

    @property
    def quantum_parameter_count(self) -> int:
        return sum(parameter.numel() for parameter in self.parameters())

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        shifts = torch.arange(self.qubits, device=token_indices.device)
        bits = ((token_indices.unsqueeze(-1) >> shifts) & 1).bool()
        angles = torch.where(bits, self.binary_angles[1], self.binary_angles[0])
        values = self.circuit(
            angles.cpu(), self.qembedding.cpu(), self.qweight.cpu()
        )
        return torch.stack(tuple(values), dim=-1)
