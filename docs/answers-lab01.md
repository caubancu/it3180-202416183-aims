# Lab 01 — Setup & Refactor flow

## Câu hỏi thảo luận

### 1. `git mv` dùng để làm gì?

`git mv` dùng để đổi tên hoặc di chuyển file trong working tree và cập nhật thay đổi đó vào staging area. Có thể làm thao tác tương tự bằng cách tự di chuyển file rồi dùng `git add` và `git rm`; Git vẫn nhận diện việc đổi tên khi so sánh nội dung ở các commit.

### 2. Vì sao cần giữ baseline của Lab 01 trên nhánh `release/lab01`?

Nhánh `release/lab01` lưu lại trạng thái code tại thời điểm hoàn thành Lab 01. Khi tiếp tục làm Lab 02–05 trên các nhánh khác, mình vẫn có thể quay lại đúng phiên bản của Lab 01 để kiểm tra hoặc đối chiếu, thay vì để các thay đổi mới làm mất mốc cũ.

### 3. Vì sao không nên commit trực tiếp lên nhánh tích hợp (`master`)?

Không commit trực tiếp giúp nhánh tích hợp chỉ nhận thay đổi đã được kiểm tra qua Pull Request. Mỗi phần việc được làm trên nhánh riêng, sau đó mở PR để xem diff, chạy test và mới tích hợp. Trong repository này, nhánh mặc định là `main), được dùng tương đương `master` trong tài liệu bài thực hành.
