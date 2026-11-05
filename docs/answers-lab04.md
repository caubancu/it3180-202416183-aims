# Lab 04 — Release flow & version

## Câu hỏi thảo luận

### 1. Vì sao release/* không merge ngược vào main trong quy trình của bài?

Nhánh release là baseline ổn định của một lần nộp/phát hành. Bài thực hành yêu cầu giữ nó độc lập, không đưa các thay đổi đặc thù của bản phát hành cũ trở lại nhánh phát triển. Khi cần sửa lỗi trên nhiều dòng phiên bản, dùng hotfix và cherry-pick phần sửa phù hợp thay vì merge toàn bộ release.

### 2. Quy trình này khác GitFlow ở điểm nào?

Cả hai đều dùng nhánh release và hotfix. Trong GitFlow cổ điển, release branch thường được merge trở lại cả nhánh main/master và develop sau phát hành. Quy trình trong tài liệu này quy định release/* không merge ngược vào main; thay vào đó, sửa lỗi được lan truyền có chọn lọc bằng cherry-pick.

### 3. Vì sao phát hành 1.0.0 thay vì 0.4.0?

Theo Semantic Versioning, phiên bản 1.0.0 đánh dấu mốc sản phẩm đạt mức ổn định và có thể công bố hợp đồng API. Các phiên bản 0.x thường biểu thị giai đoạn phát triển ban đầu, API còn có thể thay đổi không tương thích.
