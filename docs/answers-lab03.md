# Lab 03 — Bugfix, conflict & undo

## Câu hỏi thảo luận

### 1. Vì sao test nên fail trước khi sửa bug?

Nếu test fail trước khi sửa, mình biết test đã bắt được lỗi cần xử lý. Sau khi sửa code mà test pass, test đó có thể được giữ lại để kiểm tra xem lỗi có xuất hiện lại trong những lần thay đổi sau hay không.

### 2. Vì sao PR sửa bug trên feature nên có base là feature?

Vì bug đang nằm trên chức năng được phát triển ở nhánh feature. Đặt base là nhánh feature giúp PR chỉ chứa phần sửa bug và được kiểm tra trên đúng phiên bản code đang có chức năng đó. Khi feature được merge vào nhánh tích hợp, phần sửa bug cũng sẽ đi theo.

### 3. Phân biệt reset, reflog và revert.

- `reset` di chuyển HEAD (và nhánh hiện tại) về một commit khác. Tùy tùy chọn, nó có thể chỉ thay đổi vị trí HEAD, cập nhật staging area hoặc cả working tree. Vì có thể viết lại lịch sử, cần cẩn thận khi dùng trên commit đã chia sẻ.
- `reflog` lưu lại những lần HEAD và các ref local được cập nhật. Có thể dùng nó để tìm lại commit hoặc vị trí nhánh trước đó.
- `revert` tạo một commit mới để đảo ngược thay đổi của commit được chọn. Cách này phù hợp hơn khi thay đổi đã được push và có người khác sử dụng.

### 4. Merge conflict xảy ra khi nào?

Conflict xảy ra khi Git không thể tự kết hợp thay đổi của các nhánh, chẳng hạn hai nhánh sửa cùng một đoạn hoặc một nhánh sửa file trong khi nhánh kia xóa file đó. Mình cần kiểm tra nội dung hai phía, chỉnh lại thành phiên bản mong muốn, xóa các dấu đánh dấu conflict, rồi chạy test trước khi hoàn tất merge.
