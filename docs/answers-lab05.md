# Lab 05 — Hotfix & multi-version maintenance

## Câu hỏi thảo luận

### 1. Vì sao hotfix phải bắt đầu từ release bị lỗi?

Hotfix cần được xây dựng trên đúng baseline mà người dùng đang gặp lỗi. Nếu bắt đầu từ main đang phát triển, nhánh có thể chứa thay đổi mới chưa phát hành và không còn đại diện cho phiên bản cần vá.

### 2. Vì sao tách commit sửa lỗi khỏi commit bump phiên bản?

Commit sửa lỗi chứa đúng phần mã và test cần lan truyền sang các dòng phiên bản khác. Commit bump phiên bản và CHANGELOG chỉ thuộc dòng release tương ứng. Tách hai commit giúp cherry-pick phần sửa mà không vô tình kéo version của 1.0.x sang nhánh 1.1.x.

### 3. Vì sao dùng `cherry-pick -x` thay vì merge cả hotfix branch?

Cherry-pick áp dụng đúng commit sửa lỗi lên nhánh đích. Tùy chọn `-x` ghi SHA commit nguồn vào message, giúp kiểm toán nguồn gốc bản sửa. Merge toàn bộ hotfix branch có thể kéo theo commit bump version hoặc thay đổi chỉ dành cho release cũ.

### 4. Vì sao chưa gắn tag v1.1.0 trước khi hoàn tất hotfix?

Nếu tag v1.1.0 đã được phát hành rồi mới tích hợp thêm bản sửa, không nên di chuyển tag đã chia sẻ. Khi đó cần phát hành patch tiếp theo (ví dụ v1.1.1). Vì vậy bài yêu cầu để release/lab05 chưa gắn tag cho tới khi hotfix được tích hợp.
