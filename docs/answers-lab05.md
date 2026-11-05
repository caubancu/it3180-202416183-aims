# Lab 05 — Hotfix flow & multi-version maintenance

## Câu hỏi thảo luận

### 1. Ưu và nhược điểm của upstream-first so với release-first là gì?

- **Upstream-first:** sửa lỗi trên nhánh phát triển chính trước, sau đó cherry-pick sang các nhánh release bị ảnh hưởng. Cách này giúp bản sửa được tích hợp vào hướng phát triển chung sớm và tránh mỗi nhánh tự tạo một cách sửa khác nhau. Tuy nhiên, code trên upstream có thể đã khác phiên bản release cũ, nên commit có thể khó áp dụng hoặc cần điều chỉnh khi cherry-pick.
- **Release-first:** tạo hotfix từ đúng nhánh release đang bị lỗi, kiểm tra trên baseline người dùng thực sự đang chạy rồi chuyển commit sửa sang upstream và các release liên quan. Cách này bảo đảm bản vá phù hợp với phiên bản bị lỗi, nhưng phải kiểm tra và lan truyền đầy đủ sang mọi nhánh bị ảnh hưởng; nếu bỏ sót một nhánh thì lỗi vẫn còn ở phiên bản đó.

Trong Release Flow của bài thực hành, ta dùng **release-first**: tạo hotfix từ `release/lab04`, sau đó cherry-pick phần sửa sang `main` và `release/lab05`. Tài liệu gọi nhánh tích hợp là `master`; repository này dùng tên `main`.

### 2. Nếu quên lan truyền bản sửa sang `release/lab05`, dùng lệnh nào ở Phần F để phát hiện?

Lệnh kiểm tra các commit cherry-pick có ghi lại SHA nguồn là:

`git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`

Để kiểm tra trực tiếp những commit có trong nhánh tích hợp nhưng chưa có patch tương đương ở `release/lab05`, chạy:

`git cherry -v origin/release/lab05 origin/main`

Nếu commit sửa lỗi hiện dấu `+`, thay đổi đó chưa có bản tương đương trên `release/lab05`; dấu `-` cho biết đã có commit tương đương về patch. Thứ tự đối số quan trọng: nhánh thứ nhất là upstream dùng để so sánh, nhánh thứ hai là các commit cần kiểm tra.
