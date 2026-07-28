# HQCDNN standalone adaptation

This directory reconstructs the hybrid quantum-classical deep neural network
from Applied Sciences 15, 4037 (2025). The implemented path is TF-IDF,
classical dense reduction with ReLU, PennyLane AngleEmbedding,
BasicEntanglerLayers, Pauli-Z measurement, and a classical binary classifier.
Both reported two- and four-qubit variants are supported.

The paper operates on Solidity EVM opcode bigrams. This benchmark operates on
Python, so normalized Python lexical-token bigrams replace opcode bigrams.
The paper does not state the number of BasicEntanglerLayers; this source uses
one layer by default and records that choice in every report. These facts make
the implementation an architectural adaptation, not an exact reproduction.

Run locally:

```bash
python run_experiments.py \
  --repo-root /path/to/Python-VulCode-Detection \
  --protocol all --qubits 4
```

The fixed split seed is 101 and the training seeds are 101, 202, and 303.
The Kaggle helper stages one CPU notebook per protocol and does nothing
external unless `--submit` is explicitly supplied.
