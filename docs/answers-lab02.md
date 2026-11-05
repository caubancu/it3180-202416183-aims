# Lab 02 — Feature/Topic flow & Pull Request

## Câu hỏi thảo luận

### 1. Vì sao nên đồng bộ nhánh với main trước khi tạo PR?

Việc cập nhật nhánh giúp mình phát hiện xung đột sớm và kiểm tra thay đổi trên phiên bản mã nguồn mới hơn. Sau khi merge hoặc rebase với `main`, nên chạy lại test để chắc rằng phần code của nhánh vẫn hoạt động.

### 2. Khi nào không nên rebase?

Không nên rebase một nhánh đã push và đang được người khác cùng sử dụng, vì rebase viết lại lịch sử commit và làm thay đổi SHA. Với các commit còn ở máy local, chưa chia sẻ, có thể rebase để sắp xếp hoặc làm gọn lịch sử.

### 3. `feature/*` khác `topic/*` như thế nào?

Theo cách đặt tên nhánh trong bài thực hành, `feature/*` dùng cho phần bổ sung chức năng của chương trình, ví dụ tìm DVD theo tiêu đề. `topic/*` thường dùng cho một đầu việc riêng như tài liệu, cấu hình hoặc chuẩn bị quy trình, ví dụ thêm use-case hay PR template. Đây là quy ước đặt tên của dự án, không phải hai loại nhánh có cách hoạt động khác nhau trong Git.
