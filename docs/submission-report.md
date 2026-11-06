# Báo cáo tổng hợp thực hành IT3180 — Git & GitHub

Repository: https://github.com/caubancu/it3180-202416183-aims

## 1. Các mốc bài thực hành

| Lab | Nội dung | Nhánh snapshot | Tag |
| --- | --- | --- | --- |
| 01 | Setup, commit ban đầu và refactor | `release/lab01` | `v0.1.0` |
| 02 | Feature/Topic flow và Pull Request | `release/lab02` | `v0.2.0` |
| 03 | Bugfix, conflict và undo | `release/lab03` | `v0.3.0` |
| 04 | Release flow, SemVer và CHANGELOG | `release/lab04` | `v1.0.0`, `v1.0.1` |
| 05 | Hotfix và bảo trì nhiều phiên bản | `release/lab05` | `v1.1.0` |

Repository có đủ năm nhánh snapshot `release/lab01` đến `release/lab05`. Nhánh tích hợp là `main`, được dùng thay cho `master` như trong tài liệu thực hành.

## 2. Chức năng và cấu trúc

- `aims/dvd.py`: mô hình DVD.
- `aims/cart.py`: giỏ hàng giới hạn 20 DVD, tính tổng, in giỏ, giảm giá và sắp xếp.
- `aims/search.py`: tìm theo tiêu đề và thể loại, không phân biệt chữ hoa/chữ thường.
- `tests/`: kiểm thử giới hạn giỏ hàng, tìm kiếm, giảm giá, sắp xếp và nội dung in giỏ.
- `.github/pull_request_template.md`: mẫu mô tả Pull Request.
- `.github/workflows/ci.yml`: chạy unittest bằng Python 3.11 khi push lên `main` và khi có Pull Request tới `main` hoặc `release/**`.
- `CHANGELOG.md`: lịch sử thay đổi theo phiên bản.
- `docs/answers-lab01.md` đến `docs/answers-lab05.md`: câu trả lời thảo luận của năm Lab.

## 3. Pull Request và lịch sử thay đổi

Các Pull Request chính đã được tạo và merge:

- #1–#4: refactor package, bổ sung chức năng giỏ hàng, tìm kiếm tiêu đề và use-case; có sử dụng merge commit, squash merge và rebase merge.
- #6, #8, #9: sửa giới hạn 20 DVD và triển khai chức năng giảm giá.
- #10–#12: chuẩn bị phiên bản 1.0.0, tìm kiếm theo category và chuẩn bị phiên bản 1.1.0.
- #13, #15, #16: sửa lỗi tìm kiếm không phân biệt hoa thường trên release/lab04, sau đó lan truyền bản sửa sang `main` và `release/lab05`.
- #17–#19: bổ sung CI và sửa lỗi import/tìm kiếm trên `main` và `release/lab05`.
- #20–#21: bổ sung tài liệu Lab và đưa `Cart.print_cart()` vào chương trình demo cùng kiểm thử.
- #22–#25: lan truyền thay đổi demo và kiểm thử sang các nhánh snapshot release.
- #26: cập nhật báo cáo và kết quả CI.
- #27: rà soát, chỉnh sửa câu trả lời thảo luận Lab 01–05.

Lưu ý: PR #6 hiện liên kết với Issue #5. Trong khi đó, kịch bản Lab 03 của handout yêu cầu xử lý Issue #6; đây là điểm chưa khớp cần được ghi nhận, không coi là đã hoàn thành đúng quy trình.

## 4. Tag và GitHub Release

Đã tạo và đẩy các annotated tag:

- `v0.1.0`
- `v0.2.0`
- `v0.3.0`
- `v1.0.0`
- `v1.0.1`
- `v1.1.0`

Đã tạo GitHub Release `v1.0.0`, sử dụng tag `v1.0.0` và target `release/lab04`.

## 5. Kiểm thử

Workflow CI sử dụng lệnh:

```bash
python -m unittest discover -s tests -v
```

- Trên `main`: lần chạy được kiểm tra có **10 tests — OK**.
- Tag `v1.0.0`: **6 tests — PASS** khi kiểm tra local.
- Tag `v1.0.1`: **7 tests — PASS** khi kiểm tra local.
- Tag `v1.1.0`: **8 tests — PASS** khi kiểm tra local.
- Chương trình demo cho tổng tiền `Total cost: 63.89 $`.

Kết quả CI đã kiểm tra: https://github.com/caubancu/it3180-202416183-aims/actions/runs/42072027042

Các kết quả kiểm tra local nêu trên chỉ áp dụng cho đúng những tag đã liệt kê; không suy rộng thành kết quả kiểm thử của mọi tag.

## 6. Thực hành Git nâng cao của Lab 03

Các thao tác đã được thực hành và đẩy lên những nhánh riêng:

- `practice/lab03-git-operations`: `reset --soft`, `reset --mixed`, `reset --hard` và khôi phục commit bằng `git reflog`.
- `practice/conflict-b`: giải quyết merge conflict và tạo revert cho merge commit.
- `practice/rebase-source`: giải quyết rebase conflict.

Đây là các nhánh thực hành minh họa thao tác Git. Chúng chưa thay thế toàn bộ kịch bản bugfix/Issue/Pull Request theo đúng trình tự của handout.

## 7. Quy tắc bảo vệ nhánh

Đã tạo ruleset áp dụng cho `main` và `release/*`, gồm yêu cầu Pull Request, hạn chế xóa nhánh, chặn force-push, yêu cầu giải quyết conversation và dismiss stale approvals. Số approval được đặt là 0 để phù hợp với repository cá nhân.

Chưa xác minh được required status check `test` đã được bật trong ruleset. Ngoài ra, cấu hình 0 approval không tương đương yêu cầu một reviewer phê duyệt trong kịch bản release của handout.

## 8. Những điểm còn thiếu so với kịch bản handout

1. **Lab 02 — review cộng tác viên:** chưa có bằng chứng một cộng tác viên thứ hai thực hiện review thực tế theo trình tự Changes requested → cập nhật → resolve conversation → Approve. Các PR do chủ repository tự tạo không thay thế được bước này.
2. **Lab 03 — Issue và bugfix flow:** PR #6 liên kết Issue #5 thay vì Issue #6 như kịch bản yêu cầu. Các thao tác reset, reflog, merge conflict, rebase conflict và revert đã được thực hành trên nhánh riêng, nhưng chưa được nối thành đầy đủ quy trình bugfix và PR theo đề.
3. **Branch protection:** cần kiểm tra và bật required status check `test` nếu handout yêu cầu CI pass trước khi merge.
4. **Approval:** ruleset hiện để 0 approval cho repository cá nhân; nếu giảng viên chấm đúng yêu cầu 1 approval trên nhánh release, cần có cộng tác viên thật và điều chỉnh cấu hình tương ứng.

## 9. Quy ước nhánh

Handout dùng tên `master` cho nhánh tích hợp. Repository này dùng `main` làm nhánh tích hợp tương đương do đây là nhánh mặc định khi khởi tạo. Các nhánh `release/labXX` được giữ riêng để lưu snapshot của từng Lab.
