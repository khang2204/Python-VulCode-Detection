# Tổng hợp EDA các benchmark

## Tổng quan dataset

| Benchmark | Mẫu gốc có nhãn | CPG/graph xuất thành công | Benign CPG | Vulnerable CPG | Nhóm CWE/vulnerability type |
| --- | ---: | ---: | ---: | ---: | ---: |
| BenchmarkPython | 1,230 | 1,230 | 778 | 452 | 14 |
| VUDENC | 15,841 | 15,840 | 13,035 | 2,805 | 7 |
| RealVuln | 466 | 431 | 69 | 362 | 58 |

## Kết quả kiểm tra nhãn thủ công

Mỗi benchmark được chọn ngẫu nhiên cố định 10 mẫu benign và 10 mẫu vulnerable (seed `20260725`). Tỷ lệ dưới đây là số nhãn được đánh giá đúng trên 10 mẫu của từng lớp.

| Benchmark | Benign đúng | Vulnerable đúng |
| --- | ---: | ---: |
| BenchmarkPython | 10/10 | 10/10 |
| VUDENC | 10/10 | 6/10 |
| RealVuln | 7/10 | 10/10 |

## Báo cáo chi tiết

- [BenchmarkPython](BenchmarkPython/EDA_BenchmarkPython.md)
- [VUDENC](VUDENC/EDA_VUDENC.md)
- [RealVuln](RealVuln/EDA_RealVuln.md)

Mỗi báo cáo chi tiết bao gồm source-code metrics và nhận xét thủ công cho toàn bộ 20 mẫu audit.
