# Lab 05 — Hotfix & multi-version maintenance

## Câu hỏi thảo luận

### 1. Vì sao hotfix phải bắt đầu từ release bị lỗi?

Hotfix cần dựa trên đúng phiên bản đang gặp lỗi. Nếu tạo từ `main` trong khi `main` đã có thêm chức năng chưa phát hành, bản sửa có thể kéo theo những thay đổi không thuộc phiên bản cần vá.

### 2. Vì sao tách commit sửa lỗi khỏi commit bump phiên bản?

Commit sửa lỗi chứa phần code và test cần chuyển sang các nhánh phiên bản khác. Còn commit bump version và cập nhật CHANGELOG chỉ dành cho nhánh release tương ứng. Tách riêng hai phần giúp cherry-pick bản sửa mà không kéo theo số phiên bản của release khác.

### 3. Vì sao dùng `cherry-pick -x` thay vì merge cả hotfix branch?

`cherry-pick` chỉ áp dụng commit được chọn lên nhánh đích. Tùy chọn `-x` thêm thông tin SHA của commit nguồn vào message, nên sau này có thể biết bản sửa được lấy từ đâu. Nếu merge cả hotfix branch thì có thể đưa cả commit bump version hoặc thay đổi chỉ dành cho release cũ sang nhánh mới.

### 4. Vì sao chưa gắn tag v1.1.0 trước khi hoàn tất hotfix?

Trong quy trình của bài, cần hoàn tất và kiểm tra hotfix trước rồi mới đánh dấu phiên bản v1.1.0. Nếu đã phát hành tag và có người dùng rồi thì không nên di chuyển tag đó để thay nội dung; khi cần sửa tiếp, nên phát hành một phiên bản patch mới, ví dụ v1.1.1.
