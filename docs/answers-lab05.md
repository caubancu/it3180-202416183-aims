# Lab 05 — Hotfix & multi-version maintenance

## Câu hỏi thảo luận

### 1. Nên xử lý hotfix theo hướng upstream-first hay release-first?

Nếu lỗi xuất hiện trên một phiên bản release đang được sử dụng, nên tạo hotfix từ đúng nhánh release đó trước để bảo đảm bản sửa chạy trên baseline bị lỗi. Sau khi kiểm tra, chuyển commit sửa lỗi lên nhánh phát triển (upstream) và các nhánh release còn được hỗ trợ. Nếu lỗi được phát hiện đầu tiên trên nhánh phát triển và chưa có bản release nào bị ảnh hưởng, có thể sửa ở upstream trước. Quan trọng là phải xác định đúng các nhánh thực sự bị lỗi, không áp dụng máy móc một thứ tự cho mọi trường hợp.

### 2. Làm sao kiểm tra một commit sửa lỗi đã được đưa vào tag hoặc nhánh khác?

- `git tag --contains <FIX_SHA>` liệt kê các tag có lịch sử chứa commit đó. Lệnh này hữu ích khi commit được merge trực tiếp; nếu dùng cherry-pick thì commit ở nhánh đích có SHA khác, nên cần kiểm tra commit cherry-pick tương ứng.
- `git cherry -v <upstream> <branch>` so sánh các commit ở `branch` chưa có trong `upstream`. Dấu `+` cho biết thay đổi chưa có bản tương đương ở upstream; dấu `-` cho biết upstream đã có commit tương đương về patch. Cần đặt đúng thứ tự hai nhánh khi chạy lệnh.

### 3. Vì sao dùng `cherry-pick -x` khi lan truyền hotfix?

`cherry-pick` áp dụng commit sửa lỗi được chọn lên nhánh đích. Tùy chọn `-x` thêm SHA của commit nguồn vào message, giúp truy lại nguồn gốc bản sửa. Nên tách commit sửa code/test khỏi commit bump version hoặc cập nhật CHANGELOG để tránh đưa thay đổi chỉ dành cho một release sang nhánh khác.
