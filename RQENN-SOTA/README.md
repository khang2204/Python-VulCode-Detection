# RQENN standalone reproduction

This directory implements the Recurrent Quantum Embedding Neural Network
(RQENN) described in Scientific Reports 14, 13642 (2024). It retains the
reported 128-token vocabulary, seven qubits, sequence length 100, four
QEmbedding layers, four QWeight layers, 106 trainable parameters, Adam
optimizer, learning rate 0.01, batch size 64, and ten epochs.

The original study uses C/C++ code gadgets and five-fold cross-validation.
This benchmark adaptation uses raw Python tokens and one fixed stratified
70/15/15 manifest with split seed 101. Training randomness changes across
seeds 101, 202, and 303. It must be reported as a faithful architectural
adaptation rather than an exact reproduction of the original scores.

Run one resumable unit:

```bash
python run_experiments.py \
  --repo-root /path/to/Python-VulCode-Detection \
  --protocol in_domain \
  --dataset vudenc \
  --seed 101
```

Use `--protocol all` for in-domain, cross-dataset generalization, ten-percent
training, and long-tail CWE vulnerable recall. Checkpoints are written after
every epoch. CPU is recommended for `default.qubit`.
