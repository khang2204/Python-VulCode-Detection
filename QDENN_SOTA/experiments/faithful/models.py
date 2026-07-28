"""Faithful architectural adaptation of QDENN.

The circuit follows the source paper. Dataset-specific Python source
tokenization lives in ``data.py`` and is deliberately kept outside the model.
PennyLane broadcasting changes only how independent samples are evaluated,
not the circuit applied to each sample.
"""
from __future__ import annotations

import math

import pennylane as qml
import torch
from torch import nn


def indices_to_bits(indices: torch.Tensor, qubits: int) -> torch.Tensor:
    """Convert token indices [B,T] to little-endian binary values [B,T,Q]."""
    shifts = torch.arange(qubits, device=indices.device)
    return ((indices.unsqueeze(-1) >> shifts) & 1).to(torch.get_default_dtype())


class QDENN(nn.Module):
    """Quantum Deep Embedding Neural Network (Sci. Rep. 2022, 12:8053).

    A Hadamard initialization is followed by one input-encoding/variational
    block per token.  The first two Pauli-Z expectations are classification
    logits, matching the paper.  No classical recurrent layer is used.
    """

    def __init__(self, vocab_size: int = 128, max_len: int = 100):
        super().__init__()
        self.qubits = math.ceil(math.log2(vocab_size))
        self.max_len = max_len
        # The paper has two trainable Ry layers in each per-token block.
        self.theta = nn.Parameter(torch.empty(max_len, 2, self.qubits))
        nn.init.uniform_(self.theta, -0.01, 0.01)

        dev = qml.device("default.qubit", wires=self.qubits)

        @qml.qnode(dev, interface="torch", diff_method="backprop")
        def circuit(bits: torch.Tensor, theta: torch.Tensor):
            for wire in range(self.qubits):
                qml.Hadamard(wires=wire)

            for step in range(self.max_len):
                for wire in range(self.qubits):
                    qml.RX(bits[:, step, wire], wires=wire)

                for wire in range(self.qubits):
                    qml.RY(theta[step, 0, wire], wires=wire)
                for control in range(0, self.qubits - 1, 3):
                    qml.CNOT(wires=[control, control + 1])
                for control in range(1, self.qubits - 1, 3):
                    qml.CNOT(wires=[control, control + 1])

                for wire in range(self.qubits):
                    qml.RY(theta[step, 1, wire], wires=wire)
                for control in range(0, self.qubits - 3, 4):
                    qml.CNOT(wires=[control, control + 3])

            return (
                qml.expval(qml.PauliZ(0)),
                qml.expval(qml.PauliZ(1)),
            )

        self.circuit = circuit

    def forward(self, token_indices: torch.Tensor) -> torch.Tensor:
        bits = indices_to_bits(token_indices, self.qubits)
        return torch.stack(tuple(self.circuit(bits.cpu(), self.theta.cpu())), dim=-1)


MODELS = {"qdenn": QDENN}
