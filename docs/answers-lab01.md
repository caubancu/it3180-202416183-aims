# Lab 01 — Setup & Refactor flow

## Câu hỏi thảo luận

### 1. `git config --global` được lưu ở đâu? Khác gì `--local`?

- `--global` lưu cấu hình trong tệp cấu hình Git của người dùng (thường là `~/.gitconfig`), áp dụng cho các repository của tài khoản hệ điều hành đó.
- `--local` lưu trong `.git/config` của repository hiện tại, chỉ ảnh hưởng repository đó và có độ ưu tiên cao hơn cấu hình global khi cùng một khóa được đặt.

### 2. `git restore` và `git restore --staged` khác nhau thế nào?

- `git restore <file>` khôi phục nội dung ở working tree từ index, bỏ phần sửa chưa stage.
- `git restore --staged <file>` bỏ file khỏi staging area bằng cách khôi phục index từ HEAD; nội dung sửa trong working tree vẫn còn.

### 3. Khi nào dùng `git commit --amend`?

Dùng khi cần sửa commit gần nhất, thường là sửa commit message hoặc bổ sung thay đổi bị bỏ sót. Amend tạo commit mới với SHA khác, vì vậy chỉ nên dùng với commit chưa chia sẻ lên remote. Với commit đã chia sẻ, nên tạo commit mới hoặc dùng `git revert`.
