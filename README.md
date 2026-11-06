# AIMS-mini — IT3180

Bài thực hành Git & GitHub (Lab 01–05) cho học phần IT3180. Dự án mô phỏng một cửa hàng DVD nhỏ, tập trung vào cách tổ chức mã nguồn, quản lý nhánh, Pull Request, kiểm thử và phát hành phiên bản.

## Chức năng chính

- Quản lý DVD và giỏ hàng, giới hạn tối đa 20 sản phẩm.
- Tính tổng tiền và áp dụng giảm giá có kiểm tra phần trăm hợp lệ.
- In nội dung giỏ hàng.
- Tìm DVD theo tiêu đề hoặc thể loại, không phân biệt chữ hoa/chữ thường.
- Sắp xếp DVD theo tiêu đề hoặc giá.

## Yêu cầu

- Python 3.10 trở lên.
- Không cần cài thư viện bên ngoài; dự án sử dụng Python Standard Library.

## Chạy chương trình

Clone repository và mở thư mục dự án:

```bash
git clone https://github.com/caubancu/it3180-202416183-aims.git
cd it3180-202416183-aims
python main.py
```

Kết quả tổng tiền của dữ liệu demo:

```text
Total cost: 63.89 $
```

## Chạy kiểm thử

```bash
python -m unittest discover -s tests -v
```

GitHub Actions cũng chạy bộ kiểm thử này bằng Python 3.11 khi có push lên `main` hoặc Pull Request nhắm tới `main` và `release/**`.

## Các mốc thực hành

| Lab | Nội dung chính | Nhánh snapshot | Tag |
| --- | --- | --- | --- |
| 01 | Thiết lập môi trường, commit ban đầu và refactor | `release/lab01` | `v0.1.0` |
| 02 | Feature/Topic flow và Pull Request | `release/lab02` | `v0.2.0` |
| 03 | Bugfix, xung đột và hoàn tác thay đổi | `release/lab03` | `v0.3.0` |
| 04 | Release flow, SemVer và CHANGELOG | `release/lab04` | `v1.0.0`, `v1.0.1` |
| 05 | Hotfix và bảo trì nhiều phiên bản | `release/lab05` | `v1.1.0` |

GitHub Release `v1.0.0` được tạo từ tag `v1.0.0`, target `release/lab04`.

## Câu trả lời thảo luận

- [Lab 01 — Setup & Refactor](docs/answers-lab01.md)
- [Lab 02 — Feature/Topic flow & Pull Request](docs/answers-lab02.md)
- [Lab 03 — Bugfix, conflict & undo](docs/answers-lab03.md)
- [Lab 04 — Release flow & version](docs/answers-lab04.md)
- [Lab 05 — Hotfix flow & multi-version maintenance](docs/answers-lab05.md)

## Cấu trúc repository

```text
.
├── aims/                  # Các lớp DVD, Cart và chức năng tìm kiếm
├── tests/                 # Unit tests
├── docs/                  # Câu trả lời Lab 01–05 và báo cáo thực hành
├── .github/workflows/     # GitHub Actions CI
├── main.py                # Chương trình demo
├── CHANGELOG.md           # Lịch sử thay đổi theo phiên bản
└── README.md
```

## Quy ước nhánh

Tài liệu bài thực hành sử dụng `master` làm nhánh tích hợp. Repository này được khởi tạo với nhánh mặc định `main`, vì vậy `main` giữ vai trò tương đương. Các nhánh `release/labXX` lưu các mốc snapshot; những thay đổi được phát triển trên nhánh riêng và đưa vào nhánh đích thông qua Pull Request.

## Báo cáo và bằng chứng

Xem [báo cáo tổng hợp](docs/submission-report.md) để biết lịch sử Pull Request, tag, kết quả kiểm thử, các nhánh thực hành Git và những nội dung còn hạn chế so với yêu cầu của handout.
