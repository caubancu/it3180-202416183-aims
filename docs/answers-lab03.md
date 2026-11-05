# Lab 03 — Bugfix, conflict & undo

## Câu hỏi thảo luận

### 1. `git merge-base` dùng để làm gì?

`git merge-base <branch1> <branch2>` tìm commit tổ tiên chung tốt nhất của hai nhánh. Commit này giúp xác định điểm hai nhánh bắt đầu tách ra và được Git dùng làm cơ sở khi thực hiện một số kiểu merge. Có thể dùng lệnh này để kiểm tra quan hệ giữa nhánh feature và nhánh tích hợp.

### 2. Vì sao nên dùng `git revert` thay vì `git reset` trên nhánh đã chia sẻ?

`git revert` tạo một commit mới để đảo ngược thay đổi, nên không xóa hoặc viết lại các commit cũ mà người khác có thể đã lấy về. Ngược lại, `git reset` di chuyển nhánh về commit trước đó và có thể làm lịch sử trên remote lệch với lịch sử local. Vì vậy, với nhánh đã push và được dùng chung, revert thường an toàn hơn.

### 3. Phân biệt reset, reflog và revert.

- `reset` di chuyển HEAD và nhánh hiện tại về một commit khác. Tùy `--soft`, `--mixed` hay `--hard`, staging area và working tree được giữ lại hoặc cập nhật khác nhau.
- `reflog` ghi lại các lần HEAD và ref local được cập nhật; có thể dùng để tìm lại vị trí commit trước đó.
- `revert` tạo commit mới đảo ngược thay đổi của commit được chọn, phù hợp với lịch sử đã chia sẻ.

### 4. Merge conflict xảy ra khi nào?

Conflict xảy ra khi Git không thể tự kết hợp các thay đổi, chẳng hạn hai nhánh sửa cùng một đoạn hoặc một nhánh sửa file trong khi nhánh kia xóa file đó. Cần kiểm tra nội dung hai phía, chỉnh thành phiên bản mong muốn, xóa dấu đánh dấu conflict rồi chạy test trước khi hoàn tất merge.
