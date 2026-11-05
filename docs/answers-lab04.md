# Lab 04 — Release flow & version

## Câu hỏi thảo luận

### 1. Vì sao quy trình của bài giữ nhánh release riêng và không merge ngược toàn bộ vào `master`?

Trong bài thực hành, mỗi nhánh `release/*` được dùng làm mốc ổn định cho một phiên bản hoặc một lần nộp. Giữ chúng riêng giúp các thay đổi phát sinh ở release cũ không tự động đi ngược vào nhánh phát triển. Khi cần chuyển một bản sửa sang nhánh khác, có thể chọn đúng commit bằng cherry-pick. Repository này dùng `main` làm nhánh tích hợp tương đương `master` trong tài liệu.

### 2. Quy trình này khác GitFlow ở điểm nào?

Trong GitFlow phổ biến, nhánh release sau khi phát hành thường được merge trở lại cả `master/main` và `develop). Quy trình của bài thực hành đơn giản hóa luồng đó: các nhánh `release/*` được giữ như những snapshot riêng, không merge ngược toàn bộ vào nhánh tích hợp. Khi cần đồng bộ bản sửa, bài sử dụng cherry-pick thay vì merge cả nhánh release.

### 3. Vì sao chọn phiên bản 1.0.0 thay vì 0.4.0?

Theo Semantic Versioning, 1.0.0 thường đánh dấu thời điểm dự án sẵn sàng công bố API ổn định. Phiên bản 0.x thường được dùng trong giai đoạn phát triển ban đầu, khi API còn có thể thay đổi không tương thích. Đây là mốc quy ước về mức độ ổn định, không có nghĩa phần mềm đã hết lỗi.
