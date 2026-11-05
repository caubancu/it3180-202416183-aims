# Báo cáo tổng hợp thực hành IT3180 — Git & GitHub

Repository: https://github.com/caubancu/it3180-202416183-aims

## Các mốc bài thực hành

| Lab | Nội dung | Nhánh snapshot |
| --- | --- | --- |
| 01 | Setup, commit ban đầu, refactor | `release/lab01` |
| 02 | Feature/topic, PR, merge methods | `release/lab02` |
| 03 | Bugfix, Issue, regression tests, discount | `release/lab03` |
| 04 | SemVer, CHANGELOG, sorting | `release/lab04` |
| 05 | Category search, hotfix, cherry-pick | `release/lab05` |

## Chức năng và cấu trúc

- `aims/dvd.py`: mô hình DVD.
- `aims/cart.py`: giỏ hàng giới hạn 20 DVD, tính tổng, in giỏ, giảm giá, sắp xếp.
- `aims/search.py`: tìm theo tiêu đề và thể loại, không phân biệt hoa thường.
- `tests/`: kiểm thử giới hạn giỏ hàng, tìm kiếm, giảm giá và sắp xếp.
- `.github/pull_request_template.md`: mẫu mô tả PR.
- `.github/workflows/ci.yml`: chạy unittest trên push vào main và PR tới main/release/*.
- `CHANGELOG.md`: lịch sử thay đổi theo phiên bản.
- `docs/answers-labXX.md`: câu trả lời thảo luận.

## Pull Request đã tạo và merge

- #1 Refactor mã nguồn vào package aims.
- #2 Thêm Cart.print_cart.
- #3 Thêm tìm kiếm theo tiêu đề (squash merge).
- #4 Thêm use-case (rebase merge).
- #6 Sửa giới hạn 20 DVD; liên kết Issue #5.
- #8 Sửa công thức discount trên feature/discount.
- #9 Tích hợp feature discount.
- #10 Chuẩn bị phiên bản 1.0.0.
- #11 Thêm tìm kiếm theo category.
- #12 Chuẩn bị phiên bản 1.1.0.
- #13 Hotfix tìm kiếm không phân biệt hoa thường trên release/lab04.
- #15 Lan truyền hotfix sang main.
- #16 Lan truyền hotfix sang release/lab05.
- #17 Thêm GitHub Actions CI.
- #18 Sửa lỗi import search trên main.
- #19 Sửa lỗi import search trên release/lab05.
- #20 Bổ sung báo cáo và câu trả lời Lab 01–05.
- #21 Dùng Cart.print_cart trong main.py và thêm test.
- #22–#25 Lan truyền thay đổi demo/cart-print vào các snapshot release/lab02–lab05.

PR #1/#2/#6/#8/#10/#11/#12/#13/#15/#16/#17/#18/#19/#20/#21/#22–#25 dùng merge commit; PR #3 dùng squash; PR #4 dùng rebase; PR #9 dùng squash. Các PR được tạo bởi chủ repository; không có review/approval từ cộng tác viên thứ hai được ghi nhận.

## Kiểm thử

GitHub Actions run: https://github.com/caubancu/it3180-202416183-aims/actions/runs/42072027042

- Python 3.11
- Lệnh: `python -m unittest discover -s tests -v`
- Kết quả ở lần chạy được kiểm tra: **10 tests — OK**.

Ứng dụng demo được thiết kế để in `Total cost: 63.89 $`.

## Những mục còn cần hoàn tất thủ công trên GitHub

Các bước sau chưa được xác nhận là đã thực hiện, không được xem là bằng chứng hoàn thành:

1. Tạo annotated tags `v0.1.0`, `v0.2.0`, `v0.3.0`, `v1.0.0`, `v1.0.1`, `v1.1.0` và GitHub Release v1.0.0.
2. Cấu hình branch protection/ruleset cho main và release/*: yêu cầu PR, cấm force-push/xóa nhánh; approval = 0 nếu làm cá nhân. Yêu cầu status check `test` sau khi CI đã chạy.
3. Lab 02: cần cộng tác viên thật để thực hiện review theo trình tự Changes requested → sửa → Approved. Không có review giả lập.
4. Lab 03: thao tác conflict merge/rebase, reset soft/mixed/hard, reflog và revert commit đã chia sẻ chưa được lưu thành chuỗi bằng chứng riêng trong repository.
5. Kiểm tra độc lập trên máy local: `python main.py` và `python -m unittest discover -s tests -v` trên từng release snapshot.

## Quy ước nhánh

Tài liệu thực hành gọi nhánh tích hợp là `master`, nhưng repository được GitHub khởi tạo với nhánh mặc định `main`. Repository này dùng `main` làm nhánh tích hợp tương đương; các nhánh `release/labXX` được giữ riêng.
