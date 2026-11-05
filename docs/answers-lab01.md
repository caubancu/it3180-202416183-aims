# Lab 01 — Setup & Refactor flow

## Câu hỏi thảo luận

### 1. `git config --global` được lưu ở đâu? Khác gì `--local`?

- `--global` lưu cấu hình trong file `.gitconfig` của người dùng (thường nằm ở thư mục home). Cấu hình này được dùng cho các repository của người dùng đó.
- `--local` lưu trong `.git/config` của repository hiện tại, nên chỉ có tác dụng với repo này. Nếu cùng một thiết lập được khai báo ở cả hai nơi thì cấu hình local được ưu tiên.

### 2. `git restore` và `git restore --staged` khác nhau thế nào?

- `git restore <file>` đưa nội dung trong working tree về trạng thái ở staging area, tức là bỏ phần sửa chưa được stage.
- `git restore --staged <file>` đưa file trong staging area về trạng thái của commit hiện tại (HEAD). Phần sửa trong working tree vẫn được giữ lại.

### 3. Khi nào dùng `git commit --amend`?

Dùng lệnh này khi muốn sửa commit gần nhất, chẳng hạn sửa message hoặc thêm file bị bỏ sót. Lệnh tạo ra một commit mới có SHA khác. Vì vậy, nên dùng với commit chưa push/chia sẻ; nếu commit đã được chia sẻ thì thường nên tạo commit mới để tránh viết lại lịch sử của người khác.
