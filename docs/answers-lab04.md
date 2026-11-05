# Lab 04 — Release flow & version

## Câu hỏi thảo luận

### 1. Vì sao release/* không merge ngược vào main trong quy trình của bài?

Trong quy trình bài thực hành, nhánh release được giữ làm mốc cho một lần phát hành hoặc nộp bài. Vì vậy, các thay đổi riêng của release không được merge ngược toàn bộ vào `main`. Nếu cần đưa một bản sửa sang nhiều nhánh, có thể dùng hotfix rồi cherry-pick commit sửa lỗi phù hợp.

### 2. Quy trình này khác GitFlow ở điểm nào?

Cả hai quy trình đều có nhánh release và hotfix. Nhưng trong GitFlow thường gặp, sau khi phát hành, nhánh release được merge trở lại cả `main` (hoặc `master`) và `develop`. Còn quy trình trong bài yêu cầu giữ các nhánh `release/*` riêng, không merge ngược vào `main`; phần sửa lỗi được chuyển sang nhánh khác bằng cherry-pick khi cần.

### 3. Vì sao phát hành 1.0.0 thay vì 0.4.0?

Theo Semantic Versioning, phiên bản 1.0.0 thường được dùng khi dự án đã sẵn sàng công bố một API ổn định. Các phiên bản 0.x thường dành cho giai đoạn phát triển ban đầu, khi API vẫn có thể thay đổi không tương thích. Việc chọn 1.0.0 trong bài thể hiện dự án đã đạt mốc phát hành đầu tiên theo quy ước này.
