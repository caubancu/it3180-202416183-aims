# Lab 02 — Feature/Topic flow & Pull Request

## Câu hỏi thảo luận

### 1. Vì sao nên đồng bộ nhánh làm việc với `master` trước khi tạo PR?

Đồng bộ giúp nhánh làm việc có các thay đổi mới nhất từ nhánh tích hợp, nhờ đó dễ phát hiện conflict và lỗi tương thích trước khi gửi PR. Sau khi cập nhật, cần chạy lại test. Trong repository này, `main` là nhánh tích hợp tương đương `master` trong tài liệu.

### 2. Khi nào không nên rebase?

Không nên rebase nhánh đã push và đang được người khác sử dụng, vì rebase viết lại lịch sử commit và làm thay đổi SHA. Nếu commit chỉ nằm ở local và chưa chia sẻ, có thể rebase để sắp xếp hoặc làm gọn lịch sử.

### 3. `feature/*` khác `topic/*` như thế nào?

Theo quy ước của bài, `feature/*` dùng cho thay đổi chức năng của chương trình, ví dụ thêm chức năng tìm DVD. `topic/*` dùng cho một đầu việc theo chủ đề như tài liệu, cấu hình hoặc quy trình, ví dụ thêm use-case hay PR template. Đây là quy ước đặt tên của repository, không phải khác biệt về cơ chế Git.
