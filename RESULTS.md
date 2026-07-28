# QProtoGAT-Vul Binary Detection Results

## Finalized fixed-split protocol

All results below use a fixed stratified 70/15/15 train/validation/test split
with `split_seed=101`. Values are mean ± sample standard deviation across
`training_seed` 101, 202, and 303. Classical and Quantum use the same split
and training seeds. The QProtoGAT-Vul_Quantum model uses 10 qubits, circuit depth 5,
attention/value dimension 64, and learning rate 0.002. In-domain 10% also
uses the same fixed stratified 10% subset (`sampling_seed=101`) for all three
training seeds.

## In-domain

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | Classical | 93.15% ± 1.25% | 92.02% ± 1.34% | 93.23% ± 1.80% | 87.75% ± 1.70% | 90.40% ± 1.75% |
|  | QProtoGAT-Vul_Quantum | **96.58% ± 0.83%** | **96.57% ± 0.82%** | **94.27% ± 1.40%** | **96.57% ± 0.85%** | **95.40% ± 1.10%** |
| VUDENC | Classical | 86.27% ± 1.51% | 79.35% ± 1.04% | 60.00% ± 4.46% | 68.65% ± 0.48% | 63.98% ± 2.66% |
|  | QProtoGAT-Vul_Quantum | **86.60% ± 0.33%** | **80.46% ± 0.74%** | **60.40% ± 1.09%** | **70.94% ± 1.99%** | **65.23% ± 0.70%** |
| RealVuln | Classical | 83.33% ± 3.25% | 72.47% ± 2.59% | 91.68% ± 0.87% | 88.27% ± 4.28% | 89.90% ± 2.23% |
|  | QProtoGAT-Vul_Quantum | **86.46% ± 3.25%** | **72.96% ± 3.94%** | 91.45% ± 1.13% | **92.59% ± 3.21%** | **92.01% ± 2.03%** |

**Nhận xét In-domain.** Quantum cải thiện nhất quán trên BenchmarkPython và
VUDENC, đặc biệt BenchmarkPython tăng F1 từ 90.40% lên 95.40%. Trên RealVuln,
Quantum tăng Recall và F1 rõ rệt, dù Precision giảm nhẹ 0.23 điểm phần trăm.
Nhìn chung, ở cùng fixed split, Quantum thắng 14/15 metric in-domain.

## In-domain — SOTA

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | QDENN | 59.46% ± 3.29% | 52.24% ± 1.68% | 42.31% ± 4.18% | 25.00% ± 6.74% | 30.82% ± 4.82% |
|  | HQCDNN (4q) | 68.29% ± 2.05% | 65.49% ± 1.22% | 57.45% ± 3.57% | 54.90% ± 4.49% | 55.97% ± 1.59% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **96.58% ± 0.83%** | **96.57% ± 0.82%** | **94.27% ± 1.40%** | **96.57% ± 0.85%** | **95.40% ± 1.10%** |
| VUDENC | QDENN | 83.32% ± 0.11% | 56.13% ± 0.52% | 63.31% ± 1.94% | 14.01% ± 1.26% | 22.92% ± 1.61% |
|  | HQCDNN (4q) | 85.44% ± 0.22% | 72.39% ± 1.81% | 60.31% ± 0.58% | 52.18% ± 4.32% | 55.88% ± 2.33% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **86.60% ± 0.33%** | **80.46% ± 0.74%** | 60.40% ± 1.09% | **70.94% ± 1.99%** | **65.23% ± 0.70%** |
| RealVuln | QDENN | 82.81% ± 4.13% | 51.79% ± 2.79% | 84.86% ± 0.74% | 96.91% ± 5.35% | 90.44% ± 2.58% |
|  | HQCDNN (4q) | 83.85% ± 0.90% | 49.69% ± 0.53% | 84.29% ± 0.14% | 99.38% ± 1.07% | 91.22% ± 0.54% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **86.46% ± 3.25%** | **72.96% ± 3.94%** | **91.45% ± 1.13%** | 92.59% ± 3.21% | **92.01% ± 2.03%** |

**Nhận xét In-domain — SOTA.** So với QDENN, QProtoGAT-Vul_Quantum (Ours) tăng F1 lần lượt
64.58, 42.31 và 1.57 điểm phần trăm trên BenchmarkPython, VUDENC và RealVuln.
So với HQCDNN 4q, mức tăng F1 tương ứng là 39.43, 9.35 và 0.79 điểm phần trăm.
HQCDNN 4q có Recall RealVuln rất cao nhưng Balanced Accuracy thấp, trong khi
QProtoGAT-Vul_Quantum (Ours) cân bằng tốt hơn giữa hai lớp và đạt F1 cao hơn.

## Generalization

| Train → Test | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython → VUDENC | Classical | 35.78% ± 5.92% | 40.87% ± 3.15% | 13.60% ± 1.14% | 48.75% ± 3.42% | 21.23% ± 1.41% |
|  | QProtoGAT-Vul_Quantum | 31.22% ± 6.54% | **41.60% ± 3.09%** | **14.32% ± 1.06%** | **57.68% ± 6.44%** | **22.91% ± 1.54%** |
| BenchmarkPython → RealVuln | Classical | 47.33% ± 8.47% | 50.07% ± 3.16% | 84.09% ± 1.74% | 46.04% ± 12.28% | 58.82% ± 10.63% |
|  | QProtoGAT-Vul_Quantum | **51.35% ± 7.73%** | **50.32% ± 6.18%** | 83.89% ± 3.36% | **51.84% ± 8.62%** | **63.90% ± 7.69%** |
| VUDENC → BenchmarkPython | Classical | 39.57% ± 2.05% | 48.83% ± 1.47% | 36.09% ± 0.78% | 83.78% ± 8.10% | 50.40% ± 2.04% |
|  | QProtoGAT-Vul_Quantum | 39.32% ± 2.72% | 47.93% ± 1.62% | 35.60% ± 0.84% | 80.38% ± 6.11% | 49.30% ± 1.42% |
| VUDENC → RealVuln | Classical | 42.85% ± 3.71% | 46.62% ± 1.45% | 81.76% ± 1.11% | 41.07% ± 4.83% | 54.58% ± 4.54% |
|  | QProtoGAT-Vul_Quantum | **44.55% ± 2.58%** | 46.07% ± 4.84% | 81.66% ± 2.92% | **43.83% ± 1.84%** | **57.03% ± 2.13%** |
| RealVuln → BenchmarkPython | Classical | 36.78% ± 0.05% | 50.02% ± 0.04% | 36.76% ± 0.02% | 100.00% ± 0.00% | 53.76% ± 0.02% |
|  | QProtoGAT-Vul_Quantum | 36.75% ± 0.00% | 50.00% ± 0.00% | 36.75% ± 0.00% | **100.00% ± 0.00%** | 53.75% ± 0.00% |
| RealVuln → VUDENC | Classical | 32.39% ± 4.76% | 52.03% ± 2.60% | 18.50% ± 1.04% | 82.42% ± 2.60% | 30.20% ± 1.36% |
|  | QProtoGAT-Vul_Quantum | 29.02% ± 3.16% | 51.86% ± 0.99% | 18.36% ± 0.37% | **87.23% ± 2.96%** | **30.33% ± 0.42%** |

**Nhận xét Generalization.** Quantum cho kết quả tốt hơn ở các hướng
BenchmarkPython → VUDENC, BenchmarkPython → RealVuln và VUDENC → RealVuln,
chủ yếu nhờ Recall/F1 cao hơn. Ví dụ, ở BenchmarkPython → RealVuln, F1 tăng từ
58.82% lên 63.90%. Tuy vậy, Quantum kém hơn trên VUDENC → BenchmarkPython và
phần lớn metric của RealVuln → BenchmarkPython gần như bão hòa/không thay đổi.
VUDENC và RealVuln chủ yếu gồm code context/snippet, trong khi mỗi mẫu
BenchmarkPython là một tệp Python hoàn chỉnh. Hai hướng này đòi hỏi tổng hợp
ngữ cảnh ở cấp file; biểu diễn Quantum nén qua 10 qubit có thể làm mất một phần
tín hiệu cấu trúc cần thiết khi chuyển từ snippet sang full-file. Ở RealVuln →
BenchmarkPython, cả hai phương pháp gần như dự đoán toàn bộ mẫu là vulnerable,
nên chênh lệch rất nhỏ phản ánh failure mode do domain shift hơn là ưu thế thực
chất của Classical.

## Generalization — SOTA

| Train → Test | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython → VUDENC | QDENN | 52.77% ± 21.18% | 41.87% ± 6.99% | 12.48% ± 2.28% | 25.00% ± 15.00% | 15.00% ± 2.55% |
|  | HQCDNN (4q) | 64.69% ± 29.58% | 50.45% ± 3.08% | 33.50% ± 15.18% | 28.40% ± 38.05% | 16.34% ± 9.44% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 31.22% ± 6.54% | 41.60% ± 3.09% | 14.32% ± 1.06% | **57.68% ± 6.44%** | **22.91% ± 1.54%** |
| BenchmarkPython → RealVuln | QDENN | 29.54% ± 8.84% | 49.65% ± 1.81% | 85.16% ± 3.68% | 20.07% ± 13.86% | 30.72% ± 17.91% |
|  | HQCDNN (4q) | 35.50% ± 26.37% | 52.80% ± 2.05% | 90.64% ± 4.06% | 27.35% ± 37.85% | 32.83% ± 39.06% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **51.35% ± 7.73%** | 50.32% ± 6.18% | 83.89% ± 3.36% | **51.84% ± 8.62%** | **63.90% ± 7.69%** |
| VUDENC → BenchmarkPython | QDENN | **59.49% ± 3.87%** | **50.50% ± 1.93%** | **40.09% ± 5.68%** | 16.59% ± 5.89% | 22.68% ± 4.76% |
|  | HQCDNN (4q) | 40.60% ± 3.35% | 49.29% ± 0.93% | 36.36% ± 0.52% | 82.08% ± 10.73% | 50.27% ± 1.97% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 39.32% ± 2.72% | 47.93% ± 1.62% | 35.60% ± 0.84% | 80.38% ± 6.11% | 49.30% ± 1.42% |
| VUDENC → RealVuln | QDENN | 20.80% ± 1.28% | **49.53% ± 1.12%** | **82.22% ± 4.15%** | 7.27% ± 1.62% | 13.34% ± 2.74% |
|  | HQCDNN (4q) | 33.49% ± 0.97% | 46.92% ± 4.37% | 81.44% ± 4.11% | 27.16% ± 2.98% | 40.61% ± 2.99% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **44.55% ± 2.58%** | 46.07% ± 4.84% | 81.66% ± 2.92% | **43.83% ± 1.84%** | **57.03% ± 2.13%** |
| RealVuln → BenchmarkPython | QDENN | **38.37% ± 1.86%** | **50.14% ± 0.55%** | **36.83% ± 0.29%** | 94.54% ± 4.51% | 52.99% ± 0.46% |
|  | HQCDNN (4q) | 36.75% ± 0.00% | 50.00% ± 0.00% | 36.75% ± 0.00% | **100.00% ± 0.00%** | **53.75% ± 0.00%** |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 36.75% ± 0.00% | 50.00% ± 0.00% | 36.75% ± 0.00% | **100.00% ± 0.00%** | 53.75% ± 0.00% |
| RealVuln → VUDENC | QDENN | 18.02% ± 0.14% | 48.16% ± 0.55% | 17.16% ± 0.17% | 94.83% ± 1.62% | 29.06% ± 0.32% |
|  | HQCDNN (4q) | 18.82% ± 1.92% | 50.57% ± 1.00% | 17.88% ± 0.30% | **99.75% ± 0.43%** | **30.33% ± 0.41%** |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **29.02% ± 3.16%** | **51.86% ± 0.99%** | **18.36% ± 0.37%** | 87.23% ± 2.96% | **30.33% ± 0.42%** |

**Nhận xét Generalization — SOTA.** QProtoGAT-Vul_Quantum (Ours) đạt F1 cao nhất ở ba hướng
BenchmarkPython → VUDENC (22.91%), BenchmarkPython → RealVuln (63.90%) và
VUDENC → RealVuln (57.03%). Ở cả ba hướng này, lợi thế chủ yếu đến từ Recall
cao hơn: mô hình nhận diện được nhiều mẫu vulnerable hơn khi target vẫn là
context/snippet (VUDENC hoặc RealVuln), dù Precision và Balanced Accuracy
không phải lúc nào cũng cao nhất. Ngược lại, ở VUDENC → BenchmarkPython,
QDENN có F1 22.68% và HQCDNN 4q có F1 50.27%, đều cao hơn Quantum (49.30%).
Ở RealVuln → BenchmarkPython, HQCDNN 4q và Quantum cùng có F1 53.75% sau làm
tròn; tuy nhiên cả hai đều có Recall 100% và Balanced Accuracy
xấp xỉ 50%, cho thấy mô hình gần như dự đoán mọi mẫu là vulnerable. Hai hướng
kiểm chứng trên BenchmarkPython khó hơn vì source là snippet/context còn target
là tệp Python hoàn chỉnh; chúng đòi hỏi tổng hợp ngữ cảnh ở cấp file thay vì
chỉ nhận diện pattern cục bộ. Kết quả này cho thấy biểu diễn Quantum hiện tại
nhạy hơn với thay đổi granularity/context: phép nén qua 10 qubit có thể làm
giảm tín hiệu cấu trúc cần thiết khi chuyển từ snippet sang full-file, trong
khi Classical/HQCDNN giữ được lợi thế hơn ở một số hướng đó.

## In-domain 10%

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | Classical | 59.82% ± 4.84% | 58.58% ± 1.53% | 47.18% ± 5.78% | 53.92% ± 11.04% | 49.41% ± 2.38% |
|  | QProtoGAT-Vul_Quantum | **60.18% ± 5.02%** | **58.66% ± 1.96%** | **47.60% ± 6.35%** | 52.94% ± 10.29% | 49.23% ± 2.10% |
| VUDENC | Classical | 79.73% ± 1.40% | 71.68% ± 1.49% | 44.78% ± 2.02% | 59.22% ± 5.94% | 50.82% ± 0.81% |
|  | QProtoGAT-Vul_Quantum | **79.83% ± 1.53%** | **71.81% ± 1.42%** | **45.01% ± 2.29%** | **59.38% ± 5.98%** | **51.02% ± 0.61%** |
| RealVuln | Classical | 82.81% ± 3.12% | 51.79% ± 6.38% | 84.87% ± 1.76% | 96.91% ± 2.14% | 90.49% ± 1.74% |
|  | QProtoGAT-Vul_Quantum | **82.81% ± 3.12%** | **53.15% ± 5.25%** | **85.25% ± 1.45%** | 96.30% ± 3.21% | 90.42% ± 1.85% |

**Nhận xét In-domain 10%.** Với cùng tập 10% cố định, Quantum cải thiện nhẹ
Accuracy, Balanced Accuracy và Precision trên BenchmarkPython, nhưng Recall
giảm 0.98 điểm phần trăm và F1 giảm 0.18 điểm phần trăm. Trên VUDENC, Quantum
cao hơn Classical ở cả năm metric, trong đó F1 tăng từ 50.82% lên 51.02%.
Trên RealVuln, hai phương pháp đạt cùng Accuracy 82.81%; Quantum tăng Balanced
Accuracy từ 51.79% lên 53.15% và Precision từ 84.87% lên 85.25%, trong khi
Recall và F1 giảm lần lượt 0.61 và 0.07 điểm phần trăm. Nhìn chung, lợi ích của
Quantum trong chế độ ít nhãn có xuất hiện nhưng mức chênh lệch nhỏ và phụ thuộc
dataset.

## In-domain 10% — SOTA

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | QDENN | 53.87% ± 3.26% | 48.75% ± 2.46% | 35.15% ± 3.61% | 29.41% ± 1.47% | 31.95% ± 1.52% |
|  | HQCDNN (4q) | 54.41% ± 15.29% | 50.00% ± 0.00% | 12.25% ± 21.22% | 33.33% ± 57.74% | 17.92% ± 31.04% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **60.18% ± 5.02%** | **58.66% ± 1.96%** | **47.60% ± 6.35%** | **52.94% ± 10.29%** | **49.23% ± 2.10%** |
| VUDENC | QDENN | 81.72% ± 0.30% | 55.56% ± 0.47% | 45.25% ± 2.47% | 15.04% ± 0.76% | 22.58% ± 1.16% |
|  | HQCDNN (4q) | 80.08% ± 1.13% | 65.09% ± 1.97% | 43.60% ± 3.11% | 41.88% ± 4.45% | 42.65% ± 3.22% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 79.83% ± 1.53% | **71.81% ± 1.42%** | 45.01% ± 2.29% | **59.38% ± 5.98%** | **51.02% ± 0.61%** |
| RealVuln | QDENN | 78.65% ± 1.80% | 53.40% ± 3.42% | 85.38% ± 1.01% | 90.12% ± 1.07% | 87.69% ± 1.04% |
|  | HQCDNN (4q) | 38.54% ± 39.69% | 50.00% ± 0.00% | 28.12% ± 48.71% | 33.33% ± 57.74% | 30.51% ± 52.84% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **82.81% ± 3.12%** | 53.15% ± 5.25% | 85.25% ± 1.45% | **96.30% ± 3.21%** | **90.42% ± 1.85%** |

**Nhận xét In-domain 10% — SOTA.** Trên BenchmarkPython, QProtoGAT-Vul_Quantum (Ours)
vượt cả hai SOTA ở toàn bộ năm metric. Trên VUDENC, Quantum đạt Balanced
Accuracy, Recall và F1 cao nhất; Accuracy thấp hơn QDENN 1.89 điểm phần trăm
và Precision thấp hơn QDENN 0.24 điểm phần trăm. Trên RealVuln,
QProtoGAT-Vul_Quantum (Ours) đạt Accuracy 82.81%, Recall 96.30% và F1 90.42%,
cao hơn cả QDENN và HQCDNN 4q; QDENN chỉ nhỉnh hơn 0.25 điểm phần trăm ở
Balanced Accuracy và 0.13 điểm phần trăm ở Precision. HQCDNN biến động mạnh do
tập train 10% chỉ có 56 mẫu.

## Long-tail CWE Recall

Rare/Common CWEs are determined from the fixed training split: a CWE with
frequency at or below the median is Rare.

| Dataset | Method | Rare-CWE Recall | Common-CWE Recall |
| --- | --- | ---: | ---: |
| BenchmarkPython | Classical | 80.00% ± 5.00% | 90.97% ± 3.18% |
|  | QProtoGAT-Vul_Quantum | **93.33% ± 5.77%** | **97.92% ± 2.08%** |
| VUDENC | Classical | 66.67% ± 3.61% | 69.54% ± 1.90% |
|  | QProtoGAT-Vul_Quantum | **68.96% ± 4.20%** | **71.84% ± 1.00%** |
| RealVuln | Classical | 92.59% ± 6.42% | 87.41% ± 4.63% |
|  | QProtoGAT-Vul_Quantum | **100.00% ± 0.00%** | **91.11% ± 3.85%** |

**Nhận xét Long-tail CWE Recall.** QProtoGAT-Vul_Quantum tăng cả Rare/Common-CWE
Recall trên ba benchmark. Mức tăng Rare/Common lần lượt là 13.33/6.95 điểm
phần trăm trên BenchmarkPython, 2.29/2.30 điểm phần trăm trên VUDENC và
7.41/3.70 điểm phần trăm trên RealVuln. Nhóm Rare/Common chiếm tương ứng
29.4%/70.6% số mẫu vulnerable test ở BenchmarkPython, 31.1%/68.9% ở VUDENC và
16.7%/83.3% ở RealVuln. Vì RealVuln chỉ có 16.7% mẫu vulnerable thuộc nhóm
Rare, kết quả Rare-CWE Recall 100% tại đây cần được diễn giải thận trọng.

## Long-tail CWE Recall — SOTA

| Dataset | Method | Rare-CWE Recall | Common-CWE Recall |
| --- | --- | ---: | ---: |
| BenchmarkPython | QDENN | 38.33% ± 5.77% | 19.44% ± 7.89% |
|  | HQCDNN (4q) | 50.00% ± 5.00% | 56.94% ± 4.34% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **93.33% ± 5.77%** | **97.92% ± 2.08%** |
| VUDENC | QDENN | 14.50% ± 2.75% | 13.79% ± 1.50% |
|  | HQCDNN (4q) | 47.58% ± 3.84% | 54.25% ± 5.35% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **68.96% ± 4.20%** | **71.84% ± 1.00%** |
| RealVuln | QDENN | 96.30% ± 6.42% | 97.04% ± 5.13% |
|  | HQCDNN (4q) | 100.00% ± 0.00% | 99.26% ± 1.28% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **100.00% ± 0.00%** | 91.11% ± 3.85% |

**Nhận xét Long-tail CWE Recall — SOTA.** Trên BenchmarkPython,
QProtoGAT-Vul_Quantum (Ours) đạt Rare/Common-CWE Recall 93.33%/97.92%, cao
hơn HQCDNN 4q lần lượt 43.33/40.98 điểm phần trăm và cao hơn QDENN
55.00/78.48 điểm phần trăm. Trên VUDENC, mô hình đạt 68.96%/71.84%, tiếp tục
cao nhất ở cả hai nhóm. Trên RealVuln, Rare-CWE Recall 100% bằng HQCDNN 4q;
Common-CWE Recall 91.11% thấp hơn QDENN 5.93 điểm phần trăm và HQCDNN 4q
8.15 điểm phần trăm. Các hệ thống trong bảng sử dụng cùng fixed test split,
cùng 20/48 mẫu Rare/Common ở BenchmarkPython, 131/290 ở VUDENC và 9/45 ở
RealVuln, nên các chênh lệch có thể được so sánh trực tiếp.

## Artifacts

- Experiment root: `experiments/full_experiment_fixedsplit101_q10d5_lr002_20260727-005616/`
- In-domain reports: `in_domain/runs/<dataset>/<method>/seed_<seed>/report.json`
- Cross-benchmark results: `generalization/output/generalization_results/results.json`
- Ten-percent results: `in_domain_ten_percent/seed_<seed>/output/ten_percent_results/report.json`
- Long-tail results: `long_tail_cwe_recall/long_tail_results.json`
