# QProtoGAT-Vul Binary Detection Results

## In-domain

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | Classical | 93.15% ± 1.25% | 92.02% ± 1.34% | 93.23% ± 1.80% | 87.75% ± 1.70% | 90.40% ± 1.75% |
|  | QProtoGAT-Vul_Quantum | **96.58% ± 0.83%** | **96.57% ± 0.82%** | **94.27% ± 1.40%** | **96.57% ± 0.85%** | **95.40% ± 1.10%** |
| VUDENC | Classical | 86.27% ± 1.51% | 79.35% ± 1.04% | 60.00% ± 4.46% | 68.65% ± 0.48% | 63.98% ± 2.66% |
|  | QProtoGAT-Vul_Quantum | **86.60% ± 0.33%** | **80.46% ± 0.74%** | **60.40% ± 1.09%** | **70.94% ± 1.99%** | **65.23% ± 0.70%** |
| RealVuln | Classical | 83.33% ± 3.25% | 72.47% ± 2.59% | 91.68% ± 0.87% | 88.27% ± 4.28% | 89.90% ± 2.23% |
|  | QProtoGAT-Vul_Quantum | **86.46% ± 3.25%** | **72.96% ± 3.94%** | 91.45% ± 1.13% | **92.59% ± 3.21%** | **92.01% ± 2.03%** |

**Kết luận In-domain.** QProtoGAT-Vul_Quantum cải thiện 14/15 metric so với
Classical. Lợi thế rõ nhất xuất hiện trên BenchmarkPython, nơi F1 tăng từ
90.40% lên 95.40%, tương ứng 5.00 điểm phần trăm. Trên VUDENC, Quantum cải
thiện cả năm metric, nhưng mức tăng F1 chỉ đạt 1.25 điểm phần trăm. Trên
RealVuln, Quantum tăng Recall 4.32 và F1 2.11 điểm phần trăm, trong khi
Precision giảm nhẹ 0.23 điểm phần trăm. Nhìn chung, Quantum mang lại lợi ích
rõ nhất trên BenchmarkPython và cải thiện vừa phải trên hai dataset còn lại.

## In-domain — SOTA

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | QDENN | 59.46% ± 3.29% | 52.24% ± 1.68% | 42.31% ± 4.18% | 25.00% ± 6.74% | 30.82% ± 4.82% |
|  | HQCDNN (4q) | 68.29% ± 2.05% | 65.49% ± 1.22% | 57.45% ± 3.57% | 54.90% ± 4.49% | 55.97% ± 1.59% |
|  | RQENN | 51.89% ± 6.90% | 48.21% ± 6.44% | 34.90% ± 7.58% | 34.31% ± 5.94% | 34.52% ± 6.58% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **96.58% ± 0.83%** | **96.57% ± 0.82%** | **94.27% ± 1.40%** | **96.57% ± 0.85%** | **95.40% ± 1.10%** |
| VUDENC | QDENN | 83.32% ± 0.11% | 56.13% ± 0.52% | 63.31% ± 1.94% | 14.01% ± 1.26% | 22.92% ± 1.61% |
|  | HQCDNN (4q) | 85.44% ± 0.22% | 72.39% ± 1.81% | 60.31% ± 0.58% | 52.18% ± 4.32% | 55.88% ± 2.33% |
|  | RQENN | 51.70% ± 0.96% | 52.32% ± 1.76% | 19.09% ± 1.04% | 53.29% ± 3.01% | 28.10% ± 1.54% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **86.60% ± 0.33%** | **80.46% ± 0.74%** | 60.40% ± 1.09% | **70.94% ± 1.99%** | **65.23% ± 0.70%** |
| RealVuln | QDENN | 82.81% ± 4.13% | 51.79% ± 2.79% | 84.86% ± 0.74% | 96.91% ± 5.35% | 90.44% ± 2.58% |
|  | HQCDNN (4q) | 83.85% ± 0.90% | 49.69% ± 0.53% | 84.29% ± 0.14% | 99.38% ± 1.07% | 91.22% ± 0.54% |
|  | RQENN | 49.48% ± 0.90% | 44.26% ± 4.99% | 81.64% ± 2.38% | 51.85% ± 1.85% | 63.39% ± 0.92% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **86.46% ± 3.25%** | **72.96% ± 3.94%** | **91.45% ± 1.13%** | 92.59% ± 3.21% | **92.01% ± 2.03%** |

**Kết luận In-domain, so sánh SOTA.** QProtoGAT-Vul_Quantum (Ours) đạt F1 cao
nhất trên cả ba dataset. So với QDENN, F1 tăng lần lượt 64.58, 42.31 và 1.57
điểm phần trăm trên BenchmarkPython, VUDENC và RealVuln. So với HQCDNN 4q,
mức tăng tương ứng là 39.43, 9.35 và 0.79 điểm phần trăm. So với RQENN, mức
tăng đạt 60.88, 37.13 và 28.62 điểm phần trăm, đồng thời mô hình đề xuất cao
hơn ở toàn bộ 15 metric. HQCDNN 4q đạt Recall 99.38% trên RealVuln nhưng
Balanced Accuracy chỉ đạt 49.69%, cho thấy dự đoán lệch mạnh về lớp
vulnerable. QProtoGAT-Vul_Quantum duy trì cân bằng hai lớp tốt hơn với
Balanced Accuracy 72.96% và F1 92.01%.

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

**Kết luận Generalization.** Quantum cải thiện 14/30 metric và lợi thế chủ yếu
đến từ Recall. Kết quả rõ nhất xuất hiện ở BenchmarkPython → RealVuln, nơi F1
tăng từ 58.82% lên 63.90%, tương ứng 5.08 điểm phần trăm. Quantum cũng tăng F1
1.68 điểm phần trăm ở BenchmarkPython → VUDENC và 2.45 điểm phần trăm ở
VUDENC → RealVuln. Ngược lại, F1 giảm 1.10 điểm phần trăm ở VUDENC →
BenchmarkPython và gần như không thay đổi ở RealVuln → BenchmarkPython.
VUDENC và RealVuln chủ yếu gồm code context hoặc snippet, trong khi mỗi mẫu
BenchmarkPython là một tệp Python hoàn chỉnh. Khi BenchmarkPython là target,
mô hình phải tổng hợp ngữ cảnh ở cấp file thay vì chỉ nhận diện pattern cục
bộ. QProtoGAT-Vul_Quantum còn nén prototype embedding 128 chiều xuống 10
qubit trước khi sinh quantum key/value, nên bottleneck này có thể làm mất một
phần tín hiệu cấu trúc cần thiết và biểu hiện rõ hơn khi chuyển từ snippet sang
full-file. Riêng RealVuln → BenchmarkPython, cả hai phương pháp gần như dự
đoán toàn bộ mẫu là vulnerable, với Recall 100% và Balanced Accuracy xấp xỉ
50%. Vì vậy, kết quả gần hòa ở hướng này phản ánh failure mode do domain shift
hơn là ưu thế thực chất của một phương pháp.

## Generalization — SOTA

| Train → Test | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython → VUDENC | QDENN | 52.77% ± 21.18% | 41.87% ± 6.99% | 12.48% ± 2.28% | 25.00% ± 15.00% | 15.00% ± 2.55% |
|  | HQCDNN (4q) | 64.69% ± 29.58% | 50.45% ± 3.08% | 33.50% ± 15.18% | 28.40% ± 38.05% | 16.34% ± 9.44% |
|  | RQENN | 50.83% ± 1.45% | 50.72% ± 1.20% | 18.14% ± 0.72% | 50.54% ± 0.86% | 26.70% ± 0.89% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 31.22% ± 6.54% | 41.60% ± 3.09% | 14.32% ± 1.06% | **57.68% ± 6.44%** | **22.91% ± 1.54%** |
| BenchmarkPython → RealVuln | QDENN | 29.54% ± 8.84% | 49.65% ± 1.81% | 85.16% ± 3.68% | 20.07% ± 13.86% | 30.72% ± 17.91% |
|  | HQCDNN (4q) | 35.50% ± 26.37% | 52.80% ± 2.05% | 90.64% ± 4.06% | 27.35% ± 37.85% | 32.83% ± 39.06% |
|  | RQENN | 50.58% ± 2.78% | 50.64% ± 3.56% | 84.30% ± 1.90% | 50.55% ± 2.53% | 63.19% ± 2.45% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **51.35% ± 7.73%** | 50.32% ± 6.18% | 83.89% ± 3.36% | **51.84% ± 8.62%** | **63.90% ± 7.69%** |
| VUDENC → BenchmarkPython | QDENN | **59.49% ± 3.87%** | **50.50% ± 1.93%** | **40.09% ± 5.68%** | 16.59% ± 5.89% | 22.68% ± 4.76% |
|  | HQCDNN (4q) | 40.60% ± 3.35% | 49.29% ± 0.93% | 36.36% ± 0.52% | 82.08% ± 10.73% | 50.27% ± 1.97% |
|  | RQENN | 50.49% ± 0.28% | 50.20% ± 1.53% | 36.85% ± 1.37% | 49.12% ± 6.71% | 42.04% ± 3.30% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 39.32% ± 2.72% | 47.93% ± 1.62% | 35.60% ± 0.84% | 80.38% ± 6.11% | 49.30% ± 1.42% |
| VUDENC → RealVuln | QDENN | 20.80% ± 1.28% | **49.53% ± 1.12%** | **82.22% ± 4.15%** | 7.27% ± 1.62% | 13.34% ± 2.74% |
|  | HQCDNN (4q) | 33.49% ± 0.97% | 46.92% ± 4.37% | 81.44% ± 4.11% | 27.16% ± 2.98% | 40.61% ± 2.99% |
|  | RQENN | 51.51% ± 2.44% | 49.24% ± 3.50% | 83.58% ± 1.78% | 52.58% ± 1.96% | 64.55% ± 2.00% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **44.55% ± 2.58%** | 46.07% ± 4.84% | 81.66% ± 2.92% | **43.83% ± 1.84%** | **57.03% ± 2.13%** |
| RealVuln → BenchmarkPython | QDENN | **38.37% ± 1.86%** | **50.14% ± 0.55%** | **36.83% ± 0.29%** | 94.54% ± 4.51% | 52.99% ± 0.46% |
|  | HQCDNN (4q) | 36.75% ± 0.00% | 50.00% ± 0.00% | 36.75% ± 0.00% | **100.00% ± 0.00%** | **53.75% ± 0.00%** |
|  | RQENN | 50.43% ± 1.11% | 49.59% ± 0.66% | 36.35% ± 0.66% | 46.39% ± 2.59% | 40.73% ± 1.06% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 36.75% ± 0.00% | 50.00% ± 0.00% | 36.75% ± 0.00% | **100.00% ± 0.00%** | 53.75% ± 0.00% |
| RealVuln → VUDENC | QDENN | 18.02% ± 0.14% | 48.16% ± 0.55% | 17.16% ± 0.17% | 94.83% ± 1.62% | 29.06% ± 0.32% |
|  | HQCDNN (4q) | 18.82% ± 1.92% | 50.57% ± 1.00% | 17.88% ± 0.30% | **99.75% ± 0.43%** | **30.33% ± 0.41%** |
|  | RQENN | 49.00% ± 0.21% | 49.40% ± 0.33% | 17.36% ± 0.19% | 50.02% ± 0.52% | 25.78% ± 0.27% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **29.02% ± 3.16%** | **51.86% ± 0.99%** | **18.36% ± 0.37%** | 87.23% ± 2.96% | **30.33% ± 0.42%** |

**Kết luận Generalization, so sánh SOTA.** QProtoGAT-Vul_Quantum đạt F1 cao
nhất ở BenchmarkPython → RealVuln với 63.90%, đồng thời đồng hạng tốt nhất với
HQCDNN 4q ở hai hướng RealVuln → BenchmarkPython và RealVuln → VUDENC sau
làm tròn. So với RQENN, mô hình đề xuất đạt F1 cao hơn ở bốn trong sáu hướng,
nhưng thấp hơn 3.79 điểm phần trăm ở BenchmarkPython → VUDENC và 7.52 điểm
phần trăm ở VUDENC → RealVuln. Ở VUDENC → BenchmarkPython, HQCDNN 4q đạt F1
50.27%, cao hơn QProtoGAT-Vul_Quantum 0.97 điểm phần trăm. Khi
BenchmarkPython là target, sự chuyển đổi từ snippet/context sang tệp Python
hoàn chỉnh làm tăng yêu cầu tổng hợp cấu trúc cấp file. Bottleneck nén
prototype embedding từ 128 chiều xuống 10 qubit có thể làm hạn chế lượng
thông tin cấu trúc được giữ lại, qua đó giải thích vì sao lợi thế của mô hình
đề xuất không duy trì nhất quán trong các hướng này. Nhìn chung,
QProtoGAT-Vul_Quantum ưu tiên Recall và nhận diện được nhiều mẫu vulnerable
hơn ở một số cặp source–target, nhưng chưa đạt ưu thế Generalization đồng đều
trước mọi SOTA.

## In-domain 10%

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | Classical | 59.82% ± 4.84% | 58.58% ± 1.53% | 47.18% ± 5.78% | 53.92% ± 11.04% | 49.41% ± 2.38% |
|  | QProtoGAT-Vul_Quantum | **60.18% ± 5.02%** | **58.66% ± 1.96%** | **47.60% ± 6.35%** | 52.94% ± 10.29% | 49.23% ± 2.10% |
| VUDENC | Classical | 79.73% ± 1.40% | 71.68% ± 1.49% | 44.78% ± 2.02% | 59.22% ± 5.94% | 50.82% ± 0.81% |
|  | QProtoGAT-Vul_Quantum | **79.83% ± 1.53%** | **71.81% ± 1.42%** | **45.01% ± 2.29%** | **59.38% ± 5.98%** | **51.02% ± 0.61%** |
| RealVuln | Classical | 82.81% ± 3.12% | 51.79% ± 6.38% | 84.87% ± 1.76% | 96.91% ± 2.14% | 90.49% ± 1.74% |
|  | QProtoGAT-Vul_Quantum | **82.81% ± 3.12%** | **53.15% ± 5.25%** | **85.25% ± 1.45%** | 96.30% ± 3.21% | 90.42% ± 1.85% |

**Kết luận In-domain 10%.** Quantum và Classical đạt hiệu năng gần như tương
đương khi chỉ sử dụng 10% training data. Chênh lệch F1 lần lượt là −0.18,
+0.20 và −0.07 điểm phần trăm trên BenchmarkPython, VUDENC và RealVuln. Trên
BenchmarkPython, Quantum cải thiện nhẹ Accuracy, Balanced Accuracy và
Precision nhưng giảm Recall. Trên VUDENC, Quantum cao hơn ở cả năm metric,
trong khi trên RealVuln hai phương pháp có cùng Accuracy 82.81% và khác biệt
F1 không đáng kể. Kết quả cho thấy Quantum duy trì được hiệu năng ngang
Classical trong điều kiện ít dữ liệu, nhưng chưa chứng minh lợi thế sample
efficiency rõ ràng.

## In-domain 10% — SOTA

| Dataset | Method | Accuracy | Balanced Acc. | Precision | Recall | F1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | QDENN | 53.87% ± 3.26% | 48.75% ± 2.46% | 35.15% ± 3.61% | 29.41% ± 1.47% | 31.95% ± 1.52% |
|  | HQCDNN (4q) | 54.41% ± 15.29% | 50.00% ± 0.00% | 12.25% ± 21.22% | 33.33% ± 57.74% | 17.92% ± 31.04% |
|  | RQENN | 48.83% ± 2.25% | 48.77% ± 2.18% | 35.31% ± 2.11% | 48.53% ± 14.71% | 40.44% ± 6.72% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **60.18% ± 5.02%** | **58.66% ± 1.96%** | **47.60% ± 6.35%** | **52.94% ± 10.29%** | **49.23% ± 2.10%** |
| VUDENC | QDENN | 81.72% ± 0.30% | 55.56% ± 0.47% | 45.25% ± 2.47% | 15.04% ± 0.76% | 22.58% ± 1.16% |
|  | HQCDNN (4q) | 80.08% ± 1.13% | 65.09% ± 1.97% | 43.60% ± 3.11% | 41.88% ± 4.45% | 42.65% ± 3.22% |
|  | RQENN | 53.31% ± 0.99% | 52.18% ± 1.46% | 19.08% ± 0.92% | 50.44% ± 2.28% | 27.69% ± 1.31% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | 79.83% ± 1.53% | **71.81% ± 1.42%** | 45.01% ± 2.29% | **59.38% ± 5.98%** | **51.02% ± 0.61%** |
| RealVuln | QDENN | 78.65% ± 1.80% | 53.40% ± 3.42% | 85.38% ± 1.01% | 90.12% ± 1.07% | 87.69% ± 1.04% |
|  | HQCDNN (4q) | 38.54% ± 39.69% | 50.00% ± 0.00% | 28.12% ± 48.71% | 33.33% ± 57.74% | 30.51% ± 52.84% |
|  | RQENN | 52.60% ± 8.61% | 50.19% ± 14.85% | 84.44% ± 6.96% | 53.70% ± 6.68% | 65.58% ± 6.74% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **82.81% ± 3.12%** | 53.15% ± 5.25% | 85.25% ± 1.45% | **96.30% ± 3.21%** | **90.42% ± 1.85%** |

**Kết luận In-domain 10%, so sánh SOTA.** QProtoGAT-Vul_Quantum đạt F1 cao
nhất trên cả ba dataset. So với RQENN, F1 tăng 8.79 điểm phần trăm trên
BenchmarkPython, 23.33 trên VUDENC và 24.84 trên RealVuln, đồng thời mô hình
đề xuất cao hơn ở toàn bộ 15 metric. Trên BenchmarkPython, mô hình cũng vượt
QDENN và HQCDNN 4q ở cả năm metric. Trên VUDENC, F1 đạt 51.02%, cao hơn
HQCDNN 4q 8.37 và QDENN 28.44 điểm phần trăm, dù Accuracy thấp hơn QDENN 1.89
điểm phần trăm. Trên RealVuln, F1 đạt 90.42%, cao hơn QDENN 2.73 và HQCDNN 4q
59.91 điểm phần trăm. HQCDNN 4q có độ lệch chuẩn rất lớn trên BenchmarkPython
và RealVuln, cho thấy mô hình này thiếu ổn định khi tập huấn luyện chỉ còn 10%.
Kết quả chứng minh kiến trúc đề xuất hiệu quả hơn các quantum SOTA trong chế
độ ít dữ liệu, nhưng lợi thế so với Classical control vẫn chưa rõ rệt.

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

**Kết luận Long-tail CWE Recall.** QProtoGAT-Vul_Quantum cải thiện cả 6/6 chỉ
số Rare/Common-CWE Recall so với Classical. Mức tăng lớn nhất xuất hiện trên
BenchmarkPython, với Rare-CWE Recall tăng 13.33 và Common-CWE Recall tăng 6.95
điểm phần trăm. Trên VUDENC, mức tăng tương ứng là 2.29 và 2.30 điểm phần
trăm; trên RealVuln là 7.41 và 3.70 điểm phần trăm. Kết quả cho thấy Quantum
cải thiện khả năng nhận diện vulnerable samples ở cả CWE hiếm và phổ biến,
nhưng mức tăng phụ thuộc dataset. Nhóm Rare chỉ chiếm 16.7% số mẫu vulnerable
trong test set RealVuln, nên Rare-CWE Recall 100% tại đây cần được diễn giải
thận trọng.

## Long-tail CWE Recall — SOTA

| Dataset | Method | Rare-CWE Recall | Common-CWE Recall |
| --- | --- | ---: | ---: |
| BenchmarkPython | QDENN | 38.33% ± 5.77% | 19.44% ± 7.89% |
|  | HQCDNN (4q) | 50.00% ± 5.00% | 56.94% ± 4.34% |
|  | RQENN | 46.67% ± 16.07% | 29.17% ± 2.08% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **93.33% ± 5.77%** | **97.92% ± 2.08%** |
| VUDENC | QDENN | 14.50% ± 2.75% | 13.79% ± 1.50% |
|  | HQCDNN (4q) | 47.58% ± 3.84% | 54.25% ± 5.35% |
|  | RQENN | 52.93% ± 6.49% | 53.45% ± 2.76% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **68.96% ± 4.20%** | **71.84% ± 1.00%** |
| RealVuln | QDENN | 96.30% ± 6.42% | 97.04% ± 5.13% |
|  | HQCDNN (4q) | 100.00% ± 0.00% | 99.26% ± 1.28% |
|  | RQENN | 55.56% ± 11.11% | 51.11% ± 3.85% |
|  | **QProtoGAT-Vul_Quantum (Ours)** | **100.00% ± 0.00%** | 91.11% ± 3.85% |

**Kết luận Long-tail CWE Recall, so sánh SOTA.** Trên BenchmarkPython,
QProtoGAT-Vul_Quantum đạt Rare/Common-CWE Recall 93.33%/97.92%, cao hơn
HQCDNN 4q lần lượt 43.33/40.98 điểm phần trăm và cao hơn QDENN
55.00/78.48 điểm phần trăm. Trên VUDENC, mô hình tiếp tục đạt kết quả cao nhất
với 68.96%/71.84%. So với RQENN, mô hình đề xuất cao hơn cả sáu chỉ số trên ba
dataset; mức tăng Rare/Common lần lượt là 46.66/68.75 điểm phần trăm trên
BenchmarkPython, 16.03/18.39 trên VUDENC và 44.44/40.00 trên RealVuln. Trên
RealVuln, Rare-CWE Recall 100% bằng HQCDNN 4q, nhưng Common-CWE Recall 91.11%
thấp hơn QDENN 5.93 và HQCDNN 4q 8.15 điểm phần trăm. Các hệ thống sử dụng
cùng fixed test split và cùng số mẫu Rare/Common, nên có thể so sánh trực
tiếp. Kết quả cho thấy lợi thế Long-tail rõ nhất trên BenchmarkPython và
VUDENC, trong khi Common-CWE Recall trên RealVuln vẫn là hạn chế của mô hình.

## Artifacts

- Experiment root: `experiments/full_experiment_fixedsplit101_q10d5_lr002_20260727-005616/`
- In-domain reports: `in_domain/runs/<dataset>/<method>/seed_<seed>/report.json`
- Cross-benchmark results: `generalization/output/generalization_results/results.json`
- Ten-percent results: `in_domain_ten_percent/seed_<seed>/output/ten_percent_results/report.json`
- Long-tail results: `long_tail_cwe_recall/long_tail_results.json`
