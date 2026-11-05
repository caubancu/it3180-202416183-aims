# Lab 02 — Feature/Topic flow & Pull Request

## Câu hỏi thảo luận

### 1. Vì sao phải đồng bộ nhánh với main trước khi tạo PR?

Đồng bộ giúp phát hiện xung đột sớm, kiểm tra thay đổi trên nền mã nguồn mới nhất và tránh tích hợp một nhánh đã lỗi thời. Sau khi đồng bộ cần chạy lại test trước khi gửi PR.

### 2. Khi nào không được rebase?

Không nên rebase nhánh/commit đã được push và đang được người khác sử dụng, vì rebase viết lại lịch sử và thay đổi SHA. Có thể rebase các commit cục bộ chưa chia sẻ để làm lịch sử gọn hơn.

### 3. `feature/*` khác `topic/*` như thế nào?

`feature/*` thường bổ sung hành vi/chức năng của sản phẩm, ví dụ tìm DVD theo tiêu đề. `topic/*` gom một nhiệm vụ theo chủ đề, thường là tài liệu, cấu hình hoặc chuẩn bị quy trình, ví dụ thêm use-case hoặc PR template.
