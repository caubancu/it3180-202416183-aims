# Lab 03 — Bugfix, conflict & undo

## Câu hỏi thảo luận

### 1. Vì sao test phải fail trước khi sửa bug?

Test fail trước khi sửa chứng minh test thực sự tái hiện lỗi. Sau khi sửa, test pass sẽ trở thành regression test, giúp phát hiện lỗi quay trở lại trong các thay đổi sau.

### 2. Vì sao PR của bugfix tạo từ feature phải có base là feature?

Vì lỗi phát sinh trên chức năng chưa được merge vào nhánh tích hợp. Đặt base là feature giúp PR chỉ chứa phần sửa liên quan và kiểm thử nó trên đúng nền mã nguồn. Khi feature được tích hợp, toàn bộ thay đổi sẽ đi cùng nhau.

### 3. Phân biệt reset, reflog và revert.

- `reset` di chuyển HEAD/nhánh tới commit khác và có thể thay đổi staging/working tree tùy chế độ; chỉ nên dùng để chỉnh lịch sử cục bộ chưa chia sẻ.
- `reflog` ghi lại các vị trí HEAD/nhánh từng trỏ tới, giúp tìm lại commit sau khi reset hoặc checkout nhầm.
- `revert` tạo commit mới đảo ngược thay đổi của commit cũ, phù hợp với lịch sử đã push/chia sẻ.

### 4. Merge conflict xảy ra khi nào?

Conflict xảy ra khi Git không thể tự kết hợp các thay đổi, thường do hai nhánh sửa cùng vùng nội dung. Cần đọc cả hai phía, chọn nội dung cuối cùng, xóa dấu phân cách conflict, chạy test rồi commit kết quả.
