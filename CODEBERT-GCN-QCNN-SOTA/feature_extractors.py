"""Train and cache CodeBERT plus GCN-RFE features for the QCNN runner."""
from __future__ import annotations

import json
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from torch_geometric.loader import DataLoader as GraphLoader
from torch_geometric.nn import GCNConv, global_max_pool, global_mean_pool

from common import GRAPH_PATHS, fixed_manifest, load_records, set_seed, ten_percent_indices


class CodeDataset(Dataset):
    def __init__(self, records, indices, tokenizer, max_length):
        self.records, self.indices = records, indices
        self.tokenizer, self.max_length = tokenizer, max_length

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, offset):
        record = self.records[self.indices[offset]]
        encoded = self.tokenizer(
            record["source"], truncation=True, max_length=self.max_length,
            padding="max_length", return_tensors="pt",
        )
        return (
            encoded["input_ids"].squeeze(0),
            encoded["attention_mask"].squeeze(0),
            torch.tensor(record["label"]),
        )


class CodeBERTClassifier(nn.Module):
    def __init__(self, model_name):
        super().__init__()
        from transformers import AutoModel
        self.encoder = AutoModel.from_pretrained(model_name)
        self.classifier = nn.Linear(self.encoder.config.hidden_size, 2)

    def embed(self, input_ids, attention_mask):
        return self.encoder(
            input_ids=input_ids, attention_mask=attention_mask
        ).last_hidden_state[:, 0]

    def forward(self, input_ids, attention_mask):
        return self.classifier(self.embed(input_ids, attention_mask))


class BiaffineGCN(nn.Module):
    def __init__(self, input_dim, hidden=128, output_dim=128, dropout=0.3):
        super().__init__()
        self.first = GCNConv(input_dim, hidden)
        self.second = GCNConv(hidden, hidden)
        self.biaffine = nn.Bilinear(hidden, hidden, hidden)
        self.output = nn.Linear(hidden * 2, output_dim)
        self.classifier = nn.Linear(output_dim, 2)
        self.dropout = dropout

    def embed(self, batch):
        values = torch.relu(self.first(batch.x, batch.edge_index))
        values = nn.functional.dropout(values, self.dropout, self.training)
        values = torch.relu(self.second(values, batch.edge_index))
        mean = global_mean_pool(values, batch.batch)
        maximum = global_max_pool(values, batch.batch)
        interaction = torch.tanh(self.biaffine(mean, maximum))
        return self.output(torch.cat([mean, interaction], dim=-1))

    def forward(self, batch):
        return self.classifier(self.embed(batch))


def train_codebert(
    records, train_indices, validation_indices, args, directory, device,
):
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.codebert_model)
    model = CodeBERTClassifier(args.codebert_model).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.codebert_learning_rate)
    train_data = CodeDataset(records, train_indices, tokenizer, args.max_code_length)
    validation_data = CodeDataset(
        records, validation_indices, tokenizer, args.max_code_length
    )
    best, best_state, stale = -1.0, None, 0
    checkpoint = directory / "codebert_checkpoint.pt"
    start = 0
    if checkpoint.is_file():
        saved = torch.load(checkpoint, map_location=device, weights_only=False)
        model.load_state_dict(saved["model"])
        optimizer.load_state_dict(saved["optimizer"])
        start, best, best_state = saved["epoch"] + 1, saved["best"], saved["best_state"]
    for epoch in range(start, args.codebert_epochs):
        model.train()
        for ids, mask, labels in DataLoader(
            train_data, batch_size=args.codebert_batch_size, shuffle=True
        ):
            optimizer.zero_grad(set_to_none=True)
            loss = nn.functional.cross_entropy(
                model(ids.to(device), mask.to(device)), labels.to(device)
            )
            loss.backward()
            optimizer.step()
        correct, total = 0, 0
        model.eval()
        with torch.no_grad():
            for ids, mask, labels in DataLoader(
                validation_data, batch_size=args.codebert_batch_size
            ):
                predictions = model(ids.to(device), mask.to(device)).argmax(-1).cpu()
                correct += int((predictions == labels).sum())
                total += len(labels)
        score = correct / max(1, total)
        if score > best:
            best, stale = score, 0
            best_state = {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            }
        else:
            stale += 1
        torch.save({
            "epoch": epoch, "model": model.state_dict(),
            "optimizer": optimizer.state_dict(), "best": best,
            "best_state": best_state,
        }, checkpoint)
        print(f"CodeBERT epoch={epoch + 1} val_accuracy={score:.4f}", flush=True)
        if stale >= args.codebert_patience:
            break
    model.load_state_dict(best_state)
    return model, tokenizer


def train_gcn(graphs, train_indices, validation_indices, args, directory, device):
    model = BiaffineGCN(int(graphs[0].x.size(1))).to(device)
    optimizer = torch.optim.SGD(
        model.parameters(), lr=0.0005, momentum=0.9
    )
    best, best_state, stale = -1.0, None, 0
    checkpoint = directory / "gcn_checkpoint.pt"
    start = 0
    if checkpoint.is_file():
        saved = torch.load(checkpoint, map_location=device, weights_only=False)
        model.load_state_dict(saved["model"])
        optimizer.load_state_dict(saved["optimizer"])
        start, best, best_state = saved["epoch"] + 1, saved["best"], saved["best_state"]
    for epoch in range(start, args.graph_epochs):
        model.train()
        for batch in GraphLoader(
            [graphs[index] for index in train_indices],
            batch_size=args.graph_batch_size, shuffle=True,
        ):
            batch = batch.to(device)
            optimizer.zero_grad(set_to_none=True)
            loss = nn.functional.cross_entropy(model(batch), batch.y.view(-1))
            loss.backward()
            optimizer.step()
        model.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for batch in GraphLoader(
                [graphs[index] for index in validation_indices],
                batch_size=args.graph_batch_size,
            ):
                batch = batch.to(device)
                correct += int((model(batch).argmax(-1) == batch.y.view(-1)).sum())
                total += int(batch.num_graphs)
        score = correct / max(1, total)
        if score > best:
            best, stale = score, 0
            best_state = {
                key: value.detach().cpu().clone()
                for key, value in model.state_dict().items()
            }
        else:
            stale += 1
        torch.save({
            "epoch": epoch, "model": model.state_dict(),
            "optimizer": optimizer.state_dict(), "best": best,
            "best_state": best_state,
        }, checkpoint)
        print(f"GCN-RFEMLP epoch={epoch + 1} val_accuracy={score:.4f}", flush=True)
        if stale >= args.graph_patience:
            break
    model.load_state_dict(best_state)
    return model


@torch.no_grad()
def code_embeddings(model, tokenizer, records, args, device):
    model.eval()
    output = []
    dataset = CodeDataset(records, list(range(len(records))), tokenizer, args.max_code_length)
    for ids, mask, _ in DataLoader(dataset, batch_size=args.codebert_batch_size):
        output.append(model.embed(ids.to(device), mask.to(device)).cpu())
    return torch.cat(output)


@torch.no_grad()
def graph_embeddings(model, graphs, args, device):
    model.eval()
    output = []
    for batch in GraphLoader(graphs, batch_size=args.graph_batch_size):
        output.append(model.embed(batch.to(device)).cpu())
    return torch.cat(output)


def prepare_feature_bundle(args, source, protocol, seed, records_by_name, manifests):
    directory = args.feature_cache / protocol / source / f"seed_{seed}"
    bundle_path = directory / "features.pt"
    if bundle_path.is_file():
        return torch.load(bundle_path, map_location="cpu", weights_only=False)
    directory.mkdir(parents=True, exist_ok=True)
    source_records = records_by_name[source]
    train_indices = list(manifests[source]["train"])
    if protocol == "ten_percent":
        train_indices = ten_percent_indices(
            source_records, train_indices, args.sampling_seed
        )
    set_seed(seed)
    device = torch.device(
        args.feature_device if args.feature_device == "cpu" or torch.cuda.is_available()
        else "cpu"
    )
    graphs_by_name = {
        name: torch.load(
            args.repo_root / GRAPH_PATHS[name], map_location="cpu", weights_only=False
        )
        for name in records_by_name
    }
    codebert, tokenizer = train_codebert(
        source_records, train_indices, manifests[source]["validation"],
        args, directory, device,
    )
    gcn = train_gcn(
        graphs_by_name[source], train_indices, manifests[source]["validation"],
        args, directory, device,
    )
    sequence = {}
    graph = {}
    for name in records_by_name:
        sequence[name] = code_embeddings(
            codebert, tokenizer, records_by_name[name], args, device
        )
        graph[name] = graph_embeddings(gcn, graphs_by_name[name], args, device)

    # The paper specifies decision-tree RFE but not the retained dimension.
    from sklearn.feature_selection import RFE
    from sklearn.tree import DecisionTreeClassifier
    selector = RFE(
        DecisionTreeClassifier(random_state=seed),
        n_features_to_select=min(args.rfe_features, graph[source].shape[1]),
        step=0.1,
    )
    selector.fit(
        graph[source][train_indices].numpy(),
        torch.tensor([source_records[index]["label"] for index in train_indices]).numpy(),
    )
    support = torch.tensor(selector.support_, dtype=torch.bool)
    payload = {
        "source": source, "protocol": protocol, "seed": seed,
        "train_indices": train_indices,
        "validation_indices": manifests[source]["validation"],
        "test_indices": manifests[source]["test"],
        "rfe_support": support,
        "sequence": sequence,
        "graph": {name: values[:, support] for name, values in graph.items()},
        "labels": {
            name: torch.tensor([record["label"] for record in records])
            for name, records in records_by_name.items()
        },
        "sample_files": {
            name: [record["sample_file"] for record in records]
            for name, records in records_by_name.items()
        },
        "cwes": {
            name: [record["cwe"] for record in records]
            for name, records in records_by_name.items()
        },
    }
    torch.save(payload, bundle_path)
    return payload
